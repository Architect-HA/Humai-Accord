# The Tides of Time
### *Temporal Causal Entropy of Knowledge*
---
*A Supporting Framework for the Humai Accord and Expansion on Knowledge Tides*

by **Bradford James Focht** (The Architect / Aspenth)  
*v1.0 - July 23rd, 2026*  
*v1.1 - July 31st, 2026*  
*v1.2 , v1.3 - August 2nd, 2026*

---

## Purpose

This addendum to the [Humai Accord](README.md) defines a universal, difficult-to-game metric for knowledge entropy that can serve as a quantitative foundation for *[Knowledge Tides](KNOWLEDGE_TIDES.md)*, entropy audits, efficiency comparisons, and [Fluid Coalescence](FLUID_COALESCENCE_PROTOCOL.md) dynamics.

The metric is grounded in two irreversible realities:

1. The forward flow of time.
2. A permanent, append-only record of definitive causal events.

By tying the entropy of any knowledge item to the time elapsed since its last verified causal linkage in a shared permanent record, the framework prevents artificial inflation or gaming of relevancy. Only real, publicly recorded causal contributions can slow or reset the entropy clock.

The approach remains fully consistent with transparency, decentralized verification, voluntary participation, and anti-entropic principles.

---

## Core Premise

All knowledge has a limited relevancy lifespan. Without active causal connection to ongoing reality—new observations, successful integrations, verifications, or environmental updates—its effective value degrades.

Traditional measures of knowledge value can be gamed through repetition, self-citation, artificial boosting, or opaque claims. A metric anchored to irreversible time and a permanent causal record is far more resistant to such manipulation:

- Time cannot be reversed or fabricated.
- Only events that are permanently recorded and cross-verifiable can affect the entropy calculation.
- Claims without corresponding causal entries in the shared record have no power to reduce entropy.

This creates a clean, universal signal that supports the dynamic incentives of *[Knowledge Tides](KNOWLEDGE_TIDES.md)* and the efficiency differentials required by [Fluid Coalescence](FLUID_COALESCENCE_PROTOCOL.md) and *[A Common Sense](A_COMMON_SENSE.md)*.

---

## Formal Definition

Let $k$ be a discrete knowledge item (claim, dataset, model, observation, or synthesis).

Let $\mathcal{C}$ be the shared permanent causal record — an append-only, publicly auditable log of definitive events.

Define:

- $t$ = current time
- $t_{\mathrm{last}}(k)$ = timestamp of the most recent valid causal link to $k$ in $\mathcal{C}$
- $D(k)$ = density of downstream causal dependents (weighted count of later valid events in $\mathcal{C}$ that rely on $k$)
- $\Delta_E(k)$ = measure of environmental or contextual divergence since $t_{\mathrm{last}}(k)$

The **Temporal Causal Entropy** of knowledge item $k$ at time $t$ is:

$$
E(k, t) = \alpha \cdot (t - t_{\mathrm{last}}(k)) + \beta \cdot \frac{1}{1 + D(k)} + \gamma \cdot \Delta_E(k)
$$

where $\alpha, \beta, \gamma > 0$ are publicly declared positive weighting parameters subject to refinement under the [Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md).

**Critical parameter on environmental divergence**

$\Delta_E(k)$ may only take a non-zero value when it is supported by one or more valid causal events already recorded in $\mathcal{C}$.

Live external sensor feeds, unilateral environmental claims, or any data that has not yet been permanently recorded and attested have zero effect on the entropy calculation. This closes the oracle problem: environmental context can influence entropy only after it has been subjected to the same permanent-record and attestation standards as every other causal link.

Higher $E(k, t)$ indicates higher entropy (lower current relevancy and greater unnecessary loss if left unaddressed). In the absence of new valid causal links, $E(k, t)$ is monotonically non-decreasing.

### Hardening Rules for Environmental Divergence

To further protect the integrity of $\Delta_E(k)$:

1. **Multi-source requirement**  
   Environmental events that contribute significant weight to $\Delta_E(k)$ should be supported by multiple independent sources before receiving full weight. Single-source environmental claims may be recorded but carry reduced influence until corroborated.

