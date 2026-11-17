---
out: Transformer-Explorer-Guide/Transformer-Explorer-Explainer.pdf
folder: Transformer-Explorer-Guide
title: Transformer Explorer
subtitle: An offline playground and 20 illustrated lessons on how a Transformer produces the next token
fact: Document | Companion guide explainer
fact: Level | Beginner to intermediate
fact: Contents | Transformer-Explorer.html · 2-part illustrated guide
fact: Model | Small, untrained, seeded simulation — not GPT-2
fact: Folder | Transformer-Explorer-Guide
keywords: Transformer, attention, tokens, sampling, temperature
---
# What it is
lead: Type → Run → Watch → Click → Explore → Understand.
Transformer Explorer is a single, offline HTML page that shows a sentence becoming tokens, passing through attention and feed-forward blocks, and producing scores for the next token. The illustrated guide walks through it in 20 lessons and four repeatable experiments.

# How the playground computes a next token
flow: Text > Tokenize > Embed + position > 12 blocks · attention + MLP > Logits > Temperature · Top-K · Top-P > Next token
Text is split into tokens; each token gets an embedding plus position information; twelve blocks of attention and MLP layers refine those vectors; the last position becomes scores (logits); the sampling settings turn scores into probabilities; one token is chosen and appended, and the cycle repeats.

# The 20 lessons
| Lessons | Focus |
| :-- | :-- |
| 01–03 | What a Transformer is, how it works, its architecture |
| 04–07 | Embedding, token embedding, positional encoding, repeated blocks |
| 08–11 | Multi-head self-attention, query/key/value, multi-head, masked attention |
| 12–14 | Attention output and concatenation, MLP, output logits |
| 15–17 | Probabilities, temperature, sampling strategy |
| 18–20 | Residual connection, layer normalisation, dropout |

# Four experiments
| Experiment | What you should see |
| :-- | :-- |
| Repeated words | "work work": same token IDs, different combined embeddings because positions differ |
| Temperature | 0.20 vs 1.50: attention and logits unchanged; only the probability spread changes |
| Top-K = 1 | Exactly one eligible candidate with 100% sampling probability |
| View vs model | Switching blocks or heads changes the view; changing the head count changes the model |

# Use it
```text Open the playground
1. Download Transformer-Explorer.html
2. Open it in a modern browser — no install, account or internet needed
3. Enter up to 20 words, select Run Transformer, click any token to follow it
```
> [!NOTE] Scope and source
> The playground computes a small, untrained, seeded simulation (24-dimensional embeddings, 12 causal decoder blocks, 1–12 heads). It shows the mechanics; it does not understand language and does not run GPT-2. Its learning approach is informed by Cho et al. (2026), Transformer Explainer, CHI '26 — this is an independent offline implementation.

# Key takeaways
- A Transformer is a pipeline: tokens → vectors → repeated blocks → scores → sampling.
- Attention decides which earlier positions each token draws from.
- Temperature and Top-K/Top-P change how a token is chosen, not what the model computed.
- Read alongside Phase-005-LLM-Foundations-and-Practical-Tools; continue with Phase-006-LangChain-Ecosystem.
