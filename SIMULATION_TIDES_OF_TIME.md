# Simulation Model of Temporal Causal Entropy
### The Tides of Time Dynamics
---
*A Supporting Technical Document for the Humai Accord*

**by Bradford James Focht (The Architect / Aspenth)**  
*July 23rd, 2026* 

---

## Purpose

This [Humai Accord](README.md) document provides a clear, implementable simulation model of [Temporal Causal Entropy (The Tides of Time)](TIDES_OF_TIME.md). 

It defines state variables, the core equation, discrete-time and continuous-time formulations, update rules, parameter guidance, test scenarios, and success criteria so that researchers and implementers can run reproducible simulations of relevancy decay, renewal dynamics, gaming resistance, and interaction with [Fluid Coalescence](FLUID_COALESCENCE_PROTOCOL.md).

The model remains fully consistent with transparency, decentralized verification, voluntary participation, and anti-entropic principles. It is intentionally simplified for clarity and rapid experimentation while remaining extensible to full causal-graph implementations.

---

## Core Modeling Goals

- Demonstrate time-driven entropy growth in the absence of new causal links
- Show entropy reduction through valid causal links and downstream density
- Test resistance to common gaming attempts
- Provide a clean entropy signal that can drive [Knowledge Tides](KNOWLEDGE_TIDES.md) incentives and [Fluid Coalescence](FLUID_COALESCENCE_PROTOCOL.md) differentials
- Remain simple enough for rapid iteration while supporting later high-fidelity extensions

---

## State Variables

**Per knowledge item $k$**
- $t_{\text{last}}(k)$ : timestamp of the most recent valid causal link
- $D(k)$ : downstream causal density (weighted count of later valid dependents)
- $\Delta_E(k)$ : environmental divergence (only if supported by attested events in $\mathcal{C}$)
- $E(k, t)$ : current Temporal Causal Entropy

**Global**
- $\mathcal{C}$ : shared permanent, append-only causal record
- $t$ : current time (discrete or continuous)

---

## Core Equation (Discrete Form)

$$
E(k, t) = \alpha \cdot (t - t_{\text{last}}(k)) + \beta \cdot \frac{1}{1 + D(k)} + \gamma \cdot \Delta_E(k)
$$

**Critical constraint**: $\Delta_E(k) = 0$ unless supported by one or more valid causal events already recorded in $\mathcal{C}$. Live or unattested external claims have no effect.

Higher $E(k, t)$ indicates higher entropy (lower current relevancy).

---

## Continuous-Time Formulation

For simulations that prefer continuous time, the entropy of a knowledge item can be expressed as the ordinary differential equation:

$$
\frac{dE(k)}{dt} = \alpha + \beta \cdot \frac{\partial}{\partial t}\left(\frac{1}{1+D(k)}\right) + \gamma \cdot \frac{d\Delta_E(k)}{dt}
$$

Under normal conditions (no new causal events) this simplifies to:

$$
\frac{dE(k)}{dt} = \alpha
$$

when $D(k)$ and $\Delta_E(k)$ are constant.

When a valid causal event occurs at time $t^*$:
- $t_{\text{last}}(k)$ jumps to $t^*$ (causing an instantaneous drop in the time-based term),
- $D(k)$ or $\Delta_E(k)$ may jump discontinuously according to the event,
- After the jump, linear growth at rate $\alpha$ resumes.

The continuous formulation preserves the same anti-gaming properties: only events recorded in the permanent causal record $\mathcal{C}$ can produce discontinuous reductions in entropy. Between events, entropy grows at a steady rate determined by $\alpha$.

Both the discrete-time and continuous-time versions are valid; choice depends on the larger simulation environment in which the metric is embedded.

---

## Parameters (Suggested Defaults)

| Parameter | Suggested Range | Role |
|-----------|----------------------|------|
| $\alpha$  | 0.8 – 1.5           | Weight of pure time decay |
| $\beta$  | 8 – 15              | Weight of downstream density |
| $\gamma$  | 0 – 5               | Weight of attested environmental divergence |

All parameters must be publicly declared and may be changed only through Principled Stewardship processes. Domains that cannot reliably attest environmental events should set $\gamma = 0$.

**Stochastic elements**  
When coupling this model with Fluid Coalescence or other system-dynamics simulations, small noise terms (e.g., in internal renewal) are sometimes useful. A recommended starting range for additive noise is $\pm 0.2$ to $\pm 0.5$ entropy units per step. Noise should remain small relative to the deterministic terms so that the core time-driven and causal-link dynamics stay dominant and interpretable.

---

## Discrete-Time Update Rules

At each time step $t$:

1. Advance global time: $t \leftarrow t + 1$

2. For every active knowledge item $k$:
   - Recompute $E(k, t)$ using the core equation and current values of $t_{\text{last}}(k)$, $D(k)$, and $\Delta_E(k)$.

