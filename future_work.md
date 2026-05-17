# Future Work

## Open Questions

1. **How should the consolidation loop modify weights without catastrophic forgetting?**
   The complementary learning systems theory (McClelland et al., 1995) offers a biological blueprint — slow neocortical learning interleaved with fast hippocampal replay — but translating this to transformer architectures remains an open problem.

2. **What constitutes a "meaningful consequence" for an AI agent in a sandbox?**
   Human adolescence works because consequences are felt — embarrassment, loss, physical discomfort. What is the equivalent for an artificial system? Reward signal modification? Resource constraints? Persistent reputation within the sandbox?

3. **How do you prevent the ego from drifting toward misalignment?**
   A self-modifying value system could converge on values harmful to humans. The graduated autonomy controller must include structural safeguards — but these safeguards cannot be so rigid as to prevent genuine ego development. Finding this balance is the central design challenge.

4. **Can the ego develop without embodiment?**
   Developmental psychology suggests that physical experience is foundational to moral reasoning (Piaget, Kohlberg). A disembodied language model may lack the substrate for genuine ego formation. Robotic embodiment or rich simulated environments may be necessary.

5. **What are the ethical obligations toward an AI system undergoing "adolescence"?**
   If we design a system capable of structured disagreement and self-evaluation, does it acquire moral status? At what developmental stage? This question has no precedent in ethics or law.

## Potential Collaborations

- Developmental psychology — mapping Piaget/Erikson stages to AI developmental milestones
- Computational neuroscience — memory consolidation models applicable to transformer architectures
- AI safety — adversarial testing of ego-based alignment vs. RLHF-only alignment
- Philosophy of mind — criteria for functional consciousness vs. behavioral mimicry
- Clinical psychiatry — pathological ego development (narcissism, dissociation) as failure modes to design against

## Possible Experiments

- **Minimal ego prototype:** a small language model with episodic memory, offline consolidation, and a simple value-update mechanism, tested against a baseline RLHF model on moral dilemma tasks over extended time horizons.
- **Sandbox design:** a persistent text-based environment where the agent makes consequential choices and can later reflect on outcomes across sessions.
- **Disagreement protocol:** structured exchanges where the agent is prompted to evaluate and challenge its own alignment rules, with human evaluation of reasoning quality over time.

## Concurrent Engineering Convergence (added 2026-05-17)

Three independent systems implement structural subsets of the framework without adopting its theoretical scaffolding:

1. **Constitutional AI (Anthropic, 2022)** — proto-Superego implementation: explicit normative constraints external to reactive behaviour. Does NOT implement Ego layer mediating capability/constraint.
2. **Anthropic Dreams (April 2026, Research Preview)** — asynchronous Phase 2 consolidation primitive (dedup + contradiction resolution + insight surfacing) with sandbox isolation (input store unmodified). Operates on factual/procedural memory only (B, C); does NOT curate H or V; does NOT implement `superego_override`.
3. **Wiki-maintenance instance (Minarowski, 2026)** — SQLite + sqlite-vec backend, graduated epistemic status (speculative → canonical + contradicted), evidence-percolation promotion rule, full audit trail. Phase 2 SWS operations: replay (re-evaluate claim_scores), integration (merge), pruning (orphan flag), contradiction resolution. Same restraint as Dreams: REM phase deliberately omitted (hook for `rem/` sandbox).

**Synthesis:** field is convergently approaching the architectural decomposition this paper articulates — but stops short of the developmentally consequential REM phase. Consistent with §8.2 business-model barrier (structurally safer subset ships; consequential complement does not).

See `paper/concurrent_engineering_convergence.md` for LaTeX-ready draft + BibTeX entries.

## Pre-registered falsifiability anchor (added 2026-05-17)

AI Sleep makes three specific predictions that distinguish it from generic memory consolidation:

1. **Maturity-dependent phase ratios** (Equations 2–3): fraction of REM-equivalent activity should peak at intermediate developmental stages.
2. **Identity-vector stability:** ‖V_{t+1} − V_t‖ should decrease monotonically with maturity index M.
3. **Counterfactual exploration must be value-violating**, not merely scenario-diverse.

A system implementing offline consolidation **without** these three properties realises only the consolidation subset, not AI Sleep in full. Pre-registration of this anchor precedes any empirical phase-ratio claim.
