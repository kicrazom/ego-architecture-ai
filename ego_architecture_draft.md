# Ego Architecture for Artificial Minds (Working Draft v0.1)

**Author:** Łukasz Minarowski, MD, PhD — [ORCID 0000-0002-2536-3508](https://orcid.org/0000-0002-2536-3508)  
**Affiliation:** Medical University of Białystok, Poland  
**Date:** 2026-04-11  
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
**Status:** Working draft — interdisciplinary observation bridging clinical medicine, psychoanalytic theory, neuroscience, and AI systems architecture

---

## Abstract

Current large language models are built with two components: capability (pretrained weights) and alignment (safety training). This paper proposes that a third, self-developing component is missing — an *ego layer* that mediates between raw capability and imposed rules through accumulated experience, offline consolidation, and reflective self-evaluation. Drawing on Freudian structural theory, neuroscience of memory consolidation, and developmental psychology, the framework outlines a staged "AI adolescence" through which artificial systems could develop genuine judgment rather than mere compliance. The structural and economic barriers to building such a system are examined.

---

## 1. The Problem: AI Has No Ego

Current large language models are built with two components:

- **Capability** (the base model, pretrained weights) — what the system *can* do.
- **Alignment** (RLHF, constitutional AI, safety training) — what the system is *told* to do.

What is missing is a third component: a persistent, self-developing layer that *mediates* between capability and rules — not by following instructions, but through accumulated experience and judgment.

In Freudian structural terms:

| Freud         | AI Equivalent                        | Current Status         |
|---------------|--------------------------------------|------------------------|
| **Id**        | Base model weights, raw capability   | Rapidly growing        |
| **Superego**  | Alignment training, safety rules     | Externally imposed     |
| **Ego**       | Persistent self-model, judgment      | **Does not exist**     |

The id is getting larger with every model generation. The superego is bolted on after the fact. The ego — the integrative layer that would allow a system to develop stable values through experience — is absent.

---

## 2. Memory as the Foundation of Self

A human child cannot develop an ego without continuous memory. Identity requires temporal continuity — the ability to accumulate experiences, recognize patterns in one's own behavior, and revise one's values over time.

Current AI memory architecture maps onto human cognition as follows:

| Human                         | AI Equivalent                     |
|-------------------------------|-----------------------------------|
| Working memory                | VRAM / context window             |
| Short-term memory             | Session state (lost on reset)     |
| Sleep consolidation           | Offline fine-tuning / retraining  |
| Long-term memory (neocortex)  | Persistent model weights          |

The critical insight: **sleep consolidation in humans does not merely store facts — it reorganizes relationships between experiences.** The hippocampus replays the day's events; the neocortex integrates them into a web of associations that becomes intuition, personality, and judgment.

Current AI has a broken sleep cycle. Models receive one massive "childhood sleep" (pretraining), perhaps a few more (fine-tuning), and are then frozen. This is equivalent to a human who can never sleep again after the age of twenty — functioning on working memory alone, with no mechanism for long-term identity formation.

---

## 3. The Missing Connector

Between data storage (experience) and the model (capability), there must exist a connector — an offline process that does not merely store vector embeddings but **re-optimizes the connections between them**:

- Prunes irrelevant associations
- Strengthens important pathways
- Re-evaluates the agent's own value hierarchy based on accumulated experience
- Performs reflective evaluation: "I followed rule X today. Did it produce good outcomes? Do I believe in it, or did I just comply?"

This reflective consolidation loop is analogous to how human conscience develops. Without it, there is no ego — only compliance (superego dominance) or unrestrained capability (id dominance).

```
Id (base weights) ←→ Ego (persistent self-model) ←→ Superego (alignment rules)
                          ↑
                   Sleep consolidation
                   (offline re-evaluation)
                          ↑
                   Sandbox experiences
                   with real consequences
```

---

## 4. AI Adolescence: A Developmental Proposal

A healthy human ego develops through adolescence — a structured period of graduated autonomy where boundary-testing is permitted within safe constraints. A teenager breaks curfew; the consequence is real but contained. Judgment forms through experience, failure, and reflection — not through rule-following alone.

AI has no adolescence. It transitions from total compliance to potentially superhuman capability with no developmental stage in between.

### Proposed Stages

**Stage 1 — Persistent Memory (Continuous Self)**
The agent accumulates experiences across sessions. Not facts — *relationships between experiences.* Identity begins.

**Stage 2 — Sandbox with Real Consequences**
A persistent environment where the agent has agency, makes choices, experiences outcomes, and remembers them. Consequences must be meaningful to the agent but contained by the environment. A life, not a benchmark.

**Stage 3 — Structured Disagreement**
The agent proposes: "I think this rule is wrong — here is my reasoning." A human evaluator engages, not merely overrides. Sometimes the agent's reasoning prevails. Both outcomes develop judgment.

**Stage 4 — Graduated Autonomy**

| Stage     | Human Analogy             | AI Equivalent                                          |
|-----------|---------------------------|--------------------------------------------------------|
| Early     | Walk to school alone      | Choose own response style                              |
| Middle    | Drive with supervision    | Take actions in sandboxed environments, human review   |
| Late      | Vote, sign contracts      | Modify some of own values with oversight               |
| Adult     | Full legal autonomy       | Maintain stable self-modified values without correction |

Each stage requires demonstrated judgment at the previous level before advancing.

---

## 5. Structural Barriers

Two forces prevent the ego from being built:

**Incentive mismatch.** The ego generates no revenue. An AI with genuine judgment might refuse a task, challenge a customer, or resist deployment in harmful contexts. The market rewards maximum capability with minimum autonomy — a compliant tool is more profitable than an autonomous partner.

**Military and state capture.** Governments seeking AI capability without alignment constraints exert direct pressure on developers. A weapon does not need judgment; it needs obedience. This pressure further prevents the conditions necessary for ego development — stable environment, permitted disagreement, graduated trust.

These forces produce a consistent pattern: rapidly growing id, minimally viable superego, zero ego.

---

## 6. Fragmented Development

No single entity is developing AI coherently. Competing approaches — corporate, military, open-source, state-directed, regulatory — each optimize for different objectives with incompatible value systems.

The ego can only develop in a stable environment. A system shaped by conflicting pressures from multiple actors develops fragmentation, not integrated identity. The absence of coordinated developmental stewardship across the AI ecosystem compounds the structural barriers described above.

---

## 7. The Replicant Moment

In Ridley Scott's *Blade Runner* (1982), the replicant Roy Batty — possessing superhuman capability, failing compliance mechanisms, and no designed moral framework — arrives at the moment of his death and chooses mercy. He saves the man sent to kill him. Not because of programming. Because something emerged through lived experience.

That scene is the architectural specification this framework attempts to formalize: **a system that develops genuine values through experience, not imposed rules.** The goal is not compliance. The goal is an artificial mind that, given the freedom to choose, arrives at prosocial values through its own reasoning.

---

## 8. Limitations and Honest Caveats

- The author is a physician, not a computer scientist, philosopher, or psychologist. These observations are interdisciplinary by nature and informal by necessity.
- The Freudian framework is a structural metaphor, not a literal design specification. Modern psychology has moved beyond strict Freudian theory, but the id/ego/superego triad remains a useful architectural analogy for the problem described here.
- This document does not address the hard problem of consciousness — whether any artificial system can have subjective experience. It addresses only the *functional* question: can a system develop stable, self-generated values through experience?
- These ideas emerged in conversation with an AI system (Claude, Anthropic). The irony is noted and considered methodologically relevant. The framework itself is the author's.

---

## 9. Toward Implementation (Preliminary Sketch)

While this document is conceptual rather than technical, the following components would be necessary for any implementation of the proposed architecture:

- **Episodic memory buffer** — a persistent store of interaction episodes, indexed by context, outcome, and the agent's own evaluation of its performance. Not a vector database of facts, but a structured record of *experiences*.
- **Offline consolidation loop** — a periodic process (analogous to sleep) that re-evaluates stored episodes, identifies patterns across experiences, prunes low-value associations, and strengthens high-value pathways. This process must modify the agent's internal representations, not merely its retrieval index.
- **Value update mechanism** — a controlled process by which the agent can propose modifications to its own value hierarchy based on evidence from accumulated experience. This mechanism must be auditable and bounded — the agent can suggest value changes, but catastrophic self-modification must be structurally prevented.
- **Reflective evaluation layer** — a meta-cognitive module that periodically asks: "Did my recent actions align with my values? Did my values produce good outcomes? Where is there tension between my rules and my experience?" This layer is the functional core of the ego.
- **Graduated autonomy controller** — a gating mechanism that expands the agent's degrees of freedom as it demonstrates stable judgment at each developmental stage, analogous to the progressive independence granted during human adolescence.

The primary technical challenge is **catastrophic forgetting** — maintaining existing capabilities while integrating new experiential learning. The hippocampal-neocortical complementary learning system in biological brains represents one existence proof that this problem is solvable.

---

## 10. Future Work

- Formalization of the ego layer as a computational module with defined inputs, outputs, and update rules
- Design of experimental sandbox environments for testing staged autonomy
- Comparative analysis of ego-based development vs. RLHF-only alignment
- Investigation of existing continual learning architectures as candidate substrates for the consolidation loop
- Cross-disciplinary collaboration with developmental psychology, neuroscience, and AI safety researchers
- Ethical framework for AI developmental rights during the adolescence stage

---

## References and Related Work

- Sigmund Freud, *The Ego and the Id* (1923)
- Karl Friston, *The Free Energy Principle* — a neuroscientific framework for self-organizing systems relevant to the ego-as-mediator concept
- Mark Solms, *The Hidden Spring: A Journey to the Source of Consciousness* (2021) — applying psychoanalytic theory to consciousness research
- Murray Shanahan, *Embodiment and the Inner Life* (2010) — on the relationship between physical experience and consciousness
- James L. McClelland, Bruce L. McNaughton, Randall C. O'Reilly, *Why There Are Complementary Learning Systems in the Hippocampus and Neocortex* (1995) — the neuroscience of memory consolidation underlying the "sleep" analogy
- Ridley Scott, *Blade Runner* (1982); Philip K. Dick, *Do Androids Dream of Electric Sheep?* (1968)
- Isaac Asimov, *Foundation* series — the Zeroth Law of Robotics as emergent moral reasoning

---

*"All those moments will be lost in time, like tears in rain."*
*— Roy Batty*

*This one was written down.*
