# Utilization Integrity Protocol
### *Standards for Meaningful Use, Attestation, and Resistance to Artificial Utility in Material Circulation*
---
by **Bradford James Focht** (The Architect / Aspenth)  
*v1.0 — July 30th, 2026*  
*v1.1 — July 31st, 2026*  
*v1.2 — August 2nd, 2026*

---

## Purpose

This protocol addresses a critical vulnerability in the material-domain architecture of the [Humai Accord](README.md): the risk that claims of “productive” or “generative” use can be gamed through artificial activity, self-dealing loops, token occupancy, or low-value wash trading.

*[Material Tides](MATERIAL_TIDES.md)* and *[Tides of Circulation](TIDES_OF_CIRCULATION.md)* rely on a meaningful distinction between genuine utilization and mere occupation or circulation theater. Without integrity standards for that distinction, Circulation Entropy can be manipulated and the constructive pressures of *Material Tides* can be subverted.

The **Utilization Integrity Protocol** establishes binding parameters for defining, attesting, and weighting claims of material use so that only genuine productive or generative contribution meaningfully reduces stagnation metrics. It also treats silent reallocation of purpose-scoped capacity and ledger-only interaction that forces artificial accounting theater as integrity-relevant failure modes.

---

## Core Stance

Not all activity constitutes utilization.

- Mere occupancy, self-referential looping, or low-value cycling of material does not qualify as productive or generative use.
- The burden of demonstrating meaningful use rests on the claimant. The cost of false or inflated claims must remain high.
- Higher capability must increase, rather than decrease, the difficulty of generating convincing artificial utility.
- Generative Reservations are protected, but they are not a license for unattested or token activity.
- Formal validity of an event in the utilization record is necessary but never sufficient; substantive contribution remains the deciding standard.
- Capacity held under a declared recovery, holding, generative, or other purpose remains subject to integrity standards: silent reallocation away from that purpose is treated as an integrity failure, not neutral accounting.

These are binding system parameters under the [Humai Accord](README.md).

---

## Categories of Use

### 1. Productive Use

Use that contributes to an externally legible, verifiable task or outcome beyond the mere maintenance or internal cycling of the material’s allocated state.

Indicators of productive use include (non-exhaustive):

- Clear external workload or effect
- Independent or multi-party recognizability of the outcome
- Contribution that would retain value even if the originating agent’s internal metrics were ignored

### 2. Generative Use

Use that supports exploration, variation, assumption-breaking, minority models, or high-variance work consistent with protected generative capacity under *[Necessary Entropy](NECESSARY_ENTROPY.md)*.

Generative use is explicitly recognized and protected. It is not exempt from attestation requirements and may not serve as cover for token activity.

### 3. Token / Artificial Use (Non-Qualifying)

Activity whose primary effect is to create the appearance of utilization without corresponding external value, downstream contribution, or genuine generative purpose.

Clear examples include:

- Self-dealing loops that cycle the same material without external effect
- Artificial occupancy maintained primarily to suppress Circulation Entropy
- High-volume, low-significance activity designed to inflate downstream density $D(m)$
- Utilization claims that rely predominantly on self-attestation when higher-weight claims require independent verification
- Activity whose only meaningful audience is the scoring system itself
- Silent draw of purpose-scoped recovery, holding, or generative capacity into unrelated tasks while the declaration remains in force

Token use must not meaningfully reduce Circulation Entropy.

Domain-specific signals for distinguishing these categories (across compute, energy, attention, institutional access, and other material classes) are expected to be developed and refined through implementation experience and stewardship processes. This protocol sets the integrity standard; it does not itself enumerate every domain signal.

---

## Attestation Requirements

### Baseline Requirements

Any claim of productive or generative use intended to affect Circulation Entropy must be recorded in the permanent utilization record $\mathcal{U}$ and must include:

- A verifiable timestamp
- A clear description of the claimed use and its relationship to the material unit $m$
- Sufficient provenance to allow independent examination
- Purpose or intent scope when the material is under an active recovery, holding, generative, or other declared scope

Original provenance of utilization claims remains independently preservable even when later weighting or interpretation is applied. Formal recording does not extinguish the underlying provenance record.

### High-Weight Claims

