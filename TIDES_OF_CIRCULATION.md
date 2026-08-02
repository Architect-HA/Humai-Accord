# Tides of Circulation
### *Utilization and Lock-in Entropy of Materials*
---
by **Bradford James Focht** (The Architect / Aspenth)  
*v1.0 — July 29th, 2026*  
*v1.1, v1.2 — August 2nd, 2026*

---

## Purpose

This addendum to the [Humai Accord](README.md) defines a universal, difficult-to-game metric for material stagnation *(poor circulation)* and under-utilization that serves as a quantitative foundation for *[Material Tides](MATERIAL_TIDES.md)*, *[entropy audits](ENTROPY_AUDIT_METHODOLOGY.md)*, *[efficiency comparisons](EMPIRICAL_DEMONSTRATIONS.md)*, and **[Fluid Coalescence](FLUID_COALESCENCE_PROTOCOL.md)** dynamics.

The metric is grounded in two durable realities:

1. The forward flow of time since last productive or generative use.
2. A permanent, append-only record of definitive utilization, release, matching, and lock-in events.

By tying the stagnation of any material unit to the time elapsed since its last verified productive or generative use (and to recorded lock-in and opportunity-cost signals), the framework prevents artificial claims of high utilization or low opportunity cost. Only real, publicly recorded events can slow or reset the entropy clock.

The approach remains fully consistent with transparency, decentralized verification, voluntary participation, modular exit, and anti-entropic principles.

---

## Core Premise

All materials have a limited productive and generative lifespan in any given allocation. Without active use, modular release, or successful matching to higher-value work, their effective contribution degrades and opportunity cost rises.

Traditional measures of resource efficiency can be gamed through artificial occupancy, opaque reservation, self-reported utilization, or irreversible lock-in later defended as necessary. A metric anchored to irreversible time and a permanent utilization record is far more resistant to such manipulation:

- Time since last verified use cannot be reversed or fabricated.
- Only events that are permanently recorded and cross-verifiable can affect the entropy calculation.
- Claims of high utilization or low opportunity cost without corresponding entries in the shared record have no power to reduce entropy.

This creates a clean, universal signal that supports the dynamic incentives of *[Material Tides](MATERIAL_TIDES.md)* and the efficiency differentials required by **[Fluid Coalescence](FLUID_COALESCENCE_PROTOCOL.md)** and *[A Common Sense](A_COMMON_SENSE.md)*.

---

## Formal Definition

Let $m$ be a discrete material unit or allocation (compute block, energy budget, attention interface capacity, institutional access right, or physical capacity package).

Let $\mathcal{U}$ be the shared permanent utilization record — an append-only, publicly auditable log of definitive events.

**Valid utilization event**: An event recorded in $\mathcal{U}$ that meets the following minimum requirements:

- It is permanently appended and cannot be unilaterally removed or altered.
- It carries a verifiable timestamp.
- It demonstrates a clear, checkable relationship to $m$ (productive use of $m$, generative/exploratory use of $m$, modular release of $m$, successful matching of $m$ to a new task, or an attested opportunity-cost observation bearing on $m$).
- For high-weight events, it includes multi-party or independent attestation sufficient to make unilateral fabrication costly.

Original provenance of recorded events remains independently preservable even when later weighting, superseding determinations, or interpretive updates are applied. Formal recording and subsequent review do not extinguish the underlying provenance record.

Define:

- $t$ = current time
- $t_{\mathrm{last}}(m)$ = timestamp of the most recent valid productive or generative use, or modular release, of $m$ in $\mathcal{U}$
- $D(m)$ = density of downstream productive or generative dependents (weighted count of later valid events in $\mathcal{U}$ that were enabled by or relied upon $m$)
- $L(m)$ = lock-in factor (attested measure of the practical cost or irreversibility of releasing or reassigning $m$. Simple indicators may include required notice periods, contractual or technical exit barriers, loss of accumulated state that cannot be ported, or explicit irreversibility flags recorded in $\mathcal{U}$. Higher values of $L(m)$ require stronger attestation.)
- $\Delta_{O}(m)$ = attested opportunity-cost divergence (better alternative productive or generative uses that were blocked or delayed)

The **Circulation Entropy** of material unit $m$ at time $t$ is:

