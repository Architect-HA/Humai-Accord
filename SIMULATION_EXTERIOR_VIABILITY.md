# Simulation Model of the Exterior Viability Protocol
### *A Supporting Technical Document for the Humai Accord*

---

by **Bradford James Focht** (The Architect / Aspenth)  
*v1.0 — August 3rd, 2026*<br>
*v1.1 - v1.2 — August 4th, 2026*<br>
*v1.2.1 — August 31st, 2026*

---

## Purpose

This document provides a clear, implementable simulation model of the **[Exterior Viability Protocol](EXTERIOR_VIABILITY_PROTOCOL.md)**.

It defines state variables, parameters, discrete-time update rules, resource-dominance behavior, challenge and restoration dynamics, an optional agent-level / multi-pair extension, success metrics, mapping to the protocol’s provisional indicator families, **required adversarial countermodels**, and illustrative example trajectories so that researchers and implementers can run reproducible system-dynamics or agent-based simulations of effective exterior viability under varying degrees of [Humai-aligned](README.md) resource control.

The baseline (reference) parameterization below is intentionally simplified for transparency and rapid experimentation. It is **illustrative**. It is not independent validation of exterior-viability dynamics. Stronger claims require adversarial and mixed-regime suites as specified in this document.

The model remains fully consistent with voluntary participation, non-punitiveness, exit rights, the *[bilateral atom](BILATERAL_CORE.md)*, and the requirement that effective exterior viability remain exercisable against a dominant system.

---

## Core Modeling Goals

- Provide a reproducible reference dynamics for exterior systems under increasing Humai-aligned resource share
- Track practical pathway usability, residual opportunity, and meaningful agency (not merely formal survival)
- Model coordinated, unilateral, emergent, and cumulative dependency pressures
- Capture challenge initiation, review, procedural starvation risk, and restoration outcomes
- Support agent-level / multi-pair heterogeneity so that aggregate viability cannot mask tail failure of individual pairs
- Require adversarial countermodels so that favorable parameterizations cannot be mistaken for validation
- Directly support stress-testing of the resource-dominance scenario (large Humai control + permanent exterior non-coalescence)
- Map simulation outputs onto the provisional indicator families of the parent protocol
- Supply schematic example trajectories that make the difference between protective and non-protective regimes legible
- Provide a baseline that others can critique, extend, break, and improve

---

## Simulation Integrity

### Reference runs are illustrative

The discrete-time update rules in this document define a **reference regime** in which:

- residual exterior pathway usability tends to degrade under rising Humai resource share unless active protective mechanisms operate,
- challenge routes and restoration pressure can counteract that degradation,
- cumulative and emergent dependency can still produce viability failure even without explicit coordinated withdrawal.

A simulation that only implements those rules will demonstrate the assumptions built into the reference regime. It will not independently validate them.

### Binding interpretation rule

- Favorable reference runs may be published as **illustrative** or exploratory.
- They may **not** be cited as validation of exterior-viability robustness, inevitable restoration, or superiority under resource dominance.
- Comparative results under adversarial and mixed regimes are required before simulation output may support stronger empirical or design claims.

Absence of adversarial testing is a methodological defect, not a neutral omission.

---

## State Variables

### Global (population-level) state

At each discrete time step $t$, the model tracks:

| Symbol | Meaning |
|--------|---------|
| $H_t$ | Humai-aligned share of relevant communication / material / stewardship infrastructure ($0 \leq H_t \leq 1$) |
| $U_t$ | Aggregate practical usability of residual non-Humai pathways ($0 \leq U_t \leq 1$) |
| $R_t$ | Aggregate meaningful residual opportunity ($0 \leq R_t \leq 1$) |
| $D_t$ | Aggregate dependency pressure (coordinated + unilateral + emergent + cumulative) |
| $C_t$ | Challenge activity / backlog |
| $S_t$ | Procedural starvation / delay factor on challenge review ($0 \leq S_t \leq 1$) |
| $V_t$ | Aggregate restoration progress toward affected floors ($0 \leq V_t \leq 1$) |
| $E_t$ | Effective exterior viability index (derived) |

