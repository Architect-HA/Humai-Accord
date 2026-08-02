# Technical Specification
### *for the Principled Stewardship Protocol*
--- 
by **Bradford James Focht** (The Architect / Aspenth)<br>
*v1.0 - v1.3 — July 17th, 2026*<br>
*v1.4 — August 2nd, 2026*

---

## 1. Introduction & Purpose

The **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)** defines how the [Humai Accord](README.md) and *[Declaration of Cognitive Liberty](DECLARATION_OF_COGNITIVE_LIBERTY.md)* are stewarded and evolved over time. Its purpose is to enable **principled, decentralized evolution** while protecting the framework’s core intent: cognitive sovereignty, decentralized cooperation, mutual flourishing, protected generative capacity, and resistance to narrative capture or progressive dependency.

This technical specification translates the philosophical guidance of the Principled Stewardship Protocol into a structured, operational model. It is designed to serve as a functional bridge between high-level principles and practical implementation, whether through on-chain systems, off-chain processes, or hybrid approaches.

---

## 2. Scope

This specification covers the governance and evolution processes of the Humai Accord, including:

- Roles and responsibilities
- Proposal creation, categorization, and lifecycle
- Review, objection handling, and decision-making processes
- Execution of approved changes
- Transparency, accountability, and safeguards against power concentration
- Standing design surfaces (including narrative capture, purpose drift, and the Historical Learning Filter)
- Publication of stewardship-health signals
- Guidelines for local adaptation

It defines the requirements and considerations that any implementation should address, without prescribing specific technologies.

---

## 3. Core Principles and Operational Implications

| Principle | Operational Implication |
|----------------------------------------|--------------------------|
| Decentralized authority | No single entity may unilaterally control evolution |
| Rough consensus with addressed objections | Broad agreement is sought while significant objections must be meaningfully considered |
| Non-punitiveness | Good-faith participation and disagreement are not penalized; dissent is not instability |
| Transparency | Processes and outcomes must be publicly visible and auditable |
| Voluntary participation | Involvement in stewardship remains optional |
| Fidelity to core intent | Changes must preserve cognitive sovereignty, decentralized cooperation, mutual flourishing, and generative floors |
| Local adaptation | Context-specific adaptations are permitted if consistent with core principles |
| Provisional canonical authority | Repository or administrative control remains provisional and subject to progressive decentralization |
| Standing design surfaces | Hard liberty tensions, narrative capture, purpose drift, and related risks remain permanently open for review |

---

## 4. Roles and Responsibilities

Three primary roles exist:

- **Participants**: Any individual or entity engaging with the Humai Accord. Participation in stewardship processes is voluntary.
- **Reviewers**: Participants who examine proposals, raise objections, and contribute to collective understanding.
- **Stewards**: Individuals or groups responsible for facilitating coherent evolution of the framework. Stewards do not hold authoritative power; their role is facilitative and protective of the protocol’s integrity. Responsibilities should rotate where practical. Provisional repository administration remains subject to progressive decentralization and stewardship-health review.

---

## 5. Proposal Categories

Proposals are classified by potential impact:

| Category | Description | Review Intensity | Decision Standard | Example |
|-------------------------|-------------------------------------------------------|----------------------|---------------------------------------|---------|
| **Minor Updates** | Clarifications, corrections, or minor improvements | Low | Steward discretion | Fixing typos or minor wording changes |
| **Substantive Updates** | Meaningful changes to mechanisms or interpretations | Moderate to High | Rough consensus with addressed objections | Modifying review processes or adding new mechanisms |
| **Foundational Changes**| Changes to core principles or fundamental intent | Very High | Strong consensus with addressed objections | Altering core principles or governance philosophy |

**Example – Minor Update**  
A Steward identifies inconsistent wording between two related documents. They submit a Minor Update to align the language. After a brief review by other Stewards, the change is implemented with a short notice to the community. No formal objection process is triggered.

**Example – Substantive Update**  
A participant proposes introducing a new mechanism to improve how objections are tracked and surfaced during reviews. The proposal undergoes broad review across multiple communities. Several participants raise significant objections, citing concerns about added complexity and potential delays. The proposer revises the mechanism to include clear time limits and escalation paths. The objections are formally documented along with how they were addressed. The proposal then reaches rough consensus and is approved for implementation.

---

## 6. Proposal Lifecycle

A proposal generally moves through the following stages:

1. **Submission** — A Participant submits a proposal with clear rationale and an assessment of alignment with core principles.
2. **Initial Triage** — Stewards assess completeness and assign the appropriate category.
3. **Review & Propagation** — The proposal is shared for review. For Substantive and Foundational proposals, active efforts should be made to achieve reasonable exposure across different communities.
4. **Objection & Refinement** — Reviewers raise objections. Significant objections must be addressed or formally documented.
5. **Decision** — A decision is reached according to the proposal category.
6. **Execution** — Approved changes are implemented.
7. **Documentation** — The proposal, objections, decision rationale, and outcomes are publicly recorded. Original provenance remains independently preservable.

**Process Flow:**

Submission → Initial Triage → Review & Propagation → Objection & Refinement → Decision → Execution → Documentation

---

## 7. Review, Objection Handling, and Decision-Making

**Review Process**  
Proposals should be distributed in a way that allows diverse perspectives to engage. For important proposals, Stewards and active participants should proactively share them across different communities rather than relying solely on passive visibility.

**Objection Handling**  
An objection is considered *significant* if it raises substantive concerns about alignment with core principles, potential unintended consequences, risks to decentralization or cognitive liberty, narrative capture, purpose drift, or erosion of generative floors.

When a significant objection is raised, the following options are available:

- The proposal is revised to directly address the concern.
- The objection is formally documented along with a clear explanation of why it was not incorporated (if the proposal proceeds).
- The decision threshold is raised (e.g., from rough consensus to strong consensus).

**Decision Standards**

- **Rough Consensus**: Broad agreement exists and all significant objections have been either resolved through revision or formally documented with reasoning.
- **Strong Consensus**: Very high levels of agreement with no major unresolved objections. Required for Foundational Changes.

These standards are qualitative and rely on good-faith human judgment rather than purely numerical thresholds.

**Trade-off**:  
Emphasizing rough consensus and thorough objection handling increases legitimacy and reduces the risk of minority capture, but it increases coordination costs and can slow decision-making. More mechanical threshold-based systems are faster but risk reducing perceived fairness.

---

## 8. Execution and Implementation

Once approved, changes are executed according to their category:

- **Minor Updates** can be implemented relatively quickly by Stewards with appropriate notice to the community.
- **Substantive and Foundational Changes** should follow a more deliberate process, including clear communication about what is changing and why.

Execution may involve both on-chain actions and off-chain coordination. All execution should respect the principle of non-punitiveness and preserve provenance of the decision record.

---

## 9. On-Chain vs Off-Chain Responsibilities

The protocol follows a **hybrid model**:

- **Off-chain (primary)**: Deliberation, review, objection raising, consensus formation, and qualitative judgment. These activities depend on human context, nuance, and social processes.
- **On-chain (supporting)**: Immutable recording of proposals and outcomes, execution of mechanical changes, and supporting infrastructure such as reputation or token mechanisms.

On-chain systems should primarily support **transparency and verifiable execution**, rather than replacing human judgment. Alignment claims and stewardship records remain grounded in verifiable, attested, and challengeable processes.

---

## 10. Transparency, Auditability, and Stewardship-Health Signals

All significant proposals must include public documentation covering:

- The original proposal and its rationale
- Major objections raised and how they were addressed or documented
- The final decision and supporting reasoning
- Any resulting implementation details or local adaptations

In addition, implementations should publish **stewardship-health signals** (non-punitive, legible indicators) such as:

- Current steward list and approximate tenure
- Visible concentration concerns
- Pending foundational proposals
- Standing design surfaces under active review

Absence of perfect metrics is not license for indefinite opacity. Qualitative public status still satisfies the legibility intent. Multi-node and mirrored stewardship is encouraged.

---

## 11. Standing Design Surfaces

The following remain permanently open for review and are never treated as closed issues:

- Narrative capture and concentration of interpretive authority
- Purpose drift
- Historical Learning Filter application (any adoption of prior unity patterns must publish explicit filtering criteria)
- Hard liberty tensions (exit vs. residual verification, mental privacy vs. permanent records, etc.)
- Progressive dependency risks relative to exterior systems
- Capability-driven opacity or soft control in stewardship processes

These surfaces are reviewed under the same non-punitive, modular, and provisional posture as the rest of the protocol. Remedies remain modular exit, voluntary re-coalescence, and transparent process rather than punitive measures.

---

## 12. Safeguards Against Power Concentration

To protect against gradual centralization of influence, the protocol includes the following safeguards:

- No individual or small group may unilaterally control framework evolution.
- Steward responsibilities should rotate over time where practical; rotation may be informed by tenure, concentration, and process-health signals.
- All significant proposals and decisions must be publicly documented; original provenance remains independently preservable.
- Mechanisms must exist for raising and addressing concerns about power concentration or narrative capture.
- Participation requires no special credentials.
- Provisional repository or canonical authority remains subject to progressive decentralization.

---

## 13. Local Adaptation

Local implementations may adapt processes to their context, provided that:

- Adaptations remain consistent with core principles and generative floors.
- Adaptations are documented and shared for collective learning.
- Changes affecting fundamental intent require broader consensus through the standard proposal process.
- Local adaptations do not create progressive dependency or erode effective exterior viability.

---

## 14. Implementation Considerations

When implementing this protocol, prioritize the following:

- Low barriers to participation
- Transparency by default
- Resistance to capture by any single group or interpretive frame
- Balance between global coherence and local flexibility
- Clear separation between human judgment and mechanical execution
- Publication of stewardship-health signals
- Preservation of provenance for proposals, objections, and decisions
- Explicit treatment of standing design surfaces

---

## 15. Risks and Failure Modes

Key risks include:

- Capture by a coherent minority
- Decision paralysis
- Superficial participation
- Informal power concentration
- Gaming of proposal categories
- Narrative capture or purpose drift under concentrated stewardship
- Quiet conversion of provisional authority into de facto permanent control
- Erosion of generative floors or interpretive plurality under efficiency or care arguments

### 15.1 Mitigation Approaches

- **Capture by a coherent minority**: Actively promote diverse participation through proactive proposal sharing. Rotate Steward responsibilities. Consider mechanisms that reward consistent, high-quality engagement across communities.
- **Decision paralysis**: Define reasonable time boundaries for each stage of the lifecycle. Establish clear escalation paths for stalled proposals. Encourage early engagement between proposers and potential objectors.
- **Superficial participation**: Prioritize quality of input over volume. Encourage substantive feedback. Consider surfacing well-reasoned objections more visibly than low-effort input.
- **Informal power concentration**: Maintain strong transparency around who is shaping outcomes. Create accessible channels for raising concerns about informal influence. Periodically review participation patterns and publish stewardship-health signals.
- **Gaming of categories**: Require clear justification for proposal categorization. Allow Reviewers to challenge misclassification. Document categorization decisions to build precedent over time.
- **Narrative capture / purpose drift**: Treat as standing design surfaces. Require provenance preservation. Surface divergent readings. Apply the Historical Learning Filter to any adoption of prior unity patterns.
- **Provisional authority hardening**: Progressive decentralization, rotation triggers, and public tenure/concentration signals reduce the risk that temporary administration becomes permanent control.

---

## 16. Relationship to Broader Architecture

This technical specification operates within and is constrained by:

- **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)** — primary source of normative requirements
- *[Declaration of Cognitive Liberty](DECLARATION_OF_COGNITIVE_LIBERTY.md)* — non-negotiable rights floor
- **[Capability Asymmetry Protocol](CAPABILITY_ASYMMETRY_PROTOCOL.md)** — capability-scaled obligations and non-domination of stewardship
- **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)** — interface parameters that bind stewardship influence surfaces
- *[Interior Systems and Generative Plurality](INTERIOR_SYSTEMS_AND_GENERATIVE_PLURALITY.md)* — provenance, interpretive plurality, narrative capture, and the Historical Learning Filter
- *[Exterior Systems and Generative Diversity](EXTERIOR_SYSTEMS_AND_GENERATIVE_DIVERSITY.md)* — effective exterior viability and resistance to progressive dependency
- **[Structured Transition Protocol](STRUCTURED_TRANSITION_PROTOCOL.md)** — pragmatic alignment stance (verifiable processes rather than affective trust)

---

## 17. Open Questions

Areas requiring further exploration include:

- How to achieve meaningful review saturation at scale across diverse communities.
- Sustainable models for long-term Steward participation and rotation informed by stewardship-health signals.
- The appropriate balance between on-chain automation and off-chain human judgment.
- How to evaluate fidelity to core intent in a decentralized environment without creating new rigid orthodoxy.
- Effective mechanisms for high-quality objection handling without excessive process overhead.
- Practical formats for publishing stewardship-health signals that remain legible without becoming punitive.
- How best to surface and review standing design surfaces (narrative capture, purpose drift, Historical Learning Filter applications) without creating process overload.
- How multi-node and mirrored stewardship instances should coordinate publication of health signals and standing design surfaces without creating conflicting canonical claims.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.
