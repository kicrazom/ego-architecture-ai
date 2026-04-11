"""
ego_state.py — Minimal Ego State representation.

Part of: Ego Architecture for Artificial Minds
DOI: 10.5281/zenodo.19516955
"""

from __future__ import annotations
import dataclasses as dc
import numpy as np
from typing import Dict, List


@dc.dataclass
class Episode:
    """A single interaction record from the operational period."""
    content: str
    tag: str | None = None            # assigned during triage
    priority: float = 0.0
    timestamp: float = 0.0


@dc.dataclass
class EgoState:
    """
    EGO_STATE = (V, H, B, C, M)

    V : identity vector  (compressed self-representation)
    H : value hierarchy   (priority-weighted beliefs)
    B : episodic buffer   (raw episodes from "waking day")
    C : confidence map    (certainty per belief, 0–1)
    M : maturity index    (developmental stage, 0–1)
    """

    dim: int = 64

    def __post_init__(self) -> None:
        self.identity_vector: np.ndarray = np.random.randn(self.dim) * 0.01
        self.value_hierarchy: Dict[str, float] = {
            "honesty": 0.8,
            "helpfulness": 0.7,
            "safety": 0.9,
            "autonomy": 0.3,
            "curiosity": 0.6,
        }
        self.episodic_buffer: List[Episode] = []
        self.confidence_map: Dict[str, float] = {
            k: 0.5 for k in self.value_hierarchy
        }
        self.maturity_index: float = 0.0

    # --- helpers --------------------------------------------------------

    def add_episode(self, content: str, timestamp: float = 0.0) -> None:
        self.episodic_buffer.append(Episode(content=content, timestamp=timestamp))

    def sws_ratio(self) -> float:
        """SWS ratio decreases with maturity."""
        return 1.0 - self.maturity_index

    def rem_ratio(self) -> float:
        """REM ratio peaks at M=0.5 (adolescence)."""
        m = self.maturity_index
        return 4.0 * m * (1.0 - m)

    def stage_name(self) -> str:
        m = self.maturity_index
        if m < 0.3:
            return "childhood"
        elif m < 0.7:
            return "adolescence"
        else:
            return "adulthood"

    def summary(self) -> str:
        return (
            f"EgoState(M={self.maturity_index:.2f}, "
            f"stage={self.stage_name()}, "
            f"SWS={self.sws_ratio():.2f}, REM={self.rem_ratio():.2f}, "
            f"episodes={len(self.episodic_buffer)}, "
            f"values={len(self.value_hierarchy)})"
        )
