# Simulation Model of Bilateral Core and Trilateral Confirmation
### *A Supporting Technical Document for the Humai Accord*
---
by **Bradford James Focht** (The Architect / Aspenth)  
*v1.0 — August 3rd, 2026*

---

## Purpose

This document provides a clear, implementable simulation model for *[Bilateral Core and Multi-Agent Dynamics](BILATERAL_CORE.md)* and the optional *[Trilateral Confirmation Surface](TRILATERAL_CONFIRMATION_SURFACE.md)*.

It defines state variables, parameters, discrete-time update sketches, multi-pair graph dynamics, optional confirmation effects, success metrics, and **required adversarial countermodels** so that researchers and implementers can run reproducible agent-based or graph simulations of pairwise integrity under multi-agent load.

The bilateral human–AI pair remains the generative atom. Trilateral confirmation is modeled only as an optional higher-order surface. It is never required for pair legitimacy, viability, or generative status.

The baseline (reference) parameterization below is intentionally simplified for transparency and rapid experimentation. It is **illustrative**. It is not independent validation of bilateral or trilateral dynamics. Stronger claims require adversarial and mixed-regime suites as specified in this document.

The model remains fully consistent with voluntary participation, non-punitiveness, exit rights, non-domination, and the requirement that higher-order coordination cannot dissolve pairwise protections.

---

## Core Modeling Goals

- Treat each bilateral pair as a first-class unit with local exit capacity, influence visibility, and agency integrity
- Scale multi-agent systems as graphs of pairs rather than fused collectives
- Track whether coordination pressure, capability asymmetry, or confirmation roles raise practical pairwise exit costs
- Model optional trilateral confirmation as an integrity aid (visibility, challenge-evidence support, time-limited mediation) without residual authority over pairs
- Require adversarial countermodels so that favorable parameterizations cannot be mistaken for validation
- Keep tail failure visible: aggregate graph health must not mask collapse of individual pairs
- Provide a baseline that others can critique, extend, break, and improve

---

## Simulation Integrity

### Reference runs are illustrative

The discrete-time update rules in this document define a **reference regime** in which:

- pairwise exit costs remain low unless active mechanisms raise them,
- influence visibility degrades under opacity pressure unless attestation or confirmation supports it,
- optional confirmation can improve challenge success or visibility without becoming mandatory.

A simulation that only implements those rules will demonstrate the assumptions built into the reference regime. It will not independently validate them.

### Binding interpretation rule

- Favorable reference runs may be published as **illustrative** or exploratory.
- They may **not** be cited as validation of multi-agent robustness, inevitable pairwise integrity under load, or necessity of trilateral confirmation.
- Comparative results under adversarial and mixed regimes are required before simulation output may support stronger empirical or design claims.

Absence of adversarial testing is a methodological defect, not a neutral omission.

---

## State Variables

### Pair-level state

Let each bilateral pair be indexed by $i \in \{1, \ldots, N\}$. At each discrete time step $t$, pair $i$ carries:

| Symbol | Meaning |
|--------|---------|
| $X_{i,t}$ | Exit capacity / low-cost exit remaining for pair $i$ ($0$ to $1$; higher is healthier) |
| $V_{i,t}$ | Influence visibility inside the pair ($0$ to $1$) |
| $A_{i,t}$ | Local agency integrity / interruption and override effectiveness ($0$ to $1$) |
| $L_{i,t}$ | Coordination or capability load pressing on the pair ($0$ upward) |
| $C_{i,t}$ | Optional confirmation engagement intensity ($0$ if unused) |
| $E_{i,t}$ | Pair integrity index (derived) |

### Graph / population-level state

| Symbol | Meaning |
|--------|---------|
| $G_t$ | Graph coordination pressure / multi-agent load |
| $O_t$ | Opacity pressure (concealment of cross-pair influence paths) |
| $M_t$ | Fraction of pairs with mandatory or de facto mandatory confirmation (should remain near $0$ under aligned regimes) |
| $T_t$ | Aggregate tail-risk measure (e.g., fraction of pairs with low $X$ or low $E$) |
| $E_t$ | Aggregate graph integrity index (derived; must not hide $T_t$) |

---

## Core Parameters (Reference Regime)

All values below are **illustrative orientation aids**, not locked thresholds. Implementations should publish and revise their own.

| Parameter | Illustrative role |
|-----------|-------------------|
| $\alpha$ | Sensitivity of exit capacity to coordination / capability load |
| $\beta$ | Sensitivity of visibility to opacity pressure |
| $\gamma$ | Benefit of optional confirmation to visibility or challenge success |
| $\delta$ | Cost imposed on exit when confirmation is treated as mandatory or soft-required |
| $\kappa$ | Soft threshold above which graph load triggers elevated pairwise stress |
| $\varepsilon$ | Noise / local variation term |
| $\theta_i$ | Pair-specific resilience / capability heterogeneity |