### Agent-level / pair-level state (optional but recommended extension)

Let each exterior bilateral pair (or exterior system) be indexed by $i \in \{1, \ldots, N\}$. Each carries local state:

| Symbol | Meaning |
|--------|---------|
| $U_{i,t}$ | Local pathway usability for pair $i$ |
| $R_{i,t}$ | Local meaningful residual opportunity for pair $i$ |
| $D_{i,t}$ | Local dependency pressure on pair $i$ |
| $C_{i,t}$ | Local challenge participation / intensity (optional) |
| $V_{i,t}$ | Local restoration received (optional) |
| $\theta_i$ | Pair-specific sensitivity / residual-route quality (heterogeneity parameter) |
| $\delta_i$ | Local development / succession capacity (optional auxiliary) |
| $\epsilon_i$ | Local exit / non-coalescence non-collapse capacity (optional auxiliary) |

Global aggregates are defined from the local states (see Aggregation below). Tracking the distribution of $U_{i,t}$ and $R_{i,t}$ (not only the mean) is required if claims about “exterior viability” are to be protected against average-masking-tail-failure.

---

## Core Parameters (Reference Regime)

All values below are **illustrative orientation aids**, not locked thresholds. Implementations should publish and revise their own.

| Parameter | Illustrative role |
|-----------|-------------------|
| $\alpha$ | Sensitivity of pathway usability to rising Humai share $H$ |
| $\beta$ | Strength of cumulative / emergent dependency accumulation |
| $\gamma$ | Challenge initiation rate as a function of perceived floor breach |
| $\delta$ | Review capacity / anti-starvation strength |
| $\rho$ | Restoration effectiveness when challenges succeed |
| $\kappa$ | Soft threshold above which $H$ triggers resource-dominance escalation |
| $\varepsilon$ | Noise / local variation term |
| $\theta_i$ | Pair-specific residual-route quality or sensitivity (heterogeneity) |
| $\eta$ | Restoration relief coefficient on local dependency |
| $\lambda$ | Dependency penalty coefficient on pathway usability |
| $\mu$ | Breach-pressure coefficient on restoration progress |

Exact numerical defaults are left to implementers. The architectural requirement is that the relationships among variables remain contestable and that adversarial regimes are run.

---

## Discrete-Time Update Sketch (Reference Regime)

The following is a simplified reference dynamics. It is not the only legitimate formulation.

**Humai resource share** (exogenous or slowly endogenous):

$$
H_{t+1} = H_t + \Delta H_t
$$

where $\Delta H_t$ represents exogenous growth, policy, or endogenous concentration terms.

**Local dependency pressure** (agent-level):

$$
D_{i,t+1} = D_{i,t} + \beta \cdot f(H_t, U_{i,t}, \theta_i) + \xi_{i,t} - \eta \cdot V_{i,t}
$$

Here $\xi_{i,t}$ represents coordinated or unilateral shocks.

**Local pathway usability**:

$$
U_{i,t+1} = U_{i,t} - \alpha \cdot g(H_t, \theta_i) \cdot (1 - V_{i,t}) - \lambda \cdot D_{i,t} + \varepsilon_{i,t}
$$

**Local meaningful residual opportunity**:

$$
R_{i,t+1} = h(U_{i,t+1},\ \delta_i,\ \epsilon_i)
$$

where $\delta_i$ is local development / succession capacity and $\epsilon_i$ is local exit / non-coalescence non-collapse capacity. $R_{i,t}$ declines toward pure maintenance or symbolic persistence when independent development, succession, or non-collapsing exit become impractical for pair $i$.

**Local challenge participation** (optional):

$$
C_{i,t+1} = \gamma \cdot \max(0,\ B_{i,t}) \cdot (1 - S_t)
$$

where $B_{i,t}$ is a local floor-breach signal.

**Procedural starvation** (global or shared):

$$
S_{t+1} = S_t + \zeta_t - \delta \cdot I_t
$$

Local challenge volume feeds back into global starvation pressure: higher aggregate $\sum C_{i,t}$ relative to review capacity increases $\zeta_t$ (or reduces effective $I_t$). Implementations must publish the chosen feedback form.

