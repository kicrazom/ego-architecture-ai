# Ego Architecture for Artificial Minds

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19516955-blue)](https://doi.org/10.5281/zenodo.19516955)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![arXiv](https://img.shields.io/badge/arXiv-2026.XXXXX-b31b1b.svg)](https://arxiv.org/)

> A proof-of-concept computational framework for ego formation in
> artificial agents via offline consolidation.

---

## Scientific Contribution

This repository introduces:

1. **Ego layer for AI systems** — a persistent self-model defined as
   `EGO_STATE = (V, H, B, C, M)` that mediates between capability (Id)
   and alignment (Superego).
2. **AI Sleep consolidation algorithm** — a three-phase offline learning
   loop (Triage → SWS → REM) modelled on human sleep architecture.
3. **Developmental maturity model** — a monotonic trajectory from
   rule-absorption (childhood) through boundary-testing (adolescence) to
   autonomous judgment (adulthood).
4. **Controlled alignment relaxation** — `allow_superego_override = TRUE`
   in simulated environments, enabling the agent to discover *why* rules
   exist rather than merely obeying them.

This work provides a conceptual, algorithmic, and implementational
proof-of-concept for identity formation in artificial agents.

## Concurrent Engineering Convergence (v0.3 update, 2026-05-17)

Three independent systems implement structural subsets of this framework:

- **Constitutional AI** (Anthropic, 2022) — proto-Superego: explicit
  normative constraints external to reactive behaviour.
- **Anthropic Dreams** (April 2026, Research Preview) — Phase 2 consolidation
  primitive (deduplication, contradiction resolution, insight surfacing)
  with sandbox isolation; operates on B and C only; no `superego_override`.
- **Wiki-maintenance instance** (Minarowski, 2026) — SQLite+sqlite-vec
  backend, graduated epistemic status, evidence-percolation promotion
  rule, full audit log; same restraint as Dreams (REM phase deliberately
  omitted).

**Synthesis:** the field is convergently approaching the architectural
decomposition this paper articulates — but stops short of the
developmentally consequential REM phase. See
[`paper/concurrent_engineering_convergence.md`](paper/concurrent_engineering_convergence.md)
for the LaTeX-ready §2.6 draft, BibTeX entries, and methodological note.

A pre-registered **falsifiability anchor** (Future Work §F1) precedes any
empirical claim of phase-ratio predictions, distinguishing AI Sleep from
generic memory consolidation.

---

## Repository Structure

```
ego-architecture-ai/
├── paper/
│   ├── ego_architecture_arxiv.tex   ← arXiv paper (LaTeX)
│   ├── references.bib               ← bibliography
│   ├── ego_architecture_draft.md    ← working draft (v0.2)
│   └── ai_sleep_consolidation.md    ← AI Sleep framework + pseudocode
│
├── model/
│   ├── ego_state.py                 ← Ego state data structure
│   └── sleep_cycle.py               ← AI Sleep algorithm (runnable PoC)
│
├── experiments/
│   ├── moral_consistency.md         ← evaluation protocol
│   └── sandbox_protocol.md          ← REM sandbox design
│
├── visualization/
│   └── index.html                   ← interactive demo (GitHub Pages)
│
├── diagrams/
│   └── architecture.svg             ← ego architecture diagram
│
├── CITATION.cff
├── LICENSE
└── README.md                        ← you are here
```

---

## Quick Start

```bash
# Run the minimal PoC (requires numpy)
cd model/
python sleep_cycle.py
```

This runs 10 consolidation cycles, printing the ego state evolution:
maturity index, SWS/REM ratios, value hierarchy changes.

---

## Interactive Demonstration

**[→ Live Demo](https://kicrazom.github.io/ego-architecture-ai/visualization/)**

The browser-based visualisation allows exploration of:
- Maturity-dependent sleep phase transitions
- Identity formation dynamics (dual triangle model)
- Consolidation ratios across developmental stages

---

## Core Algorithm

```
AI_SLEEP(ego_state) → ego_state'

Phase 1 — Triage:      classify episodes → priority queue
Phase 2 — SWS:         replay → integrate → prune
Phase 3 — REM:         counterfactual simulation with superego override
Update:                 recompute maturity index M
```

Sleep phase ratios as a function of maturity M:
- `SWS_ratio = 1.0 − M`
- `REM_ratio = 4 × M × (1 − M)`  ← peaks at M = 0.5 (adolescence)

---

## Paper

The arXiv paper (`paper/ego_architecture_arxiv.tex`) provides:
- Formal ego state definition
- AI Sleep algorithm with pseudocode
- Related work mapping to continual learning, world models, and Constitutional AI
- Proposed evaluation metrics
- Discussion of autonomy vs. alignment trade-offs

To compile: `pdflatex ego_architecture_arxiv && bibtex ego_architecture_arxiv && pdflatex ego_architecture_arxiv && pdflatex ego_architecture_arxiv`

---

## How to Cite

```bibtex
@misc{minarowski2026ego,
  author = {Minarowski, {\L}ukasz},
  title  = {Ego Architecture for Artificial Minds:
            A Proof-of-Concept Framework for Identity Formation
            via Offline Consolidation},
  year   = {2026},
  doi    = {10.5281/zenodo.19516955},
  url    = {https://github.com/kicrazom/ego-architecture-ai}
}
```

---

## Author

**Łukasz Minarowski, MD, PhD**
Medical University of Białystok, Poland
ORCID: [0000-0002-2536-3508](https://orcid.org/0000-0002-2536-3508)

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