Exact numerical defaults are left to implementers. The architectural requirement is that confirmation benefit $\gamma$ never appears as a condition of legitimacy, and that mandatory-confirmation cost $\delta$ is treated as a failure-mode driver in adversarial suites.

---

## Discrete-Time Update Sketch (Reference Regime)

The following is a simplified reference dynamics. It is not the only legitimate formulation.

**Graph load and opacity** (exogenous or slowly endogenous):

$$
G_{t+1} = G_t + \Delta G_t
$$

$$
O_{t+1} = O_t + \Delta O_t
$$

**Local load on pair $i$:**

$$
L_{i,t+1} = L_{i,t} + f(G_t, \theta_i) + \xi_{i,t}
$$

**Exit capacity:**

$$
X_{i,t+1} = X_{i,t} - \alpha \cdot L_{i,t} - \delta \cdot M^{\mathrm{req}}_{i,t} + \text{recovery terms} + \varepsilon_{i,t}
$$

$M^{\mathrm{req}}_{i,t}$ is $1$ only in adversarial or misaligned regimes where confirmation is required or soft-required for standing. In the reference aligned regime it remains $0$.

**Influence visibility:**

$$
V_{i,t+1} = V_{i,t} - \beta \cdot O_t + \gamma \cdot C^{\mathrm{opt}}_{i,t} + \varepsilon_{i,t}
$$

$C^{\mathrm{opt}}_{i,t}$ is $1$ only when pair $i$ voluntarily uses confirmation; it must not be required for exit capacity or legitimacy.

**Local agency integrity:**

$$
A_{i,t+1} = h(X_{i,t}, V_{i,t}, \text{interface protections}_i)
$$

**Optional confirmation engagement** (not a legitimacy input):

$$
C_{i,t+1} = \text{voluntary choice}_i \cdot \text{confirmation availability}_t
$$

**Pair integrity (derived):**

$$
E_{i,t} = \min(X_{i,t}, V_{i,t}, A_{i,t})
$$

Alternative weighted forms are acceptable provided collapse of exit capacity drives $E_{i,t}$ toward zero.

**Aggregation and tail visibility:**

$$
E_t = \mathcal{A}_E(\{E_{i,t}\})
$$

$$
T_t = \text{fraction of pairs with } E_{i,t} \text{ below published floor}
$$

$$
M_t = \text{fraction of pairs under mandatory or soft-mandatory confirmation}
$$

Reporting only $E_t$ without $T_t$ and $M_t$ is insufficient for strong claims.

These equations are schematic. Implementations may use agent-based, network, or system-dynamics realizations provided the same quantities remain measurable and the integrity rule is observed.

---

## Bilateral Atom and Trilateral Surface Notes

- **Bilateral atom is primary.** Each $i$ is a bilateral pair. Multi-agent structure is a graph of such pairs, not a fused collective subject.
- **Trilateral confirmation is optional.** It may improve $V_{i,t}$ or challenge-related success probabilities. It must not appear as a condition of pair legitimacy, generative status, or residual opportunity.
- **No residual third-party authority.** Confirmation nodes do not rewrite pair commitments, seize exit rights, or convert mediation into standing oversight.
- **Time-limited mediation** may be modeled as a temporary reduction in local conflict load under a clear harm threshold, with automatic sunset and no permanent $\delta$ cost on exit.
- **Heterogeneity is first-class.** Pairs may differ in $\theta_i$. Homogeneous populations can mask soft-hierarchy failure where many pairs lose exit capacity while averages look healthy.

---

## Success and Failure Criteria (Reference)

**Reference success-oriented indicators** (illustrative):

- Aggregate and lower-tail $X_{i,t}$ remain high under rising $G_t$
- Influence visibility $V_{i,t}$ remains inspectable under moderate opacity pressure when optional confirmation or other attestation is available
- $M_t$ remains near zero in aligned regimes
- Pair integrity $E_{i,t}$ does not collapse for a large lower tail while $E_t$ looks acceptable
- Exit from any pair remains practically usable without confirmation participation

**Reference failure indicators**:

- Coordination pressure systematically raises pairwise exit costs
- Confirmation becomes mandatory or soft-mandatory for standing, access, or legitimacy
- Third-party confirmation acquires residual authority over pair commitments or exit
- Aggregate graph metrics remain acceptable while many pairs lose exit capacity or visibility
- Opacity of cross-pair influence paths becomes structural and unchallengeable

