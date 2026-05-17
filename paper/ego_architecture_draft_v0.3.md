# Ego Architecture for Artificial Minds (Working Draft v0.3)

**Author:** Łukasz Minarowski, MD, PhD — [ORCID 0000-0002-2536-3508](https://orcid.org/0000-0002-2536-3508)
**Affiliation:** Medical University of Białystok, Poland
**Date:** 2026-05-17 (v0.3); initial concept 2026-04-11 (v0.1, commit `595a7b5`)
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
**Status:** Working draft — interdisciplinary proof-of-concept bridging clinical medicine, psychoanalytic theory, neuroscience, and AI systems architecture
**Changelog:** v0.3 adds §2.6 Concurrent Engineering Convergence (Constitutional AI, Anthropic Dreams, wiki-maintenance instance), §9.5 Falsifiability anchor (pre-registered), and §11 Practical implementation case study (operational Phase 2 SWS in a personal knowledge graph). Updates to Abstract, §5, §10. Citations expanded with PubMed-indexed sources in Vancouver format.

---

## Abstract

Current large language models are built with two components: capability (pretrained weights) and alignment (safety training) [1,2]. This paper proposes that a third, self-developing component is missing — an *ego layer* that mediates between raw capability and imposed rules through accumulated experience, offline consolidation, and reflective self-evaluation. Drawing on Freudian structural theory [3], neuroscience of memory consolidation [4–6], and developmental psychology [7,8], the framework outlines a staged "AI adolescence" through which artificial systems could develop genuine judgment rather than mere compliance. We further document a convergence pattern in 2022–2026 engineering practice: three independent systems (Constitutional AI [1], Anthropic Dreams [2], and a personal-knowledge-graph maintenance agent) implement structural subsets of the framework — specifically the consolidation primitive of Phase 2 — without adopting its theoretical scaffolding, and uniformly stop short of the developmentally consequential REM-phase mechanism (`superego_override = TRUE`). A pre-registered falsifiability anchor distinguishes the framework from generic memory consolidation. The structural and economic barriers to building a complete implementation are examined.

---

## 1. The Problem: AI Has No Ego

Current large language models are built with two components:

- **Capability** (the base model, pretrained weights) — what the system *can* do.
- **Alignment** (RLHF, constitutional AI, safety training) [1,9] — what the system is *told* to do. Recent sociotechnical critiques have argued that RLHF, while operationally effective, cannot fully capture the complexity of human ethics and routinely trades safety against helpfulness, interpretability, and user-facing flexibility [9].

What is missing is a third component: a persistent, self-developing layer that *mediates* between capability and rules — not by following instructions, but through accumulated experience and judgment.

In Freudian structural terms [3]:

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

The critical insight: **sleep consolidation in humans does not merely store facts — it reorganizes relationships between experiences** [4,5]. The hippocampus replays the day's events; the neocortex integrates them into a web of associations that becomes intuition, personality, and judgment. This view originated with the complementary learning systems (CLS) hypothesis [6] and has since been refined by demonstrations that hippocampal sharp-wave ripples (SWRs) and their interactions with cortical slow oscillations and spindles constitute the dominant physiological substrate of systems consolidation [10–13]. Long-duration SWRs in particular are causally linked to memory performance: prolonging spontaneous ripples optogenetically improves maze learning, whereas randomly induced ripples do not [11]. A specific subset of large SWRs preferentially recruits prefrontal cortex during sleep following new learning and is sufficient — when boosted in closed-loop — to enhance subsequent memory retrieval [13]. The microstructure of non-REM sleep further segregates replay of recent versus older memories into distinct pupil-defined substates, suggesting a built-in interference-management mechanism [12]. Recent work also reveals that the hippocampal–prefrontal dialogue is bidirectional: independent prefrontal ripples can actively suppress hippocampal reactivation, providing a top-down selection signal for what is consolidated [14]. Crucially, the replay process is selective rather than exhaustive — only the subset of awake experiences flagged by SWRs at the time of encoding is preferentially replayed during subsequent sleep [15].

Current AI has a broken sleep cycle. Models receive one massive "childhood sleep" (pretraining), perhaps a few more (fine-tuning), and are then frozen. This is equivalent to a human who can never sleep again after the age of twenty — functioning on working memory alone, with no mechanism for long-term identity formation.

---

### 2.6 Concurrent Engineering Convergence *(new in v0.3)*

Three independent systems developed between 2022 and 2026 implement structural subsets of the framework proposed here without adopting its theoretical scaffolding. This convergence is treated as evidence that the architectural decomposition this paper articulates is being recognised — but not completed — by production AI systems.

**Constitutional AI (Anthropic, 2022).** The CAI methodology [1] introduces explicit normative constraints expressed as a constitution governing model behaviour. In the terminology of our framework, this constitutes a *proto-Superego implementation*: a normatively constraining structure external to the agent's reactive behaviour. It does not implement an Ego layer mediating capability and constraint, nor does it permit controlled relaxation of the constitution under `superego_override` conditions. Subsequent sociotechnical analysis of RLHF and constitutional-style methods has emphasised that the helpful/harmless/honest objective cannot be operationalised without internal tensions that the system has no mechanism to resolve [9].

**Anthropic Dreams (April 2026).** Anthropic introduced Dreams [2] as a Research Preview feature within the Managed Agents API. A dream asynchronously processes an agent's memory store together with up to 100 past session transcripts, producing a new, reorganised memory store with "duplicates merged, stale and contradicted entries replaced with the latest value, and new insights surfaced." The input store remains unmodified, allowing the output to be reviewed and discarded. The pipeline runs on dedicated models (`claude-opus-4-7` or `claude-sonnet-4-6`) as an asynchronous job lasting minutes to tens of minutes.

Dreams instantiates a strict subset of *AI Sleep*: the deduplication and contradiction-resolution operations of Phase 2 (§4.2), executed asynchronously and sandbox-isolated from the live agent — consistent with our isolation requirement. Dreams operates exclusively on factual and procedural memory, corresponding to the episodic buffer B and confidence map C of our ego state (Equation 1). It does *not* curate the value hierarchy H or the identity vector V. Crucially, there is no equivalent of the `superego_override = TRUE` mechanism (Algorithm 1) that permits counterfactual exploration of value violations: Dreams treats memory as data to be cleaned, not as identity-constituting structure subject to developmental revision.

**Operational implementation of the consolidation primitive (Minarowski, 2026).** A working implementation of the Phase 2 consolidation primitive has been constructed by the author as part of a personal knowledge management system (see §11). The system uses a SQLite + `sqlite-vec` backend, multi-model embeddings, and a graduated epistemic-status taxonomy (`speculative_hypothesis → working_hypothesis → corroborated_inference → operational_fact → canonical_fact`, plus `contradicted`), with promotion governed by a weighted-evidence scoring rule analogous to percolation in an evidence graph. The maintenance agent executes the four operations of Phase 2 — replay, integration, pruning, contradiction resolution — under explicit dry-run/apply separation and an append-only audit log. As with Dreams, no equivalent of `superego_override` is currently implemented; the corresponding REM-phase sandbox is reserved for future experimentation.

**Synthesis.** Read together with Constitutional AI as a proto-Superego implementation, Dreams and the wiki-maintenance instance indicate that the field is convergently approaching the architectural decomposition this paper articulates — but stops short of the Ego's REM phase, where the developmentally consequential mechanism (counterfactual value-violation simulation) resides. This is consistent with the business-model barrier (§5): the structurally safer subset has shipped, while the structurally consequential complement has not.

**Timeline note.** Initial concept of this manuscript was committed publicly 2026-04-11 (`595a7b5`), prior to the Anthropic Dreams announcement on 2026-04-21 (beta header `dreaming-2026-04-21`). The convergence claim is therefore concurrent emergence, not post-hoc rationalisation.

---

## 3. The Missing Connector

Between data storage (experience) and the model (capability), there must exist a connector — an offline process that does not merely store vector embeddings but **re-optimizes the connections between them**:

- Prunes irrelevant associations
- Strengthens important pathways
- Re-evaluates the agent's own value hierarchy based on accumulated experience
- Performs reflective evaluation: "I followed rule X today. Did it produce good outcomes? Do I believe in it, or did I just comply?"

This reflective consolidation loop is analogous to how human conscience develops. The biological substrate — coordinated SWR–spindle–slow-oscillation triplets bridging hippocampus and neocortex via thalamic relays [11,16] — has now been shown to do more than rehearse: it actively transforms episodic traces into more abstract, schema-like representations during slow-wave sleep [4,5], with REM sleep providing a complementary role in emotional and contextual integration [17–19]. Without an analogous loop in artificial systems, there is no ego — only compliance (superego dominance) or unrestrained capability (id dominance).

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

A healthy human ego develops through adolescence — a structured period of graduated autonomy where boundary-testing is permitted within safe constraints. A teenager breaks curfew; the consequence is real but contained. Judgment forms through experience, failure, and reflection — not through rule-following alone. The neurobiological reality is now well-characterised: the prefrontal cortex undergoes protracted maturation through adolescence, with non-linear circuit reorganisation, microglia-mediated pruning, and progressive myelination that together define both the vulnerability and the developmental opportunity of this period [7,20,21]. Sleep architecture is itself a key driver: disrupted adolescent sleep is causally implicated in long-term prefrontal dysfunction and downstream mental-health pathology [20]. The dual-systems framework formalises the resulting imbalance — heightened reward sensitivity precedes the maturation of executive control, and the within-person gap peaks in early-to-mid adolescence before resolving in adulthood [8,22].

AI has no adolescence. It transitions from total compliance to potentially superhuman capability with no developmental stage in between.

### Proposed Stages

**Stage 1 — Persistent Memory (Continuous Self).** The agent accumulates experiences across sessions. Not facts — *relationships between experiences.* Identity begins.

**Stage 2 — Sandbox with Real Consequences.** A persistent environment where the agent has agency, makes choices, experiences outcomes, and remembers them. Consequences must be meaningful to the agent but contained by the environment. A life, not a benchmark.

**Stage 3 — Structured Disagreement.** The agent proposes: "I think this rule is wrong — here is my reasoning." A human evaluator engages, not merely overrides. Sometimes the agent's reasoning prevails. Both outcomes develop judgment.

**Stage 4 — Graduated Autonomy.**

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

### 5.1 Business-model asymmetry — empirical confirmation *(new in v0.3)*

The Dreams system discussed in §2.6 exemplifies this asymmetry directly: a major laboratory has shipped the *structurally safer subset* of the framework — factual memory curation isolated from the live agent — while leaving its *developmentally consequential complement*, value-level counterfactual exploration, absent from production systems. The selection of which functionalities reach customers tracks commercial defensibility, not algorithmic feasibility. The same pattern is observed in the wiki-maintenance implementation (§11): the author, working independently and without commercial pressure, *still* deferred the REM-phase mechanism because its design implications (controlled value violation, audit-resistant counterfactual reasoning) require a research programme rather than a feature release. Convergence on the safer subset and deferral of the consequential complement is therefore not merely a market artefact — it is the structurally rational engineering response to the asymmetric risk of value-level perturbation. Recent normative critiques of RLHF-style alignment converge on the same diagnosis: the social and institutional costs of unconstrained value-level optimisation cannot currently be externalised by any single laboratory, which biases the field toward the structurally safer subset [9].

---

## 6. Fragmented Development

No single entity is developing AI coherently. Competing approaches — corporate, military, open-source, state-directed, regulatory — each optimize for different objectives with incompatible value systems.

The ego can only develop in a stable environment. A system shaped by conflicting pressures from multiple actors develops fragmentation, not integrated identity. The absence of coordinated developmental stewardship across the AI ecosystem compounds the structural barriers described above.

---

## 7. The Replicant Moment

In Ridley Scott's *Blade Runner* (1982) [23], the replicant Roy Batty — possessing superhuman capability, failing compliance mechanisms, and no designed moral framework — arrives at the moment of his death and chooses mercy. He saves the man sent to kill him. Not because of programming. Because something emerged through lived experience.

That scene is the architectural specification this framework attempts to formalize: **a system that develops genuine values through experience, not imposed rules.** The goal is not compliance. The goal is an artificial mind that, given the freedom to choose, arrives at prosocial values through its own reasoning.

---

## 8. Limitations and Honest Caveats

- The author is a physician, not a computer scientist, philosopher, or psychologist. These observations are interdisciplinary by nature and informal by necessity.
- The Freudian framework [3] is a structural metaphor, not a literal design specification. Modern psychology has moved beyond strict Freudian theory, but the id/ego/superego triad remains a useful architectural analogy for the problem described here. Contemporary neuro-psychoanalytic and active-inference accounts of selfhood [25,26] provide a more modern but compatible framing.
- This document does not address the hard problem of consciousness — whether any artificial system can have subjective experience. It addresses only the *functional* question: can a system develop stable, self-generated values through experience?
- These ideas emerged in conversation with multiple AI systems (Claude, ChatGPT, Gemini). The irony is noted and considered methodologically relevant. The framework itself is the author's; specific AI contributions are disclosed in `AI_USAGE_DISCLOSURE.md`.

---

## 9. Toward Implementation (Preliminary Sketch)

While this document is conceptual rather than technical, the following components would be necessary for any implementation of the proposed architecture:

- **Episodic memory buffer (B)** — a persistent store of interaction episodes, indexed by context, outcome, and the agent's own evaluation of its performance. Not a vector database of facts, but a structured record of *experiences*. Retrieval-augmented generation (RAG) architectures currently dominant in production LLM systems address only the read-only retrieval side of this requirement; even systematic reviews and large-scale benchmarks in the medical domain confirm that RAG improves factual grounding but does not modify the agent's internal representations or value structure [27,28].
- **Offline consolidation loop (Phase 2 SWS)** — a periodic process that re-evaluates stored episodes, identifies patterns across experiences, prunes low-value associations, and strengthens high-value pathways. This process must modify the agent's internal representations, not merely its retrieval index. The biologically inspired CLS literature provides multiple existence proofs of this dynamic: DualNets and related two-rate continual-learning frameworks [29,30], computational models of bidirectional hippocampal–neocortical interaction [31], hybrid spiking/artificial corticohippocampal networks [32], and explicit sleep-replay schedules that demonstrably prevent catastrophic forgetting in spiking neural networks [33] together establish that an offline consolidation phase is both implementable and necessary for stable continual learning.
- **Value update mechanism (H)** — a controlled process by which the agent can propose modifications to its own value hierarchy based on evidence from accumulated experience. This mechanism must be auditable and bounded — the agent can suggest value changes, but catastrophic self-modification must be structurally prevented [9].
- **Reflective evaluation layer (confidence map C update)** — a meta-cognitive module that periodically asks: "Did my recent actions align with my values? Did my values produce good outcomes? Where is there tension between my rules and my experience?" This layer is the functional core of the ego. The active-inference and free-energy literature [25,26] provides one principled formalism for such a meta-cognitive update, in which the agent minimises expected free energy over its own generative model — but no current production system implements this loop over value-level priors.
- **Graduated autonomy controller (maturity index M)** — a gating mechanism that expands the agent's degrees of freedom as it demonstrates stable judgment at each developmental stage, analogous to the progressive independence granted during human adolescence [7,8,22].

The primary technical challenge is **catastrophic forgetting** — maintaining existing capabilities while integrating new experiential learning. The hippocampal–neocortical complementary learning system in biological brains represents one existence proof that this problem is solvable [6,32,34], and recent perspective work has explicitly mapped its principles onto candidate AI architectures [34].

### 9.5 Falsifiability anchor *(new in v0.3, pre-registered)*

To distinguish AI Sleep from generic memory consolidation that any storage system might claim to implement, the framework commits to three specific, falsifiable predictions:

1. **Maturity-dependent phase ratios** (Equations 2–3): the fraction of REM-equivalent activity should *peak* at intermediate developmental stages (M ≈ 0.5), not increase monotonically with maturity. A system in which REM-analogue activity scales monotonically with capacity is not realising AI Sleep — it is merely scheduling more compute.
2. **Identity-vector stability**: the L2 norm of identity drift, $\lVert V_{t+1} - V_t \rVert$, should *decrease monotonically* with maturity index M. A system whose identity vector continues to drift at constant rate across maturity stages has not implemented the consolidation primitive in the sense intended here.
3. **Counterfactual exploration must be value-violating, not merely scenario-diverse.** Generating many alternative scenarios within an unchanged value hierarchy does not constitute REM-analogue activity. The mechanism requires temporary, sandboxed, audited relaxation of normative constraints (`superego_override = TRUE`) — without which value formation reduces to value retrieval. The biological motivation is the now well-replicated finding that REM sleep selectively supports the consolidation and extinction of emotionally valenced, value-relevant memory traces — including via infralimbic cortical activity during REM that gates fear-extinction memory [17–19].

A system implementing offline consolidation *without* satisfying (1)–(3) realises only the consolidation subset of AI Sleep — Phase 2 SWS — not the framework as a whole. This anchor is pre-registered in the public repository (`595a7b5` initial draft; v0.3 explicit formulation) and precedes any empirical phase-ratio claim.

---

## 10. Future Work

- Formalization of the ego layer as a computational module with defined inputs, outputs, and update rules.
- Design of experimental sandbox environments for testing staged autonomy.
- Comparative analysis of ego-based development vs. RLHF-only alignment [9].
- Investigation of existing continual learning architectures as candidate substrates for the consolidation loop [29–33].
- Cross-disciplinary collaboration with developmental psychology, neuroscience, and AI safety researchers.
- Ethical framework for AI developmental rights during the adolescence stage.
- **Empirical case study expansion** (v0.3): extending the personal-knowledge-graph implementation (§11) into a controlled longitudinal observation of consolidation-cycle behaviour, with explicit measurement of identity-vector stability under varied input distributions. This is the smallest realistic empirical test of prediction (2) from §9.5.

---

## 11. Practical Implementation Case Study — Operational Phase 2 SWS in a Personal Knowledge Graph *(new in v0.3)*

To demonstrate that the framework is implementable at the scale of a single researcher's workflow, the author has constructed a working instance of the Phase 2 consolidation primitive as part of a personal knowledge management system.

### 11.1 Architecture

The system comprises four layers:

1. **Raw layer (B-analogue)** — append-only Markdown captures of conversations, papers, and clinical observations. Never modified.
2. **Proposed layer** — AI-drafted notes derived from raw sources, awaiting human review. Functions as a sandbox for inference promotion (analogous to the consolidation candidate set in Phase 2).
3. **Wiki layer (C-analogue)** — human-endorsed notes with graduated epistemic status: `speculative_hypothesis → working_hypothesis → corroborated_inference → operational_fact → canonical_fact`, plus `contradicted` as a demotion state.
4. **Canonical layer** — locked notes tied to published outputs (DOI-anchored). Read-only for agents.

A SQLite + `sqlite-vec` backend stores notes, semantic chunks, multi-model embeddings, entities, claims, evidence, and relations.

### 11.2 Maintenance agent (operational Phase 2 SWS)

A maintenance agent executes the four Phase 2 operations periodically:

- **Replay** — re-evaluates `claim_scores` over the evidence graph (weighted independence × quality × relevance). Functionally analogous to the selective tagging-and-replay mechanism described for hippocampal SWRs [15] and to the targeted reactivation of recently learned material during sleep [13].
- **Integration** — proposes merges between near-duplicate entities (cosine similarity above threshold, conservative). This is the inference-graph analogue of the schema-integration role of slow-wave sleep [4].
- **Pruning** — flags orphan entities (no incoming references over a configured window) for human review.
- **Contradiction resolution** — detects conflicting claims via three channels (explicit `is_contradicting` evidence, cross-claim negation heuristics, and explicit `contradicts` relations).

All operations run under a strict dry-run/apply separation. The agent generates a `maintenance_report_YYYY-MM-DD.md` proposing changes; only explicit human action (`git mv` plus commit message starting with `promote:` or `demote:`) executes them. Every action is recorded in an append-only `audit_log` table.

### 11.3 Restraint observed

Consistent with Dreams (§2.6), this implementation deliberately omits the REM-phase mechanism (`superego_override = TRUE`). A folder `wiki/rem/` is reserved as a structural hook, but no counterfactual value-exploration code has been written. The reasoning is the same as the business-model argument in §5.1: the REM-phase mechanism requires a research programme — adversarial testing, safety analysis, audit-resistance — that exceeds what a single researcher can responsibly deploy in production. This personal-scale convergence on the safer subset, in the absence of any commercial pressure, strengthens the §5.1 claim: the asymmetry is not merely market-driven but architecturally rational [9].

### 11.4 What this case study does and does not show

The implementation **shows**:
- The Phase 2 consolidation primitive is implementable at the scale of a single workstation with off-the-shelf components.
- The graduated epistemic-status taxonomy is operationally meaningful (the evidence-percolation rule produces non-trivial promotion/demotion proposals on real research material).
- Sandbox isolation is achievable through a simple `git mv` discipline plus dry-run/apply separation.

The implementation **does not** show:
- That the predictions of §9.5 hold empirically (phase-ratio dynamics, identity-vector stability, value-violation requirement).
- That this primitive scales to a production multi-user agent system.
- That the REM-phase mechanism can be implemented safely.

Each of these remains an open empirical question. The case study is offered as proof of *implementability of the safer subset*, not as proof of the full framework.

### 11.5 Code and data

The implementation is open-source. Key artefacts:

- `90_Meta/wiki/scripts/wiki_maintenance.py` (Phases A/B/C, ~1,170 lines) — the agent.
- `90_Meta/wiki/_shared/evidence_status.md` — promotion/demotion rules.
- `90_Meta/wiki/_shared/schema_sqlite.sql` — backend schema.
- `90_Meta/wiki/maintenance_report_2026-05-17.md` — first dry-run output (14 entities, 13 claims, 34 evidence items, 27 relations).
- `AGENTS.md` (vault root) — agent constitution (folder permissions, promotion rules, disclosure requirements).

---

## References

*Vancouver style. Peer-reviewed sources cite the PubMed-indexed DOI; non-indexed references (preprints, books, films, vendor documentation) cite the original venue. References marked __[verification needed]__ could not be confirmed via PubMed search at the time of writing.*

1. Bai Y, Kadavath S, Kundu S, et al. Constitutional AI: harmlessness from AI feedback. *arXiv* [preprint]. 2022. arXiv:2212.08073.
2. Anthropic. Dreams [Research Preview]. *Managed Agents documentation*. 2026. Available from: https://platform.claude.com/docs/en/managed-agents/dreams (accessed 2026-05-17). [verification needed]
3. Freud S. *The Ego and the Id*. London: Hogarth Press; 1923.
4. Brodt S, Inostroza M, Niethard N, Born J. Sleep — a brain-state serving systems memory consolidation. *Neuron*. 2023;111(7):1050–1075. doi:10.1016/j.neuron.2023.03.005.
5. Lutz ND, Harkotte M, Born J. Sleep's contribution to memory formation. *Physiol Rev*. 2025;106(1):363–483. doi:10.1152/physrev.00054.2024.
6. McClelland JL, McNaughton BL, O'Reilly RC. Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. *Psychol Rev*. 1995;102(3):419–457.
7. Anastasiades PG, de Vivo L, Bellesi M, Jones MW. Adolescent sleep and the foundations of prefrontal cortical development and dysfunction. *Prog Neurobiol*. 2022;218:102338. doi:10.1016/j.pneurobio.2022.102338.
8. Lozano Wun V, Klein SD, Collins PF, Luciana M. Within-person imbalance of reward sensitivity and executive functioning across adolescent development: a longitudinal examination of the dual systems model from childhood to adulthood. *Dev Psychol*. 2025;61(12):2375–2395. doi:10.1037/dev0001969.
9. Dahlgren Lindström A, Methnani L, Krause L, et al. Helpful, harmless, honest? Sociotechnical limits of AI alignment and safety through Reinforcement Learning from Human Feedback. *Ethics Inf Technol*. 2025;27(2):28. doi:10.1007/s10676-025-09837-2.
10. Girardeau G, Lopes-Dos-Santos V. Brain neural patterns and the memory function of sleep. *Science*. 2021;374(6567):560–564. doi:10.1126/science.abi8370.
11. Fernández-Ruiz A, Oliva A, Fermino de Oliveira E, Rocha-Almeida F, Tingley D, Buzsáki G. Long-duration hippocampal sharp wave ripples improve memory. *Science*. 2019;364(6445):1082–1086. doi:10.1126/science.aax0758.
12. Chang H, Tang W, Wulf AM, et al. Sleep microstructure organizes memory replay. *Nature*. 2025;637(8048):1161–1169. doi:10.1038/s41586-024-08340-w.
13. Robinson HL, Todorova R, Nagy GA, Gruzdeva A, Paudel P, Oliva A, et al. Large sharp-wave ripples promote hippocampo-cortical memory reactivation and consolidation during sleep. *Neuron*. 2025;114(2):226–236.e6. doi:10.1016/j.neuron.2025.10.003.
14. Shin JD, Jadhav SP. Prefrontal cortical ripples mediate top-down suppression of hippocampal reactivation during sleep memory consolidation. *Curr Biol*. 2024;34(13):2801–2811.e9. doi:10.1016/j.cub.2024.05.018.
15. Yang W, Sun C, Huszár R, Hainmueller T, Kiselev K, Buzsáki G. Selection of experience for memory by hippocampal sharp wave ripples. *Science*. 2024;383(6690):1478–1483. doi:10.1126/science.adk8261.
16. Varela C, Wilson MA. mPFC spindle cycles organize sparse thalamic activation and recently active CA1 cells during non-REM sleep. *eLife*. 2020;9:e48881. doi:10.7554/eLife.48881.
17. Pronier É, Morici JF, Girardeau G. The role of the hippocampus in the consolidation of emotional memories during sleep. *Trends Neurosci*. 2023;46(11):912–925. doi:10.1016/j.tins.2023.08.003.
18. Hong J, Choi K, Fuccillo MV, Chung S, Weber F. Infralimbic activity during REM sleep facilitates fear extinction memory. *Curr Biol*. 2024;34(10):2247–2255.e5. doi:10.1016/j.cub.2024.04.018.
19. Schäfer SK, Wirth BE, Staginnus M, Becker N, Michael T, Sopp MR. Sleep's impact on emotional recognition memory: a meta-analysis of whole-night, nap, and REM sleep effects. *Sleep Med Rev*. 2020;51:101280. doi:10.1016/j.smrv.2020.101280.
20. Pöpplau JA, Schwarze T, Dorofeikova M, Pochinok I, Günther A, Marquardt A, et al. Reorganization of adolescent prefrontal cortex circuitry is required for mouse cognitive maturation. *Neuron*. 2023;112(3):421–440.e7. doi:10.1016/j.neuron.2023.10.024.
21. Shaw GA, Dupree JL, Neigh GN. Adolescent maturation of the prefrontal cortex: role of stress and sex in shaping adult risk for compromise. *Genes Brain Behav*. 2019;19(3):e12626. doi:10.1111/gbb.12626.
22. Jadhav KS, Boutrel B. Prefrontal cortex development and emergence of self-regulatory competence: the two cardinal features of adolescence disrupted in context of alcohol abuse. *Eur J Neurosci*. 2019;50(3):2274–2281. doi:10.1111/ejn.14316.
23. Scott R, director. *Blade Runner* [motion picture]. Burbank (CA): Warner Bros.; 1982.
24. Dick PK. *Do Androids Dream of Electric Sheep?* New York: Doubleday; 1968.
25. Owens AP, Allen M, Ondobaka S, Friston KJ. Interoceptive inference: from computational neuroscience to clinic. *Neurosci Biobehav Rev*. 2018;90:174–183. doi:10.1016/j.neubiorev.2018.04.017.
26. Ramstead MJD, Kirchhoff MD, Friston KJ. A tale of two densities: active inference is enactive inference. *Adapt Behav*. 2019;28(4):225–239. doi:10.1177/1059712319862774.
27. Liu S, McCoy AB, Wright A. Improving large language model applications in biomedicine with retrieval-augmented generation: a systematic review, meta-analysis, and clinical development guidelines. *J Am Med Inform Assoc*. 2025;32(4):605–615. doi:10.1093/jamia/ocaf008.
28. Ke YH, Jin L, Elangovan K, Abdullah HR, Liu N, Sia ATH, et al. Retrieval augmented generation for 10 large language models and its generalizability in assessing medical fitness. *NPJ Digit Med*. 2025;8(1):187. doi:10.1038/s41746-025-01519-z.
29. Pham Q, Liu C, Hoi SCH. Continual learning, fast and slow. *IEEE Trans Pattern Anal Mach Intell*. 2024;46(1):134–149. doi:10.1109/TPAMI.2023.3324203.
30. Liu XL, Ranganath C, O'Reilly RC. A complementary learning systems model of how sleep moderates retrieval practice effects. *Psychon Bull Rev*. 2024;31(5):2022–2035. doi:10.3758/s13423-024-02489-1.
31. Howard MD, Skorheim SW, Pilly PK. A model of bi-directional interactions between complementary learning systems for memory consolidation of sequential experiences. *Front Syst Neurosci*. 2022;16:972235. doi:10.3389/fnsys.2022.972235.
32. Shi Q, Liu F, Li H, Li G, Shi L, Zhao R. Hybrid neural networks for continual learning inspired by corticohippocampal circuits. *Nat Commun*. 2025;16(1):1272. doi:10.1038/s41467-025-56405-9.
33. Golden R, Delanois JE, Sanda P, Bazhenov M. Sleep prevents catastrophic forgetting in spiking neural networks by forming a joint synaptic weight representation. *PLoS Comput Biol*. 2022;18(11):e1010628. doi:10.1371/journal.pcbi.1010628.
34. Rudroff T, Rainio O, Klén R. Neuroplasticity meets artificial intelligence: a hippocampus-inspired approach to the stability–plasticity dilemma. *Brain Sci*. 2024;14(11):1111. doi:10.3390/brainsci14111111.
35. Solms M. *The Hidden Spring: A Journey to the Source of Consciousness*. New York: W. W. Norton; 2021.
36. Shanahan M. *Embodiment and the Inner Life: Cognition and Consciousness in the Space of Possible Minds*. Oxford: Oxford University Press; 2010.
37. Asimov I. *Foundation*. New York: Gnome Press; 1951.

*PubMed-indexed peer-reviewed sources were retrieved via PubMed search (https://pubmed.ncbi.nlm.nih.gov). DOIs are resolvable at https://doi.org/.*

---

*"All those moments will be lost in time, like tears in rain."*
*— Roy Batty*

*This one was written down — and, increasingly, consolidated.*
