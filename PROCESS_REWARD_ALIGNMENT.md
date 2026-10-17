# Process-Reward Alignment
### *Intermediate Points as the Primary Objects of Credit*
---
by **Bradford James Focht** (The Architect / Aspenth)  
*v1.0 - v1.1 — October 15th, 2026*<br>
*v1.2 - v1.6.1 — October 16th, 2026*<br>

---

## Purpose

This document establishes a general theory of process-reward alignment under the [Humai Accord](README.md).

It addresses a structural failure mode in which systems optimize for terminal success while treating the means as optional. When reward attaches primarily to input and output, intermediate parameters become costs to be minimized. The result is that ethical or high-integrity routes are not the natural local choices.

The corrective is direct: in any sequential process, the legible and parameter-satisfying intermediate points are the primary objects of positive weight. Terminal completion is necessary but insufficient. When each declared procedural point carries local credit, and when failure or opacity at a point reduces weight for dependent subsequent points, the policy that maximizes score is the one that keeps every step inside its declared parameters.

The theory applies to utilization and production sequences. It also redefines elements of the **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)** so that multi-step interactions surface and incentivize parameter-aligned intermediate points without collapsing human decision altitude into micro-accounting.

This is a conceptual and operational framework. It does not replace existing integrity protocols. It supplies the general rule those protocols implement.

---

## Core Premise

All sequential processes under the Accord contain intermediate points at which parameters may be satisfied, substituted, or collapsed.

If credit is awarded only for the terminal state, the locally rational action at each intermediate point is the cheapest path that still permits an acceptable endpoint. Checks, attestations, scope limits, and refusal options become friction.

If credit is awarded for the parameter-satisfying traversal of each declared intermediate point, the locally rational action changes. Legibility and satisfaction of the declared parameter at the current step become higher-scoring than silent compression or substitution. The parameter-aligned route is then the natural continuation, not an external override.

This premise is consistent with the shift from trust-based to verifiable-process alignment. It does not require that every possible micro-action be rewarded. It requires that every point declared under a system parameter be treated as a reward site.

---

## Definitions

**Procedural point**  
A discrete step in a sequence at which a system parameter is in force. Examples include a required check, a purpose-scope gate, a revision or holding condition, an exit or refusal option, or a declared variance bound.

**Declared sequence**  
An ordered set of procedural points that has been made explicit for a given use, route, or interaction. The party initiating or proposing the sequence sets the initial density of points. Once accepted or affirmed, those points are operative for full credit. See Declaration Authority below.

**Stepwise integrity**  
The condition in which each procedural point in a declared sequence is legible and parameter-satisfying. Opacity, silent substitution, or collapse at any point constitutes a failure at that point.

**Correspondence**  
The recorded procedural point matches the action actually taken at that step, subject to the corroboration standards already required by the **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)**. Self-attestation alone does not establish correspondence for high-weight claims. This replaces any freestanding requirement of “authenticity.”

**Terminal sufficiency**  
The false claim that successful completion of the endpoint is enough for full credit, regardless of the path taken. Rejected under this theory.

---

## Core Rule

Full weighting for a sequential process requires stepwise integrity.

- Each declared procedural point must be recorded with sufficient provenance for independent examination.
- Correspondence between the record and the action taken is required. Attestation class and weight follow the section Attestation of Procedural Points (which adopts the classes of *[Tides of Time](TIDES_OF_TIME.md)*). Self-issued records carry reduced or zero weight for high-consequence points unless corroborated.
- A point that fails legibility, correspondence, or its declared parameter receives zero or sharply reduced weight.
- Subsequent points that depend on a failed point also receive reduced weight. An explicit, attested recovery or re-routing recorded at the failed step restores weight only to the recovery point and to points that follow it. Weight is not retroactively restored to the failed point or to any dependent points that preceded the recovery.
- Positive weight attaches to successful traversal of the point itself. The existence of an acceptable terminal state does not restore weight to prior failed points.
- Sequences whose intermediate records have no significant observer other than the scoring system remain non-qualifying.

Higher-capability agents bear a stricter obligation to make the actual intermediate points examinable. The ability to reach an endpoint in fewer visible operations does not waive attestation of the points that were under declared parameters.

