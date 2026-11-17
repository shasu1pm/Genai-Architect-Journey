"""Add the official Connect row (social logos + links) to the footer of a bundled HTML page.

The page bundle stores resources in a JSON manifest (uuid -> base64) and the HTML in a JSON
template string; the loader swaps every uuid for a blob URL. Logos from
zz-Brand-Assets/Social-Media-Logos/PNG are downscaled in memory to 64 px and added to the
manifest — no files are copied. Idempotent: skipped when the row is already present.

Run:  python zz-Brand-Assets/pdf-kit/brand_web_social.py Transformer-Explorer-Guide/Transformer-Explorer.html
"""
from __future__ import annotations

import base64
import io
import json
import re
import sys
import uuid
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from social import LINKS, logo_path, open_logo  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
MARK = "brand-social-row"
SLASH_ESC = "<" + chr(92) + "u002F"          # how '</' is written inside the JSON template


def main(rel):
    path = REPO / rel
    s = path.read_text(encoding="utf-8")
    if MARK in s:
        print("already present:", rel)
        return
    ttag = '<script type="__bundler/template">'
    ti = s.index(ttag) + len(ttag)
    te = s.index("</script>", ti)
    template = json.loads(s[ti:te].strip())

    new_res, items = {}, []
    for l in LINKS:
        lp = logo_path(l)
        if lp:
            im = open_logo(lp)
            im.thumbnail((64, 64), Image.LANCZOS)
            buf = io.BytesIO()
            im.save(buf, "PNG", optimize=True)
            uid = str(uuid.uuid4())
            new_res[uid] = {"mime": "image/png", "compressed": False,
                            "data": base64.b64encode(buf.getvalue()).decode()}
            inner = (f'<img src="{uid}" alt="{l["label"]}" style="height:22px;width:auto;display:block">'
                     f'<span>{l["label"]}</span>')
        else:
            inner = f'<span>{l["label"]}</span>'
        target = "" if l["url"].startswith("mailto:") else ' target="_blank" rel="noopener"'
        items.append(f'<a href="{l["url"]}"{target} title="{l["label"]}: {l["text"]}" '
                     'style="display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:700;'
                     'border:1.5px solid #DCE3F3;border-radius:99px;padding:6px 12px;color:#031273;'
                     f'text-decoration:none;background:#fff">{inner}</a>')
    row = (f'\n  <div class="{MARK}" style="flex:1 1 100%;display:flex;flex-wrap:wrap;gap:8px;align-items:center;'
           'justify-content:center;padding-top:10px;border-top:1px solid #DCE3F3">'
           '<span style="font-size:11px;font-weight:800;letter-spacing:.14em;color:#FF4A62">CONNECT</span>'
           + "".join(items) + "</div>\n")

    m = re.search(r"</nav>\s*</footer>", template)
    if not m:
        raise SystemExit("footer anchor not found")
    template = template[:m.start()] + "</nav>" + row + "</footer>" + template[m.end():]
    enc = json.dumps(template, ensure_ascii=False).replace("</", SLASH_ESC)
    s = s[:ti] + enc + s[te:]

    mtag = '<script type="__bundler/manifest">'
    mi = s.index(mtag) + len(mtag)
    j = s.index("{", mi)
    extra = ",".join(json.dumps(k) + ":" + json.dumps(v) for k, v in new_res.items())
    s = s[:j + 1] + extra + "," + s[j + 1:]

    path.write_text(s, encoding="utf-8", newline="")
    # verify both JSON blocks still parse and every new uuid is referenced
    s2 = path.read_text(encoding="utf-8")
    a = s2.index(ttag) + len(ttag)
    t2 = json.loads(s2[a:s2.index("</script>", a)].strip())
    b = s2.index(mtag) + len(mtag)
    man = json.loads(s2[b:s2.index("</script>", b)].strip())
    assert all(u in man and u in t2 for u in new_res), "verification failed"
    print(f"added Connect row with {len(new_res)} logos:", rel)


if __name__ == "__main__":
    main(sys.argv[1])