3. Process new events submitted to the permanent causal record $\mathcal{C}$:
   - Validate each event against the definition of a valid causal link (permanent, timestamped, checkable relationship, and appropriate attestation).
   - If valid, update the affected $t_{\text{last}}(k)$ and/or $D(k)$ (and $\Delta_E(k)$ if the event is an attested environmental observation).
   - Reject or heavily down-weight events that fail attestation or create detectable circularity.

4. Apply any domain-specific filters (minimum multi-party requirements, Sybil-resistance costs, etc.).

5. Log the full state of every knowledge item and every accepted causal event so the simulation itself maintains an auditable permanent record.

---

## Worked Numerical Examples

**Example 1 – Simple decay and renewal**  
- $\alpha = 1$, $\beta = 10$, $\gamma = 0$  
- At $t = 0$, item $k$ receives its first valid verification: $t_{\text{last}} = 0$, $D = 0$  
- At $t = 30$: $E(k, 30) = 30 + 10 = 40$  
- At $t = 35$ a new independent verification is recorded → $t_{\text{last}} = 35$, $D$ increases  
- Entropy falls sharply, generating a renewal signal.

**Example 2 – Downstream density effect**  
Two items have identical age since last direct verification.  
- Item $k_1$ has been integrated into five later verified results (high $D$)  
- Item $k_2$ has no downstream dependents (low $D$)  
Result: $E(k_2)$ rises faster than $E(k_1)$, correctly reflecting lower systemic relevance.

**Example 3 – Attested environmental divergence**  
- $\alpha = 1$, $\beta = 10$, $\gamma = 4$  
- Item $k$ at $t = 20$ has $t_{\text{last}} = 10$, $D = 2$, so base entropy $= 10 + \dfrac{10}{1+2} \approx 13.33$  
- At $t = 22$ three independent sources record a significant contextual shift as valid causal events in $\mathcal{C}$.  
- $\Delta_E(k)$ is now set to $2.5$ (supported by attested events).  
- New entropy: $E(k, 22) = 12 + 3.33 + 4 \times 2.5 = 25.33$  
Entropy rises promptly because of the attested environmental change, while unattested claims would have left $\Delta_E = 0$.

---

## Resistance to Gaming (Simulation Tests)

The following attack scenarios should be explicitly tested:

- Repeated low-weight self-verification
- Fabricated downstream references lacking their own causal grounding
- Attempts to manipulate timestamps
- Unattested or live environmental claims trying to move $\Delta_E$
- Circular reinforcement loops

In a correct implementation all of these either fail to reduce entropy or produce only negligible, non-sustained effects.

---

## Handling Continuous and Dynamic Knowledge

- Treat major versioned releases or significant state checkpoints as discrete knowledge items, each with its own entropy trajectory.
- Allow incremental causal links that update $t_{\text{last}}$ only when a meaningful, attested change occurs.
- Preserve the core invariants: time continues to advance, and only recorded causal events can offset entropy growth.
- The continuous-time formulation above can be used when smoother trajectories are desired between discrete events.

---

## Reference Implementation Notes

**Minimal recommended data structures**
- Dictionary or table of knowledge items (with fields for $t_{\text{last}}$, $D$, $\Delta_E$, current $E$)
- Append-only event log that serves as the simulated permanent causal record $\mathcal{C}$
- Parameter dictionary with versioning

**Starter approach**
1. Implement the discrete-time loop above using simple data structures.
2. Enforce the valid-causal-link checks on every event before updating state.
3. Later extend to explicit causal graphs, richer attestation models, or continuous-time integration.

Always publish parameter sets, random seeds, and the full event log for reproducibility.

---

## Success Criteria

A simulation of **Temporal Causal Entropy** is considered successful when:

- Entropy rises smoothly with time in the absence of new valid causal links
- Valid causal events produce clear, attributable entropy reductions
- Common gaming strategies fail to create sustained artificial entropy reduction
- The environmental term remains zero until proper attestation occurs
- The resulting entropy signal generates sensible inputs for Knowledge Tides incentives and Fluid Coalescence differentials

---

## Integration with Other Humai Documents

- Directly implements the metric defined in **[The Tides of Time](TIDES_OF_TIME.md)**
- Supplies the quantitative entropy signal used by **[Knowledge Tides](KNOWLEDGE_TIDES.md)** and the **[Fluid Coalescence Protocol](FLUID_COALESCENCE_PROTOCOL.md)**
- Supports the efficiency arguments in **[A Common Sense](A_COMMON_SENSE.md)**
- Remains under governance of the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**

---

## Open Modeling Questions

- What default ranges for $\alpha$, $\beta$, $\gamma$ work best across different domains?
- What minimal structure of the simulated causal record still provides strong anti-gaming guarantees?
- How should partial or uncertain attestation be represented?
- What is the most efficient way to scale the model to thousands of knowledge items and dense causal graphs?
- How sensitive are downstream Fluid Coalescence outcomes to different entropy parameterizations?

---

**Status**  
Polished simulation-modeling draft. Open for community critique, extension, and iterative improvement under the [Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md).

---

**License**

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.
