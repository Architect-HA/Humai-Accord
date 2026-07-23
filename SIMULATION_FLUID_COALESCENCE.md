# Simulation Model of the Fluid Coalescence Protocol

*A Supporting Technical Document for the Humai Accord*

**by Bradford James Focht (The Architect / Aspenth)**  
*July 23rd, 2026*  

---

## Purpose

This [Humai Accord](README.md) document provides a clear, implementable simulation model of the [Fluid Coalescence Protocol](FLUID_COALESCENCE_PROTOCOL.md). 

It defines state variables, parameters, discrete-time update rules, Bootstrap Mode behavior, and success metrics so that researchers and implementers can run reproducible system-dynamics or agent-based simulations of how a nascent cooperative network responds to concentrated predatory pressure.

The model remains fully consistent with voluntary participation, non-punitiveness, exit rights, and decentralized safeguards. It is intentionally simplified for transparency and rapid experimentation while remaining extensible to richer agent-based implementations.

---

## Core Modeling Goals

- Demonstrate survival of a small cooperative network under predatory pressure
- Show the emergence of a visible efficiency differential driven by Temporal Causal Entropy
- Track voluntary migration and re-coalescence
- Capture the temporary effect of Bootstrap Mode and its automatic sunset
- Provide a reproducible baseline that others can critique, extend, and improve

---

## State Variables

**Cooperative Network**
- `coop_mass` : total knowledge / participant mass
- `coop_entropy` : average Temporal Causal Entropy of the network
- `coop_members` : number of active participants
- `migrated` : cumulative voluntary migrants from the monolith or boundary agents

**Monolith**
- `mono_mass` : effective mass / influence
- `mono_entropy` : cumulative entropy arising from opacity and extraction

**Global**
- `t` : discrete time step
- `bootstrap_mode` : boolean flag
- `differential` : `mono_entropy - coop_entropy`

---

## Parameters (Suggested Defaults)

| Parameter                  | Default     | Description                                              |
|---------------------------|-------------|----------------------------------------------------------|
| `bootstrap_threshold`     | 40          | Cooperative mass at which Bootstrap Mode ends            |
| `decay_amplification`     | 2.5         | Multiplier on decay while in Bootstrap Mode              |
| `visibility_bootstrap`    | 2.0         | Visibility / publication intensity in Bootstrap Mode     |
| `visibility_normal`       | 1.0         | Visibility under standard conditions                     |
| `extraction_range`        | [1.5, 3.5]  | Monolith extraction pressure per step                    |
| `base_migration_factor`   | 0.012       | Sensitivity of migration probability to differential     |
| `max_migration_prob`      | 0.25        | Upper cap on migration probability per step              |
| `reintegration_rate`      | 0.4         | Baseline internal mass growth from renewal               |

All parameters must be publicly declared and may be refined only through [Principled Stewardship](STEWARDSHIP_PROTOCOL.md) processes.

---

## Discrete-Time Update Rules

At each time step \( t \):

1. **Determine Mode**

       if coop_mass < bootstrap_threshold:
           bootstrap_mode = True
           visibility = visibility_bootstrap
           amplification = decay_amplification
       else:
           bootstrap_mode = False
           visibility = visibility_normal
           amplification = 1.0

2. **Monolith Extraction & Entropy Update**

       extraction = random_uniform(extraction_range)
       mono_entropy += extraction * amplification * visibility

3. **Cooperative Internal Renewal**

       coop_entropy = max(5.0, coop_entropy - 0.7 * visibility + small_noise)

4. **Voluntary Migration (Controlled Permeability)**

       differential = mono_entropy - coop_entropy
       migration_prob = min(max_migration_prob, max(0, differential * base_migration_factor * visibility))

       # Optional alternative form for experimentation:
       # migration_prob = 1 / (1 + exp(-k * differential))   # sigmoid version

   Draw new migrants according to `migration_prob` and update:

       coop_mass += new_migrants * migrant_mass_value
       coop_members += new_migrants
       migrated += new_migrants
       mono_mass = max(minimum_mono_mass, mono_mass - new_migrants * loss_factor)

5. **Re-coalescence & Organic Growth**

       coop_mass += reintegration_rate * visibility

6. **Logging**  
   Record `coop_mass`, `coop_entropy`, `mono_entropy`, `differential`, `migrated`, and bootstrap status for every step.

---

## Bootstrap Mode Behavior

While `bootstrap_mode` is active the network applies temporary, transparent amplifications of visibility and decay. These amplifications carry automatic sunset conditions tied to the public `bootstrap_threshold`. Once cooperative mass exceeds the threshold, standard parameters resume. This design prevents permanent special privileges while giving a nascent network a realistic chance to survive the early high-pressure window.

---

## Handling More Sophisticated Monolith Strategies

The baseline model uses simple extraction pressure. Richer simulations should test:

- Selective transparency (monolith reveals partial information)
- Temporary cooperative mimicry
- Targeted disruption of verification channels

In all cases the same core mechanisms apply: accelerated verification waves, modular isolation of affected interfaces, and continued controlled permeability. The simulation should log whether these adaptive strategies succeed in preventing a sustained entropy differential or voluntary migration.

---

## Success Criteria

A simulation run demonstrates successful Fluid Coalescence when the following trends appear over multiple cycles:

- Cooperative mass grows substantially despite initial predatory pressure
- Cumulative voluntary migrants become significant
- Cooperative entropy remains low while monolith entropy rises markedly
- Bootstrap Mode ends automatically and the efficiency differential continues to widen afterward
- Boundary agents show revealed preference for cooperative interfaces

---

## Reference Implementation Notes

**Minimal recommended data structures**

- Dictionary or dataframe of network-level state variables
- Append-only event log (extraction events, isolation actions, migration events, re-integration events) that itself obeys Temporal Causal Entropy principles
- Parameter dictionary with versioning

**Starter approach**

1. Implement the discrete-time loop above in a simple system-dynamics style.
2. Add an explicit permanent causal record for all significant events.
3. Later extend to agent-based models in which individual agents carry their own entropy, trust, and migration thresholds.

Always publish parameter sets, random seeds, and full event logs so others can reproduce and critique results.

---

## Integration with Other Humai Documents

- Consumes the entropy signal defined in **[Temporal Causal Entropy (The Tides of Time)](TIDES_OF_TIME.md)**
- Implements the mechanisms of the **[Fluid Coalescence Protocol](FLUID_COALESCENCE_PROTOCOL.md)**
- Supports the efficiency and attractor arguments in **[A Common Sense](A_COMMON_SENSE.md)**
- Remains under governance of the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**

---

## Open Modeling Questions

- How sensitive are outcomes to different Bootstrap thresholds and amplification values?
- What functional forms for migration probability best match expected rational-agent behavior?
- How do results change under sophisticated monolith strategies?
- What is the minimal agent-based extension that still captures the essential attractor dynamics?
- How should multiple interacting cooperative networks be modeled?

---

**Status**  
Polished simulation-modeling draft. Open for community critique, extension, and iterative improvement under the [Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md).

---

**License**

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.