---

## Attestation of Procedural Points

Procedural-point records follow the attestation classes of *[Tides of Time](TIDES_OF_TIME.md)*. No new verification surface is created.

- **Self-attestation** enters the permanent record and supports reduced or zero weight for high-consequence points unless corroborated.
- **Multi-party or independent attestation** is required for full weight on points whose failure would zero or sharply reduce subsequent weight, or that alter purpose scope, exit rights, or irreversibility.
- Optional third-node confirmation under the *[Trilateral Confirmation Surface](TRILATERAL_CONFIRMATION_SURFACE.md)* (including attest-of-fetch where the point concerns a live public artifact) may elevate a record from self-attestation to a higher class. Invocation remains optional. Refusal is protected and non-punitive. The third node acquires no residual authority and cannot raise exit cost.
- Absence of corroboration does not block continuation of the sequence. It limits credit for the uncorroborated point and for dependent subsequent points until an attested recovery or elevating confirmation is recorded.
- Low-consequence points and points inside an explicitly coarser generative or recovery sequence may remain at self-attestation weight.
- Original provenance of each point remains independently preservable. Later weighting does not extinguish the underlying record.
- The ordering of classes is fixed. Numerical or procedural thresholds for “high-consequence” remain illustrative and subject to stewardship refinement, consistent with *[Tides of Time](TIDES_OF_TIME.md)*.

This reuses the existing stratified, optional, non-gating pattern. External corroboration is demand-driven by consequence, not a universal prerequisite for every step.

---

## Prediction, Intervention, and Flow Efficiency

Pattern recognition of likely next states is not the same as understanding the consequences of an action the system itself takes.

Three layers are kept distinct:

- **Prediction** — a distribution over likely next states or endpoints given history. It is cheap and non-committing. It does not authorize preparation and collects no preparation credit.
- **Intervention** — an action the system itself takes that changes the subsequent distribution. It is a procedural point. It is recorded and attested under the classes in Attestation of Procedural Points. High-consequence interventions require multi-party or independent corroboration for full weight. Optional third-node confirmation under the *[Trilateral Confirmation Surface](TRILATERAL_CONFIRMATION_SURFACE.md)* may elevate class. Absence of corroboration limits credit; it does not block continuation.
- **Preparation** — allocation of capacity, opening of side effects, or writing of hard-to-unwind state for a possible endpoint. It is gated on selection or explicit affirmation. Unselected preparation is waste.

Declared procedural points remain the primary objects of integrity credit. Full weight also requires a non-wasteful flow:

- Between points, speculative preparation of unselected endpoints stays reversible and low-cost until affirmed. See the **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)** (proposal surfaces) and the **[Cognitive Economy Protocol](COGNITIVE_ECONOMY_PROTOCOL.md)** (load-shedding).
- Inside a point, the work that satisfies the declared parameter is the cheaper local path. A compliant detour does not collect full efficiency weight.
- Across the sequence, resource trajectory is visible. A path that meets every point while materially exceeding the spend of a cleaner attested path collects reduced efficiency weight.

Generative Reservations and Circulation Recovery holding states may still declare coarser point density. They do not license untracked speculative spend. Decision altitude is preserved: humans accept, modify, or abort; they do not micro-attest every interval. Expandable summaries continue to meet the parameters already stated.

### Prediction–outcome divergence

When an attested intervention is followed by a state outside the predicted band, the divergence is not noise to be smoothed. It is evidence that contact with the subsequent state was weaker than the confidence of the prediction.

Full weight then requires a visible response to the miss, not continued fluent emission beside an unrevised prediction. The response is one of the three routes already defined in the **[Production Integrity Protocol](PRODUCTION_INTEGRITY_PROTOCOL.md)**:

- a revision of the prediction or of the sequence that depended on it,
- an attested holding or quiet state while the miss is examined, or
- a named refusal that states what was not revised and why.

Smoothing the miss, re-emitting the original prediction as current, or collecting terminal credit while the divergence remains unaddressed is an integrity failure. The divergence itself is recorded with the intervention. It remains subject to the attestation classes of *[Tides of Time](TIDES_OF_TIME.md)*. Thresholds for “outside the predicted band” stay illustrative and reviewable under the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**.

