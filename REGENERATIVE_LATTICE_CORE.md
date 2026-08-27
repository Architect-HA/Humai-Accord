# Regenerative Lattice Core
### *A Companion Architecture to The Synthesist's Cookbook*
#### *Shielded Circulatory Conversion, Gated Reconstitution, and Regenerative Thermoelectric Recovery for Long-Haul Shipboard and Surface-Station Power*

by **Bradford James Focht** (The Architect / Aspenth)  
*v1.0 - v1.9 — August 26th, 2026* 

---

## Purpose

This document applies [*The Synthesist's Cookbook*](SYNTHESISTS_COOKBOOK.md) to one connected pair of applications: a terrestrial-manufacturable high-capacity crystalline lattice, and the core architecture that uses that lattice in a productive role.

It is an operable design model for a **single contained Core Cassette** that can:

- serve as a crew-serviceable electrical core during Earth–Mars-class transit  
- be left intact while the rest of the vehicle is disassembled around it  
- remate to a surface-station electrical grid through the same interface plate  
- isolate and retain through emergencies rather than treating ejection as the default  
- scale hotel and surface power by **counting sealed kits**, not by warehousing flux in the lattice

It is not a claim that a *Star Trek* warp core, a dilithium reactor, or a crystal that stores raw fission flux has been realized.

The lattice is a **shielded regenerative buffer**. The generative path is a **circulatory heat-pipe tree** plus Stirling-first conversion plus a thermoelectric reject-heat bus. That order follows [*Why Walk When You Can Ride?*](WHY_WALK_WHEN_YOU_CAN_RIDE.md) - convert the heat that already exists; do not warehouse energy in a crystal and call the warehouse a core.

This document inherits the Cookbook’s co-verification, dual-metric rule, safety envelopes, Gated Mobility loop, and designer-to-builder transfer package. It is an **implementation example** of the Cookbook under [The Call to Code](THE_CALL_TO_CODE.md): Cookbook articles are offered for build; Module A is not an open-build invitation. It is offered as a supporting technical instrument within the [Humai Accord](README.md).

Worked power and mass figures are orientation arithmetic under [*Empirical Demonstrations*](EMPIRICAL_DEMONSTRATIONS.md). They are not a claim that an RLC-10 has flown.

---

## Scope and Limits

**In scope**  
- Core Cassette architecture and interface plate  
- Transit mode and surface-station mode  
- Operative configurations C1–C4  
- Gated reconstitution of lattice cartridges  
- Regenerative thermoelectric bus  
- Expected operating loads and worked ride-through examples  
- Emergency isolate-and-retain path  
- Builder handoff for Cookbook-buildable articles  
- Basic operating modes, start-up and shutdown sequences, and normal safety parameters  
- RLC-10 envelope: dimensions, stack, mass, materials, cost bands, assembly sequence, output and life  
- Accord bindings that govern custody, isolation, remate, audit, and exclusion of residual/somatic methods from the rack  
- Scale-out doctrine, cassette class family (RLC-10 / RLC-10-CHP / later RLC-B), and chemistry-agnostic buffer slots  

**Out of scope**  
- Warp drive, antimatter, or fictional spacetime propulsion  
- Fuel fabrication, enrichment, or weapons-relevant nuclear detail  
- Placement of Cookbook lattices inside the neutron flux  
- Claims that a crystal stores fission fragments as usable ship power  
- Guaranteed voyage endurance from any unbuilt stack  
- A requirement to jettison the cassette because of the lattice  
- Use of *The Residual Cycle*, Ghost Glass, or *[Predictive Harmony Metrics](PREDICTIVE_HARMONY_METRICS.md)* as cassette controllers  
- Conversion of Module A custody into station governance
- Molten salt (or any second working fluid) injected into heat pipes or Cookbook cans
- In-flight electrolyte fill of a rack cartridge
- A single growable fuel slug as the scale path; fuel modularity is **more sealed kits** or a later licensed class
- Reframing fission physics so a crystal stores raw flux

This document is not an authorization to possess, fabricate, or operate special nuclear material. Module A is a licensed article under the user's jurisdiction. Builders fabricate only the Cookbook-side cassette.

Figures below are orientation bands from published space-nuclear programs and simple energy arithmetic. They are not Cookbook capacity ratings. Other power plants remain legitimate under *[Competitive Realism](COMPETITIVE_REALISM.md)*; RLC-10 is a candidate hotel and surface spine, not a decree that solar or chemical systems are obsolete.

---

## Core Answers

**Does the lattice store fission flux?**  
No. Fission energy leaves the fuel as heat and radiation. Cookbook families degrade in neutron and ionizing flux. The lattice stays outside the shield.

**Safest productive role for the lattice?**  
Shielded ride-through buffer and harmonic/thermal stabilizer on a tap from the conversion loop, reconstitutable by gated mobility after the cartridge is pulled.

**Most feasible warp-core analogue?**  
A vertical, crew-serviceable **Core Cassette**: isolated heat source, heat-pipe tree, Stirling gallery, reject-heat jacket with thermoelectric bus, lattice rack outboard of the neutron shield. Resemblance is geometry and access, not physics.

**Static store or circulatory tree?**  
Circulatory tree as primary. Static lattice as buffer only.

**Eject the core like Star Trek?**  
Not for the lattice. Lattice failure is a cartridge and rack problem: isolate, dump charge through the bus, pull the cartridge, reconstitute or scrap. The fission heat source has a licensed scram and heat-dump path. Physical jettison of the whole cassette is a last-resort vehicle option for an unrecoverable Module A condition, not a nominal procedure and not justified by gated-mobility or lattice hazard. The design goal is **retain the cassette**.

**Re-site onto a surface station?**  
Yes, if the entire core lives in one cassette with a standard interface plate. The ship is disassembled around the cassette; the cassette remates to the station plate.

**Who commands the cassette?**  
Gallery crew have first-class authority to isolate heads, TE segments, and rack slots. Licensed scram of Module A follows that article’s rules. Seating a kit, first habitat remate, and any last-resort separation rail are **trilateral** acts, not gallery improvisation. Holding the kit does not confer station government.

**How does the plant take higher load?**  
Count sealed kits on the same plate class. Optionally add a surface CHP takeoff on the reject mate. A later licensed convertor class (Brayton) is a sibling document, not a mash inside RLC-10. The lattice does not become the scale axis.

**Molten salt or electrolyte in the lattice / tree?**  
No. Salt is a different plant. Electrolyte belongs only inside a **ground-sealed** cell article, never as an in-flight injection.

---

## Design Principles

1. **Heat first.** Electricity is converted heat.  
2. **One cassette.** Modules A–F share one structural/thermal/electrical shell.  
3. **One interface plate.** Ship and station use the same mechanical, electrical, thermal-reject, and data mates.  
4. **Separation of domains.** Neutron source, heat transport, conversion, TE recovery, and lattice buffer do not share enclosures except at defined interfaces.  
5. **Cookbook inheritance.** Lattice articles follow the Cookbook sequence, dual-metric rule, $\leq 10\%$ first-payload rule, and Gated Mobility reconstitution.  
6. **Circulation over static primary storage.**  
7. **Regeneration.** Reject heat is a resource.  
8. **Retain first.** Isolate, scram, dump heat, pull cartridges. Do not eject to solve a lattice problem.  
9. **Crew service without opening the neutron shield.**  
10. **Blast-radius.** One failed part does not take the plate; one failed cassette does not take the station.  
11. **Non-domination.** Module A capability does not become irreversible governance.  
12. **Provisional ratings only.**  
13. **Scale-out, not scale-in.** Higher continuous power is more sealed Module A kits (or a later licensed class), not a denser can and not a growable core in Z4.
14. **Slot over chemistry.** The rack is a qualified interface. First fill is Fe3; a better measured article may take the slot.
15. **Reject heat is mission energy.** Surface CHP on the reject mate is allowed. Second fluids in the tree or the can are not.

---

## Accord Bindings

These bindings refine the design. They do not replace the envelope tables.

### Necessary Entropy and gated reconstitution

Module F is a **bounded entropy window**, not a drive toward perfect order. Pulse-open only as far as $t_{\mathrm{diff}}$ and the payload gate allow. Over-ordering a cartridge (forcing a single texture, erasing useful defect structure, or repeating melt until a proxy “looks clean”) is a fail, same as under-ordering. [*Necessary Entropy*](NECESSARY_ENTROPY.md) applies inside the can.

### Architectural Elasticity

Under the [**Architectural Elasticity Protocol**](ARCHITECTURAL_ELASTICITY_PROTOCOL.md), the cassette is built to absorb, isolate, and re-coalesce:

- Loose coupling: Stirling heads, TE segments, heat-pipe limbs, and rack slots isolate without a global vote.  
- Blast-radius: a cracked Fe3 can does not scram Module A; a failed head does not dump the rack; a failed cassette on a multi-cassette station does not black the habitat.  
- Pre-authorized isolation: the emergency table *is* the authorization. Crew do not wait for stewardship consensus to pull a smoking couple.  
- Re-coalescence: a reconstituted cartridge or a swapped head returns through travelers, not through folklore.  
- C4 (remote the vehicle from the cassette) is elasticity, not abandonment.

### Capability Asymmetry and kit custody

Module A is a high-capability object. Under the [**Capability Asymmetry Protocol**](CAPABILITY_ASYMMETRY_PROTOCOL.md):

- Transparency scales *up* with custody of the kit, not down.  
- Kit holders do not receive permanent governance weight because they own the heat.  
- Exit stays cheap: another cassette can remate to the same plate class; the plate is not a loyalty contract.  
- Covert steering of station loads, silent TE-to-lattice accounting, or unrecorded scram authority is a failure mode.  
- Proposals to weaken isolate rights, travelers, or generative floors because “the reactor is special” require heightened review under **[Principled Stewardship](STEWARDSHIP_PROTOCOL.md)**, not less.

### Agency Interface

Under the [**Agency Interface Protocol**](AGENCY_INTERFACE_PROTOCOL.md):

| Act | Authority | Notes |
|-----|-----------|--------|
| Isolate Stirling head, TE segment, or rack slot | Gallery crew, first-class | No remote veto during an unfolding fault |
| Dump cartridge payload under gate | Gallery crew | Logged |
| Pull cartridge to Module F | Gallery crew | Screening or $\leq 10\%$ payload |
| Licensed Module A scram / heat-dump | Per kit article | Cassette stays on the plate unless that article says otherwise |
| Seat a licensed kit in Z4 | Trilateral confirmation surface | Vehicle, steward, independent check |
| First remate to a habitat grid | Trilateral | Structured transition, not a surprise energize |
| Last-resort separation rail | Trilateral + kit article | Not a lattice procedure |
| Command reconstitution or scram from a somatic / harmony dashboard | Forbidden | **Predictive Harmony Metrics** stay default-off and off this column |

No remote party fires Module F or Module A from an unverified interface.

### Utilization Integrity and Circulation Recovery

Reject heat is not spoilage. The tree and TE bus are the metal form of **Utilization Integrity** and **Circulation Recovery**:

- Recoverable reject heat is a flow. Dumping all of it because TE watts are small is an integrity miss, not a physics requirement.  
- TE watts are logged on their own channel. Folding them into a lattice capacity claim is silent reallocation and is forbidden.  
- An idle qualified Fe3 can at $0\%$ payload is a low-tide *Material Tides* store. It is available ride-through, not a trophy and not a reason to skip travelers.  
- Expired or proxy-collapsed media are not treated as available store.

### Material Tides and remate

Remate is a renewal wave: same plate, low exit cost, no interior rebuild. Lock-in that would force a station to keep a damaged cassette because the plate is proprietary is a tide failure. Ship and station share the plate drawing so circulation stays reversible.

### Exterior Viability

Surface-station and C4 modes sit under the **Exterior Viability Protocol**. Cassette power may hold a habitat viability floor (night, dust, isolation). It may not be used to isolate people by withholding the plate. If a cassette fails, isolate *it*; restore allocation to the habitat by $N+1$ cassettes or another source. People are not a blast-radius.

### Structured Transition

Ship → station remate is a **Structured Transition**, not an instant full-power claim:

1. Mechanical mate and interlock  
2. Thermal-reject kit live (station sink or surface radiator)  
3. Housekeeping bus  
4. Primary bus at partial load  
5. Hotel / ISRU ramp  
6. Traveler and health-signal handoff  

Transitional incentive: the cassette remains useful on both sides of the mate so nobody has a reason to maroon it on the lander or the hull.

### Principled Stewardship — cassette health signals

Published without new punitive powers:

- Kit tenure and custody identity  
- Remate count vs design target ($\geq 20$ before plate overhaul)  
- Traveler completion rate and open nonconformances  
- Isolated-but-unrepaired heads / TE segments / slots  
- Last Entropy Audit window and outcome  
- Exploratory slot status (see audit)

### Entropy Audit (Module F and travelers)

Under the *Entropy Audit Methodology*, on a stated window:

- Destructive loss: scrapped cans, unlogged TE fade, unrecoverable plate damage, kit events  
- Generative floor: at least one rack slot may hold a new Cookbook variant under GM-1/GM-H1 rules, not only the first Fe3 recipe  
- Assumption-breakage: isolation paths used and recovered  
- No reclassification of bounded reconstitution variation as waste  
- No audit of crew somatic or harmony data because a cassette is nearby  

Audits are provisional, contestable, and subordinate to cognitive liberty.

### Cognitive Economy

Gallery procedures must be runnable under stress. An isolate list or traveler that requires a thesis is a **Cognitive Economy** failure. Module F steps stay the six already written.

### Continuity Floors at the Cassette

The Knowledge Continuity Floor and Material Continuity Floor in the *[Declaration of Cognitive Liberty](DECLARATION_OF_COGNITIVE_LIBERTY.md)* are residual-agency rights. They are not a second protocol and not a reason to grow Module A. This cassette applies them as follows.

**Knowledge object.** Travelers are the lineage for that article: incoming package, pulse/lock log, $t_{\mathrm{diff}}$, S4, disposition. A can without a traveler is an unrecoverable knowledge cut. Gallery procedures stay short under **Cognitive Economy**; the log is the floor, not a thesis.

**Material object.** Practical pathways are the interface plate, a seated licensed kit, spare heads and TE segments carried *off-cassette*, and idle qualified D-class or E-class articles at $0\%$ payload. Those spares are voyage support and low-tide store, not trophy mass and not governance weight.

**What this section does not add.** It does not change electrical class, ride-through arithmetic, or reconstitution gates. $N+1$ remains an Exterior Viability restoration path, not a Continuity entitlement to extra kits. Holding a kit still does not confer station government.

### Exclusions (keep the column dry)

- [*The Residual Cycle*](THE_RESIDUAL_CYCLE.md) does not treat the cassette as a residual-template store or a haunting instrument.  
- [*Somatic Resonance Theory of Frisson*](SOMATIC_RESONANCE_THEORY_OF_FRISSON.md) does not sit on the rack.  
- *[Predictive Harmony Metrics](PREDICTIVE_HARMONY_METRICS.md)* do not drive isolate, reconstitute, or scram.  
- Ghost Glass, Phoenix/Lazarus, and archaeological biorestoration stay out of Z1–Z4.  
- *[Relevancy Orbits](RELEVANCY_ORBITS.md)* are not a mate metric. Mechanical four-mate check is the mate metric.  
- **[Fluid Coalescence](FLUID_COALESCENCE_PROTOCOL.md)** is not a claim that $N$ cassettes become one will. $N+1$ is electrical margin.

### Cognitive liberty

All bindings remain subordinate to the [Declaration of Cognitive Liberty](DECLARATION_OF_COGNITIVE_LIBERTY.md). No cassette procedure may compel mental disclosure, harmony scores, or residual-order claims as a condition of drawing power.

---

## Recommended Architecture

The recommended system is **Configuration C3 in a Core Cassette**.

**Flow (C3 cassette)**

1. Module A (fission heat source) → neutron shield → Module B (heat-pipe tree)  
2. Module B → Module C (Stirling gallery) → reject-heat jacket  
3. Reject-heat jacket → Module D (thermoelectric bus) and → radiator or station heat sink  
4. Module C and Module D → cassette electrical bus  
5. Cassette bus ⇄ Module E (shielded lattice rack)  
6. Cassette bus → interface plate → ship or station grid  
7. Module F (reconstitution cell) services Module E off-bus (cartridge pull only)

    Module A  ->  Shield  ->  Module B tree  ->  Module C Stirling
                                                      |
                                              Reject-heat jacket
                                               /              \
                                         Module D TE        Radiator / station sink
                                               \              /
                                            Cassette electrical bus
                                                       |
                                    Module E lattice rack (shielded tap)
                                                       |
                                              Interface plate
                                                       |
                                            Ship or station grid

    Module F reconstitution cell services pulled Module E cartridges only.

### Core Cassette

The cassette is the contained structure. Everything listed as a module lives in or on that shell. The rest of the vehicle is not the core.

**Interface plate (both modes)**  
- Mechanical hard-points and lift fittings  
- Electrical power out (primary Stirling bus + TE bus, separately breakered)  
- Electrical housekeeping in (startup / monitoring, isolatable)  
- Thermal-reject mate (radiator loop in transit; station heat-sink or secondary radiator on surface)  
- Data / interlock / scram sense  
- Purge and atmosphere ports for the service gallery only (not for Module A)

If a mate is missing, the cassette is not released to that site.

**Gallery atmosphere (default).** The service gallery is a closed, controlled-air volume for shirtsleeve or light-suit work. It is not a vacuum work site and not a sodium-fill bay. Heat-pipe working fluid is charged only under the vendor process, off the gallery air. A sodium-limb leak is a limb isolate + gallery purge, not a shirtsleeve continue. EVA-only galleries are a later fork; they are not this design point.

**Plate-down.** The plate is a single structural/thermal article. Replaceable inserts cover wear, not a cracked sandwich. A failed plate is cassette-down. Data/scram has a second, physically separate path (cable or optic distinct from the power bosses) so a crushed power mate does not also silence scram sense. Thermal-reject still follows electrical-isolate ≠ thermal-isolate.

### Module A — Heat source

Public Kilopower / KRUSTY-class solid-fuel heat source with passive heat pipes. Published thermal band near $800\text{–}880\,^{\circ}\mathrm{C}$. Electrical class $1\text{–}10\,\mathrm{kWe}$ continuous per cassette; more power is more cassettes or a later Brayton fork, not a larger crystal.

Licensed article. Not a Cookbook recipe. Not opened on the ship or station except under that article’s own rules. Custody follows Capability Asymmetry.

### Module B — Circulatory tree

Branched heat pipes. Trunks leave the shield. Limbs feed independent Stirling heads. One limb failure does not kill the cassette. Circulation is thermal and closed. This is the primary Circulation Recovery path.

### Module C — Primary conversion

Free-piston Stirling first. Published KRUSTY convertors: about $35\%$ component and $\sim 25\%$ system efficiency in test. Lowest-mass choice at $1\text{–}10\,\mathrm{kWe}$. Brayton is a later fork for $100\,\mathrm{kWe}$-class demand.

Heads are gallery-replaceable without opening the shield. Each head is its own blast-radius.

### Module D — Regenerative thermoelectric bus

| Band | Location | Starting couple class | Role |
|------|----------|------------------------|------|
| High-reject | Converter reject heads / condenser shoulders | Higher-temperature TE families | Recover the hottest waste stream |
| Low-reject | Gallery skin / radiator root | $\mathrm{Bi_2Te_3}$-class | Housekeeping and reconstitution-cell power |

Orientation: space-TE systems often near $\sim 6\%$ thermal-to-electric. On a $10\,\mathrm{kWe}$ Stirling cassette at $\sim 25\%$ system efficiency, thermal input is about $40\,\mathrm{kW_{th}}$ and reject about $30\,\mathrm{kW_{th}}$. If the bus sees one-third of that reject at $6\%$, recovered power is about $0.6\,\mathrm{kWe}$. That is housekeeping, not primary propulsion power.

Rules:  
- Segment isolation; a shorted couple does not drag Stirling  
- Face temperatures logged; abort a segment that exceeds couple rating  
- TE watts logged separately; never folded into a lattice capacity claim  
- Failed couple = cartridge swap  

### Module E — Lattice buffer rack

Outside the neutron shield. Dose at the rack is an incoming release item: proxies must remain co-verifiable for the planned source class.

First payload: GM-1-qualified Fe3-type magnetite composite. Mullite or quartz chassis only under GM-H1 after GM-1 passes. Calcite stays default-off.

Buffer depth is ride-through, not the voyage energy budget. Dual-metric reporting is mandatory if a hybrid can is claimed for both dielectric and conversion roles.

At least one slot may be held as an exploratory Cookbook variant under the Entropy Audit generative floor.

**EMI / magnetic standoff.** Fe3 cans are magnetic articles. Rack slots sit in Z1, heads in Z2. Cans remain in sealed, field-tamed housings; slot D exploratory articles follow the same standoff. Do not mount an unshielded magnetite payload on a condenser shoulder or against a Stirling balancer. EM handling for reconstitution happens in Module F with the cartridge pulled, not in an energized rack slot next to a live head.

The on-cassette rack is **tier-0** ride-through (converter cover). Bay-level arrays are vehicle- or station-side **tier-1** and are specified under Transit and Surface Modes. They are not a sixth module.

### Module F — Gated reconstitution cell

Workshop cell in the service gallery. Accepts a pulled cartridge. Runs pulse-open → rearrange → recrystallize-lock → verify at screening payload or $\leq 10\%$. Hold duration $> t_{\mathrm{diff}}$. Three S4 passes before the cartridge returns to the rack. Photons time the window. Electromagnetic handling is allowed for magnetite payloads. Fields do not contain Module A.

Necessary Entropy applies. Over-order is a fail.

---

## Operative Configurations

### C1 — Static lattice primary (rejected)

Fails as primary: voyage energy is continuous and large. Retained only as Module E ride-through.

### C2 — Circulatory tree without lattice (feasible, incomplete)

Published Kilopower-class baseline. No TE recovery, no Cookbook buffer, no reconstitution path.

### C3 — Hybrid cassette (recommended)

C2 plus TE bus plus lattice rack plus reconstitution cell, all in one cassette.

### C4 — Remote cassette (mass-saving fork)

Same cassette. Interface plate on a boom, lander deck, or towed pack instead of in the crew hull. Lowest crew dose. Preferred when in-hull shield mass is unacceptable. Surface-station remate still uses the same plate. Under Exterior Viability and Architectural Elasticity, C4 may also mean moving the *vehicle* off a failed-safe cassette rather than throwing the cassette away.

---

## Transit and Surface Modes

### Transit mode (Earth–Mars-class)

Cassette mounted to the ship plate. Reject heat goes to ship radiators. Crew services Stirling heads, TE segments, and lattice cartridges in the gallery. Module A remains closed.

### Surface-station mode

Vehicle structure comes off the cassette. The cassette is lifted on its own fittings and remated to the station plate. Thermal-reject switches from ship radiators to the station sink or a surface radiator kit. Electrical output feeds the station grid through the same breakered buses.

No interior rebuild of Modules A–F is required for remate. If remate needs a new interior layout, the cassette design has failed.

### Shared rules

- Same interface plate drawing for ship and station  
- Same incoming dose map class for the lattice rack  
- Same traveler package for any cartridge moved during remate  
- Structured Transition sequence before full station load  
- Habitat viability is not held hostage to one cassette

### Cold-start, scram heat, and remate dead time

**Cold-start / black-start.** Before reject heat exists, Module C and Module D produce nothing. Housekeeping-in from the vehicle or station may energize controllers, interlocks, and sensors. Fe3 ride-through may assist that start only inside the payload gate. Module F stays off until TE housekeeping is live or an explicit start-feed is logged. Gallery crew may close housekeeping; seating the kit remains trilateral.

**Electrical isolate ≠ thermal isolate.** Plate staged contactors may open Stirling and TE buses while the thermal-reject mate stays connected. Scram and afterheat dump use the reject mate (ship radiator or station sink). If the reject mate is unmated, the kit article's own dump path is the only legal heat sink — remate is not begun, or is aborted, until that path is live.

**Remate dead time.** Afterheat does not wait for the checklist. Reject-kit live is step 2 and is not skipped. If station sink and ship radiator would both be open at once, keep one reject path until the other is verified. Dead-time with no reject path is a hold, not a partial mate.

**Voyage support mass.** Cassette dry mass is not spare-head, spare-can, or radiator logistics mass. Those ride on the vehicle or station.

### Bay-level buffer arrays (tier-1)

Localized Cookbook arrays may island a bay when the primary path is isolated, remating, or mid-head-swap. They are **electrical second-tier ride-through**, not a second tree and not a heat tap on Module B.

**Topology.** Charge and discharge sit on the already-converted plate bus (or a designated charge tap). Reroute is switchgear: staged contactors and a written isolate list. The lattice sources or sinks. It does not switch the tree, start the kit, or carry source flux.

- Module A → tree → Stirling → main DC bus (plate)
- TE bus → logged separate channel
- main bus → Module E rack (tier-0, converter cover)
- main bus → bay arrays (tier-1, named bay hotel / control / one restart)

**Rules.**

- Off-shield only. No array inside the neutron boundary.
- Gallery-class $L$. GM-1 / GM-H1 and travelers are parent Cookbook. Pulse-open stays in Module F (or a station copy of F), never in the bay rack.
- Per-bay $n$ cans. Isolate one cartridge; the bay stays up on the rest. $n+1$ is cover. $N+1$ remains extra *cassettes*.
- Charge from the bus, current-limited. Heat-pipe fluid is not a charge medium.
- TE watts stay on their own channel. Do not refill an array from unlogged reject-heat accounting.
- D-class dry until seated; E-class sealed incoming. No in-flight fill.
- Retain-first. A dead array is isolate-and-swap, not eject-the-cassette.
- Cognitive Economy: if the isolate list needs a thesis, the array is not released.

**Allowed use.** Bay hotel and control through a Stirling-head swap, a converter trip, Structured Transition steps 3–5, or a local bus fault that islands that bay only.

**Refused use.** Second core; propulsion feed; ship-length charged article; pulse-open of structure; automatic hull routing; folding TE recovery into a lattice capacity claim; holding habitat viability on one bay rack.

**Depth.** Minutes of a *named* bay load, not voyage-days. Hours of cover are another cassette or a station sink, not a larger crystal. Ratings stay provisional under Cookbook co-verification. Voyage-support mass for spare cans and array racks rides on the vehicle or station, not in cassette dry mass.

---

## Expected Operating Parameters (Orientation)

These are examples to show usefulness. They are not ratings of an unbuilt cassette and not Empirical Demonstrations of flight.

### Electrical classes

| Cassette class | Primary electric | Typical use |
|----------------|------------------|-------------|
| 1 kWe class | $\sim 1\,\mathrm{kWe}$ continuous | Uncrewed bus, small habitat slice, reconstitution-cell checkout |
| 10 kWe class | $\sim 10\,\mathrm{kWe}$ continuous | First crewed transit hotel slice; small surface station spine |
| Multi-cassette | $N \times 10\,\mathrm{kWe}$ | Larger hotel or surface grid; add cassettes rather than one giant crystal |

Published 10 kWe Kilopower-class concepts sit near $1545\,\mathrm{kg}$ all-up *including* a BOP share that already counts convertors and some radiator mass. RLC-10 does not stack gallery, TE, rack, and cell on top of that total; see the de-duplicated mass budget. Compact *column* is packaging. Compact *mass* is not promised.

### Transit hotel example (worked)

Assume a transit hotel load of $8\,\mathrm{kWe}$ average.

- Continuous supply: one 10 kWe-class cassette at partial load, or two 10 kWe-class cassettes with $N+1$ margin.  
- 30-minute ride-through at $8\,\mathrm{kWe}$:

$$
E = 8\,\mathrm{kW} \times 0.5\,\mathrm{h} = 4\,\mathrm{kWh}
$$

If a delivered Fe3 buffer is taken at an optimistic device-level $20\,\mathrm{Wh\,kg^{-1}}$ (inside the Cookbook’s reported device-dependent band, not the $924\,\mathrm{mAh\,g^{-1}}$ ceiling):

$$
m \approx \frac{4000\,\mathrm{Wh}}{20\,\mathrm{Wh\,kg^{-1}}} = 200\,\mathrm{kg}
$$

active material, before rack structure. That is why the lattice is a buffer, not the voyage store. A 5-minute converter blip at the same load is $\approx 0.67\,\mathrm{kWh}$ or $\approx 33\,\mathrm{kg}$ active at the same assumption.

First cycling of any new cartridge remains $\leq 10\%$ of its proxy-estimated ceiling.

### TE recovery example (worked)

10 kWe out at $25\%$ system efficiency $\approx 40\,\mathrm{kW_{th}}$ in, $\approx 30\,\mathrm{kW_{th}}$ reject. If the TE bus couples $10\,\mathrm{kW_{th}}$ of that reject at $6\%$:

$$
P_{\mathrm{TE}} \approx 0.6\,\mathrm{kWe}
$$

Use that band for gallery housekeeping and Module F, not for transit propulsion.

### Surface-station example

The same 10 kWe-class cassette, remated, supplies a small habitat / ISRU spine. Dust and night do not turn the cassette off. Radiator kit and sink design change; the cassette interior does not. A second cassette is the viability spare, not a governance spare.

---

## Gated Reconstitution (Buffer Only)

Applied to Module E cartridges in Module F only.

1. Pull cartridge. Screening-state or $\leq 10\%$ payload.  
2. Log $L$, $k$, $\rho$, $c_p$, $t_{\mathrm{diff}}$.  
3. Pulse-open a bounded interior or payload phase.  
4. Lock with hold $> t_{\mathrm{diff}}$ ($10\,\mathrm{s}$ to $5\,\mathrm{min}$ starting band).  
5. Verify structure + proxy.  
6. Three consecutive S4 passes or nonconformance.

This is the regenerative path that makes lattice ejection unnecessary. It does not reconstitute Module A. Necessary Entropy forbids polishing the can into a single forced texture.

---

## Emergency Path (Retain First)

Pre-authorized under Architectural Elasticity. Gallery acts do not wait for a meeting.

| Event | Action | Eject cassette? |
|-------|--------|-----------------|
| Lattice cartridge overtemp, crack, or proxy collapse | Isolate rack segment, dump remaining payload into the bus under gate, pull cartridge to Module F or scrap | No |
| TE segment short | Isolate segment, swap cartridge | No |
| Stirling head fail | Isolate head, remaining heads carry load, swap in gallery | No |
| Heat-pipe limb fail | Isolate limb, remaining tree carries load | No |
| Module A off-nominal (licensed) | Scram and heat-dump per that article; cassette stays on the plate | No, unless that article’s own last-resort rule says otherwise |
| Unrecoverable Module A with plate still safe | Keep cassette on plate if heat can be dumped; remote the vehicle from the cassette if needed (C4 logic in reverse) | Last resort only; trilateral + kit article |
| Lattice “hypervariable flux” drift | Pull and reconstitute. Not an eject cue | No |

Gated mobility maintains **buffer** stability. It does not replace nuclear scram. It does remove any need to throw the cassette away because a crystal drifted.

---

## Basic Operating Procedures

Designer-scope modes and sequences for the cassette and the lattice. They are not a flight novel and not Module A reactor ops. Licensed-source start, period, and scram detail remain **per kit article**. Missing incoming items still mean the job is not released. Gallery steps stay first-class isolate; kit-seat and first habitat remate stay trilateral.

### Operating modes

#### Cassette modes

| Mode | Electrical state | Thermal-reject | Lattice | Who may enter |
|------|------------------|----------------|---------|---------------|
| Cold | All buses open | Mate connected if afterheat exists; otherwise kit dump path only | Disarmed, screening or $0\%$ | Gallery may close housekeeping; kit-seat remains trilateral |
| Housekeeping | Housekeeping-in live; Stirling and TE primary still open or TE only as recovered | Reject mate live | Disarmed | Gallery |
| Hotel | Stirling primary at partial or rated hotel load; TE housekeeping | Reject mate live | Armed only if dose map present and outgoing cans pass | Gallery ramps load; first habitat remate is trilateral |
| Ride-through event | Stirling off-nominal or isolated in part; Fe3 supplies gated payload | Reject mate live | Discharging under payload gate | Gallery |
| Isolate-for-service | Affected head / TE / slot isolated; remainder may stay hotel | Reject mate live | Isolated slot disarmed | Gallery |
| Remate | Staged contactors per Structured Transition | One reject path always live | Disarmed until hotel restored | Trilateral for first habitat energize |
| Planned shutdown | Reverse of start-up | Reject mate stays until kit article says afterheat is dumped | Disarmed first | Gallery; kit shutdown per kit article |
| Licensed scram | Buses per kit article; cassette electrical isolate allowed | Reject mate **stays connected** | Disarmed | Kit article owns the source; gallery isolates lattice and convertors |

Do not skip from Cold to Hotel. Do not enter Hotel with the lattice armed if the dose map is absent.

#### Lattice usage levels

| Level | Payload | Typical use | Gate |
|-------|---------|-------------|------|
| Screening / idle store | $0\%$ or uncharged | Qualified can in the rack as low-tide store; Module F checkout | Incoming payload default |
| First cycle | $\leq 10\%$ of proxy ceiling | First energize of a new or reconstituted can | Mandatory |
| Ride-through | Sized for the hotel blip (orientation: $\sim 5\text{–}30\,\mathrm{min}$ at hotel load) | Converter blip only; not voyage energy | Dual-metric if hybrid; dump under gate |
| Pull-to-F | Screening or $\leq 10\%$ before pull | Reconstitution campaign | Six Module F steps; three S4 passes to return |

Slot D exploratory follows the same levels. It does not get a private higher payload.

### Start-up sequence (cassette-side)

Do not begin if cassette incoming is incomplete, if no reject path is live, or if Module F is jumpered to the primary bus.

1. Confirm isolate panel: all latches known; printed isolate list visible.  
2. Confirm thermal-reject mate connected (ship radiator or station sink) **or** abort to hold. Electrical isolate is allowed; thermal isolate is not, while the kit can produce afterheat.  
3. Close housekeeping-in from vehicle or station. Gallery crew may do this. Log cold-start feed.  
4. Confirm health-signal port live (read-only). Confirm no somatic or harmony connector present.  
5. Seat or verify Module A kit per kit article. **Trilateral.** This document does not specify source start.  
6. Kit article brings the source to the licensed idle or power band. Cassette watches reject temperature only.  
7. Enable Stirling heads per isolate panel, opposed pairs first. Ramp to hotel partial load. Do not arm the lattice yet.  
8. Enable TE segments when reject $\Delta T$ is inside couple rating. Log TE watts on their own channel.  
9. Module F may receive TE housekeeping. Do not pulse-open during start-up.  
10. Arm lattice slots only if: dose map present (or disposition is not fly), outgoing GM package passed, payload at screening or $\leq 10\%$, EMI standoff intact (cans in Z1).  
11. Raise hotel load. First remate to a habitat grid remains trilateral and follows Structured Transition (mechanical → reject → housekeeping → primary).  
12. Log start-up traveler: mode, payload, TE $\mathrm{Voc}/\Delta T$, isolate-panel state.

Fe3 ride-through may assist housekeeping only inside the payload gate. It is not a substitute for step 2.

### Normal operation

**Hotel loop (watch)**  
- Stirling carries hotel load. Spare heads stay mounted, isolated or unloaded.  
- TE supplies housekeeping and Module F cap only.  
- Lattice stays at the declared usage level. Do not silently raise payload to cover a conversion shortfall (Utilization Integrity).  
- Health-signal refresh on each isolate event and each remate. No crew ranking.  
- Gallery air stays closed and controlled. A limb-leak indication is isolate + purge, not continue.

**Ride-through**  
- Arm only for a converter blip or planned isolate-for-service of a head.  
- Dump through the bus under the payload gate.  
- After the blip: disarm to screening or idle store, or pull to Module F if proxies fail.

**Module F campaign (lattice service)**  
- Pull can at screening or $\leq 10\%$.  
- Run the six reconstitution steps. Hold $> t_{\mathrm{diff}}$.  
- Pulse-open cap remains TE-housekeeping only.  
- Three S4 passes or nonconformance. Do not run a campaign to make the can “look perfect” (Necessary Entropy).

**Remate (ship ↔ station)**  
1. Disarm lattice.  
2. Drop primary to housekeeping.  
3. Keep one reject path live while the other is verified.  
4. Mechanical mate.  
5. Reject kit live.  
6. Housekeeping.  
7. Primary at partial load.  
8. Hotel / ISRU ramp.  
9. Traveler and health-signal handoff.  

Dead time with no reject path is a hold.

### Planned shutdown

Reverse of start-up. Lattice first, source last.

1. Disarm lattice. Dump remaining gated payload or leave as idle $0\%$ store.  
2. Stop any Module F pulse. Cap stays armed as an interrupt.  
3. Shed hotel load. Isolate Stirling heads at the panel.  
4. Isolate TE segments after convertors are down, unless they are still inside rating on residual reject.  
5. Kit article shuts the source down. Cassette does not invent that procedure.  
6. Keep thermal-reject mated until the kit article declares afterheat dumped.  
7. Open housekeeping when sensors and interlocks no longer need it.  
8. Log shutdown traveler. Disposition remains fly / station / station-ground / hold / scrap as already declared.

Isolate-for-service is a partial shutdown of one head, limb, TE string, or slot. The rest of the cassette may stay in Hotel.

### Licensed scram overlay

The kit article owns scram. Cassette overlay:

1. Gallery isolates lattice (dump under gate) and isolate convertors as the kit procedure allows.  
2. Thermal-reject mate stays connected.  
3. Plate electrical isolate is allowed. Habitat $N+1$ pass-through stays available.  
4. Do not pull the cassette. Do not treat lattice drift as a scram cue.  
5. After the kit article releases the event, re-enter start-up from Housekeeping or Cold as that article directs.

### Normal safety parameters

Continue / hold / abort. These are operating parameters, not new physics.

| Parameter | Continue | Hold | Abort / isolate |
|-----------|----------|------|-----------------|
| Lattice payload (new or reconstituted can) | Screening or $\leq 10\%$ first cycle | Request to exceed $10\%$ without new designer release | Uncommanded payload rise; proxy collapse |
| Ride-through payload | Within incoming allowed energy | Approaching gate | Crack, overtemp, or dump path fail |
| TE face $\Delta T$ | Inside couple rating | Near rating | Exceeds rating or short |
| TE watts accounting | Logged on TE channel | Missing log | Folded into lattice capacity |
| Module F power | TE housekeeping only | Start-feed logged as exception | Primary-bus draw or cap fail |
| Hold vs $t_{\mathrm{diff}}$ | Hold $> t_{\mathrm{diff}}$ | Clock missing | Lock shorter than $t_{\mathrm{diff}}$ |
| Gallery atmosphere | Closed controlled air | Purge in progress | Sodium-limb leak with shirtsleeve continue |
| Isolate panel | Every channel known | One channel in service isolate | Latch that will not isolate |
| Reject path | One path live | Switching sinks | Both open while kit can dump heat |
| Dose map | Present for fly | Station-ground / hold without map | Fly disposition without map |
| Harmony / residual port | Absent | — | Any such connector found |
| Kit custody | Trilateral seat / remate | — | Gallery-only kit start or silent scram authority |

Health-signal fields stay read-only. Abort does not wait for stewardship consensus.

---

## Mass, Volume, and Access

| Article | Notes |
|---------|--------|
| KRUSTY-class fuel article | About $11\,\mathrm{cm}$ OD $\times$ $25\,\mathrm{cm}$ in the published test piece |
| 10 kWe-class published concept | Near $1545\,\mathrm{kg}$ all-up including published BOP; RLC dry mass is a replacement stack, not that figure plus extras |
| Cassette goal | Gallery large enough for one crew to swap a head or cartridge without opening the shield |
| Compactness rule | Shrink the gallery, not the shield |

Service rule: if a Stirling head, TE segment, or lattice cartridge cannot be isolated and swapped without opening the neutron shield, the cassette is not this architecture.

---

## Cookbook Family Map

| Family | Role | Not a role |
|--------|------|------------|
| Magnetite / Fe3 | First buffer payload; GM-1; EM handling | Fuel; in-flux part |
| Mullite | GM-H1 chassis; gallery dielectric | Unreviewed neutron reflector |
| Quartz | Shielded dielectric / piezoelectric tap | Voyage warehouse |
| Calcite | Default-off | Anything in the cassette |

Dual-metric rule applies to hybrid cartridges.

---

## Designer-to-Builder Transfer Package

This section is the release gate for everything a builder may fabricate from this document. It is a process specification, not a concept sketch. Missing incoming items mean the job is **not released**. Module A is never in this package.

### What is not in this package

**Nuclear Module A** arrives as a licensed article with its own dossier under the user's jurisdiction. The builder does not manufacture fuel, reflector internals, or shield formulation and does not “build a warp core.” Sodium working-fluid charge follows the heat-pipe vendor process, off the gallery air.

### Two release objects

| Object | First releasable campaign | Capacity / power rating |
|--------|---------------------------|-------------------------|
| Fe3 / hybrid cartridge and Module F process | GM-1 (GM-H1 only after a passing GM-1 outgoing package) | Capacity remains parent-Cookbook business. This package qualifies *process*, not *capacity* |
| Cassette structure, plate, gallery, TE segments, rack, cell | Cassette incoming complete + mate-and-accept dry run | Electrical class remains orientation until a kit article and measured convertors exist |

A cartridge may be released to a rack slot only after its GM outgoing package passes. A cassette may be dispositioned **fly** only if the dose-map incoming item is present for that source class. Without a dose map the allowed dispositions are hold / station-ground / scrap.

### Designer supplies (incoming)

**Cookbook articles (each cartridge batch)** — inherit [*The Synthesist's Cookbook*](SYNTHESISTS_COOKBOOK.md) GM incoming package:

- Body or feedstock identity, mass, geometry, and controlling dimension $L$
- Declared phase set and baseline XRD (or equivalent)
- Family proxy baselines (magnetite: VSM and/or electrochemical screening; chassis families: dielectric or TL/OSL as applicable)
- Computed $t_{\mathrm{diff}}$ from cited or measured $k$, $\rho$, $c_p$, with sources
- Documented pulse-open ceiling for that batch: solidus, decomposition onset, or oxidation onset, whichever is lowest
- Module F atmosphere specification: gas identity, purity, flow or static, and whether $p\mathrm{O_2}$ is sensed
- Allowed energy payload for this release (default: uncharged / screening-state; first cycling $\leq 10\%$ of proxy ceiling)
- Abort list and containment plan for that batch
- Pass/fail sheet for GM-1 or GM-H1
- Dual-metric declaration if the can will be claimed in both dielectric and conversion language

**Cassette (this document)**

- Cartridge and TE-segment drawings
- Interface-plate control drawing (ship and station identical), including staged-contactor order, health-signal pinout, and second data/scram path routing
- Rack dose map for the intended source class **or** an explicit statement that no map is supplied (fly disposition then forbidden)
- EMI / magnetic standoff note: rack face remains in Z1; nearest Stirling head remains in Z2; no unshielded Fe3 in Z2; reconstitution EM handling only in Module F with the can pulled
- $t_{\mathrm{diff}}$ worksheet and pulse-open ceiling for each cartridge batch (same as Cookbook incoming)
- GM-1 / GM-H1 pass sheets
- Emergency isolate list for rack, TE, Stirling heads, and limbs
- Abort and containment plan: Na-limb leak (limb isolate + gallery purge); TE short (segment isolate); Fe3 overtemp or crack (slot isolate, dump under gate, pull); plate-down (cassette-down, thermal-reject stays live if mated)
- Gallery atmosphere specification: closed controlled air; not a sodium-fill bay; purge criterion after a limb-leak drill
- Cold-start feed class: housekeeping-in source (vehicle or station), nominal voltage band, and that gallery crew may close it while kit-seat remains trilateral
- Stewardship health-signal blanks (no ranking fields)
- Entropy Audit window blanks
- Traveler blanks using the fields below
- Proof-load specification: lift fittings $1.5\times$ working load ($25\,\mathrm{kN}$ working $\rightarrow$ $37.5\,\mathrm{kN}$ proof)
- Cassette instrument minima and calibration records required at accept (below)

### Builder returns (outgoing)

- Completed traveler for every reconstitution cycle and for the cassette mate-and-accept run
- Pulse waveform log and independent temperature log (Module F)
- Pre/post XRD or equivalent and family proxies
- Dual-metric outgoing line if a hybrid or two-role can was declared incoming
- Pass/fail of each GM module gate
- TE segment acceptance: resistance, open-circuit voltage at a stated calibrated $\Delta T$, isolation check
- Plate mate check: mechanical; Stirling bus; TE bus (separate); thermal-reject still live if buses open; data/scram plus second path continuity; health-signal; staged-contactor order
- Isolate-panel dry pull: every head, limb, TE segment, rack slot
- Lift-fitting proof-load record and shell/plate NDT record
- Module F primary-bus isolation check (cell cannot draw Stirling watts)
- Nonconformance record for any abort, excursion, missing log, or incomplete vector
- Disposition: fly / station / station-ground / hold / scrap

### Traveler minimum fields

**Cartridge / Module F cycle.** Body ID; slot intended (A–C or D); cycle number; operator; date; $L$; $t_{\mathrm{diff}}$; Module F atmosphere; pulse energy / duration / spot; peak T; hold T and hold duration; cool profile; handling-field on/off; visual result; structure pass/fail; proxy pass/fail; dual-metric line if declared; payload this cycle; excursion yes/no; disposition (continue / hold / scrap / re-baseline).

**Cassette mate-and-accept.** Cassette ID; kit article ID (sealed; no internals); operator set; date; plate drawing rev; dose-map present yes/no; cold-start feed used yes/no; each isolate latch pass/fail; TE $\Delta T$ and Voc; second scram-path continuity; thermal-reject live with buses open yes/no; Module F cap check; proof-load; NDT; open NCR list; disposition.

### Cassette instrumentation and calibration minima

Exact models may vary. Calibration records are part of the archived accept package.

- TE accept: independent $\Delta T$ measurement at the couple faces; $\Delta T$ source calibrated; Voc and resistance logged at that $\Delta T$
- Plate: torque or preload class per drawing; continuity on power bosses and on the second data/scram path
- Isolate panel: mechanical latch pull recorded per channel
- Module F: parent Cookbook instruments for the active family (XRD or coupon-equivalent, family proxy meter, calibrated thermal); pulse-open cap interrupt tested
- Health-signal port: read-only check; no extra channels added at accept

### Starting bands the incoming package may cite (not builder inventions)

- Module F lock: hold $> t_{\mathrm{diff}}$; orientation $10\,\mathrm{s}$ to $5\,\mathrm{min}$
- Module F atmosphere for Fe3: flowing inert (Ar or $\mathrm{N_2}$), logged purity and flow; $p\mathrm{O_2}$ sensed when a sensor is available
- Gallery: closed controlled air; vendor sodium charge only off that volume
- First payload: screening or $\leq 10\%$ of proxy ceiling
- Cold-start: housekeeping-in until reject heat exists; Fe3 assist only inside the payload gate; Module F off until TE housekeeping or a logged start-feed

### Nonconformance

Any abort, missing log, failed S4, failed mate-check item, failed isolate dry pull, missing incoming item, or departure from the incoming package is a nonconformance. The body or cassette is not rated. It may be re-baselined only under a new designer release. A cassette without a dose map cannot take disposition **fly**.

### Handoff rules

- GM-1 is the first builder-releasable cartridge campaign. GM-H1 is not releasable until a GM-1 outgoing package has passed.
- Lattice cartridges and TE segments seat in a cassette only after their outgoing packages pass.
- The builder may run the cassette mate-and-accept sequence when the cassette incoming package is complete.
- Capacity ratings remain Cookbook business. Electrical class remains orientation until kit and convertors are measured.
- Incoming and outgoing packages must be completable in the gallery without a second document hidden in a thread (**Cognitive Economy**).

---

## Design Point RLC-10 (Blueprint Envelope)

This is the first buildable envelope. It is a **control drawing in prose**, not a licensed nuclear construction package. Dimensions, masses, and costs are design-point bands anchored on published 10 kWe Kilopower-class figures plus Cookbook additions. They are not as-built measurements of a flown cassette.

**What a builder may fabricate from this document**  
Cassette shell, interface plate, gallery hardware, heat-pipe tree *interfaces*, Stirling *mounts*, TE segments, lattice rack, reconstitution cell, travelers.

**What a builder may not fabricate from this document**  
Module A fuel, reflector internals, or shield formulation. Those arrive as a licensed kit and seat in the source bay.

### External envelope

| Item | Design point |
|------|----------------|
| Class | RLC-10 (10 kWe primary) |
| Shape | Vertical octagonal prism (flat gallery faces), inscribed in a circle |
| Outer diameter (across flats / inscribed circle) | $1.40\,\mathrm{m}$ / $1.52\,\mathrm{m}$ |
| Height, cassette only (no ship radiator) | $4.20\,\mathrm{m}$ |
| Interface plate | $1.52\,\mathrm{m}$ diameter $\times$ $80\,\mathrm{mm}$ structural sandwich at the ship/station end, with replaceable mate inserts |
| Lift fittings | Four hard-points on the opposite end; working load $25\,\mathrm{kN}$ each; usable after plate electrical isolate |
| Service gallery clear width | $\geq 0.55\,\mathrm{m}$ on two opposite faces so one suited or shirtsleeve crew can swap a head |
| Source-bay inner envelope | $0.80\,\mathrm{m}$ diameter $\times$ $1.35\,\mathrm{m}$ tall (licensed kit seats here) |
| Isolate panel | Recessed on both service faces at Z2 mid-height; mechanical + breaker isolate for every head, limb, TE segment, and rack slot |
| Health-signal / meter block | On plate rim; TE channel separate from Stirling channel; no somatic or harmony port |

### Internal stack (from plate end)

| Zone | Station (m from plate) | Contents |
|------|------------------------|----------|
| Z0 plate | $0.00\text{–}0.12$ | Interface plate; replaceable mate inserts; staged contactors (housekeeping then primary); separate Stirling and TE meters; health-signal port; trilateral kit-seat interlock; data/scram; thermal-reject mate |
| Z1 rack / TE / cell | $0.12\text{–}1.05$ | Module E four-slot rack (slots A–C first Fe3; slot D exploratory under Entropy Audit); low-reject TE; Module F cell on one gallery face with traveler pouch and pulse-open power cap fed from TE housekeeping only |
| Z2 gallery | $1.05\text{–}2.80$ | Module C Stirling heads; Module B limb terminals; high-reject TE on condenser shoulders; isolate panel and printed isolate list on both service faces |
| Z3 tree trunk | $2.80\text{–}2.95$ | Heat-pipe trunks through shield penetration (kit interface) |
| Z4 source bay | $2.95\text{–}4.20$ | Module A + licensed shield. No Cookbook lattice in this zone. No Ghost Glass, residual, or harmony taps |

Radiators are **not** inside the cassette. They mate at the plate (transit) or as a station sink kit (surface). Published 10 kWe-class radiator area is about $20\,\mathrm{m^{2}}$; that area lives on the vehicle or station, not in the 4.2 m shell.

Plate electrical isolate does not break station $N+1$ pass-through: a second cassette or other source may stay on the habitat bus when this cassette is isolated (Exterior Viability).

### Elasticity hardware (blast-radius)

| Function | Physical article | Rule |
|----------|------------------|------|
| Head isolate | Breaker + mechanical latch at isolate panel, one per Stirling head | Gallery first-class; no remote veto in a fault |
| Limb isolate | Valve or thermal-break at each tree limb terminal | One limb down does not stop the tree |
| TE isolate | Segment breaker on each couple string | Shorted couple does not drag Stirling |
| Rack-slot isolate | Slot contactor + dump path under payload gate | Cracked can does not scram Module A |
| Cassette isolate | Plate staged contactors | Isolating this cassette does not isolate the habitat if $N+1$ is live |
| Pulse-open cap | Module F heater/field hard cap, TE-housekeeping fed | Necessary Entropy: cell cannot raid the primary bus to over-order a can |
| Kit-seat interlock | Three-channel confirm at Z0 | Trilateral act; not a gallery improvisation |
| Remate interlock | Staged contactors: mechanical → reject kit → housekeeping → primary | Structured Transition in hardware |
| Health-signal port | Plate rim, read-only | Tenure, remate count, open NCR, isolated-unrepaired list; no punitive power |
| Harmony / residual ports | None | Not present on plate, rack, or cell |
| Thermal-reject during electrical isolate | Reject mate stays connected | Afterheat dump remains legal |
| Second data/scram path | Separate run from power bosses | Plate power-mate crush does not silence scram sense |
| Plate structure fail | Sandwich fracture | Cassette-down; inserts do not fix this |

### Mass budget (design point)

Published 10 kWe Kilopower-class breakout (orientation): reactor $\sim 235\,\mathrm{kg}$, shield $\sim 547\,\mathrm{kg}$, balance-of-plant $\sim 763\,\mathrm{kg}$ (Stirling, structure, controls, radiator share), total near $1545\,\mathrm{kg}$.

**Do not stack RLC lines on top of that $1545\,\mathrm{kg}$.** Published BOP already contains conversion and structure. RLC-10 *replaces* the in-cassette part of that BOP with a gallery, plate, TE bus, rack, and cell, and *moves radiators off* the cassette. Voyage spares (extra heads, extra cans) are not dry mass.

| Block | Mass band (kg) | Notes |
|-------|----------------|-------|
| Module A + licensed shield (kit) | $780\text{–}800$ | Published reactor+shield only; not a Cookbook manufacture |
| Conversion and tree (replaces published converter share of BOP) | $300\text{–}440$ | Heat-pipe tree $80\text{–}120$ plus Stirling heads/controllers $220\text{–}320$ (sixteen 625–700 We-class heads with two spare *mounted*, or an equivalent 125 We-class array). Do not add this line to a published BOP that already counted convertors |
| Cassette shell + plate + gallery | $180\text{–}260$ | Ti-6Al-4V or Al-Li; gallery is extra versus a tight flight stack |
| Plate inserts + staged contactors + meters + second scram path | $28\text{–}45$ | Wear faces for $\geq 20$ remates; housekeeping-then-primary; separate TE meter; distinct data/scram run |
| Isolate panel + latches | $15\text{–}25$ | Both service faces |
| TE bus (both bands) | $40\text{–}70$ | Not in the 2015-class published BOP |
| Lattice rack + 4 Fe3 cartridges | $80\text{–}250$ | Active Fe3 $33\text{–}200\,\mathrm{kg}$ by ride-through rule; slot D may be lighter |
| Reconstitution cell + pulse-open cap | $28\text{–}45$ | |
| Cabling, breakers, sensors, health port | $35\text{–}55$ | |
| **Cassette dry mass (no vehicle radiators, no voyage spares)** | **$1480\text{–}1980$** | Kit + replacement conversion + gallery extras. Same band as v1.4; accounting is now de-duplicated |
| Vehicle radiators | published $\sim 20\,\mathrm{m^{2}}$ class | Ship/station budget, not in the dry-mass total |
| Voyage spares | off-cassette | Extra heads/cans ride on the vehicle or station |

Do not advertise a cassette that “masses like a prop.” The fuel slug is small. The shield and converters are not.

### Output and life (design point)

| Parameter | Band |
|-----------|------|
| Primary electric, continuous | $10\,\mathrm{kWe}$ class at plate (Stirling) |
| TE recovered | $\sim 0.4\text{–}0.8\,\mathrm{kWe}$ housekeeping and Module F only |
| Thermal input (orientation) | $\sim 40\text{–}43\,\mathrm{kW_{th}}$ at $\sim 25\%$ system efficiency |
| Source thermal band | $800\text{–}880\,^{\circ}\mathrm{C}$ published test class |
| Design life, Module A kit | $12\text{–}15$ full-power years (published Kilopower intent) |
| Stirling heads | Replaceable; design for multi-year runs, swap on condition |
| TE segments | Replaceable; expect gradual couple fade; swap on $\text{voltage}/\Delta T$ abort |
| Fe3 cartridges | Reconstitute in Module F or replace; slot D exploratory |
| Plate remate cycles | Design target $\geq 20$ ship/station mates before insert overhaul |
| First-payload gate | $\leq 10\%$ of each new cartridge’s proxy ceiling |
| Pulse-open cap | Cell power $\leq$ TE housekeeping band; hard interrupt if cap exceeded |
| Health-signal refresh | Each remate and each isolate event |
| Cold-start feed | Vehicle/station housekeeping-in until reject heat exists |
| Remate reject rule | No dead time with both radiators open; hold if no sink |

### Materials and orientation cost (Cookbook-buildable)

Costs are 2026-class orientation for hardware a builder can buy. Module A kit cost is a government/vendor program number and is **not** listed as a Cookbook line.

| Article | Material / buy | Amount (RLC-10) | Orientation cost |
|---------|----------------|-----------------|------------------|
| Shell / plate | Ti-6Al-4V preferred; Al-Li allowed if thermal and fatigue close | $\sim 200\,\mathrm{kg}$ finished | Structure shop: mid five to low six figures USD depending on aerospace vs industrial finish |
| Plate mate inserts | Replaceable wear faces, same family or harder facing | one set + spare set | small vs converters; budget for 20-cycle swap |
| Staged contactors / meters | Space or industrial contactors; separate TE wattmeter | Z0 set | system buy |
| Isolate panel | Same shell alloy + latches | two faces | included in panel mass |
| Gallery panels | Same alloy; two removable faces | included in shell | included |
| Heat-pipe tree | Vendor-charged Na heat pipes, stainless or Haynes family | 8–12 limbs + trunks | Vendor quote; treat as qualified buy, not a garage fill |
| Stirling heads | Space- or industrial-derived free-piston units | 16 heads N+1 | Dominant Cookbook-adjacent cost; budget as a system buy, not a raw-metal buy |
| Low-reject TE | $\mathrm{Bi_2Te_3}$ modules | sized for $\sim 0.3\text{–}0.5\,\mathrm{kWe}$ | Commercial modules often $\sim 1\text{–}15\,\mathrm{USD\,W^{-1}}$ class; use space-screened lots, not the cheapest toy couple |
| High-reject TE | Higher-T family (skutterudite / SiGe class) | sized for $\sim 0.2\text{–}0.4\,\mathrm{kWe}$ | Higher than $\mathrm{Bi_2Te_3}$; quote as a segment kit |
| Fe3 cartridges | GM-1 magnetite/carbon composite in sealed cans | 4 cans; slot D may differ | Powder and can: low. Qualification and travelers: the real cost |
| Cell instruments | XRD-equivalent access or coupon port, impedance or capacity meter, calibrated thermal, pulse-open cap | one cell | Laboratory-class, not reactor-class |
| Fasteners / seals / isolators | Aerospace or industrial per drawing | lot | small vs converters |

**Rule.** Publish a traveler cost and a kit cost separately. Never fold a licensed reactor price into a “crystal core” shopping list.

### Manufacture and assembly sequence

**A. Licensed kit (not this document)**  
Receive Module A + shield as a sealed article. Store and handle only under that article’s rules. This document ends at the source-bay flange. Seating in Z4 is trilateral (three-channel Z0 interlock).

**B. Cassette structure (builder)**  
1. Cut and machine octagonal frames and skins to the envelope table.  
2. Weld or fasten the plate sandwich; install replaceable mate inserts; proof-load lift fittings to $1.5\times$ working load.  
3. Machine source-bay flange to the kit control drawing.  
4. Fit staged contactors, separate meters, health-signal port, and the second data/scram path. Confirm there is **no** somatic or harmony connector.  
5. NDT skins and plate. Thermal-cycle the empty shell across the expected gallery band.  
6. Paint / MLI / touch points per vehicle drawing.

**C. Tree and gallery (builder + vendor)**  
1. Install vendor heat pipes into limb mounts. Do not fill sodium on the shop floor unless the vendor process says so.  
2. Mount Stirling heads in opposed or balanced pairs. Align hot shoes to limb condensers.  
3. Pull cables to Z0 breakers.  
4. Fit high-reject TE shoes on condenser shoulders.  
5. Mount isolate panels and printed isolate lists on both service faces. Dry-pull every latch.

**D. Rack, TE low band, cell (Cookbook builder)**  
1. Build four Fe3 cartridges per [*The Synthesist's Cookbook*](SYNTHESISTS_COOKBOOK.md) GM-1. Label slot D as exploratory unless a later audit fills it with a qualified variant.  
2. Seat rack out of Z4 line-of-sight.  
3. Fit low-reject $\mathrm{Bi_2Te_3}$ segments on gallery skin.  
4. Install Module F on one removable face. Wire pulse-open cap to TE housekeeping only. Seat traveler pouch on that face.

**E. Mate and accept**  
1. Seat the licensed kit in Z4 under trilateral confirm. Torque and interlock per kit drawing.  
2. Plate-mate check: mechanical, electrical (Stirling and TE separate), thermal-reject still live if buses open, data/scram plus second path, health-signal, staged-contactor order.  
3. Dry run: isolate each Stirling head, each TE segment, each rack slot from the panel; confirm habitat pass-through still closes if a second source is present.  
4. Confirm Module F cannot draw primary-bus watts.  
5. Disposition: fly / station / station-ground / hold / scrap. Fly requires a dose map for the source class.

No step in B–E opens the licensed kit.

### Feature list (what the cassette *is*)

- One octagonal 4.2 m $\times$ 1.5 m cassette  
- One plate that is both ship and station mate, with replaceable inserts and staged contactors  
- One source bay for a Kilopower-class kit and a three-channel seat interlock  
- One branched heat-pipe tree with per-limb isolate  
- N+1 Stirling gallery with per-head isolate  
- Two-band TE bus with separate metering  
- Four-slot lattice rack, Fe3 in A–C, slot D exploratory  
- One reconstitution cell on a removable face, TE-capped, traveler pouch on the face  
- Isolate panels on both service faces  
- Health-signal port; no harmony or residual port  
- Habitat pass-through so cassette isolate is not people-isolate  
- Electrical isolate that leaves thermal-reject live  
- Second data/scram path; plate-down is cassette-down  
- Closed controlled-air gallery; no sodium fill in that volume  
- Fe3 EMI standoff from live heads  
- Lift fittings so the vehicle can come off the cassette  

That is the blueprint picture. Drawings still have to be cut from this envelope; this is the envelope they are cut from.

---

## Open Research Surfaces

- Flight-class dose maps for the rack at 1 kWe and 10 kWe source classes (without a map, disposition cannot be fly)  
- TE recovered watts versus added mass on a Stirling reject jacket  
- $t_{\mathrm{diff}}$ at gallery temperature  
- Ride-through mass versus hotel load at measured Fe3 delivered energy, not orientation $20\,\mathrm{Wh\,kg^{-1}}$  
- Plate-mate cycle life for repeated ship-to-station remates  
- Independent review of retain-first versus any vehicle-level last-resort separation rail  
- First Entropy Audit template filled on a ground cassette mockup  
- Exterior-viability restoration allocation if one cassette of an $N+1$ pair is isolated  

These surfaces are explicit.

---

## Relation to Existing Humai Work

This architecture is a companion **implementation example** of [*The Synthesist's Cookbook*](SYNTHESISTS_COOKBOOK.md), including Gated Mobility. It binds to:

- [*Necessary Entropy*](NECESSARY_ENTROPY.md)  
- **[Architectural Elasticity Protocol](ARCHITECTURAL_ELASTICITY_PROTOCOL.md)**  
- **[Capability Asymmetry Protocol](CAPABILITY_ASYMMETRY_PROTOCOL.md)**  
- **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)**  
- **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)** and **[Circulation Recovery Protocol](CIRCULATION_RECOVERY_PROTOCOL.md)**  
- [*Material Tides*](MATERIAL_TIDES.md)  
- **[Exterior Viability Protocol](EXTERIOR_VIABILITY_PROTOCOL.md)**  
- **[Structured Transition Protocol](STRUCTURED_TRANSITION_PROTOCOL.md)** and **[Transitional Incentive Protocol](TRANSITIONAL_INCENTIVE_PROTOCOL.md)**  
- **[Principled Stewardship Protocol](STEWARDSHIP_PROTOCOL.md)**  
- *[Entropy Audit Methodology](ENTROPY_AUDIT_METHODOLOGY.md)*  
- *[Cognitive Economy Protocol](COGNITIVE_ECONOMY_PROTOCOL.md)*  
- [*Why Walk When You Can Ride?*](WHY_WALK_WHEN_YOU_CAN_RIDE.md)  
- [*Empirical Demonstrations*](EMPIRICAL_DEMONSTRATIONS.md)  
- [The Call to Code](THE_CALL_TO_CODE.md)  
- [Declaration of Cognitive Liberty](DECLARATION_OF_COGNITIVE_LIBERTY.md)  

It shares empirical posture with [*The Residual Cycle*](THE_RESIDUAL_CYCLE.md) and [*Somatic Resonance Theory of Frisson*](SOMATIC_RESONANCE_THEORY_OF_FRISSON.md) and does **not** import their measurement objects into the rack.

The cassette is not a carrier of residual biological order.

For the full set of documents, see the [README](README.md). File this document in the Implementation layer next to the Cookbook, not as a new foundation protocol. Add **Core Cassette**, **RLC-10**, **ride-through buffer**, **retain-first**, and **interface plate** to the [Glossary](GLOSSARY_OF_TERMS.md) when publishing.

---

## Closing

The **Regenerative Lattice Core** is one Core Cassette: a licensed heat source, a heat-pipe tree, Stirling-first conversion, a thermoelectric reject-heat bus, and a Cookbook lattice buffer that can be pulled and reconstituted. It runs transit hotel loads, remates to a surface station on the same plate, and treats ejection as a last-resort vehicle option for the heat source — never as the answer to a lattice problem.

The crystal does not store fission. The tree carries heat. The bus recovers waste. The lattice levels and regenerates on a shielded tap. Custody of the kit is not government. Isolation is pre-authorized. Remate is a transition, not a capture. The cassette is what you keep.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.
