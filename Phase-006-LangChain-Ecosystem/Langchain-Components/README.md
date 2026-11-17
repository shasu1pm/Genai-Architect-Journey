<!-- brand:header:start -->
<p align="center">
  <img src="../../zz-Brand-Assets/Dragon-Motivation-Logo.png" alt="Dragon Motivation logo" height="64">
  <br><br>
  <img src="../../zz-Brand-Assets/ShasuVathanan-GEN%20AI-Product-Manager.png" alt="Shasu Vathanan - GEN AI - Product Manager" width="420">
  <br><br>
  <a href="https://SHASUVATHANAN.COM">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan">LinkedIn</a>
</p>
<!-- brand:header:end -->

# LangChain Components — The Building Blocks of a RAG App

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

📘 **Explainer:** [LangChain-Components-Explainer.pdf](./LangChain-Components-Explainer.pdf) — this folder in a short, branded guide.

**Seven notebooks, one building block each: load → split → embed → store → retrieve → chain → trace.**

A **Phase-006-LangChain-Ecosystem** track. Run the notebooks in order; notebooks 01–05 need no API key, while 06 and 07 call OpenAI.

---

## Notebooks

| # | Notebook | What you learn |
| :-- | :-- | :-- |
| 01 | [01_Data_Ingestion.ipynb](./01_Data_Ingestion.ipynb) | `TextLoader` turns a file into Documents; other loaders such as `PyPDFLoader` |
| 02 | [02_Text_Splitter.ipynb](./02_Text_Splitter.ipynb) | `RecursiveCharacterTextSplitter`, `chunk_size` and `chunk_overlap` |
| 03 | [03_Embeddings.ipynb](./03_Embeddings.ipynb) | Free local `all-MiniLM-L6-v2` or OpenAI `text-embedding-3-small`; cosine similarity |
| 04 | [04_Vector_Store.ipynb](./04_Vector_Store.ipynb) | FAISS — `from_texts`, `similarity_search`, `save_local` / `load_local` |
| 05 | [05_Retriever.ipynb](./05_Retriever.ipynb) | `.as_retriever(search_kwargs={"k": 2})` and `retriever.invoke(question)` |
| 06 | [06_Chains.ipynb](./06_Chains.ipynb) | Prompt → Model → Output parser joined with the pipe operator |
| 07 | [07_LangSmith.ipynb](./07_LangSmith.ipynb) | Tracing with environment variables, `@traceable` and `wrap_openai` |

## Supporting files

| File | Purpose |
| :-- | :-- |
| [requirements.txt](./requirements.txt) | Packages for all seven notebooks |
| [.env.example](./.env.example) | Placeholder keys — copy to `.env` and fill in your own |
| [sample.txt](./sample.txt) | The small text file created and loaded by notebook 01 |
| [my_store/](./my_store/) | The FAISS index saved by notebook 04 |

## Run

```powershell
cd "Phase-006-LangChain-Ecosystem\Langchain-Components"
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
copy .env.example .env      # then paste your own keys into .env
```

> [!IMPORTANT]
> Real keys belong only in the local `.env` file, which is git-ignored.

## Navigation

| Up | Index | Next track |
| :-- | :--: | --: |
| [Phase-006-LangChain-Ecosystem](../) | [Journey index](../../README.md) | [Advanced Model Integration →](../Langchain_Advanced_Model_Integration/) |

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank">LinkedIn</a>

<!-- brand:footer:start -->
<!-- brand:social:start -->
<p align="center">
  <a href="https://shasuvathanan.com"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/website-personal-logo.png" alt="Website" title="Website" height="24"></a>
  &nbsp;
  <a href="mailto:shasu1pm@gmail.com"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/Gmail_Logo.svg" alt="Email" title="Email" height="24"></a>
  &nbsp;
  <a href="https://linkedin.com/in/shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/linkedin.png" alt="LinkedIn" title="LinkedIn" height="24"></a>
  &nbsp;
  <a href="https://github.com/shasu1pm"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/github-custom.png" alt="GitHub" title="GitHub" height="24"></a>
  &nbsp;
  <a href="https://huggingface.co/Shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/huggingface.png" alt="Hugging Face" title="Hugging Face" height="24"></a>
  &nbsp;
  <a href="https://www.youtube.com/@ShasuVathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/youtube.png" alt="YouTube" title="YouTube" height="24"></a>
  &nbsp;
  <a href="https://x.com/shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/x.png" alt="X (Twitter)" title="X (Twitter)" height="24"></a>
  &nbsp;
  <a href="https://higgsfield.ai/@shasuvathanan"><img src="../../zz-Brand-Assets/Social-Media-Logos/PNG/Higgsfield_AI.png" alt="Higgsfield AI" title="Higgsfield AI" height="24"></a>
  <br>
  <sub><b>Connect:</b> <a href="https://shasuvathanan.com">Website</a> &nbsp;&#8226;&nbsp; <a href="mailto:shasu1pm@gmail.com">Email</a> &nbsp;&#8226;&nbsp; <a href="https://linkedin.com/in/shasuvathanan">LinkedIn</a> &nbsp;&#8226;&nbsp; <a href="https://github.com/shasu1pm">GitHub</a> &nbsp;&#8226;&nbsp; <a href="https://huggingface.co/Shasuvathanan">Hugging Face</a> &nbsp;&#8226;&nbsp; <a href="https://www.youtube.com/@ShasuVathanan">YouTube</a> &nbsp;&#8226;&nbsp; <a href="https://x.com/shasuvathanan">X (Twitter)</a> &nbsp;&#8226;&nbsp; <a href="https://higgsfield.ai/@shasuvathanan">Higgsfield AI</a></sub>
</p>
<!-- brand:social:end -->
<p align="center">
  <img src="../../zz-Brand-Assets/NeGot-My-AI-Avatar.png" alt="NeGot - my AI avatar" height="56">
  <br>
  <sub><b>Shasu Vathanan - GEN AI - Product Manager</b> &nbsp;&#8226;&nbsp; NeGot, my AI avatar &nbsp;&#8226;&nbsp; <a href="../../README.md">Back to the journey index</a></sub>
</p>
<!-- brand:footer:end -->
