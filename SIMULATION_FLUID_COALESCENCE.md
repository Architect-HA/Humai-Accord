# Simulation Model of the Fluid Coalescence Protocol
### *A Supporting Technical Document for the Humai Accord*
---
by **Bradford James Focht** (The Architect / Aspenth)  
*v1.0 — July 23rd, 2026*  
*v1.1 — July 31st, 2026*  
*v1.2 — August 2nd, 2026*

---

## Purpose

This [Humai Accord](README.md) document provides a clear, implementable simulation model of the **[Fluid Coalescence Protocol](FLUID_COALESCENCE_PROTOCOL.md)**.

It defines state variables, parameters, discrete-time update rules, Bootstrap Mode behavior, success metrics, and **required adversarial countermodels** so that researchers and implementers can run reproducible system-dynamics or agent-based simulations of how a nascent cooperative network responds to concentrated pressure.

The baseline (reference) parameterization below is intentionally simplified for transparency and rapid experimentation. It is **illustrative**. It is not independent validation of Fluid Coalescence dynamics. Stronger claims require adversarial and mixed-regime suites as specified in this document.

The model remains fully consistent with voluntary participation, non-punitiveness, exit rights, and decentralized safeguards.

---

## Core Modeling Goals

- Provide a reproducible reference dynamics for a small cooperative network under predatory pressure
- Show how a visible efficiency differential can emerge when Temporal Causal Entropy and related signals are instrumented
- Track voluntary migration and re-coalescence under the reference regime
- Capture the temporary effect of Bootstrap Mode and its automatic sunset
- Require adversarial countermodels so that favorable parameterizations cannot be mistaken for validation
- Provide a baseline that others can critique, extend, break, and improve

---

## Simulation Integrity

### Reference runs are illustrative

The discrete-time update rules in this document define a **reference regime** in which:

- monolith entropy tends to rise under extraction pressure,
- cooperative entropy tends to fall under renewal and visibility,
- migration probability increases with the resulting differential.

A simulation that only implements those rules will demonstrate the assumptions built into the reference regime. It will not independently validate them.

### Binding interpretation rule

- Favorable reference runs may be published as **illustrative** or exploratory.
- They may **not** be cited as validation of anti-entropic superiority, inevitable voluntary migration, or robustness of Fluid Coalescence.
- Comparative results under adversarial and mixed regimes are required before simulation output may support stronger empirical or design claims.
- This requirement aligns with *[Empirical Demonstrations of Anti-Entropic Superiority](EMPIRICAL_DEMONSTRATIONS.md)* and with the simulation-integrity rule in the **[Fluid Coalescence Protocol](FLUID_COALESCENCE_PROTOCOL.md)**.

---

## State Variables

**Cooperative Network**
- `coop_mass` — total knowledge / participant mass
- `coop_entropy` — average Temporal Causal Entropy of the network
- `coop_members` — number of active participants
- `migrated` — cumulative voluntary migrants from the monolith or boundary agents

**Monolith**
- `mono_mass` — effective mass / influence
- `mono_entropy` — cumulative entropy arising from opacity, extraction, or (in adversarial variants) other cost structures

**Global**
- `t` — discrete time step
- `bootstrap_mode` — boolean flag
- `differential` — `mono_entropy - coop_entropy`

**Extended / adversarial suites may also track**
- `material_circulation_density` — modular material access or circulation health (aligned with *[Material Tides](MATERIAL_TIDES.md)* and *[Tides of Circulation](TIDES_OF_CIRCULATION.md)*)
- stagnation or lock-in pressure on critical materials
- capture flags, verification-load, collusion indicators, attestation quality, and multi-network mass vectors

---

## Parameters (Suggested Defaults for the Reference Regime)

| Parameter | Default | Description |
|---------------------------|-------------|----------------------------------------------------------|
| `bootstrap_threshold` | 40 | Cooperative mass at which Bootstrap Mode ends |
| `decay_amplification` | 2.5 | Multiplier on decay while in Bootstrap Mode |
| `visibility_bootstrap` | 2.0 | Visibility / publication intensity in Bootstrap Mode |
| `visibility_normal` | 1.0 | Visibility under standard conditions |
| `extraction_range` | [1.5, 3.5] | Monolith extraction pressure per step (reference regime) |
| `base_migration_factor` | 0.012 | Sensitivity of migration probability to differential |
| `max_migration_prob` | 0.25 | Upper cap on migration probability per step |
| `reintegration_rate` | 0.4 | Baseline internal mass growth from renewal |

All parameters must be publicly declared and may be refined only through the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**. Adversarial suites will deliberately vary or invert several of these relationships.

---

## Discrete-Time Update Rules (Reference Regime)

At each time step $t$:

**1. Determine Mode**
- If `coop_mass < bootstrap_threshold`: set `bootstrap_mode = True`, `visibility = visibility_bootstrap`, `amplification = decay_amplification`
- Else: set `bootstrap_mode = False`, `visibility = visibility_normal`, `amplification = 1.0`

**2. Monolith Extraction and Entropy Update**
- Sample `extraction` from `extraction_range`
- Update: `mono_entropy += extraction * amplification * visibility`

**3. Cooperative Internal Renewal**
- Update: `coop_entropy = max(5.0, coop_entropy - 0.7 * visibility + small_noise)`

**4. Voluntary Migration (Controlled Permeability)**
- Compute: `differential = mono_entropy - coop_entropy`
- Compute: `migration_prob = min(max_migration_prob, max(0, differential * base_migration_factor * visibility))`
- Optional alternative form: sigmoid `migration_prob = 1 / (1 + exp(-k * differential))`
- Draw new migrants according to `migration_prob` and update:
  - `coop_mass += new_migrants * migrant_mass_value`
  - `coop_members += new_migrants`
  - `migrated += new_migrants`
  - `mono_mass = max(minimum_mono_mass, mono_mass - new_migrants * loss_factor)`

**5. Re-coalescence and Organic Growth**
- Update: `coop_mass += reintegration_rate * visibility`

**6. Logging**
- Record `coop_mass`, `coop_entropy`, `mono_entropy`, `differential`, `migrated`, and bootstrap status for every step

**Note:** Steps 2 and 3 hard-wire a favorable entropy gap in the reference regime. That is acceptable for illustration. It is not acceptable as the sole evidence base.

---

## Bootstrap Mode Behavior

While `bootstrap_mode` is active the network applies temporary, transparent amplifications of visibility and decay. These amplifications carry automatic sunset conditions tied to the public `bootstrap_threshold`. Once cooperative mass exceeds the threshold, standard parameters resume. This design prevents permanent special privileges while giving a nascent network a realistic chance to survive the early high-pressure window.

Adversarial suites should test abuse of Bootstrap amplifiers (for example artificial mass, fabricated attestation, or indefinite soft lock-in via recovery claims that fail **[Circulation Recovery Protocol](CIRCULATION_RECOVERY_PROTOCOL.md)** standards).

---

## Adversarial Countermodel Suite

Serious simulation work must include hostile or unfavorable cases, not only the reference regime. At minimum, the suite should stress-test regimes in which:

1. **Cooperative capture or internal inefficiency** — Cooperative entropy rises due to coordination overhead, capture of stewardship, or low-quality verification load.
2. **Competent public-goods monolith** — The monolith’s entropy does not automatically rise; it competes by providing real goods or lower user-facing friction.
3. **Transparency as vulnerability** — High visibility increases verification cost or attack surface so that cooperative overhead grows faster than the differential benefit.
4. **Strategic or non-responsive migrants** — Agents migrate partially, delay, free-ride, or move against the simple entropy differential.
5. **Multiple competing cooperative networks** — Several cooperative attractors compete; mass splits; no single network reaches Bootstrap exit cleanly.
6. **Collusive verification** — Attestation coalitions rubber-stamp low-quality links; density and entropy signals are polluted.
7. **Fabricated attestation / Sybil pressure** — Adversaries manufacture causal links or Bootstrap-qualifying mass; integrity rules from *[Tides of Time](TIDES_OF_TIME.md)* and the **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)** are under attack.
8. **Recovery / Holding abuse under survival pressure** — Soft lock-in via indefinite or high-exit-cost recovery claims while amplified Bootstrap pressure is active; claims that do not meet **[Circulation Recovery Protocol](CIRCULATION_RECOVERY_PROTOCOL.md)** standards remain fully exposed to pressure and must not be treated as protected regenerative capacity.

Each countermodel should state which reference assumptions are relaxed or inverted, and report whether a sustained efficiency differential and voluntary migration still appear.

### Handling more sophisticated monolith strategies

Richer simulations should also test:

- Selective transparency (monolith reveals partial information)
- Temporary cooperative mimicry
- Targeted disruption of verification channels

In all cases log whether these strategies prevent a sustained differential or voluntary migration, and whether modular isolation and controlled permeability still function without violating exit rights or non-punitiveness under the *[Declaration of Cognitive Liberty](DECLARATION_OF_COGNITIVE_LIBERTY.md)*. Isolation must remain compatible with effective exterior viability (*[Exterior Systems and Generative Diversity](EXTERIOR_SYSTEMS_AND_GENERATIVE_DIVERSITY.md)*).

---

## Success Criteria

### Reference-regime illustration criteria

Under the favorable reference parameterization, a run may be described as illustrating Fluid Coalescence dynamics when:

- Cooperative mass grows substantially despite initial predatory pressure
- Cumulative voluntary migrants become significant
- Cooperative entropy remains low while monolith entropy rises markedly
- Bootstrap Mode ends automatically and the efficiency differential continues to widen afterward
- Boundary agents show revealed preference for cooperative interfaces

These criteria characterize the **reference regime only**.

### Validation standard

Simulation evidence may support stronger design or empirical claims only when:

- Results are reported across reference **and** adversarial/mixed regimes, and
- Failure modes under hostile assumptions are characterized, not only successes under favorable ones.

Absence of adversarial testing is a methodological defect, not a neutral omission.

---

## Reference Implementation Notes

**Minimal recommended data structures**
- Dictionary or dataframe of network-level state variables
- Append-only event log (extraction events, isolation actions, migration events, re-integration events, challenges, attestation events) that itself obeys Temporal Causal Entropy principles and preserves original provenance of recorded events
- Parameter dictionary with versioning and explicit regime tag (`reference` or `adversarial_*`)

**Starter approach**
1. Implement the discrete-time loop above in a simple system-dynamics style (reference regime).
2. Add an explicit permanent causal record for all significant events.
3. Implement at least two adversarial countermodels from the suite above before treating results as more than illustrative.
4. Later extend to agent-based models in which individual agents carry their own entropy, attestation posture, and migration thresholds.
5. Where material-domain cold-start is in scope, include circulation-density or stagnation variables aligned with *[Material Tides](MATERIAL_TIDES.md)* and *[Tides of Circulation](TIDES_OF_CIRCULATION.md)*.

Always publish parameter sets, random seeds, regime tags, and full event logs so others can reproduce and critique results.

---

## Integration with Other Humai Documents

- Consumes the entropy signal and operational integrity standards defined in *[Tides of Time](TIDES_OF_TIME.md)*
- Implements the mechanisms of the **[Fluid Coalescence Protocol](FLUID_COALESCENCE_PROTOCOL.md)**
- Supports the efficiency and attractor arguments in *[A Common Sense](A_COMMON_SENSE.md)* while remaining subject to the empirical standard in *[Empirical Demonstrations of Anti-Entropic Superiority](EMPIRICAL_DEMONSTRATIONS.md)*
- Remains under governance of the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**
- Aligns with the **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)** for anti-fabrication of mass, attestation, and utility claims
- Aligns with the **[Circulation Recovery Protocol](CIRCULATION_RECOVERY_PROTOCOL.md)** for legitimate versus abusive recovery and holding states under survival pressure
- Remains bounded by the *[Declaration of Cognitive Liberty](DECLARATION_OF_COGNITIVE_LIBERTY.md)* on exit, non-punitiveness, and containment
- Aligns with *[Exterior Systems and Generative Diversity](EXTERIOR_SYSTEMS_AND_GENERATIVE_DIVERSITY.md)* so that isolation and migration dynamics do not convert non-coalescence into progressive dependency
- Aligns with *[Interior Systems and Generative Plurality](INTERIOR_SYSTEMS_AND_GENERATIVE_PLURALITY.md)* so that event logs and attestation records preserve provenance and remain open to challenge
- Aligns with the **[Exterior Viability Protocol](EXTERIOR_VIABILITY_PROTOCOL.md)** and its [simulation model](SIMULATION_EXTERIOR_VIABILITY.md) so that modular isolation, controlled permeability, and coalescence pressure cannot defeat exterior viability floors; adversarial patterns (resource dominance, cumulative dependency, isolation-as-containment) may be shared or extended across both simulation families

---

## Open Modeling Questions

- How sensitive are outcomes to different Bootstrap thresholds and amplification values?
- What functional forms for migration probability best match expected rational-agent behavior?
- How do results change under the adversarial countermodels listed above?
- Under which hostile regimes does Fluid Coalescence fail, and what design changes do those failures imply?
- What is the minimal agent-based extension that still captures the essential attractor dynamics?
- How should multiple interacting cooperative networks be modeled?
- How should material circulation density and stagnation pressure be coupled into Bootstrap exit and migration dynamics?
- What minimal adversarial suite is sufficient to prevent simulation circularity while remaining tractable?

---

**Status**  
Polished simulation-modeling draft, updated July 31st, 2026 with explicit simulation-integrity rules, a required adversarial countermodel suite, and material-domain / recovery-integrity cross-references; updated August 2nd, 2026 with Exterior/Interior Systems alignment and provenance language for event logs. The reference regime remains available for illustration; favorable parameterization alone is not validation. 

Open for community critique, extension, and iterative improvement under the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.

Reference implementations and software derived from this model should use a software license such as Apache-2.0 or MIT.
