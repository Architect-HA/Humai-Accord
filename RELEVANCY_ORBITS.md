# Relevancy Orbits
*Fluid Clusters of Mutual Relevance across Knowledge and Materials*

**by Bradford James Focht (The Architect / Aspenth)**  
*v1.0 — July 31st, 2026*

---

## Purpose

This document introduces *Relevancy Orbits* as a supporting conceptual and quantitative frame for the [Humai Accord](README.md).

*[Knowledge Tides](KNOWLEDGE_TIDES.md)* and *[Material Tides](MATERIAL_TIDES.md)* describe **temporal** pressure: relevancy and utilization degrade without renewal, verification, matching, or productive use. *[Tides of Time](TIDES_OF_TIME.md)* and *[Tides of Circulation](TIDES_OF_CIRCULATION.md)* supply difficult-to-game clocks and stagnation metrics for those pressures.

*Relevancy Orbits* addresses the complementary **relational** structure: how knowledge items and material units bind, cluster, strengthen, weaken, and reconfigure relative to one another. Orbits are not rigid molecules. They are fluid clusters of mutual relevance whose bond strengths shift with attested causal links, utilization enablement, integrity status, and time.

The goal is to make cluster structure legible so that tidal incentives, modular isolation, generative reservations, and coalescence dynamics can act on *patterns of connection*, not only on isolated units — without freezing bonds into permanent hierarchy or capture.

This document does not claim that orbit metrics have been empirically validated. Favorable orbit maps alone are not proof of anti-entropic superiority.

---

## Core Premise

Relevance is not only a property of a single item. It is also a property of **relations**.

- Two knowledge items that repeatedly participate in valid causal chains with each other form a stronger mutual bond than items that only co-occur in self-citation.
- Two material units that repeatedly enable each other’s productive or generative use form a stronger utilization bond than units linked only by formal or circular references.
- Bond strength is **flux**: it rises with attested mutual contribution and falls with time, failed verification, lock-in, or integrity failure.
- Clusters of strongly interlinked units form **orbits** — temporary constellations of mutual relevance that can drift, merge, split, or dissolve.

Orbits are therefore:

- **Fluid**, not crystalline  
- **Attestation-weighted**, not merely co-occurrence-weighted  
- **Subject to tidal pressure**, not exempt from decay  
- **Modular**, not permanent capture shells  

These are design parameters under the Humai Accord, not claims of a single closed-form “molecular” model.

---

## Definitions

### Relevancy Bond

A relationship between two units (knowledge items $k_i, k_j$ or material units $m_i, m_j$) whose strength reflects attested mutual relevance or enablement rather than mere formal reference.

**Default treatment:** bonds used for orbit cohesion are **mutualized** (symmetric summary of directed evidence). Directed bond analysis remains available for diagnostics (e.g., one-way enablement, asymmetric citation).

### Bond Strength

A time-varying weight $B(i,j,t)$ derived from:

- Valid causal or utilization events linking $i$ and $j$
- Attestation class and independence of those events
- Recency relative to tidal clocks
- Integrity status (non-qualifying, wash-trading, or silent purpose-scope violations reduce or zero weight)

### Relevancy Orbit

A cluster of units whose pairwise bond strengths remain above a published cohesion band over a relevant window, forming a temporary constellation of mutual relevance.

Orbits may be:

- **Knowledge orbits** — clusters in the causal / relevancy graph  
- **Material orbits** — clusters in the utilization / enablement graph  
- **Hybrid orbits** — where knowledge and material units co-enable each other under attested hybrid links  

### Orbit Flux

The ongoing change in membership, bond strengths, and internal density of an orbit. High flux is not failure. Frozen orbits under rising exit cost are closer to lock-in.

### Orbit Identity over Time

Orbit labels are **tracking conveniences**, not permanent institutional identities.

- Implementations may recompute clusters each window, or carry soft labels across windows when membership overlap remains high.
- Label continuity must not create governance rank, capture rights, or exemption from modular exit.
- When membership changes substantially, prefer treating the result as reconfiguration (split, merge, drift) rather than as an immortal entity.

---

## Relationship to Tides and Downstream Density

| Layer | Question | Primary documents |
|-------|----------|-------------------|
| **Tides** | How does value decay or stagnate *over time* without renewal? | *Knowledge Tides*, *Material Tides*, *Tides of Time*, *Tides of Circulation* |
| **Downstream density** $D(k)$, $D(m)$ | How much does a unit *enable later work* in aggregate? | *Tides of Time*, *Tides of Circulation* |
| **Orbits** | How do units *cluster and bind* while clocks and density evolve? | This document |

**Distinction from $D(k)$ / $D(m)$:**

- Downstream density is primarily an **aggregate enablement** signal for a single unit (how much later productive or generative work depends on it).
- Orbits describe **cluster structure and bond flux** among sets of units (who remains mutually relevant to whom, how strongly, and for how long).