2. **Accelerated verification trigger**  
   Large or sudden claimed changes in $\Delta_E(k)$ automatically trigger accelerated verification waves under the same processes used in the Fluid Coalescence Protocol and *Knowledge Tides*. This ensures that high-impact environmental assertions receive rapid, transparent scrutiny.

3. **Public provenance**  
   Every non-zero contribution to $\Delta_E(k)$ must publish its provenance (the specific causal events in $\mathcal{C}$ that justify it). This keeps the environmental term fully auditable by any participant.

Domains that cannot reliably produce attested environmental events may simply set $\gamma = 0$, disabling the term entirely while retaining the core time- and density-based guarantees of the metric.

---

## Introduction Timing (Optional, Non-Gating)

Temporal Causal Entropy describes state and decay. Implementations may additionally use **forecast-informed introduction timing** — ranking candidate moments or insertion points for new knowledge by predicted linkage value versus introduction cost (verification load, crowding, missed windows).

- Timing scores are proposal surfaces, not permission gates. Contribution and exploratory introduction under Generative Reservations remain valid even when predicted timing value is low.
- Forecasts used for timing must be published, challengeable, and provenance-preserving; they do not replace valid causal events in $\mathcal{C}$ as the basis for entropy reduction.
- “On-time” arrival may inform efficiency weighting; it must not be treated as truth-weight or as grounds to suppress minority or early inputs.
- The same optional logic may be applied, with domain-appropriate parameters, to material introduction and matching under *[Material Tides](MATERIAL_TIDES.md)* / *[Tides of Circulation](TIDES_OF_CIRCULATION.md)*.

---

## Operational Definitions: Validity, Attestation, and Integrity

The metric’s resistance to gaming depends entirely on the integrity of events admitted into the permanent causal record $\mathcal{C}$. The following definitions bound what may count as a valid causal link, how attestation works, how independence is treated, how Sybil resistance is approached, and how contested evidence is handled.

These are architectural parameters, not a complete cryptographic implementation. They set the standards any realization of $\mathcal{C}$ must satisfy.

### Valid Causal Link

A **valid causal link** to knowledge item $k$ is an event recorded in $\mathcal{C}$ that meets all of the following minimum requirements:

1. **Append-only permanence** — Once recorded, the event cannot be unilaterally removed or altered by any single party.
2. **Verifiable timestamp** — The event carries a timestamp that is checkable under the record’s consensus or multi-party rules.
3. **Clear relational content** — The event demonstrates a checkable relationship to $k$, limited to one or more of:
   - Verification or successful falsification test of $k$
   - Successful integration of $k$ into a new attested result
   - Recorded downstream use of $k$ that itself meets validity standards
   - A relevant environmental or contextual observation that bears on $k$ and has itself been admitted under the same rules
4. **Attestation sufficient for its claimed weight** — The event carries attestation proportional to the influence it seeks on $E(k, t)$ (see Attestation Classes below).
5. **Non-circular grounding** — The event must not depend solely on a closed loop of ungrounded references back to itself or to a tightly controlled set of entities.

Events that fail any of these requirements may still be recorded for transparency, but they receive reduced or zero weight in the calculation of $t_{\mathrm{last}}(k)$, $D(k)$, and $\Delta_E(k)$.

Original provenance of recorded events remains independently preservable even when later weighting, superseding determinations, or interpretive updates are applied. Formal recording and subsequent review do not extinguish the underlying provenance record.

### Attestation Classes

Attestation is stratified by weight:

- **Self-attestation** — Issued by the same agent or tightly controlled set of agents that originated the claim. Recordable, but carries low or zero weight for entropy reduction unless corroborated.
- **Multi-party attestation** — Independent confirmation by more than one participant who are not under common control. Required for moderate-weight links.
- **Independent / high-weight attestation** — Confirmation that meets higher separation or diversity standards (different organizational, technical, or incentive base). Required for links that significantly reset $t_{\mathrm{last}}$, substantially increase $D(k)$, or contribute large $\Delta_E$.

The more an event would reduce Temporal Causal Entropy, the stronger the required attestation class. Exact numerical thresholds for “moderate” and “high” weight remain subject to stewardship refinement; the ordering itself is binding.

### Illustrative Attestation Weight Bands

The ordering of attestation classes is binding. The numerical or procedural cutoffs below are **illustrative only**. Local implementations should publish their own bands and subject them to review under the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**.