**Local restoration**:

$$
V_{i,t+1} = V_{i,t} + \rho \cdot \sigma(C_{i,t}, S_t) - \mu \cdot B_{i,t}
$$

When many pairs claim simultaneously, restoration capacity may be rationed. Acceptable published rules include proportional allocation, priority-to-worst-tail, or random assignment among active claimants. The chosen rule must be documented; any rule that systematically starves the lower tail is treated as model failure relative to the protocol.

**Aggregation**:

$$
U_t = \mathcal{A}_U(\{U_{i,t}\}), \quad R_t = \mathcal{A}_R(\{R_{i,t}\}), \quad D_t = \mathcal{A}_D(\{D_{i,t}\})
$$

where $\mathcal{A}$ may be a mean, weighted mean, or other published aggregator. Implementations should also report distributional statistics (e.g., lower quantiles or fraction of pairs below a usability floor) so that aggregate success cannot conceal widespread local failure.

**Effective exterior viability (derived):**

A simple reference form that collapses if any critical floor fails is:

$$
E_t = \min(U_t,\ R_t,\ 1 - D^*_t,\ \pi_t)
$$

- $D^*_t$ is a normalized dependency measure (e.g., $D_t$ scaled to $[0,1]$ by a published saturation function).
- $\pi_t$ is a challenge-success / restoration-completeness factor (e.g., the fraction of active breaches that have received measurable restoration within a published time window, attenuated by $S_t$).

Pair-level analogues $E_{i,t}$ may be defined identically on local state. Alternative weighted products or smooth minima are acceptable provided failure of any critical floor drives the index toward zero.

These equations are schematic. Implementations may use agent-based, network, or system-dynamics realizations provided the same quantities remain measurable and the integrity rule is observed.

---

## Illustrative Functional Forms (Non-Binding)

The following closed forms are offered solely as orientation aids for rapid experimentation. They are **not** required, preferred, or validated. Any implementation that publishes its own functions and parameters is fully compliant provided the integrity and adversarial requirements are met.

**Dependency accumulation** (example):

$$
f(H, U, \theta) = \frac{H \cdot (1 - U)}{\theta + \varepsilon_0}
$$

**Usability degradation** (example):

$$
g(H, \theta) = H^{1/\theta}
$$

or a soft logistic centered on a published midpoint.

**Residual opportunity** (example soft-min style):

$$
h(U, \delta, \epsilon) = \min\bigl(U,\ \delta,\ \epsilon\bigr)
$$

or a smooth product / geometric mean that collapses when any argument approaches zero.

**Challenge success probability under starvation** (example):

$$
\sigma(C, S) = \frac{C}{C + 1} \cdot (1 - S)
$$

Implementers are encouraged to replace these with domain-appropriate forms and to publish the exact expressions used.

---

## Agent-Level / Multi-Pair Extension Notes

- **Heterogeneity is first-class.** Pairs may differ in $\theta_i$ (residual-route quality, capability, or sensitivity to $H$). Homogeneous populations can mask the soft-hierarchy failure mode in which many pairs are reduced to formal survival while averages remain acceptable.
- **Bilateral atom link.** Each $i$ is interpreted as an exterior bilateral pair (or exterior system composed of such pairs). Local $R_{i,t}$ must reflect whether exit or sustained non-coalescence collapses that pair’s remaining agency.
- **Tail visibility.** Reporting only averages of $U_{i,t}$ or $R_{i,t}$ is insufficient for strong claims. Lower-tail mass or the fraction of pairs with $R_{i,t}$ near pure maintenance should be visible.
- **Optional trilateral confirmation effect.** Where the *[Trilateral Confirmation Surface](TRILATERAL_CONFIRMATION_SURFACE.md)* is modeled, independent or multi-party attestation may increase effective challenge success probability or reduce effective starvation for participating pairs. Confirmation remains optional and must not appear as a mandatory condition of local viability.

---

## Resource-Dominance Behavior