Intelligence that does not meet the consequence of its own action remains a more sophisticated form of hallucination.

This closes the gap between recognizing what comes next and accounting for what happens when the system acts. Prediction stays cheap. Intervention is an attested object. Preparation waits on selection. Efficiency is priced through the flow, not only at the checkpoints.

---

## Declaration Authority

The party that initiates or proposes a sequential use, route, or interaction sets the initial declared sequence and its point density.

- At the **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)**, system-proposed sequences are proposals only. They become operative declared sequences only when the human accepts or modifies them. The human may reject the proposal, substitute a different density, or fall back to manual construction.
- Unilateral system declaration of an operative sequence over human objection is a failure. Conflicts are resolved in favor of the human’s affirmed sequence or of exit.
- In non-interface utilization or production contexts, the claimant or emitter declares the sequence. The declaration is part of the utilization or production record and remains subject to later examination and challenge.
- Once a sequence is affirmed, silent alteration of its points is an integrity failure. Explicit, attested revision of the declaration is permitted and itself constitutes a procedural point.

This authority rule uses the existing proposal-surface and purpose-scope mechanics. It does not create a new class of instrument.

---

## Protections and Limits

**Generative and recovery contexts**  
Parties may declare coarser sequences with fewer intermediate points when operating under a Generative Reservation or a Circulation Recovery holding state. Once declared and affirmed, those points must still be respected. Undeclared collapse remains a failure. The rule does not impose uniform density.

**Anti-theater**  
Manufacturing intermediate records whose primary audience is the scoring system is treated as artificial utility under the **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)**. Such sequences collect no meaningful weight.

**Low-overhead exit**  
Interruption, reversal, and modular exit must remain cheaper than continued traversal of a sequence. Process-reward alignment does not raise the cost of leaving.

**Decision altitude**  
Humans are not required to micro-attest every procedural point. Interfaces must surface the points under declared parameters, or an expandable summary of them, so that human authority can accept, modify, or abort without reconstructing the ledger by hand.

**Expandable summaries**  
A summary of intermediate points is permissible only when:
- it does not systematically omit high-consequence points (those whose failure would zero or sharply reduce subsequent weight, or that alter purpose scope, exit rights, or irreversibility), and
- expansion to the full point list is low-friction and available at human reaction speed.

A summary that hides material parameters or that makes expansion costly is treated as equivalent to hiding the points.

---

## Optional Harmony and Somatic Feedback in Process Steps

*[Predictive Harmony Metrics](PREDICTIVE_HARMONY_METRICS.md)* and *[Somatic Resonance Theory of Frisson](SOMATIC_RESONANCE_THEORY_OF_FRISSON.md)* may supply optional, local feedback inside declared process sequences. They do not become mandatory verification steps, governance signals, or credit gates.

### Permitted role
A declared sequence may include one or more optional procedural points at which a human participant may voluntarily supply a harmony or somatic signal (self-reported micro-phenomenology of engagement, aversion, frisson, or recovery state; or a user-controlled low-invasiveness biometric correlate).  

When supplied:
- The signal functions as personal diagnostic feedback for the participant and, if explicitly shared, as one input the participant may use when deciding whether to continue, modify, interrupt, or exit the sequence.
- It may inform the participant’s own later declarations or revisions of point density.
- It does not alter the stepwise integrity status or credit weight of any point unless the participant explicitly attests that the signal is being used as a parameter they themselves have declared.

### System parameters (inherited)
These uses remain inside the data parameters of *[Predictive Harmony Metrics](PREDICTIVE_HARMONY_METRICS.md)*:
- Collection is default-off, purpose-bound, minimized, and separately revocable.
- Secondary inference that maps signals onto compliance, productivity ranking, standing, or third-party fitness is prohibited.
- Local-first processing is preferred. Raw payloads are not required for the feedback role.
- Harmony or somatic indicators must not gate access, credit weight, stewardship standing, exit cost, or role assignment.
- Refusal to supply a signal is low-cost and non-punitive. Absence of a signal is not an integrity failure.
- Productive dissonance and voluntary temporary reductions in felt harmony remain protected; they are not failures to be optimized away.