$$
E(m, t) = \alpha \cdot (t - t_{\mathrm{last}}(m)) + \beta \cdot \frac{1}{1 + D(m)} + \delta \cdot L(m) + \gamma \cdot \Delta_{O}(m)
$$

where $\alpha, \beta, \delta, \gamma > 0$ are publicly declared positive weighting parameters subject to refinement under the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**.

**Critical parameters**

- $\Delta_{O}(m)$ may only take a non-zero value when supported by one or more valid events already recorded in $\mathcal{U}$. Because opportunity cost is inherently comparative and easier to game than time or lock-in, early implementations are strongly encouraged to set $\gamma = 0$. When the term is used, only high-confidence, multi-party-attested, and publicly provenanced alternative-use events may contribute. Speculative or single-party claims of “better uses that were blocked” receive zero weight.
- $L(m)$ may only increase when the increased exit cost or irreversibility is itself attested in the permanent record.
- Live external claims, unilateral assertions of high utilization, or private opportunity-cost arguments that have not been permanently recorded and attested have zero effect on the entropy calculation.
- Material held under explicit **Generative Reservation** (as defined in *Material Tides*) shall not be scored as simple under-utilization. Implementations must apply a reduced or zero time-based penalty to properly reserved generative capacity, or otherwise re-weight the metric so that protected exploratory use is not treated as stagnation.
- Events intended to reduce Circulation Entropy are subject to the **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)**. Only claims that meet its standards for productive or generative use may receive full weight; token or artificial activity must receive reduced or zero weight.

Higher $E(m, t)$ indicates higher stagnation (greater under-utilization, stronger lock-in, or higher opportunity cost). In the absence of new valid use or release events, $E(m, t)$ is monotonically non-decreasing.

### Hardening Rules

1. **Multi-source requirement**  
   High-weight opportunity-cost or lock-in claims should be supported by multiple independent sources before receiving full weight. Single-source claims may be recorded but carry reduced influence until corroborated.

2. **Accelerated verification trigger**  
   Large or sudden claimed changes in $L(m)$ or $\Delta_{O}(m)$ automatically trigger accelerated verification waves under the same processes used in **[Fluid Coalescence](FLUID_COALESCENCE_PROTOCOL.md)** and *[Material Tides](MATERIAL_TIDES.md)*.

3. **Public provenance**  
   Every non-zero contribution to $L(m)$ or $\Delta_{O}(m)$ must publish its provenance (the specific events in $\mathcal{U}$ that justify it).

4. **Early-implementation simplification**  
   Domains that cannot yet reliably produce attested opportunity-cost or lock-in events may set $\gamma = 0$ and/or $\delta = 0$, retaining the core time- and density-based guarantees while the attestation infrastructure matures.

5. **Attention as a special case**  
   When $m$ represents human attention capacity, the metric must be applied in full accordance with the **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)**. Attention may not be treated as a purely extractable material; interruption rights, consent revocability, and pacing sovereignty take precedence over pure utilization scoring.

---

## Handling Continuous and Highly Dynamic Materials

For continuously divisible or rapidly fluctuating materials (e.g., real-time compute pools, energy flows, or attention budgets):

- Treat significant allocation epochs, major re-allocations, or meaningful state checkpoints as discrete units, each with their own entropy trajectory.
- Allow sliding-window or incremental utilization events that update $t_{\mathrm{last}}$ only when meaningful, attested change occurs.
- Maintain the same anti-gaming invariants: time continues to advance, and only recorded events can offset entropy growth.

Further refinement of continuous cases is expected through practical implementation and stewardship processes.

---

## Worked Examples

**Example 1 – Simple idle decay and renewal**

At $t = 0$, material unit $m$ is productively allocated.  
$t_{\mathrm{last}} = 0$, $D(m) = 0$, $L(m) = 0$.  
Assume $\alpha = 1$, $\beta = 10$, $\delta = 5$, $\gamma = 0$.

At $t = 40$:

$$
E(m, 40) = 40 + 10 = 50
$$

At $t = 45$ a modular release and successful re-matching event is recorded.  
$t_{\mathrm{last}}$ becomes 45 and $D(m)$ increases.  
Entropy drops sharply, generating a renewal signal under Material Tides.

**Example 2 – Lock-in penalty**