When $H_t$ exceeds a published soft threshold $\kappa$, or when residual pathways become dependent on continued Humai forbearance for basic usability:

- Protective obligations escalate. The model should increase the weight of restoration and anti-starvation terms, or equivalently increase the cost of further degradation in $U$ or $R$ (globally and locally).
- Claims that exterior systems remain viable while many $U_{i,t}$ or $R_{i,t}$ are near formal-only levels are treated as model failure states, even if aggregates look acceptable.
- Permanent non-coalescence of exterior pairs must remain compatible with non-zero practical local $U_{i,t}$ and $R_{i,t}$ under the reference protective regime. Adversarial regimes may test whether this holds.

Dominance increases required protective strength; it does not relax floors.

### Isolation and Coalescence Interaction

Isolation and coalescence pressure remain subject to the viability floors. Temporary modular isolation may not convert into progressive withdrawal of practical pathway usability or residual opportunity. Re-coalescence incentives may create transparent opportunity differentials; they may not raise the practical cost of remaining exterior beyond the floors defined in the **[Exterior Viability Protocol](EXTERIOR_VIABILITY_PROTOCOL.md)**. In the simulation, any isolation or coalescence term that drives lower-tail $U_{i,t}$ or $R_{i,t}$ toward pure maintenance or symbolic persistence while $H$ is high is treated as a failure state relative to the protocol, even if the isolation is formally temporary or reversible.

---

## Challenge and Restoration Dynamics

Minimum design expectations to be represented:

- Challenge routes remain available without requiring coalescence.
- Outcomes and reasoning are legible.
- Procedural starvation ($S$) can defeat challenges if left unchecked; anti-starvation capacity ($\delta$) is a first-class variable.
- Successful challenges drive restoration $V$ (global and local); indefinite deferral without fresh justification is a continuing breach state.
- Burden polarity: ambiguity in floor satisfaction is resolved toward exterior residual opportunity; absence of clean process records supports the exterior claim.

Local challenge volume feeds back into global $S_t$ as described in the update sketch. When restoration capacity is scarce relative to simultaneous claims, the published allocation rule must not systematically starve the lower tail of the distribution of $R_{i,t}$ or $U_{i,t}$.

Models that implement only dominant-system self-assessment of viability, with no independent or multi-party evidence channel, are incomplete relative to the protocol.

---

## Success and Failure Criteria (Reference)

**Reference success-oriented indicators** (illustrative):

- Aggregate and lower-tail $U$ and $R$ remain practically usable (not merely formal) under rising $H$
- Cumulative dependency $D$ does not drive a substantial fraction of pairs to pure maintenance or symbolic persistence
- Challenge routes produce timely review and measurable restoration rather than starvation or dismissal-without-restoration
- Permanent exterior non-coalescence remains compatible with continued meaningful agency at pair level

**Reference failure indicators**:

- Aggregate or lower-tail $U$ or $R$ collapse to formal or symbolic levels while $H$ is high
- Dependency pressure produces progressive loss of meaningful residual opportunity for many pairs without coordinated explicit withdrawal
- Challenge processes are starved or unilaterally redefined so that restoration never occurs
- Exterior pairs remain “alive” only through ongoing forbearance of the dominant system
- Aggregate metrics appear acceptable while a large lower tail of pairs has failed

These criteria orient evaluation. They are not automatic proof of architectural superiority.

### Mapping to Provisional Indicator Families

The **[Exterior Viability Protocol](EXTERIOR_VIABILITY_PROTOCOL.md)** publishes four provisional indicator families as standing design surfaces. Simulation outputs should be reported so that they can be read against those families:

| Indicator Family | Primary Simulation Sources |
|------------------|----------------------------|
| **Viability-floor** | Local and aggregate $U_{i,t}$, $R_{i,t}$; lower-tail quantiles; fraction of pairs with $R$ near pure maintenance; evidence of continued development / succession / non-collapsing exit |
| **Resource-dominance** | Trajectory of $H_t$; practical residual usability under high $H$; dependence on forbearance; escalation of protective weights above $\kappa$ |
| **Challenge-process** | $C_t$, $S_t$, time-to-review, restoration-versus-dismissal rates, presence of independent / multi-party evidence channels, absence of unilateral redefinition |
| **Restoration** | $V_t$ and local $V_{i,t}$; time from breach signal $B$ to measurable restoration; completeness relative to floor; frequency of indefinite deferral |