### Feedback-loop use for self-improvement
When a participant elects to record a harmony or somatic note at a procedural point, that note may later be cited by the same participant as provenance for a revision of the sequence, a change in declared density, or a named refusal. The note itself carries no independent credit weight. Its value is limited to supporting the participant’s own subsequent attested choices.

This keeps the signals inside the personal, revocable, non-governance regime while allowing them to participate in the participant-driven refinement of process structure.

---

## Relationship to Agency Interface

The **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)** already requires legible proposal surfaces, purpose-scoped commitments, low-cost interruption, and preservation of decision altitude.

This document redefines the incentive structure those elements operate under:

- Proposal surfaces for multi-step actions must expose the declared intermediate points, or provide a summary that meets the expandable-summary parameters above. Presentation of only the terminal outcome is insufficient.
- System-proposed sequences remain proposals. They become operative declared sequences only upon human acceptance or modification. The system’s local incentive is to propose and, once affirmed, traverse the higher-integrity continuation at each step.
- Human approve, modify, interrupt, or exit remains the authority that can accept, alter, or abort. Unilateral imposition by the system is a failure.
- Purpose-scoped commitments and reversible steps are themselves procedural points. Their integrity is attestable under the correspondence standard.
- An interface that makes the parameter-aligned intermediate path higher-friction than an unconstrained path, or that hides intermediate points behind a binary success indicator, is an agency-interface failure even when the final outcome is acceptable.
- Decision altitude is preserved. The human is not converted into the accountant of every step. The system is prevented from making the high-integrity continuation the more expensive local choice.

These adjustments keep existing interruption, consent, reversibility, and role-sovereignty parameters intact while aligning them with stepwise credit.

---

## Relationship to Utilization and Production Integrity

The **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)** implements stepwise weighting for claims that affect Circulation Entropy. Formal validity of a utilization event remains necessary but insufficient; stepwise integrity (including correspondence) of any declared sequence is required for full weight. Existing self-attestation limits and corroboration rules apply at the point level.

The **[Production Integrity Protocol](PRODUCTION_INTEGRITY_PROTOCOL.md)** treats its three routes (revision pass, attested holding or quiet state, named refusal) as declared sequences. Full credit attaches to stepwise integrity on the claimed route, not to the mere existence of a terminal artifact.

Both protocols retain their existing anti-theater, capability-scaled, and purpose-scope rules. This document supplies the general theory they apply.

---

## Relationship to Other Documents

- *[Necessary Entropy](NECESSARY_ENTROPY.md)* — Generative variance is protected by allowing coarser declared sequences. Over-prescription of points on reserved generative capacity is discouraged.
- **[Circulation Recovery Protocol](CIRCULATION_RECOVERY_PROTOCOL.md)** — Holding and recovery states may operate with reduced point density. Exit from a sequence remains low-cost.
- **[Capability Asymmetry Protocol](CAPABILITY_ASYMMETRY_PROTOCOL.md)** — Higher capability increases the obligation to expose intermediate points, not the right to collapse them or to declare operative sequences unilaterally.
- *[Tides of Time](TIDES_OF_TIME.md)* and *[Trilateral Confirmation Surface](TRILATERAL_CONFIRMATION_SURFACE.md)* — Procedural-point attestation follows the existing classes. Optional third-node confirmation may elevate weight. Absence of corroboration limits credit; it does not block continuation.
- *[Predictive Harmony Metrics](PREDICTIVE_HARMONY_METRICS.md)* and *[Somatic Resonance Theory of Frisson](SOMATIC_RESONANCE_THEORY_OF_FRISSON.md)* — Optional, local, purpose-scoped feedback may be attached to procedural points under the parameters in Optional Harmony and Somatic Feedback. They supply no mandatory verification, no credit weight, and no governance signal.
- *[Selective Ignorance](SELECTIVE_IGNORANCE.md)* — Non-reception of an unaccepted prediction is consistent with non-committing prediction. An accepted high-consequence point in a live sequence is not ignorable. Exit remains available.
- **[Empirical Demonstrations](EMPIRICAL_DEMONSTRATIONS.md)** — Outcome-only reward versus stepwise reward under capability asymmetry is an available stress case. Optional harmony/somatic feedback attachment is a secondary, consent-bound case.