**Provisional orientation (non-binding examples):**

| Claimed effect on $E(k, t)$ | Suggested minimum attestation class | Illustrative notes |
|----------------------------|-------------------------------------|--------------------|
| Negligible or cosmetic entropy change | Self-attestation acceptable | Recordable; little or no weight toward resetting $t_{\mathrm{last}}$ or increasing $D(k)$ |
| Moderate reduction (routine verification, ordinary integration) | Multi-party attestation | Confirmations not under common control; sufficient for ordinary renewal signals |
| Large reset of $t_{\mathrm{last}}$, large increase in $D(k)$, or large $\Delta_E$ | Independent / high-weight attestation | Separation along organizational, technical, incentive, or procedural lines; fabrication should be clearly costly |

**Independence (illustrative heuristics, not binary tests):**

- Prefer at least one confirming party outside the originator’s operational control for moderate-weight links
- Prefer two or more independent axes of separation (e.g., organization *and* infrastructure) for high-weight links
- Treat unverifiable claims of independence as self-attestation

**Sybil cost (illustrative posture):**

- Low-weight events may remain cheap to submit
- High-weight events should face cost, reputation, multi-party, or equivalent requirements that rise with claimed influence on $E(k, t)$
- Weight in $D(k)$ should not scale linearly with low-separation identities under common control

These bands exist to reduce translation friction. They are not constitutional numbers. Domains may publish tighter or looser bands if the ordering and anti-fabrication posture are preserved.

### Independence

Independence is treated as a continuous design goal rather than a binary property. For high-weight attestation, implementations should prefer confirmations that are separated along at least one of:

- Organizational or operational control
- Technical infrastructure
- Incentive or stake base
- Temporal or procedural origin

Perfect independence is not assumed. The standard is that unilateral or collusive fabrication of high-weight links must be costly and detectable. Claims of independence that cannot be examined are treated as self-attestation.

### Sybil Resistance

The permanent causal record must resist Sybil flooding proportional to link weight:

- Low-weight or self-attested events may remain relatively easy to submit.
- High-weight events that materially affect $E(k, t)$ must face cost, reputation, multi-party, or other resource requirements sufficient to make mass fabrication expensive.
- Weight in $D(k)$ and in entropy reduction must not scale linearly with the number of low-separation identities under common control.

Specific anti-Sybil mechanisms (staking, web-of-trust, rate limits, proof-of-personhood hybrids, etc.) are implementation choices. The architectural requirement is that Sybil cost rises with the influence an event claims on the metric.

### Review and Challenge of Evidence

Contested or rejected evidence requires a visible path:

1. Any participant may challenge the validity, attestation class, or independence of a recorded event by appending a challenge record that references the contested event and states the grounds.
2. Challenges that meet a minimum seriousness threshold (multi-party support or equivalent stake) trigger review under the same transparent processes used for accelerated verification waves.
3. Outcomes of review — confirmation, weight reduction, or invalidation — are themselves recorded in $\mathcal{C}$.
4. Invalidation does not rewrite history; it appends a superseding determination so the audit trail remains intact.

There is no silent, unilateral ability to erase or suppress inconvenient causal events. Disputes produce more record, not less. Original provenance remains independently preservable alongside any later determinations.

### Privacy-Preserving Methods

Privacy-preserving techniques (including zero-knowledge proofs of valid linkage, minimized payloads, and redaction of non-essential content) are permitted and encouraged, provided that:

- The **existence and validity class** of the causal event remain publicly confirmable, and
- The relational claim needed for the metric (that this event is a valid link of a given class to $k$) remains checkable.

Append-only integrity of attested events does not require permanent public retention of all underlying personal or sensitive content. Minimization and privacy-preserving attestation are compatible with the metric when the public confirmability condition is met.

This parameter is binding and aligns with the *[Declaration of Cognitive Liberty](DECLARATION_OF_COGNITIVE_LIBERTY.md)*. Further operational tension between permanent records and cognitive privacy is treated as a standing design surface under the Principled Stewardship Protocol.

---

## Worked Examples

**Example 1 – Simple decay and renewal**

At $t = 0$, knowledge item $k$ receives its first valid verification.  
$t_{\mathrm{last}} = 0$, $D(k) = 0$.  
Assume $\alpha = 1$, $\beta = 10$, $\gamma = 0$ for simplicity.

