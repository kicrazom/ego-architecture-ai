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