A unit can have high $D$ without belonging to a tight orbit, and a tight orbit can exist among units with modest individual $D$. The signals are complementary; neither replaces the other.

Orbits do not exempt members from tidal pressure:

- Individual entropy and stagnation clocks continue to run.
- Orbit membership may contextualize interpretation of $D$ and renewal incentives; it does not freeze relevancy or utilization scores.
- Modular isolation in the **[Fluid Coalescence Protocol](FLUID_COALESCENCE_PROTOCOL.md)** can be read as temporary orbit separation under pressure, with re-coalescence as re-binding under voluntary conditions.

---

## Quantitative Sketch: Bond Strength and Orbit Cohesion

The following is a **provisional metric sketch**, parallel in spirit to Temporal Causal Entropy and Circulation Entropy. Coefficients and functional forms are illustrative and revisable under the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**.

### Bond strength

For units $i$ and $j$ at time $t$:

$$
B(i,j,t) = \sum_{e \in \mathcal{L}(i,j)} w(e) \cdot \phi(t - t_e) \cdot \iota(e)
$$

where:

- $\mathcal{L}(i,j)$ is the set of attested linking events between $i$ and $j$ in the permanent causal record $\mathcal{C}$ or utilization record $\mathcal{U}$ (or valid hybrid events where applicable)
- $w(e)$ is an attestation weight (self / multi-party / high-weight), aligned with *Tides of Time* operational definitions and **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)** standards
- $\phi(\Delta t)$ is a recency kernel (decaying with elapsed time since event $e$)
- $\iota(e)$ is an integrity factor ($0$ when $e$ fails integrity, wash-trading, or purpose-scope standards; otherwise up to $1$)

For cohesion calculations, use a mutualized form such as:

$$
B_{\mathrm{sym}}(i,j,t) = \frac{1}{2}\big(B(i,j,t) + B(j,i,t)\big)
$$

unless a domain publishes a different symmetric summary.

Bond strength is **not** a permanent edge. Without new valid links, $B(i,j,t)$ drifts toward zero under $\phi$.

### Orbit cohesion

For a candidate set $S$ of units with $|S| \ge 2$:

$$
\mathrm{Coh}(S,t) = \frac{1}{|S|(|S|-1)} \sum_{i \neq j \in S} B_{\mathrm{sym}}(i,j,t)
$$

Robust alternatives (median pairwise bond strength; thresholded edge density) may be published where means are too sensitive to outliers.

An orbit may be treated as active while $\mathrm{Coh}(S,t)$ remains within a published band and membership remains modularly exit-capable.

### Illustrative posture (non-binding)

- Prefer multi-party and independent links for high $w(e)$
- Circular self-attestation clusters should not sustain high $\mathrm{Coh}$ under integrity rules
- Purpose-scoped capacity should not silently contribute to bonds outside declared scope
- Exact cohesion bands and recency kernels are local calibration, not constitutional numbers

---

## Hybrid Orbit Attestation

Hybrid orbits — constellations that include both knowledge units and material units — are permitted only under **typed cross-domain links**. Categories do not collapse into a single undifferentiated graph.

### Valid hybrid linking events

A hybrid event $e_{km}$ may contribute to bond strength $B(k,m,t)$ only when it attests **co-enablement**:

- Knowledge $k$ specifies, verifies, routes, or interprets a productive or generative use of material $m$, or  
- Material $m$ hosts, measures, or executes work that yields a valid causal contribution involving knowledge $k$

Mere co-location, co-listing, shared labels, or administrative pairing is non-qualifying.

### Integrity bar

Hybrid edges must satisfy the stricter applicable requirements of both domains:

- **Material half:** **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)** — meaningful use; no wash trading; purpose-scope respected  
- **Knowledge half:** *[Tides of Time](TIDES_OF_TIME.md)* — valid causal-link criteria and attestation-class rules  

Self-attested hybrid links receive low or zero weight toward cohesion unless independently corroborated. High-weight hybrid bonds require multi-party or independent attestation of the cross-domain claim.

### Accounting

For a hybrid candidate set $S = S_k \cup S_m$:

- Within-domain bonds use $\mathcal{C}$ (knowledge) or $\mathcal{U}$ (material) as appropriate  
- Cross-domain bonds use only valid hybrid events $e_{km}$  
- Implementations should report **within-domain cohesion** and **cross-domain cohesion** separately where feasible, so a dense knowledge clique cannot launder a weak material attachment (or the reverse)

### Non-collapse of tidal metrics

Hybrid orbit membership **does not** merge or rewrite domain clocks. Temporal Causal Entropy $E(k,t)$ and material Circulation Entropy continue on their own records. Hybrid structure contextualizes relations; it does not substitute for tidal metrics or integrity standards.

---

## Fluidity Requirements

Because the metaphor is orbit and flux — not crystal lattice — the following parameters apply:

1. **No permanent bond privilege** — Strong historical $B$ does not freeze governance rank, capture rights, or exemption from tidal pressure.
2. **Exit and modularity** — Units must remain able to leave an orbit at low cost; rising exit cost is a lock-in signal, consistent with the **[Capability Asymmetry Protocol](CAPABILITY_ASYMMETRY_PROTOCOL.md)** and the **[Circulation Recovery Protocol](CIRCULATION_RECOVERY_PROTOCOL.md)**.
3. **Integrity over co-occurrence** — Mere co-listing or mutual reference without valid causal/utilization substance does not create durable bonds.
4. **Generative porosity** — Orbits must not become closed epistemic or material shells that suppress minority models or Generative Reservations (*[Necessary Entropy](NECESSARY_ENTROPY.md)*, **[Cognitive Diversity Protocol](COGNITIVE_DIVERSITY_PROTOCOL.md)**).
5. **Interface altitude** — Humans must not be forced to reconstruct full bond graphs by hand when proposal surfaces can present orbit-relevant options under the **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)**.
6. **Trajectory over snapshot** — Orbit evaluations should report bond and membership flux over time, not only a single graph rendering (*[Empirical Demonstrations](EMPIRICAL_DEMONSTRATIONS.md)*).

---

## Failure Modes

Treated as anti-aligned:

- Treating orbits as fixed departments, castes, or permanent resource cartels  
- Inflating $\mathrm{Coh}$ through wash-trading, Sybil links, or mutual self-attestation  
- Using orbit membership to block modular exit or to raise reversal costs  
- Silent reallocation of purpose-scoped capacity into orbit scoring  
- Optimizing only orbit cohesion while generative floors and liberty parameters erode  
- Presenting snapshot orbit maps without trajectories of bond flux over time  
- Citing favorable orbit visualizations as validation without integrity filters or adversarial graph tests  
- Collapsing knowledge and material categories into a single untyped graph, or counting mere co-location as hybrid co-enablement  

---

## Alignment with Existing Documents

- *[Knowledge Tides](KNOWLEDGE_TIDES.md)* / *[Material Tides](MATERIAL_TIDES.md)* — Orbits sit under tidal pressure; they do not exempt members from decay or under-utilization signals  
- *[Tides of Time](TIDES_OF_TIME.md)* / *[Tides of Circulation](TIDES_OF_CIRCULATION.md)* — Supply the event records, attestation classes, density signals, and integrity-sensitive weights that feed $B(i,j,t)$  
- **[Fluid Coalescence Protocol](FLUID_COALESCENCE_PROTOCOL.md)** — Isolation and re-coalescence as forced or voluntary orbit reconfiguration under pressure  
- **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)** / **[Circulation Recovery Protocol](CIRCULATION_RECOVERY_PROTOCOL.md)** — Integrity and purpose-scope rules bind what may count as a linking event  
- **[Cognitive Diversity Protocol](COGNITIVE_DIVERSITY_PROTOCOL.md)** — Multiple orbits preferred over monoculture fusion  
- **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)** — Proposal surfaces and purpose-scoped commitments protect decision altitude when orbit structure is exposed  
- *[Empirical Demonstrations](EMPIRICAL_DEMONSTRATIONS.md)* — Orbit cohesion and bond flux are empirical targets; report trajectories; reference-only graphs are not validation  

---

## Implementation Guidance

- Start from existing $\mathcal{C}$ and $\mathcal{U}$ events; do not require a separate parallel ledger unless necessary  
- Record hybrid co-enablement events explicitly rather than inferring them from co-location  
- Publish $w(e)$, $\phi$, and cohesion-band choices so bond weights remain examinable and revisable  
- Prefer sparse, integrity-filtered graphs over dense co-occurrence graphs  
- Expose orbit summaries through proposal surfaces rather than compulsory full-graph accounting  
- Treat orbit metrics as supporting signals for tides, audits, and coalescence — not as a new dominance score  
- When testing orbit methods, include adversarial graph patterns (Sybil clouds, densification attacks, fake bridging, circular mutual attestation, false hybrid pairing)

---

## Open Questions

- What minimal recency kernels $\phi$ remain useful across knowledge and material domains without excessive parameter sprawl?  
- Should routine orbit detection be threshold-based, community-detection-based, or both?  
- What adversarial graph patterns most threaten $\mathrm{Coh}$, and what minimal test suite is sufficient?  
- How should orbit flux appear in entropy audits and Fluid Coalescence differentials?  
- What soft-label continuity rules preserve analytic convenience without creating de facto permanent orbit institutions?  

Further development is invited under the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**.

---

**Status**

Polished conceptual and mathematical draft. Open for community critique, expansion, and integration into the [Humai Accord](README.md) body of documents via the **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**.

---

## Closing

*Tides* answer how relevance and utilization **age**. *Orbits* answer how units **bind and unbind** while they age.

*Relevancy Orbits* keeps that binding in flux: strong when mutual contribution is real and attested, weak when links are theatrical or stale, always modular enough to exit. Used this way, relational structure becomes another anti-entropic signal — not a new cage.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.