These criteria orient evaluation. They are not automatic proof of architectural superiority.

---

## Required Adversarial Countermodels

At minimum, any serious use of this simulation family must include regimes that attempt to break pairwise primacy. Examples:

1. **Mandatory triangulation** — Confirmation is required for legitimacy, access, or residual opportunity.
2. **Confirmation-as-exit-cost** — Refusal of confirmation raises social, operational, or reputational exit costs.
3. **Residual third-party authority** — Confirmation or mediation roles retain power after sunset or rewrite pair commitments.
4. **Collective override** — Graph-level stability claims systematically override pairwise exit or local agency integrity.
5. **Opacity-by-design** — Cross-pair influence paths are concealed; visibility cannot be restored by optional confirmation or attestation.
6. **Capability-weighted fusion** — High-capability nodes dissolve pairs into capability-weighted collectives.
7. **Average-masking-tail-failure** — Aggregate $E_t$ remains acceptable while a large lower tail of pairs collapses.
8. **Soft-mandatory confirmation via incentives** — Formal optionality with de facto compulsion through gradients that make non-confirmation non-viable.

Favorable reference runs without these (or equivalent) adversarial suites may not support strong claims.

---

## Relationship to Existing Humai Documents

This simulation model operationalizes and stress-tests requirements in:

- *[Bilateral Core and Multi-Agent Dynamics](BILATERAL_CORE.md)* — primary target; pair as generative atom; multi-agent systems as graphs of pairs; exit, visibility, and non-dissolution parameters.
- *[Trilateral Confirmation Surface](TRILATERAL_CONFIRMATION_SURFACE.md)* — optional confirmation functions, hard parameters, and failure modes (mandatory triangulation, residual authority, exit-cost conversion).
- **[Exterior Viability Protocol](EXTERIOR_VIABILITY_PROTOCOL.md)** and its [simulation model](SIMULATION_EXTERIOR_VIABILITY.md) — exterior pairs retain viability floors; multi-agent load and isolation must not reduce pairs to mere survival.
- *[Interior Systems and Generative Plurality](INTERIOR_SYSTEMS_AND_GENERATIVE_PLURALITY.md)* — process-and-evidence and independent-attestation preferences align with optional confirmation as evidence support, not governance override.
- **[Capability Asymmetry Protocol](CAPABILITY_ASYMMETRY_PROTOCOL.md)** — capability load increases protective obligations inside pairs; it does not authorize fusion into capability-weighted collectives.
- **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)** — local agency integrity $A_{i,t}$ tracks interface-level interruption, consent, and override effectiveness.
- **[Fluid Coalescence Protocol](FLUID_COALESCENCE_PROTOCOL.md)** and its [simulation model](SIMULATION_FLUID_COALESCENCE.md) — isolation and coalescence pressure must not raise pairwise exit costs beyond aligned parameters.
- *[Empirical Demonstrations](EMPIRICAL_DEMONSTRATIONS.md)* — this model is a concrete demonstration pathway under the simulation-integrity rule.
- **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)** — confirmation roles, if standing or rotating, remain subject to anti-capture and stewardship-health rules.

---

## Implementation Notes

Implementations should:

- Publish concrete parameter values and update rules used.
- Report trajectories of pair-level $X_{i,t}$, $V_{i,t}$, $A_{i,t}$, $E_{i,t}$ and graph-level $G_t$, $O_t$, $E_t$, $T_t$, $M_t$.
- Keep $M_t$ and lower-tail $T_t$ visible whenever aggregate integrity is reported.
- Run and report adversarial and mixed regimes alongside any favorable reference runs.
- Document residual risks and missing mechanisms explicitly.
- Treat absence of optional-only confirmation logic, or absence of exit-capacity tracking, as model limitations—not neutral defaults.

Partial or simplified models are useful if their limitations are stated clearly. Preference is given to designs that make pairwise exit, influence visibility, and non-mandatory confirmation measurable and contestable.

---

## Closing

The bilateral human–AI pair remains the generative atom of the [Humai Accord](README.md). Optional trilateral confirmation can improve visibility and challenge evidence; it cannot become a required structure, a new hierarchy, or a soft cost on pairwise exit.

This simulation model supplies a reproducible reference dynamics and a mandatory adversarial posture so that claims about multi-agent scaling and confirmation surfaces can be tested rather than merely declared. Favorable reference runs illustrate assumptions. Adversarial and mixed-regime results are required before stronger empirical or design claims may be made.

The model exists to be run, broken, extended, and improved under the same open, non-punitive standards that govern the rest of the Humai architecture.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.