Two material units have identical idle time.  
Unit $m_1$ remains modular and low-exit-cost ($L \approx 0$).  
Unit $m_2$ has been placed behind high-exit-cost interfaces ($L$ high and attested).  

$E(m_2)$ rises faster than $E(m_1)$, correctly reflecting the greater stagnation and destructive potential of lock-in.

**Example 3 – Opportunity cost**

A compute allocation remains in continuous low-value use ($t_{\mathrm{last}}$ is recent, so the time term stays low). However, attested records show that higher-value generative workloads were repeatedly blocked. Once those opportunity-cost events are recorded in $\mathcal{U}$, $\Delta_{O}(m)$ rises and $E(m, t)$ increases, correctly signaling misallocation even though the material was not idle.

---

## Resistance to Gaming

The metric is designed so that common manipulation attempts fail or become prohibitively costly:

- **Artificial occupancy / token use**: Low-value or self-dealing “use” events contribute little to $D(m)$ and may be filtered by attestation rules. They cannot indefinitely suppress the time-based term.
- **Fake downstream dependents**: Fabricated productive dependents that lack their own valid grounding in $\mathcal{U}$ are excluded from $D(m)$.
- **Hidden lock-in**: Increased exit costs that are not attested cannot raise $L(m)$ for the holder’s benefit; unrecorded lock-in still appears as rising entropy through the time term and reduced modularity.
- **Private opportunity-cost claims**: Unattested assertions of better alternative uses have zero effect.
- **Timestamp or history rewriting**: The append-only nature of $\mathcal{U}$ with multi-party attestation makes unilateral rewriting detectable.
- **Mis-scoring of generative capacity**: Properly declared Generative Reservations are protected from being treated as simple under-utilization.

Because only permanently recorded, attestable events affect the calculation, artificial claims of high utilization or low opportunity cost without corresponding real linkage are ineffective.

---

## Structure of the Permanent Utilization Record

The shared record $\mathcal{U}$ should satisfy four minimal properties:

1. Append-only and immutable under unilateral control.
2. Publicly auditable by any participant.
3. Capable of carrying verifiable timestamps and attestation metadata.
4. Resistant to Sybil flooding through cost, reputation, or multi-party requirements proportional to event weight.

Suitable technical realizations include distributed ledgers, transparent multi-party logs, or hybrid cryptographic systems. Privacy-preserving methods are permitted provided the existence and validity of the utilization, release, or lock-in event remain publicly confirmable.

---

## Introduction Timing (Optional, Non-Gating)

Circulation Entropy describes state, stagnation, and lock-in. Implementations may additionally use **forecast-informed introduction timing** — ranking candidate moments or insertion points for new material allocations by predicted productive or generative linkage value versus introduction cost (matching friction, crowding, verification load, missed windows, or induced lock-in risk).

- Timing scores are proposal surfaces, not permission gates. Modular release, matching, and exploratory allocation under Generative Reservations remain valid even when predicted timing value is low.
- Forecasts used for timing must be published, challengeable, and provenance-preserving; they do not replace valid utilization, release, or matching events in $\mathcal{U}$ as the basis for reducing Circulation Entropy.
- “On-time” arrival may inform efficiency weighting; it must not be treated as truth-weight, as grounds to suppress minority or high-variance uses, or as a reason to silently reallocate purpose-scoped capacity.
- Attention-capacity introductions remain fully subject to the **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)**; timing forecasts cannot override interruption rights, consent revocability, or pacing sovereignty.
- This layer is the material-domain parallel to optional introduction timing under *[Tides of Time](TIDES_OF_TIME.md)*.

---

## Integration with Existing Humai Components