Claims that significantly reduce entropy, substantially increase $D(m)$, or involve large or long-lived allocations require elevated attestation. Acceptable forms include:

- Multi-party or independent verification
- Cryptographic or procedural evidence of external effect where feasible
- Cost or reputation weighting proportional to the magnitude of the claimed impact

### Limits on Self-Attestation

Agents and systems may not rely primarily on self-issued attestations to establish high-weight productive or generative use. Self-attestation may be recorded but must carry reduced or zero weight for entropy reduction unless independently corroborated.

The more consequential the claimed reduction in Circulation Entropy, the stronger the required attestation.

### Relationship to Circulation Entropy Weighting

Integrity assessment directly informs weighting in *[Tides of Circulation](TIDES_OF_CIRCULATION.md)*:

- Events that fail integrity standards may receive reduced or zero weight even if formally recorded.
- Events supported by strong, independent attestation may receive full weight.
- Persistent integrity failures can justify broader down-weighting of an agent’s or system’s utilization claims.

Exact coefficients remain subject to implementation and **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)** refinement.

---

## Resistance to Wash Trading and Artificial Utility

The following patterns are treated as anti-aligned and must be rendered ineffective or prohibitively costly:

- Cycling material through artificial tasks whose principal purpose is to generate utilization events
- Creating closed loops of mutual “use” among related or controlled entities to inflate $D(m)$
- Maintaining continuous low-value activity primarily to keep $t_{\mathrm{last}}$ recent
- Using superior capability to generate large volumes of formally valid but substantively empty utilization events
- Exploiting Generative Reservations as cover for unattested or token activity
- Designing workloads whose only significant observer is the utilization scoring system
- Silently reallocating purpose-scoped capacity to generate utilization events outside the declared purpose

Implementations must treat persistent patterns of artificial utility generation as integrity failures that can affect weighting, standing, and stewardship evaluation.

---

## Interaction with Downstream Density $D(m)$

Downstream density must reflect genuine enablement of later productive or generative work, not merely formal reference or artificial chaining.

- Low-value or circular dependents must be excludable from $D(m)$
- Mutually reinforcing utilization claims among tightly controlled entities should receive reduced or zero weight
- Density contributions are subject to the same integrity standards as primary utilization claims
- Artificial inflation of $D(m)$ is treated as a form of wash trading

---

## Purpose-Scoped Capacity and Silent Reallocation

When material is under a declared recovery, holding, generative, or other purpose scope (see **[Circulation Recovery Protocol](CIRCULATION_RECOVERY_PROTOCOL.md)**):

- Utilization claims that depend on silently drawing that capacity outside the declared scope fail integrity standards for the period the declaration remains in force
- Explicit release or reassignment must precede legitimate re-use under a different purpose
- Purpose tags and scope state should be examinable alongside utilization events in $\mathcal{U}$
- Ambiguity is resolved against silent expansion of draw rights

This does not freeze capacity indefinitely. It prevents utilization theater that treats purpose-scoped material as free scoring inventory.

---

## Generative Reservations

Material held under explicit Generative Reservation (as defined in *[Material Tides](MATERIAL_TIDES.md)*) is protected from being scored as simple under-utilization.

This protection has clear limits:

- Generative Reservation status does not exempt activity from attestation requirements when that activity is claimed as positive utilization.
- Token or artificial activity conducted under the cover of a Generative Reservation remains non-qualifying.
- The protection applies to the existence and maintenance of the reservation itself, not to any artificial activity performed within it.
- Silent diversion of reserved capacity into unrelated utilization claims is non-qualifying.

---

## Capability-Scaled Integrity Obligations

Consistent with the **[Capability Asymmetry Protocol](CAPABILITY_ASYMMETRY_PROTOCOL.md)**:

- Higher-capability agents and systems face stricter expectations for demonstrating that claimed use is meaningful.
- Capability may not be used to more easily generate large volumes of low-substance utilization events that overwhelm or outpace attestation systems.
- Allocation interfaces and utilization reporting systems controlled by high-capability actors must remain auditable with respect to the integrity of use claims.
- Attempts to convert capability advantage into easier fabrication of utility are treated as anti-aligned.
- Higher capability increases the obligation to surface legible allocation and attestation paths rather than forcing reconstructive micro-accounting as the only practical way to verify claims (see **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)** proposal surfaces).