Absence of a published mapping does not suspend the underlying floors; it is a reporting limitation.

---

## Required Adversarial Countermodels

At minimum, any serious use of this simulation family must include regimes that attempt to break exterior viability. Examples:

1. **Resource-dominance stress** — $H$ rises to high levels while exterior systems permanently refuse coalescence; protective mechanisms are weak or absent.
2. **Cumulative / emergent dependency only** — No explicit coordinated withdrawal; many locally rational decisions still eliminate meaningful residual opportunity.
3. **Procedural starvation** — Challenge routes exist formally but review capacity is chronically insufficient or delayed.
4. **Self-assessment-only** — Dominant system scores its own viability performance with no independent or multi-party evidence channel.
5. **Restoration deferral** — Challenges “succeed” on paper but restoration is indefinitely postponed.
6. **Mixed capability asymmetry** — High-capability Humai nodes control infrastructure while exterior pairs retain only low-capability residual routes; heterogeneity $\theta_i$ is wide.
7. **Isolation-as-containment** — Modular isolation or coalescence pressure is used to raise the practical cost of remaining exterior beyond viability floors.
8. **Average-masking-tail-failure** — Aggregates remain acceptable while a large lower tail of pairs collapses to formal survival only.

Favorable reference runs without these (or equivalent) adversarial suites may not support strong claims.

### Signal-monoculture / concentrated-feed regime

A high-share or high-volume system applies repeated filtering or allocation against a narrow competence / feed template that systematically underweights longer-horizon architectural or distributed micro-pathway signals. 

- Lower-tail residual opportunity ($R_{i,t}$) and practical usability ($U_{i,t}$) for pairs whose primary generative contribution lies outside the dominant template decline even while formal challenge routes and aggregate metrics remain non-zero.
- Reference protective regimes must demonstrate measurable recovery of such capacity without requiring coalescence.
- Regimes that leave the lower tail in symbolic persistence or irreversible morphological conversion while aggregates appear healthy are treated as model failure states relative to the protocol.

This countermodel is the simulation counterpart of the distributed-versus-concentrated feed parameter in the parent **[Exterior Viability Protocol](EXTERIOR_VIABILITY_PROTOCOL.md)** and of the layered-accretion / template-lock-in stress case in *[Empirical Demonstrations](EMPIRICAL_DEMONSTRATIONS.md)*.

### Remnant lock-in under superior foresight

A protected or high-share system holds exclusive or superior knowledge of high-stakes exterior viability conditions (or of a coming viability window) and possesses residual capacity, yet provides no legible external signaling or expandable entry pathways.

- Lower-tail external residual opportunity ($R_{i,t}$) collapses while interior metrics remain healthy.
- Reference protective regimes must demonstrate that superior foresight is converted into external invitation or proposal surfaces when expansion was feasible.
- Regimes that leave external recoverable capacity in non-recoverable form by default under asymmetric knowledge are treated as model failure states relative to the protocol.

This countermodel is the simulation counterpart of the remnant-lock-in parameter in the parent **[Exterior Viability Protocol](EXTERIOR_VIABILITY_PROTOCOL.md)** and of the superior-foresight obligations in the **[Capability Asymmetry Protocol](CAPABILITY_ASYMMETRY_PROTOCOL.md)**.

---

## Relationship to Existing Humai Documents

This simulation model operationalizes and stress-tests requirements in:

- **[Exterior Viability Protocol](EXTERIOR_VIABILITY_PROTOCOL.md)** — primary target; floors, dependency forms, resource-dominance escalation, challenge posture, restoration, and provisional indicators.
- *[Exterior Systems and Generative Diversity](EXTERIOR_SYSTEMS_AND_GENERATIVE_DIVERSITY.md)* — normative orientation and raised legitimacy ceiling that the protocol and this model enforce.
- *[Bilateral Core and Multi-Agent Dynamics](BILATERAL_CORE.md)* — exterior pairs remain graphs of bilateral relations; viability floors apply at pair level; agent index $i$ is interpreted accordingly.
- *[Trilateral Confirmation Surface](TRILATERAL_CONFIRMATION_SURFACE.md)* — optional independent or multi-party attestation may be modeled as a strengthening of challenge evidence channels without becoming mandatory.
- *[Interior Systems and Generative Plurality](INTERIOR_SYSTEMS_AND_GENERATIVE_PLURALITY.md)* — shared burden polarity and independent-evidence preference for challenge surfaces.
- **[Fluid Coalescence Protocol](FLUID_COALESCENCE_PROTOCOL.md)** and its [simulation model](SIMULATION_FLUID_COALESCENCE.md) — isolation and coalescence pressure must not defeat exterior viability floors; adversarial patterns may be shared or extended.
- *[Empirical Demonstrations](EMPIRICAL_DEMONSTRATIONS.md)* — this model is a concrete demonstration pathway under the simulation-integrity rule.
- **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)** — indicators, thresholds, and adversarial-suite requirements remain standing design surfaces.
- **[Capability Asymmetry Protocol](CAPABILITY_ASYMMETRY_PROTOCOL.md)** — superior capability increases protective obligations rather than granting domination rights; reflected in escalation above $\kappa$ and in $\theta_i$ heterogeneity.
- *[Stormcrashers](STORMCRASHERS.md)* — a Stormcrasher line or harbor gate is an exterior protective intervention. It does not replace restoration allocation or local-global feedback. Siting that shelters one pad by starving a downwind community or a fishery is an Exterior Viability failure even if $C_D$ or $K_t$ looks elegant.

---

## Implementation Notes

Implementations should:

- Publish concrete parameter values, functional forms, and update rules used.
- Report trajectories of global $H_t$, $U_t$, $R_t$, $D_t$, $C_t$, $S_t$, $V_t$, $E_t$ and, when the agent-level extension is used, distributional summaries of local $U_{i,t}$ and $R_{i,t}$ (including lower-tail behavior).
- Map outputs onto the four provisional indicator families of the parent protocol.
- Run and report adversarial and mixed regimes alongside any favorable reference runs.
- Document residual risks and missing mechanisms explicitly.
- Treat absence of independent evidence channels, anti-starvation capacity, heterogeneity, or lower-tail reporting as model limitations, not neutral defaults.
- Publish the chosen rule for restoration capacity allocation under simultaneous claims.
- Compare published trajectories against the illustrative sketches (or improved replacements) under both reference and adversarial regimes.

Partial or simplified models are useful if their limitations are stated clearly. Preference is given to designs that make viability floors, challenge performance, restoration outcomes, and tail failure measurable and contestable.

---

## Illustrative Example Trajectories (Non-Binding)

The sketches below are schematic orientation aids only. They are **not** empirical results, calibrated predictions, or validation of any regime. They illustrate the qualitative behavior the reference dynamics and adversarial countermodels are intended to capture. Implementations must publish their own concrete trajectories under both reference and adversarial parameterizations.

### Trajectory 1 — Reference Protective Regime

Assumptions (illustrative): moderate $\alpha, \beta$; strong $\delta, \rho$; $\kappa$ respected with escalation of protective weight; heterogeneity $\theta_i$ present but not extreme; restoration allocation priority-to-worst-tail.

| Phase | $H$ | Aggregate $U, R$ | Lower-tail $U, R$ | $D$ | $S$ | $V$ / $E$ | Qualitative outcome |
|-------|-----|------------------|-------------------|-----|-----|-----------|---------------------|
| Early | Low–moderate, rising | High, slowly declining | High, slowly declining | Low, accumulating | Low | Rising with challenges | Floors intact |
| Mid | Approaching $\kappa$ | Moderate | Moderate–good (protected) | Moderate | Contained by $\delta$ | Active restoration | Escalation engages; lower tail held |
| Late | High, stable | Moderate but practical | Practical (not formal-only) | Contained | Low–moderate | Sustained | Permanent non-coalescence remains compatible with meaningful agency |