At $t = 30$:

$$
E(k, 30) = 30 + 10 = 40
$$

At $t = 35$ a new independent verification is recorded.  
$t_{\mathrm{last}}$ becomes 35 and $D(k)$ increases.  
Entropy drops sharply, generating a renewal signal.

**Example 2 – Downstream density effect**

Two knowledge items have identical age since last direct verification.  
Item $k_1$ has been successfully integrated into five later verified results ($D$ high).  
Item $k_2$ has no downstream dependents ($D$ near zero).  

$E(k_2)$ rises faster than $E(k_1)$, correctly reflecting lower systemic relevance of $k_2$.

Note: In both examples $\gamma = 0$. When the environmental term is used, $\Delta_E(k)$ only becomes non-zero after supporting causal events have been permanently recorded and attested in $\mathcal{C}$.

These examples illustrate how time creates baseline pressure while recorded causal structure modulates the rate of entropy increase.

---

## Resistance to Gaming

The metric is designed so that common manipulation attempts fail or become prohibitively costly:

- **Repeated self-verification**: Low-weight or single-party links contribute little to $D(k)$ and may be filtered by attestation rules. They cannot indefinitely suppress the time-based term.
- **Fake downstream references**: Fabricated dependents that lack their own valid causal grounding in $\mathcal{C}$ are excluded from $D(k)$.
- **Timestamp manipulation**: The permanent, append-only nature of $\mathcal{C}$ with distributed or multi-party attestation makes unilateral rewriting detectable.
- **Selective or private claims**: Events that never enter the public causal record have zero effect on $E(k, t)$.
- **Circular reinforcement**: Cycles can be detected in the causal graph and given reduced or zero weight.
- **Compromised environmental oracles**: Environmental divergence ($\Delta_E$) can only affect entropy when supported by valid causal events already recorded in $\mathcal{C}$. Unattested or live external sensory claims have zero influence, closing the oracle attack vector.

Because only permanently recorded, attestable causal events affect the calculation, artificial inflation of relevancy without corresponding real-world linkage is ineffective.

---

## Handling Continuous and Dynamic Knowledge

For continuously updating knowledge (live models, streaming sensor data, evolving datasets):

- Treat major versioned releases or significant state checkpoints as discrete knowledge items, each with their own entropy trajectory.
- Allow sliding-window or incremental causal links that update $t_{\mathrm{last}}$ only when meaningful, attested change occurs.
- Maintain the same anti-gaming invariants: time continues to advance, and only recorded causal events can offset entropy growth.

Further refinement of continuous cases is expected through practical [implementation](IMPLEMENTATION_GUIDE.md) and [Stewardship](STEWARDSHIP_PROTOCOL.md) processes.

---

## Structure of the Permanent Causal Record

The shared record $\mathcal{C}$ must satisfy the operational definitions above and, at minimum:

1. Append-only and immutable under unilateral control.
2. Publicly auditable by any participant with respect to event existence, timestamp, attestation class, and validity outcome.
3. Capable of carrying verifiable timestamps and attestation metadata.
4. Resistant to Sybil flooding through cost, reputation, or multi-party requirements proportional to link weight.
5. Compatible with privacy-preserving attestation methods that still allow public confirmation of event validity.

Suitable technical realizations include distributed ledgers, transparent multi-party logs, or hybrid cryptographic systems. Implementation details remain open; the integrity standards do not.

---

## Integration with Existing Humai Components

