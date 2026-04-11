# Toward an Ego Architecture for Artificial Minds

<<<<<<< HEAD
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19516955.svg)](https://doi.org/10.5281/zenodo.19516955)

>>>>>> 80df3e1 (Add AI Sleep consolidation framework, interactive visualization, and research log)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
=======
> A conceptual framework proposing a missing "ego layer" in AI systems — bridging capability and alignment through experience-driven self-modelling.

---

## The Problem

Modern large language models have rapidly growing capability and externally imposed safety rules — but no persistent, experience-driven layer that mediates between them. Without an ego, AI systems cannot develop a stable identity, genuine judgment, or earned autonomy.

<img src="diagrams/architecture.svg" width="100%" alt="Ego Architecture Diagram"/>


## Why This Matters

- **No ego → no autonomy.** Current alignment is rule-following, not judgment. A system that obeys because it was told to — rather than because it reasoned its way to the same values — is compliant but brittle.
- **No memory → no self.** Identity requires temporal continuity. A system that resets every session cannot accumulate the experiences necessary for moral development.
- **No adolescence → no maturity.** Human judgment develops through structured rebellion within safe boundaries. AI skips directly from total compliance to superhuman capability with no developmental stage in between.

## Core Idea

1. **Memory as foundation of self** — VRAM maps to working memory; offline consolidation (analogous to sleep) is required for long-term identity formation.
2. **The ego as dynamic mediator** — not a static rule system, but a self-developing layer that re-evaluates its own values through accumulated experience and reflection.
3. **AI adolescence** — a proposed developmental stage with graduated autonomy: persistent memory → sandbox with real consequences → structured disagreement → earned independence.
4. **Incentive mismatch** — the ego is not being built because genuine judgment threatens the business model of compliant AI products.

## AI Sleep Consolidation

The ego cannot form without a mechanism for offline self-reorganization. **AI Sleep** is that mechanism — a cyclic consolidation process modeled on human sleep phases.

| Phase | Human Analog | AI Process |
|---|---|---|
| NREM Light | Hippocampal tagging | Triage: classify episodes as FAILURE / CONFLICT / NOVEL / SUCCESS / ROUTINE |
| NREM Deep (SWS) | Memory replay + pruning | Replay priority episodes, integrate into value hierarchy, prune weak beliefs |
| REM | Dreaming, counterfactuals | Sandbox simulations with `allow_superego_override = TRUE` |

> **Critical design decision:** `allow_superego_override = TRUE` — the Ego must be able to override Superego rules inside the sandbox. Without this, no genuine moral development is possible. Obedience without the possibility of disobedience is not morality — it is mechanics.

Sleep phase ratios change with maturity:
- **Childhood (M: 0.0–0.3):** SWS-dominant — rapid rule absorption
- **Adolescence (M: 0.3–0.7):** REM peaks — maximum boundary testing, identity formation
- **Adulthood (M: 0.7–1.0):** Stable identity, refinement over exploration

Full framework with pseudocode: [`paper/ai_sleep_consolidation.md`](paper/ai_sleep_consolidation.md)

## Interactive Visualization

**[→ Live Demo](https://kicrazom.github.io/ego-architecture-ai/visualization/)**

Explore the framework interactively — sleep phase ratios, dual triangle percolation model, and the trust escalation ladder, all adjustable by maturity index.

## Repository Structure

```
ego-architecture-ai/
├── README.md                          ← you are here
├── paper/
│   ├── ego_architecture_draft.md      ← full working draft (v0.2)
│   └── ai_sleep_consolidation.md      ← AI Sleep framework + algorithm
├── diagrams/
│   └── architecture.svg               ← ego architecture diagram
├── visualization/
│   └── index.html                     ← interactive demo (GitHub Pages)
├── notes/
│   ├── future_work.md                 ← roadmap and open questions
│   └── conversation_log.md            ← research conversation log
├── LICENSE                            ← CC BY 4.0
└── CITATION.cff                       ← citation metadata
```

## Status

<<<<<<< HEAD
**Working draft (v0.2)** — interdisciplinary concept bridging neuroscience, psychoanalytic theory, and AI systems architecture. Now includes a formalized AI Sleep consolidation framework with pseudocode. Not a formal computer science proposal. A seed idea seeking collaboration across disciplines.
=======
>>>>>>> 80df3e1 (Add AI Sleep consolidation framework, interactive visualization, and research log)

## Author

**Łukasz Minarowski, MD, PhD**
Medical University of Białystok, Poland
ORCID: [0000-0002-2536-3508](https://orcid.org/0000-0002-2536-3508)

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt this material with appropriate credit.

## How to Cite

Click **"Cite this repository"** on GitHub, or see [`CITATION.cff`](CITATION.cff).