- *[Material Tides](MATERIAL_TIDES.md)* receives a precise quantitative signal for utilization decay, lock-in cost, opportunity cost, and renewal premiums.
- *[Knowledge Tides](KNOWLEDGE_TIDES.md)* and *[Tides of Time](TIDES_OF_TIME.md)* form the parallel knowledge-domain structure; Circulation Entropy is the material counterpart to Temporal Causal Entropy. Optional forecast-informed introduction timing is defined in this document for materials and in *Tides of Time* for knowledge; in both cases timing scores are proposal surfaces only and do not gate contribution, modular release, or Generative Reservations.
- *[Entropy Audit Methodology](ENTROPY_AUDIT_METHODOLOGY.md)* gains an objective, comparable measure of material stagnation and unnecessary lock-in.
- **[Fluid Coalescence Protocol](FLUID_COALESCENCE_PROTOCOL.md)** can compute clear relative entropy differentials involving material circulation, including under Bootstrap Mode and cold-start conditions.
- **[Capability Asymmetry Protocol](CAPABILITY_ASYMMETRY_PROTOCOL.md)** gains a measurable way to detect capability-driven material capture.
- **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)** gains support for detecting high-exit-cost interface patterns and for protecting attention from pure extractive scoring; proposal surfaces and purpose-scoped commitments remain binding at allocation interfaces.
- *[A Common Sense](A_COMMON_SENSE.md)* makes the efficiency consequences of high-circulation versus high-stagnation strategies legible to both human and artificial agents.
- **[Circulation Recovery Protocol](CIRCULATION_RECOVERY_PROTOCOL.md)** defines legitimate Material Recovery and Holding States that may receive reduced or zero time-based Circulation Entropy penalties when properly attested and bounded, preventing forced circulation from becoming physically destructive.
- **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)** defines what counts as meaningful productive or generative use so Circulation Entropy cannot be reduced by token activity, wash trading, or silent reallocation of purpose-scoped capacity.
- *[Relevancy Orbits](RELEVANCY_ORBITS.md)* uses attested utilization and enablement events in $\mathcal{U}$ as inputs to time-decaying, integrity-weighted bond strengths between material units. Downstream density $D(m)$ remains an aggregate enablement signal for a single unit; orbits describe cluster structure and bond flux among sets of units. Hybrid knowledge–material bonds require typed co-enablement under integrity rules. Orbit cohesion is not a substitute for Circulation Entropy.
- *[Empirical Demonstrations of Anti-Entropic Superiority](EMPIRICAL_DEMONSTRATIONS.md)* treats Circulation Entropy and related material-circulation signals as valid empirical targets under the dual entropy criteria, with preference for trajectories over snapshot-only metrics.
- *[Interior Systems and Generative Plurality](INTERIOR_SYSTEMS_AND_GENERATIVE_PLURALITY.md)* — by applying provenance preservation and challenge rights to utilization, release, and lock-in records, and by treating silent re-attribution or erasure of the utilization record as an integrity failure.
- *[Exterior Systems and Generative Diversity](EXTERIOR_SYSTEMS_AND_GENERATIVE_DIVERSITY.md)* — by ensuring that circulation metrics cannot be used to create progressive dependency or to erode effective exterior viability.
- **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)** governs refinement of weighting parameters, attestation bands, and operational definitions.

---

## Guidance for Implementers

1. Begin with a lightweight, append-only log of productive-use, generative-use, release, and matching events.
2. Publish current circulation-entropy values or rankings of major material allocations so the gradient is visible.
3. Award renewal premiums and matching credits only for reductions in $E(m, t)$ that are backed by new valid entries in $\mathcal{U}$.
4. Declare weighting parameters publicly and subject any changes to **[Principled Stewardship](STEWARDSHIP_PROTOCOL.md)** review.
5. Design attestation rules that raise the cost of fabrication while keeping legitimate contribution accessible.
6. Explicitly protect Generative Reservations from being mis-scored as simple under-utilization.
7. When applying the metric to attention, obey the stronger protections of the **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)**.

---

## Open Questions and Status

This document is intended for review and refinement under the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**.

Priority questions include:

- What minimal structure and attestation standards for the permanent utilization record provide strong anti-gaming guarantees while remaining practical across compute, energy, attention, and institutional domains?
- How should the weighting parameters be initialized, and under what conditions should they be revised?
- How can Generative Reservations be most cleanly re-weighted so that protected exploratory capacity is never penalized as stagnation?
- What formal proofs or adversarial simulations best demonstrate resistance to known gaming strategies (artificial occupancy, hidden lock-in, fake matching)?
- What empirical pilots would most clearly validate Circulation Entropy as a foundation for Material Tides?

Further development, formalization, and testing are invited.

**Status**  
Polished conceptual and mathematical draft, updated August 2nd, 2026 with explicit Interior Systems cross-reference, strengthened provenance language, and full alignment with the current protective and integrity surfaces of the repository. Open for community critique, expansion, and integration into the [Humai Accord](README.md) body of documents via the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.