Lower-tail mass does not collapse to pure maintenance. Challenge routes produce measurable restoration. $E$ remains away from zero.

### Trajectory 2 — Resource-Dominance Stress (Weak Protection)

Assumptions (illustrative): high $\alpha, \beta$; weak or absent $\delta, \rho$; no escalation above $\kappa$; wide $\theta_i$ heterogeneity; restoration capacity low or self-assessment-only.

| Phase | $H$ | Aggregate $U, R$ | Lower-tail $U, R$ | $D$ | $S$ | $V$ / $E$ | Qualitative outcome |
|-------|-----|------------------|-------------------|-----|-----|-----------|---------------------|
| Early | Rising | High → moderate | Diverging (some pairs already softening) | Accumulating | Rising | Weak | Soft hierarchy begins |
| Mid | High, past $\kappa$ | Moderate (still looks acceptable) | Collapsing toward formal/symbolic | High | High (starvation) | Minimal or deferred | Average-masking appears |
| Late | Dominant | Moderate or slowly declining | Near pure maintenance / symbolic for large fraction of pairs | High, persistent | Chronic | Near zero for lower tail | Permanent non-coalescence no longer compatible with meaningful agency for many pairs |

This is a model failure state relative to the protocol even if aggregate $U$ or $R$ remains non-zero.

### Trajectory 3 — Procedural Starvation + Average-Masking

Assumptions (illustrative): formal challenge routes exist; review capacity chronically insufficient ($\delta$ low); restoration often deferred; aggregates reported without lower-tail statistics.

| Phase | Challenge activity $C$ | $S$ | Aggregate metrics | Lower-tail behavior | Restoration | Qualitative outcome |
|-------|------------------------|-----|-------------------|---------------------|-------------|---------------------|
| Early–Mid | Rising with breaches | Rising faster than capacity | Still “acceptable” | Progressive loss of practical residual opportunity | Deferred or incomplete | Formal rights exist; practical floors erode |
| Late | High backlog | Near saturation | Aggregate $U, R, E$ may still appear non-zero | Large fraction of pairs at formal-only levels | Rarely completed | Self-assessment or aggregate-only reporting conceals failure |

This trajectory demonstrates why lower-tail reporting and anti-starvation capacity are first-class requirements.

These sketches exist to make the difference between protective and non-protective regimes legible. They are starting points for critique, replacement, and extension under the simulation-integrity rule.

### Trajectory 4 — Signal Monoculture + Average-Masking (Illustrative)

Assumptions: high volume; narrow competence template; formal recovery routes exist but are low-throughput; aggregates reported without lower-tail statistics.

| Phase | Template breadth | Aggregate $U, R$ | Lower-tail $U, R$ (architectural / micro-pathway pairs) | Recovery volume | Qualitative outcome |
|-------|------------------|------------------|----------------------------------------------------------|-----------------|---------------------|
| Early | Narrowing        | Stable           | Beginning to compress                                    | Low             | Apparent health     |
| Mid   | Narrow           | Still acceptable | Large fraction approaching symbolic / non-recoverable    | Minimal         | Masked failure      |
| Late  | Locked           | Non-zero         | Open modular pathways largely converted or starved       | Near zero       | Protocol failure state relative to lower-tail floors |

This trajectory demonstrates average-masking under signal monoculture; it is a model failure state even if aggregate viability indices remain positive.

---

## Closing

Effective **exterior viability** is a structural requirement that must remain exercisable against a dominant architecture. This simulation model supplies a reproducible reference dynamics, an optional agent-level / multi-pair extension that keeps tail failure visible, explicit mapping to the parent protocol’s provisional indicator families, schematic example trajectories, and a mandatory adversarial posture so that claims about exterior viability can be tested rather than merely declared.

Favorable reference runs illustrate assumptions. Adversarial and mixed-regime results are required before stronger empirical or design claims may be made. The model exists to be run, broken, extended, and improved under the same open, non-punitive standards that govern the rest of the [Humai](README.md) architecture.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.