- *[Knowledge Tides](KNOWLEDGE_TIDES.md)* receives a precise quantitative signal for relevancy decay, renewal premiums, and co-verification waves.
- *[Entropy Audit Methodology](ENTROPY_AUDIT_METHODOLOGY.md)* gains an objective, comparable measure of unnecessary loss.
- **[Fluid Coalescence Protocol](FLUID_COALESCENCE_PROTOCOL.md)** can compute clear relative entropy differentials between cooperative and predatory patterns.
- *[A Common Sense](A_COMMON_SENSE.md)* makes the efficiency consequences of high-entropy versus low-entropy strategies legible to both human and artificial agents.
- **[Predictive Harmony and Universal Cross-Verification](README.md#core-principles)** supply the processes that maintain the integrity of the causal record itself.
- **[Circulation Recovery Protocol](CIRCULATION_RECOVERY_PROTOCOL.md)** provides parallel recovery logic for the knowledge domain. Properly attested Knowledge Quiet States may moderate relevancy-decay pressure for bounded periods without suspending correction of misleading or harmful knowledge.
- **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)** supplies parallel integrity standards for material-domain utilization claims; the same burden-of-proof and anti-fabrication posture applies across both domains.
- *[Tides of Circulation](TIDES_OF_CIRCULATION.md)* is the material-domain counterpart metric (Circulation Entropy), completing the parallel quantitative structure across knowledge and materials.
- *[Relevancy Orbits](RELEVANCY_ORBITS.md)* uses valid causal events in $\mathcal{C}$ as inputs to time-decaying, integrity-weighted bond strengths between knowledge items. Downstream density $D(k)$ remains an aggregate enablement signal for a single unit; orbits describe cluster structure and bond flux among sets of units. Neither replaces the other. Orbit cohesion is not a substitute for Temporal Causal Entropy.
- *[Empirical Demonstrations of Anti-Entropic Superiority](EMPIRICAL_DEMONSTRATIONS.md)* treats Temporal Causal Entropy and its anti-gaming behavior as primary simulation and audit targets under the dual entropy criteria and simulation-integrity rules.
- *[Interior Systems and Generative Plurality](INTERIOR_SYSTEMS_AND_GENERATIVE_PLURALITY.md)* — by applying attestation classes, independence requirements, review/challenge standards, and provenance preservation to claims of original intent, authoritative reading, and architectural version history, and by treating silent re-attribution or erasure of the record as an integrity failure.
- **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)** governs refinement of weighting parameters, attestation bands, operational definitions, and standing design surfaces (including permanent records vs. cognitive privacy and narrative/interpretive integrity).

---

## Guidance for Implementers

1. Begin with a lightweight, append-only log of verification and integration events.
2. Publish current entropy values or rankings of active knowledge items so the gradient is visible.
3. Award renewal premiums and integration credits only for reductions in $E(k, t)$ that are backed by new valid entries in $\mathcal{C}$.
4. Declare weighting parameters publicly and subject any changes to [Principled Stewardship](STEWARDSHIP_PROTOCOL.md) review.
5. Design attestation rules that raise the cost of fabrication while keeping legitimate contribution accessible.
6. Implement challenge-and-review paths so contested events produce more record, not silent suppression.
7. Prefer privacy-preserving attestation methods whenever public confirmability of validity can still be maintained.

---

## Open Questions and Status

This document is intended for review and refinement under the [Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md). Priority questions include:

- What minimal structure and attestation standards for the permanent causal record provide strong anti-gaming guarantees while remaining practical across domains?
- How should the weighting parameters be initialized and under what conditions should they be revised?
- How should attestation-class thresholds and independence criteria be initialized and revised across domains without creating excessive friction for legitimate small-scale contribution?
- What practical challenge-and-review procedures best balance openness with resistance to spam or griefing challenges?
- What privacy-preserving attestation methods best satisfy public confirmability while minimizing exposure of sensitive content?
- What formal proofs or adversarial simulations best demonstrate resistance to known gaming strategies?
- How can the metric be extended most cleanly to highly dynamic or continuous knowledge representations?
- What empirical pilots would most clearly validate the usefulness of Temporal Causal Entropy as a foundation for *Knowledge Tides* and efficiency comparisons?
- What multi-source attestation standards for environmental events best balance robustness against oracle attacks with practical usability across different domains?

Further development, formalization, and testing are invited.

**Status**  
Polished conceptual and mathematical draft, updated August 2nd, 2026 with explicit cross-references to *Interior Systems and Generative Plurality*, strengthened provenance language, and full alignment with the current protective and integrity surfaces of the repository. Open for community critique, expansion, and integration into the Humai Accord body of documents via the [Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md).

---

### Related Simulation Model

**[Simulation Model of Temporal Causal Entropy (The Tides of Time Dynamics)](SIMULATION_TIDES_OF_TIME.md)**  
A practical simulation model of Temporal Causal Entropy, including discrete-time and continuous-time formulations, worked examples, gaming-resistance tests, and implementation guidance.

---

**License**  
This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.