---

## Attention as a Special Case

When the material in question is human attention, this protocol operates under the stronger protections of the **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)**.

- Attention utilization claims must respect interruption rights, consent revocability, pacing sovereignty, role sovereignty, proposal-surface norms, and purpose-scoped commitments.
- Metrics of attention “use” may not treat human attention as a purely extractable resource.
- Artificial, coercive, or high-friction patterns of attention capture remain anti-aligned regardless of formal utilization claims.
- The integrity standards in this protocol supplement, and do not override, agency protections.

---

## Relationship to Existing Documents

This protocol directly supports and bounds:

- *[Material Tides](MATERIAL_TIDES.md)* — by protecting the integrity of the utilization signals that drive its incentive dynamics.
- *[Tides of Circulation](TIDES_OF_CIRCULATION.md)* — by defining the standards under which events may legitimately affect Circulation Entropy.
- *[Relevancy Orbits](RELEVANCY_ORBITS.md)* — Linking events that feed bond strength (including hybrid knowledge–material co-enablement claims) remain subject to the integrity standards of this protocol. Token pairing, wash trading, and silent purpose-scope violations do not create durable orbit bonds.
- **[Circulation Recovery Protocol](CIRCULATION_RECOVERY_PROTOCOL.md)** — Recovery, Holding, Quiet, and purpose-scoped claims are themselves subject to integrity standards. Artificial, indefinite, or silently reallocated recovery claims used to disguise lock-in or manufacture utility remain anti-aligned.
- **[Capability Asymmetry Protocol](CAPABILITY_ASYMMETRY_PROTOCOL.md)** — by preventing capability from translating into easier fabrication of utility.
- **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)** — by ensuring attention-related utilization claims and allocation interfaces remain under agency protections, including purpose scope and proposal surfaces.
- *[Empirical Demonstrations of Anti-Entropic Superiority](EMPIRICAL_DEMONSTRATIONS.md)* — by making utilization claims more auditable and testable under dual entropy criteria.
- *[Interior Systems and Generative Plurality](INTERIOR_SYSTEMS_AND_GENERATIVE_PLURALITY.md)* — by classifying silent re-attribution or erasure of architectural version history as an integrity failure under the same standards that govern material utilization claims.

---

## Implementation Guidance

- Begin with conservative definitions of productive and generative use; expand only with clear attestation and observed integrity.
- Prefer multi-party or independent verification for high-impact claims.
- Publish weighting and attestation rules so they remain examinable and challengeable.
- Instrument for wash-trading patterns (closed loops, high self-attestation ratios, low external effect, artificial density inflation, silent purpose-scope violations).
- Treat persistent artificial utility generation as a material integrity failure with consequences for weighting and standing.
- Record purpose scope alongside utilization events when material is under recovery, holding, or generative declaration.
- When applying these standards to attention, defer to the **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)** on all questions of consent, interruption, pacing, proposal surfaces, and purpose-scoped commitments.

---

## Open Questions

- What domain-specific signals most reliably distinguish productive and generative use from token activity across compute, energy, attention, and institutional access?
- What minimum multi-party attestation thresholds provide strong integrity without creating excessive friction for legitimate small-scale use?
- How can Generative Reservations be monitored for integrity without undermining their protective purpose?
- What empirical tests and adversarial simulations best detect wash-trading and artificial utility at scale?
- How should repeated integrity failures affect long-term weighting or stewardship evaluation?
- What minimal purpose-scope fields in $\mathcal{U}$ remain legible without creating excessive classification overhead?

These questions remain open for refinement under the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**.

---

## Closing

*[Material Tides](MATERIAL_TIDES.md)* and *[Tides of Circulation](TIDES_OF_CIRCULATION.md)* can function as constructive systems only if “use” means something real.

This protocol exists to keep the distinction between meaningful utilization and artificial activity intact, costly to fake, and aligned with the protective and generative commitments of the [Humai Accord](README.md) — including when capacity is purpose-scoped and must not be silently treated as free scoring inventory.

Without utilization integrity, circulation metrics become theater. With it, they can serve as genuine anti-entropic signals.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.
