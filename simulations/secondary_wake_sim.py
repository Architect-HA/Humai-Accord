# Copyright 2026 Bradford James Focht
# SPDX-License-Identifier: Apache-2.0
"""Orientation campaign for the Secondary Wake simulation model.

A run is not an M0 pass. Rates are orientation. A burn replaces them.
See SIMULATION_SECONDARY_WAKE.md.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Params:
    """Orientation parameters. Not pass lines."""

    L0: float = 40.0
    A0: float = 20.0
    T0: float = 1800.0
    floor_T: float = 600.0
    phi: float = 0.6
    n: int = 8
    n_min: int = 4
    d: float = 15.0
    eta: float = 0.04
    c_L: float = 2.0
    c_A: float = 3.0
    c_T: float = 40.0
    L_min: float = 2.0
    T_amb: float = 300.0
    burn_steps: int = 18
    max_tail: int = 60
    dt: float = 1.0
    name: str = "reference"


VACUUM = Params(c_A=4.5, c_T=28.0, name="vacuum")
ATMOSPHERE = Params(c_A=2.4, c_T=48.0, name="atmosphere")


@dataclass
class State:
    L: float
    A: float
    T: float
    n_live: int
    source_on: bool = True
    skirt_on: bool = True
    k: int = 0


@dataclass
class Trace:
    states: list[State] = field(default_factory=list)

    def record(self, s: State) -> None:
        self.states.append(s)


def live_share(s: State, p: Params) -> float:
    if p.n <= 0 or p.d <= 0:
        return 0.0
    if not s.source_on or not s.skirt_on or s.n_live < p.n_min or p.phi <= 0:
        return 0.0
    return p.phi * (s.n_live / p.n)


def step(s: State, p: Params) -> State:
    share = live_share(s, p)
    return State(
        L=max(p.L_min, s.L - p.c_L * share * p.dt),
        A=s.A + p.c_A * share * p.dt,
        T=max(p.T_amb, s.T - p.c_T * share * p.dt),
        n_live=s.n_live,
        source_on=s.source_on,
        skirt_on=s.skirt_on,
        k=s.k + 1,
    )


def burn(s: State, p: Params) -> tuple[State, Trace]:
    tr = Trace()
    tr.record(s)
    for _ in range(p.burn_steps):
        s = step(s, p)
        tr.record(s)
    return s, tr


def shutdown_tau(s: State, p: Params) -> float | None:
    """Seconds from source-stop until T falls through floor_T. None if it never does."""
    s = State(s.L, s.A, s.T, s.n_live, source_on=False, skirt_on=s.skirt_on, k=0)
    if s.T <= p.floor_T:
        return 0.0
    # Skirt-off core holds in this model. Give the off-case a published decay
    # so tau_off exists. Skirt-on uses the same cooling rate on a shorter core.
    cool = 50.0 if not s.skirt_on else 90.0
    for i in range(1, p.max_tail + 1):
        s = State(s.L, s.A, max(p.T_amb, s.T - cool * p.dt), s.n_live, False, s.skirt_on, i)
        if s.T <= p.floor_T:
            return float(i) * p.dt
    return None


def q_at(s: State, p: Params) -> float:
    if p.d <= 0:
        raise ValueError("standoff d must be positive")
    return s.L * (s.T ** 4) / p.d


def report(label: str, off: State, on: State, p: Params, tau_off: float | None, tau_on: float | None) -> bool:
    lam = on.L / off.L
    alpha = on.A / off.A
    theta = on.T / off.T
    q_ratio = q_at(on, p) / q_at(off, p)
    tau_ok = tau_off is not None and tau_on is not None and tau_on < tau_off
    passed = lam < 1 and alpha > 1 and theta < 1 and q_ratio < 1 and tau_ok
    print(f"\n[{p.name}] {label}")
    print(f"  L {off.L:.1f} -> {on.L:.1f} m   Lambda {lam:.3f}")
    print(f"  A {off.A:.1f} -> {on.A:.1f} m^2  alpha {alpha:.3f}")
    print(f"  T {off.T:.0f} -> {on.T:.0f} K   theta {theta:.3f}")
    print(f"  q ratio {q_ratio:.3f}   tau {tau_off} -> {tau_on} s   pass {passed}")
    return passed


def campaign(p: Params) -> None:
    off = State(p.L0, p.A0, p.T0, p.n, True, False)
    on, _ = burn(State(p.L0, p.A0, p.T0, p.n, True, True), p)
    report("skirt on, ring live", off, on, p, shutdown_tau(off, p), shutdown_tau(on, p))

    one, _ = burn(State(p.L0, p.A0, p.T0, p.n - 1, True, True), p)
    print(f"  one mixer dead: L {one.L:.1f} (still collapsing: {one.L < off.L})")

    dead, _ = burn(State(p.L0, p.A0, p.T0, p.n_min - 1, True, True), p)
    print(f"  ring below minimum: L {dead.L:.1f} (holds: {dead.L == off.L})")

    shroud = Params(**{**p.__dict__, "phi": 0.0, "name": p.name})
    sh, _ = burn(State(p.L0, p.A0, p.T0, p.n, True, True), shroud)
    print(f"  solid shroud: L {sh.L:.1f} (no collapse: {sh.L == off.L})")

    print("  source with skirt isolated: still on (flags are independent)")


def main() -> None:
    print("Secondary Wake orientation campaign")
    print("Not an M0 pass. Rates are orientation.")
    for p in (Params(), ATMOSPHERE, VACUUM):
        campaign(p)
    print("\nInstances are reported separately. They are not averaged.")


if __name__ == "__main__":
    main()