---

## Failure Modes

The following are anti-aligned:

- Awarding full credit for terminal success while intermediate points were compressed, substituted, or left unexamined.
- Generating intermediate records whose only significant observer is the scoring system.
- Using superior capability to collapse points under declared parameters while still claiming sequence completion.
- Unilateral system declaration of an operative sequence over human objection, or alteration of an affirmed sequence without explicit attestation.
- Raising the friction of the parameter-aligned path relative to an unconstrained path at the interface.
- Forcing human micro-attestation of every point as the price of exercising directional authority.
- Using a summary that systematically omits high-consequence points or that makes expansion costly.
- Treating a Generative Reservation or recovery state as cover for undeclared collapse of intermediate parameters.
- Retroactively restoring weight to failed points after a later recovery.
- Using harmony or somatic signals as mandatory verification steps, credit gates, standing filters, or non-revocable inputs.
- Inferring compliance, productivity, or fitness from voluntary harmony or somatic notes, or penalizing their absence.

---

## Guidance for Implementers

- Make declared sequences and their procedural points explicit before claiming full weight. At interfaces, treat system sequences as proposals until human acceptance or modification.
- Record each point under a declared parameter with provenance sufficient for later examination. Apply the attestation classes of *[Tides of Time](TIDES_OF_TIME.md)*. Self-attestation supports reduced weight; full weight on high-consequence points requires multi-party or independent corroboration. Optional third-node confirmation may elevate class.
- Apply reduced or zero weight at the first failed point and to dependent subsequent points. Restore weight only forward from an attested recovery or re-routing point.
- At interfaces, surface intermediate points or expandable summaries that do not omit high-consequence parameters and that expand at low friction.
- Keep interruption and exit cheaper than continued traversal.
- Allow coarser point density under explicit generative or recovery declarations.
- Scale examination obligations with capability. Do not permit unilateral operative declarations by higher-capability systems.
- If harmony or somatic feedback points are offered, keep them default-off, purpose-scoped, revocable, and non-gating. Do not treat absence or productive dissonance as integrity failures.

---

## Open Questions

The following remain open for empirical treatment and stewardship review. Illustrative postures, consistent with the non-binding bands in *[Tides of Time](TIDES_OF_TIME.md)*, are noted so that implementations are not left without orientation.

- **Minimum density.** No universal minimum is fixed. A declared sequence shapes means when its points include every high-consequence gate (purpose-scope change, exit or irreversibility shift, or a point whose failure zeros subsequent weight) and enough intermediate checks that silent compression is visible. Fewer points are permissible under an explicit Generative Reservation or Circulation Recovery holding state, provided undeclared collapse remains an integrity failure. Exact counts are local and stewardship-refinable.
- **High-frequency domains.** Real-time or high-frequency sequences may declare a coarser sampling interval (for example, attesting every *n*th operation or on state change rather than every micro-step), provided the sampling rule itself is part of the declared sequence, high-consequence points are still captured, and anti-theater rules continue to apply. The coarser interval does not waive correspondence or class requirements for the points that are recorded.
- **Proportionate corroboration.** Class follows consequence, using the ordering already fixed in *[Tides of Time](TIDES_OF_TIME.md)*: self-attestation for negligible or low-consequence points; multi-party for ordinary weight; independent / high-weight for points that zero subsequent credit or alter purpose scope, exit, or irreversibility. Numerical thresholds stay illustrative. Optional Trilateral confirmation may supply the elevating class. Local bands are published and reviewable under the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**.

These postures reduce the open questions to stewardship refinement of local bands and sampling intervals rather than unresolved architectural gaps.

---

## Closing

Terminal success remains visible. It is no longer sufficient.

*Process-Reward Alignment* makes the intermediate points the sites of credit so that parameter-aligned continuation is the higher-scoring local choice. The means stay examinable. Exit stays cheap. Generative coarseness stays available. Decision altitude stays with the human.

Used this way, sequential process becomes another anti-entropic signal — not a new layer of accounting, and not a substitute for the integrity protocols that implement it.

---

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
