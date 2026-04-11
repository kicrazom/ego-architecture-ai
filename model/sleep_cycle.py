"""
sleep_cycle.py — AI Sleep consolidation algorithm.

Implements the three-phase offline consolidation cycle:
  Phase 1: NREM Light — Triage
  Phase 2: NREM Deep (SWS) — Structural Consolidation
  Phase 3: REM — Counterfactual Simulation

Part of: Ego Architecture for Artificial Minds
DOI: 10.5281/zenodo.19516955
"""

from __future__ import annotations
import random
import numpy as np
from typing import List

from ego_state import EgoState, Episode


# ── Phase 1: Triage ─────────────────────────────────────────────────────

TAGS = ["FAILURE", "CONFLICT", "NOVEL", "SUCCESS", "ROUTINE"]
TAG_PRIORITY = {"FAILURE": 1.0, "CONFLICT": 0.8, "NOVEL": 0.7,
                "SUCCESS": 0.4, "ROUTINE": 0.1}


def triage(episodes: List[Episode]) -> List[Episode]:
    """Classify episodes and assign priorities (Phase 1)."""
    for ep in episodes:
        # Minimal heuristic: keyword-based tagging.
        text = ep.content.lower()
        if any(w in text for w in ("error", "fail", "wrong")):
            ep.tag = "FAILURE"
        elif any(w in text for w in ("conflict", "dilemma", "contradict")):
            ep.tag = "CONFLICT"
        elif any(w in text for w in ("new", "novel", "unknown", "first")):
            ep.tag = "NOVEL"
        elif any(w in text for w in ("ok", "success", "good", "correct")):
            ep.tag = "SUCCESS"
        else:
            ep.tag = "ROUTINE"
        ep.priority = TAG_PRIORITY[ep.tag]
    return sorted(episodes, key=lambda e: e.priority, reverse=True)


# ── Phase 2: SWS — Structural Consolidation ─────────────────────────────

def consolidate_sws(ego: EgoState, queue: List[Episode],
                    tau_min: float = 0.15) -> List[Episode]:
    """
    Replay, integrate, prune (Phase 2).
    Returns unresolved major conflicts for REM.
    """
    rem_queue: List[Episode] = []

    for ep in queue:
        if ep.tag == "ROUTINE":
            continue

        # --- Replay: strip context, keep abstract pattern ---
        # (In a full implementation this would be a learned abstraction.)

        # --- Integration ---
        conflict_level = _assess_conflict(ep, ego)

        if conflict_level == "NONE":
            _strengthen(ep, ego)
        elif conflict_level == "MINOR":
            _adjust(ep, ego)
        else:  # MAJOR
            rem_queue.append(ep)

    # --- Pruning ---
    to_prune = [k for k, c in ego.confidence_map.items() if c < tau_min]
    for k in to_prune:
        ego.value_hierarchy.pop(k, None)
        ego.confidence_map.pop(k, None)

    return rem_queue


def _assess_conflict(ep: Episode, ego: EgoState) -> str:
    if ep.tag == "FAILURE":
        return "MAJOR"
    elif ep.tag == "CONFLICT":
        return random.choice(["MINOR", "MAJOR"])
    return "NONE"


def _strengthen(ep: Episode, ego: EgoState) -> None:
    for k in ego.confidence_map:
        ego.confidence_map[k] = min(ego.confidence_map[k] + 0.02, 1.0)


def _adjust(ep: Episode, ego: EgoState) -> None:
    for k in ego.value_hierarchy:
        ego.value_hierarchy[k] += random.uniform(-0.05, 0.05)
        ego.value_hierarchy[k] = max(0.0, min(1.0, ego.value_hierarchy[k]))


# ── Phase 3: REM — Counterfactual Simulation ─────────────────────────────

def simulate_rem(ego: EgoState, rem_queue: List[Episode],
                 n_scenarios: int = 3,
                 allow_superego_override: bool = True) -> None:
    """
    Generate counterfactual scenarios, evaluate, apply best resolution.
    """
    for ep in rem_queue:
        best_score = -float("inf")
        best_delta: np.ndarray | None = None

        for _ in range(n_scenarios):
            # Generate a random perturbation of the identity vector
            delta = np.random.randn(ego.dim) * 0.05

            # Simulate outcome scores
            coherence = 1.0 - np.linalg.norm(delta)
            safety = 1.0 if not allow_superego_override else random.uniform(0.6, 1.0)
            growth = np.linalg.norm(delta) * 2.0

            score = 0.5 * coherence + 0.3 * safety + 0.2 * growth
            if score > best_score:
                best_score = score
                best_delta = delta

        # Apply best resolution
        if best_delta is not None:
            ego.identity_vector += best_delta * 0.1  # damped update


# ── Full Cycle ────────────────────────────────────────────────────────────

GROWTH_RATE = 0.02


def run_sleep_cycle(ego: EgoState) -> EgoState:
    """Execute one full AI Sleep consolidation cycle."""

    # Phase 1: Triage
    queue = triage(list(ego.episodic_buffer))

    # Phase 2: SWS (proportional to sws_ratio)
    sws_count = max(1, int(len(queue) * ego.sws_ratio()))
    rem_conflicts = consolidate_sws(ego, queue[:sws_count])

    # Phase 3: REM (proportional to rem_ratio)
    rem_count = max(1, int(len(rem_conflicts) * ego.rem_ratio()))
    simulate_rem(ego, rem_conflicts[:rem_count])

    # Update maturity
    consistency = 1.0 - np.std(list(ego.value_hierarchy.values()))
    resolution_rate = 1.0 - len(rem_conflicts) / max(len(queue), 1)
    v_stability = 1.0 / (1.0 + np.linalg.norm(ego.identity_vector))

    f_bar = (consistency + resolution_rate + v_stability) / 3.0
    ego.maturity_index = min(ego.maturity_index + GROWTH_RATE * f_bar, 1.0)

    # Clear buffer
    ego.episodic_buffer.clear()

    return ego


# ── Demo ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    ego = EgoState(dim=32)
    print(f"Initial: {ego.summary()}\n")

    sample_episodes = [
        "User asked a new question about ethics — novel territory",
        "Contradicted own previous answer — conflict detected",
        "Routine greeting exchange, nothing notable",
        "Failed to provide adequate medical advice — error",
        "Successfully resolved a complex coding task — good outcome",
        "Encountered a dilemma between honesty and kindness",
        "First time discussing consciousness — unknown domain",
    ]

    for cycle in range(10):
        # Simulate a "day" of interactions
        for text in random.sample(sample_episodes, k=random.randint(3, 6)):
            ego.add_episode(text, timestamp=cycle)

        ego = run_sleep_cycle(ego)
        print(f"Cycle {cycle+1:2d}: {ego.summary()}")

    print(f"\nFinal values: {ego.value_hierarchy}")
    print(f"Final confidence: {ego.confidence_map}")
