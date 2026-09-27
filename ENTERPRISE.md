# Enterprise
### Modular Disc-Train for a Second-Generation Interplanetary Vessel
#### *Orbital Architecture after Chemical Starship — Not a Warp Core*

---

by **Bradford James Focht (The Architect / Aspenth)**  
*v0.1 - v1.0 — September 24th, 2026*   
*v1.1 - v1.9 — September 26th, 2026*  
*v1.10 - v1.14 — September 27th, 2026*  

---

## Purpose

This document is an architecture for **Enterprise**: a modular **second-generation** vessel assembled in Earth orbit after a first generation of chemical ships (Starship-class and similar) has already cheapened mass to orbit and opened early interplanetary flights. Those first ships remain the cargo and crew lifters.

Enterprise is the reusable train for the infrastructure and colony work that follows them — survey, drill-prep, long stores, and surface-ops support — not a replacement for the first generation and not a warp ship.

The spacecraft is a linked train of rotating disc modules. A licensed fission plant sits forward. Propulsion and primary telecommunications sit on the flanks of that forward stack. Crew discs trail on retractable, reinforced inflatable tethers and airlocks. A detachable lander is the last car.

Two first working variants share one spine:

- **Enterprise-L** — Moon survey and drill-prep  
- **Enterprise-M** — Mars transit and surface-ops support  

Both fly **12 crew**. Both default to **hybrid** drive: electric for daily attitude and cruise trim, storable chemical assist on the flanks for published departure, capture, and abort burns.

The name is a debt and a limit. *Enterprise* means a ship that goes out to work, carry people, and come home — not a license to copy a television interior or to claim faster-than-light travel. Where a popular saucer, a multi-deck engineering hall, or a separated crew boom is efficient, this file uses it. Where the fiction needs antimatter, dilithium, or directed-energy weapons, this file stops.

Power, heat, and hotel electrics inherit the [Regenerative Lattice Core](REGENERATIVE_LATTICE_CORE.md) and the Transit Hotel Bus subsection below. This file does not teach anyone how to build a reactor. It sizes the ship to a published class of licensed space-fission kits and counts those kits.

It is a supporting technical instrument within the [Humai Accord](README.md). It follows [*Necessary Entropy*](NECESSARY_ENTROPY.md), [*Why Walk When You Can Ride?*](WHY_WALK_WHEN_YOU_CAN_RIDE.md), the **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)**, the **[Exterior Viability Protocol](EXTERIOR_VIABILITY_PROTOCOL.md)**, the **[Cognitive Economy Protocol](COGNITIVE_ECONOMY_PROTOCOL.md)**, the **[Capability Asymmetry Protocol](CAPABILITY_ASYMMETRY_PROTOCOL.md)**, the **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)**, and [The Call to Code](THE_CALL_TO_CODE.md).

This file is not a flight manual, not a bid, and not a launch license. Figures below are orientation arithmetic. Named kit counts, stores, and the feasibility register live in [ENTERPRISE_E0_MANIFEST.xlsx](ENTERPRISE_E0_MANIFEST.xlsx). Docking geometry is locked in [IRIS](IRIS_MIDS.md) I0 and copied on [Space Dock](SPACE_DOCK.md). E0 still needs a licensed plant-kit article before steel.

---

## Scope and Limits

**In scope**

- Train layout: forward plant and drive, tethered crew discs, aft comms, detachable lander  
- Enterprise-L and Enterprise-M consists for 12 crew  
- Default hybrid stationkeeping and cruise  
- Reorder and reconnection of cars; power and data follow the new consist  
- Disc modules that rotate for about $0.3\,g$ at the rim  
- Licensed fission as the primary heat source; RLC cassettes as the conversion and buffer layer  
- Transit Hotel Bus as the ship electrical grid  
- Smart outer hull: solar built into the skin (no unfolding arrays) plus regenerative ballistic gel  
- Magnetorquers and reaction wheels; flex joints for propellant-free turns  
- Life support, hydroponics, stores, and labs as module classes with isolate lists  
- Orientation stores and kit counts for 12 crew  
- Campaign E0 before steel or inflation of a first tether  
- Assumption that an Earth-orbit Space Dock exists as a neighbor article  

**Out of scope**

- Warp, antimatter, dilithium, or fictional spacetime propulsion  
- How to fabricate, enrich, or operate special nuclear material  
- Weapons or dual-use “deflector” language that hides a weapon  
- Quake Columns fills or geothermal loops inside a disc  
- Ghost Glass, *The Residual Cycle*, or **Predictive Harmony Metrics** as ship controllers  
- Kit custody becoming ship government  
- Unfolding solar wings  
- RCS as the only way to turn the train  
- A guarantee that this vessel has flown  
- The Space Dock drawing itself  

---

## Locked defaults

| Item | Default | May change only if |
|------|---------|-------------------|
| Crew | **12** | E1/E2 watch of 4; never a cruise below 12 without a new card |
| Drive | **Hybrid** | Pure electric is allowed if you name it. It is not the usual setting. |
| Core discs | **6** | Shakedown may fly 4; cruise does not |
| Rim | **$25\,\mathrm{m}$**, ring **$4\text{–}5\,\mathrm{m}$** | $20\,\mathrm{m}$ if E0-G fails mass; $40\,\mathrm{m}$ is a later car |
| Rim gravity | **$\approx 0.3\,g$** at $\approx 3.3\,\mathrm{rpm}$ | Spin-down abort always published |
| Plant | Counted licensed fission kits + RLC conversion. Hotel **$N$** from the E0 workbook (online = CEILING(hotel kWe / kit class); at least one spare) | No growable core |
| Burn structure | **Thrust-lock longerons** carry assist loads | Inflatable tethers are not a keel |
| Solar | In the skin only | No paddles |
| Daily attitude | Wheels + magnetorquers + flex | RCS abort-class only |
| Egress | **Lock Node** — pump-down airlock, no suitports | A suitport is not an airlock |

---

## Why a train, and why discs

A single rigid hull that holds the reactor, the crew, and the lander in one can puts dose, vibration, and blast-radius in the same room. A train lets the hot and loud end live forward. Crew discs sit behind a published tether length. If a tether or a disc fails, you isolate that car.

Each habitat car is a **circular disc**. The hub is a near-zero- $g$ crossing. The rim is the floor. Climb a spoke ladder down; at the rim you stand at about $0.3\,g$.

| Rim radius | Spin for $0.3\,g$ | Floor if ring width $4\,\mathrm{m}$ | Role |
|------------|-------------------|--------------------------------------|------|
| $15\,\mathrm{m}$ | $\approx 4.2\,\mathrm{rpm}$ | $\approx 380\,\mathrm{m^2}$ | Mass-tight shakedown only |
| $20\,\mathrm{m}$ | $\approx 3.7\,\mathrm{rpm}$ | $\approx 500\,\mathrm{m^2}$ | Allowed if E0-G passes |
| $25\,\mathrm{m}$ | $\approx 3.3\,\mathrm{rpm}$ | $\approx 630\,\mathrm{m^2}$ | **Default** |
| $40\,\mathrm{m}$ | $\approx 2.6\,\mathrm{rpm}$ | $\approx 1000\,\mathrm{m^2}$ | Later wide disc |

Twelve people need private cabins, wash, and a commons — not a $40\,\mathrm{m}$ saucer on the first train. One $25\,\mathrm{m}$ quarters disc at $4\,\mathrm{m}$ ring width has enough floor for twelve cabins plus wash if cabins stay modest ($\sim 12\text{–}16\,\mathrm{m^2}$ private plus shared rim).

---

## Train order (bow to stern)

1. **Fore stack** — plant, flanks, primary comms, hybrid assist tanks  
2. **Tether boom** — retractable, reinforced, separable. Not the ship’s door.  
3. **Crew train** — core discs, then mission cars  
4. **Aft comms disc** — second array  
5. **Lock Node** — four waist rings (lander or space door) plus fore and aft  
6. **Optional reverse-prop module** — aft face of the Lock Node; not required on first L  

Thrust structure lives in the fore stack and flank mounts. The crew train is not the keel.

---

## Fore stack — plant, hall, and flanks

### Engineering hall

A vertical multi-level chamber: galleries around a central well, ladders and rails, line-of-sight to the conversion deck. What sits in the well is **counted licensed kits**, not a single growable core.

- Source kits seat under that kit’s own rules. This file does not describe fuel, reflectors, or start-up.  
- Each kit feeds an RLC-class tree, Stirling gallery, thermoelectric bus, and ride-through rack.  
- More continuous power is more sealed kits (or a later licensed class).  
- Crew isolate heads, TE segments, and racks. Licensed source actions follow the kit article. Seating a kit is trilateral. Holding the plant does not confer command of the ship.  
- RLC-10-G (closed-loop geothermal coupler) is a **surface-station** source, not a transit source.

### Power class (orientation, 12 crew, hybrid default)

Hotel for twelve people, wet loops, spin motors, wheels, flex drives, and two comms chains is treated as a **$30\text{–}60\,\mathrm{kWe}$** band. Electric cruise trim and stationkeeping sit on top of that. Hybrid chemical assist does **not** feed the hotel bus.

Starting kit picture (replace with the kit article in E0):

| Load | Orientation | How it is met |
|------|-------------|----------------|
| Hotel + attitude + wet loops | $30\text{–}60\,\mathrm{kWe}$ | Several RLC-10-class cassettes ($1\text{–}10\,\mathrm{kWe}$ each) or fewer larger licensed units |
| Electric cruise / stationkeeping | Extra plant as E0 names | More kits or a later class on the same plate language |
| Hybrid assist | Chemical impulse, not watts | Flank tanks on the fore stack |
| Hull solar | House and dark-face trim | Skin only |
| TE bus | Logged housekeeping | Never folded into plant class |
| Lander (own power) | Hours to a surface window | Small plate or batteries; not the ship’s only source |

$N$ is cassette count. Do not invent a television gigawatt so the hall looks busy.

### Plant kit lock (examples, not a build recipe)

The **hall and plate stay**. The licensed source article is what upgrades. This file still does not teach fuel, reflectors, or start-up.

**Existing classes used as examples only**

| Example class | Electric | Thermal (order) | Flight-concept mass (order) | Notes |
|---------------|----------|-----------------|------------------------------|-------|
| Kilopower / KRUSTY family | $1\text{–}10\,\mathrm{kWe}$ | $\sim 4\text{–}43\,\mathrm{kWt}$ | $\sim 0.4\text{–}1.5\,\mathrm{t}$ per 10 kWe-class unit | Stirling + heat pipes. Flown-demo is the 1 kWe KRUSTY test, not a ship plant. |
| Fission Surface Power goal class | $\geq 40\,\mathrm{kWe}$ | $\sim 250\,\mathrm{kWt}$ order | Goal $<6\,\mathrm{t}$; Phase-1 concepts often heavier | HALEU path in current NASA/DOE work. Surface-first; hall must still accept a later space article of the same plate language. |

**First-article pick (planning)**

- Hotel band $45\,\mathrm{kWe}$ default (workbook).  
- Meet it with **one 40 kWe-class licensed article plus margin**, or **five 10 kWe-class articles plus two spare** so the 45 kWe hotel target and the workbook $N$ match. Same hall. Same RLC plate language.  
- Conversion stays RLC: Stirling first, TE on the reject path, ride-through rack.  
- A later higher-power core drops into the **same well**. Do not rebuild the chamber to chase watts.

**Planning article IDs** (names for E0-P; not a license and not a core recipe)

| ID | Meaning | First-article use |
|----|---------|-------------------|
| **KP-10-S** | 10 kWe-class Stirling space article in the Kilopower family | Default cluster: **5 online + 2 spare** (matches 45 kWe hotel ÷ 10 kWe) |
| **FSP-40-S** | 40 kWe-class article in the Fission Surface Power goal class, space-seated | Allowed alternate: **1 online + 1 spare seat** |

E0-P names one of those two rows. Swapping later is a new kit article in the same well. This file still does not describe fuel, reflectors, or start-up. A name on this table is not a purchased license.

### Heat reject (cannot delete)

Thermoelectrics recover a **slice** of leftover heat. They do not replace radiators. Space has nowhere else for the rest of the thermal power to go.

Planning lock:

| Path | Role |
|------|------|
| Stirling | Main electric from source heat ($\sim 20\text{–}25\%$ of thermal is a honest band) |
| TE bus | Logged house power from the reject stream ($\sim 5\text{–}8\%$ of *remaining* heat). Never counted as plant class. |
| Primary reject panels | Required. Order-of-magnitude **$2\,\mathrm{m^2}$ per kWe** of plant class (Kilopower 10 kWe used $\sim 20\,\mathrm{m^2}$). Skin solar is not this area. |
| Emergency panels | Isolated second set at about **25%** of primary area, for isolate/afterheat if a main loop is opened |

“Emergency radiators only” as the *sole* reject path would overheat the hall. Afterheat still needs a named path after electric isolate.

### Propulsion — hybrid default

**Daily.** Wheels, magnetorquers (in Earth field), flex joints. Electric thrusters on the flanks for low-thrust cruise and stationkeeping.

**Published burns.** Storable chemical or hybrid assist on the **fore flanks**: Earth departure, lunar plane change, Mars departure, abort. Tanks and engines for those burns stay on the fore stack. Plume is not a crew-disc problem.

**Reverse-prop module (optional).** A second pair of the same engine class may dock on the **aft face of the Lock Node**, engines facing forward along the train, for braking and capture. Same longeron lock, train straight, discs stopped or spin-locked. Not the daily attitude system. Not required on first Enterprise-L. Do not fire it at a berth. Count it as kit RP-1 when flown.

**Thrust lock.** Assist burns do **not** run through inflatable tethers. Before a burn the train straightens, flex joints lock, and **thrust-lock longerons** take compression and tension from the fore stack into the first disc (and a mid-train lock on Enterprise-M). Bladders go slack or isolate. No longeron, no burn. Kits L-C05 / M-C05 in the E0 workbook.

**Flank assist article (planning).** Two storable engines, **$50\text{–}80\,\mathrm{kN}$** each (SuperDraco-class thrust, or four AJ10-190-class at $\sim 27\,\mathrm{kN}$ if that is what the license allows). Hypergolic or other storable pair named by the vendor. Not a Raptor. Not cryogenic LH2 on the first card. Combined planning load through the longerons: **$100\text{–}160\,\mathrm{kN}$**. Electric thrusters stay on the flanks for cruise trim (Hall or similar, kW-class, not the burn).

This file does not teach how to build those engines. E0-T names the vendor article the same way E0-P names KP-10-S or FSP-40-S.

**Where the burn starts.** A first heavy train does not do TMI off a small flank pair from low Earth orbit. Stack and tanker at the Space Dock, then depart from a published high orbit. That altitude lives in the dock article.

**Mode card (required).** Electric-only daily / assist-armed / assist-firing / abort. You do not “just burn” because the wheels saturated.

Pure electric is allowed if E0 drops the assist tanks. It is not the default.

### Forward telecommunications

High-gain and omni on the fore stack. Flight-critical comms do not share a rack with hydroponics or a survey lab.

---

## Tethers and umbilicals

Each tether is a short ship: pressure bladder, restraint webbing, micrometeoroid layers, flex joint, at least two independent utility lines.

- Retract for dock, spin rehearsal, abort  
- Hard docks at both ends  
- One tear does not drop the neighbor car  
- Electrical isolate is not the same as closing air  
- Fail-closed flex: power loss **locks** mid-range angle  
- Not a thrust keel — see thrust lock  

Hub-to-hub span is an E0 number. Orientation: tens of metres, not kilometres, on the first train.

---

## Disc module (common article)

**Hub.** Airlock, spoke hatches, tanks, trunks, spin bearings, wheel set, emergency restraints.  
**Spokes.** Ladders; cable and duct.  
**Rim.** Floor at $0.3\,g$.  
**Skin.** Solar-in-hull, gel layer, bumpers as E0 requires.

**Isolate card.** Power tie, air, water, spin, tether clamps, flex lock, wheel safing, fire dump, spin down. If the card needs a speech, the disc is not released.

### Access and service

No Jeffries-tube city. Cabin and commons floor is for people. What must be reached is either in the open, behind a panel you can open standing, or a whole replaceable kit.

| Where | How you work on it |
|-------|-------------------|
| **Rim living** | Easy-access panels at floor, kick, and ceiling. Wet stubs, air returns, cable. One person with a driver, not a crawl. |
| **Rim service band** | A shallow ring behind those panels — ducts and buses, not a hallway. Depth planning **$0.3\text{–}0.4\,\mathrm{m}$**. |
| **Spokes** | Ladder plus a closed trunk. Cable and duct only. You climb through; you do not live in the spoke. |
| **Hub** | Service nexus at near-zero $g$: tanks, bearings, wheels, IRIS face, trunk ends. Reach from the hub volume. No extra tunnel. |
| **Fore hall** | Galleries around the well. This is the one walkway that stays: line-of-sight to kits and Stirling, not a habitat crawlspace. |
| **Skin** | Solar tiles and gel bumpers from outside (EVA or dock crane). Not from inside the cabin. |
| **Deep kit** | Pull the unit (cassette, wheel pack, IRIS face, processor skid). Do not tunnel to the middle of a tank. |

**Rules.** If a weekly check needs a crawl, the layout is wrong. If a failed part cannot come out through a spoke hatch or the hub IRIS, it is not a first-train part. Tethers are walked only for inspect-and-isolate, not as a daily workshop corridor.

### How a disc spins

The whole cabin does not spin as one piece on the tether. If it did, every remate would fight a rotating IRIS face.

**What stays still.** The **hub core**: IRIS faces, tether clamps, tanks that feed the train, reaction wheels. That core is fixed to the train. You float there at near-zero $g$.

**What turns.** The **rim, spokes, and floor** turn around that core on a bearing set (kit C04). At $25\,\mathrm{m}$ the rim runs about **$3.3\,\mathrm{rpm}$** for $0.3\,g$. You leave the still hub, take a spoke ladder that is already turning, and climb down to the floor.

**What drives it.** Electric motors on the hub core push the rim. Power comes from the hotel bus. Brakes on the same bearing stop the rim for remate or abort.

**What crosses the bearing.** Air, water, power, and data use rotary unions and slip rings (or an equivalent rotating joint). A weekly check of those joints is a panel job at the hub, not a crawl.

**Torque.** Spinning a disc up tries to twist the train the other way. First spin is on the [Space Dock](SPACE_DOCK.md) boom, with the ship berths locked. On the train, spin-up is slow, one disc at a time, with wheels on the hub core and the fore stack taking the leftover twist. Do not spin two discs up in the same direction at the same moment unless E0-G says the wheels can hold it.

**Stop.** Published spin-down before any IRIS remate. Power-loss: brakes come on. The Lock Node and the fore stack do not spin.

This is ordinary rotating-habitat practice: still axis, turning floor, motors and brakes you can pull as kits. It is not a gravity beam and not a spinning train of sealed cans.

**Moving between cars.** Daily traffic is hub → tether → hub, not rim to rim. You climb the spoke to the still hub, float or handrail the tether (about $15\text{–}25\,\mathrm{m}$, $2\,\mathrm{m}$ class tunnel), and enter the next still hub. The Lock Node and the fore stack are already still; you do not cross a bearing to reach them. Cargo uses the same path, or an IRIS face and a tug at the yard. Do not cut a door in the rim skin as a shortcut between discs.

**Living with $3.3\,\mathrm{rpm}$.** At the rim you feel about $0.3\,g$ toward the floor. Turn your head fast or drop a tool and it will drift in a curve (Coriolis). That is expected. Cabins keep the head toward the hub or along the rim, not a mix that fights the inner ear. First weeks use short rim shifts. If E0-G cannot show a crew can work at this rate, drop the first discs to $20\,\mathrm{m}$ (faster spin, worse Coriolis) only as a mass save — or keep $25\,\mathrm{m}$ and accept the floor area. Do not claim Earth-normal $g$ on a $15\,\mathrm{m}$ rim.

**Spin-up and spin-down (planning).** On the dock boom: minutes, per D0-S. On the train: **$15\text{–}30\,\mathrm{min}$** to $3.3\,\mathrm{rpm}$, one disc at a time. Remate: full stop first. Abort spin-down: same order, brakes on if power dies.

---

## Core six discs (both variants)

| # | Car | Floor use (orientation) | 12-crew note |
|---|----------------|-------------------------|--------------|
| 1 | Commons / galley | Mess, brief, watch copy | **First disc after the plant tether** — acoustic buffer. Last crew disc to shed |
| 2 | Quarters | Twelve cabins, wash, quiet, **storm shelter in the hub** | Sleep is not next to the hall. Bunks only if E0 fails cabin area |
| 3 | Life-support / hydro | Wet loops, plants as buffer | Not the only oxygen path |
| 4 | Medical / quarantine | Two-bay clinic + closeable air | Sized for 12, not for a hospital ship |
| 5 | Stores / shop | Food bulk, parts, repair | Moon: smaller food, more EVA parts. Mars: opposite |
| 6 | Aft comms | Second array, outbound watch | Independent of the fore stack |

Ends: fore stack (not a habitat disc) and **Lock Node** (landers on the waist; optional reverse-prop on the aft face). The Lock Node is not one of the six spinning core discs.

---

## Enterprise-L — Moon

**Job.** Survey from orbit, pick drill-prep sites, send a lander with people and a shallow rig, come home in weeks, not years.

**Time band (orientation).** Earth–Moon days; orbital survey days to a few weeks; surface windows measured in days. Design stores for **45 crew-days** on the train plus lander consumables, with a published margin. That is $12 \times 45 = 540$ person-days.

**Consist (bow to stern, default)**

1. Fore stack (hybrid)  
2. Commons  
3. Quarters  
4. Life-support / hydro  
5. Medical  
6. Stores / shop  
7. **Survey / mapping lab**  
8. **Drill-prep / sample shop**  
9. Aft comms  
10. **Lock Node** (landers on the waist)  
11. Optional RP-1 on the Lock Node aft face (off by default on L)  

Eight spinning discs plus the Lock Node. Landers are not a twelfth car on the axis. Survey and drill-prep are the two Moon extra cars. EVA lives on the Lock Node, not on a ninth spinner. Do not add a Mars long-stores disc “for symmetry.”

**Moon cars**

- **Survey lab.** Cameras, altimetry, downward comms, its own data network. No ship-control bus.  
- **Drill-prep shop.** Shallow rigs, cores, cuttings cans. Cuttings stay in the shop air until bagged.  
- **Lock Node.** Four waist rings: lander or space door. Dust vestibule on the dirty face. Lunar dust does not share quarters air.

**Lander-L.** Crew swap of **4** of the 12 for a surface window (survey lead, two EVA, one medical cross-trained). Eight stay on the train. Lander carries a battery or small plate, water for the window, and the rig. Losing the lander must leave eight people and a second path (dock abort or stay-aboard stores).

**Stores-L (orientation)**

| Class | Band | Note |
|-------|------|------|
| Food | $\sim 1\text{–}1.5\,\mathrm{t}$ packed | $540$ person-days at $\sim 1.8\,\mathrm{kg}$ plus margin; hydro is garnish |
| Water makeup | Low hundreds of kg | Recycle is the loop; tanks are leak-home |
| EVA | 6–8 suit-days of wear parts | Dominant Moon spare |
| Gel / hull | First-article inject reserve | Dock can restock |
| Assist propellant | E0 flank load for TLI / LOI / TEI / abort | Not in a crew rim |

**Attitude-L.** Magnetorquers work in Earth–Moon space near Earth; weaker at the Moon. Wheels and flex carry lunar-orbit pointing. Assist burns are the published plane changes.

---

## Enterprise-M — Mars

**Job.** Carry twelve people through a conjunction-class transit, keep them well, support a surface campaign from the train and a heavier lander, come home.

**Time band (orientation).** Outbound $\sim 180\text{–}260$ days; surface stay set by the ticket (this file uses a **500-day** class stay as the stores driver unless E0 shortens it); inbound $\sim 180\text{–}260$ days. Design the *train* food for transit plus a published stay-aboard reserve if the lander is late. Surface calories that live on the pad are a lander/pad traveler, not hidden in the rim.

Person-days on the train at 12 crew, two 220-day transits: $12 \times 440 = 5280$ person-days, plus reserve. That is why Mars gets a **long-stores disc**.

**Consist (bow to stern, default)**

1. Fore stack (hybrid, more plant than L)  
2. Commons  
3. Quarters (12 cabins; storm-shelter volume in the hub)  
4. Life-support / hydro  
5. **Second hydro / food-buffer disc**  
6. Medical  
7. Stores / shop  
8. **Long-stores**  
9. **Surface-ops lab**  
10. Aft comms  
11. **Lock Node** (Lander-M and optional second lander on opposite waist faces)  
12. Optional RP-1 on the Lock Node aft face  

Nine spinning discs plus the Lock Node. Landers are not the last axial car. Shelter is a **published hub volume** with extra mass on the quarters disc first; a tenth “shelter-only” disc is a later add if E0 dose says the hub is not enough.

**Mars cars**

- **Second hydro / food-buffer.** Plants and packed food overflow. Still not the only oxygen path.  
- **Long-stores.** Food, water makeup, spare gel, spare wheels, spare flex drives.  
- **Surface-ops lab.** Sample benches, ISRU *bench* (test, not a plant). Isolates. Suit work for the surface party happens on the Lock Node, not in this lab.

**Lander-M.** Surface party **6** of 12. Six remain on the train as the hotel and abort watch. Second path home: stay-aboard stores through the next window, or a second cargo/crew lander if E0 funds it. One lander as the only lifeboat is a failed Exterior Viability line.

**Stores-M (orientation)**

| Class | Band | Note |
|-------|------|------|
| Food on train | $\sim 8\text{–}12\,\mathrm{t}$ class | $5280$ person-days at $\sim 1.5\text{–}1.8\,\mathrm{kg}$ plus margin; hydro offsets some mass after E0 grows it |
| Water makeup | Tonnes-class tanks | Recycle still primary |
| Medical | Transit clinic + quarantine consumables | Months, not a lunar week |
| EVA | Mars-dust lock parts | Less than Moon-L unless E0 puts more EVA on the train |
| Spares | Wheels, bearings, pumps, bus gear for ~2 years | Counted |
| Assist propellant | TMI / MOI / TEI / abort | Fore-stack tanks |

**Attitude-M.** Magnetorquers fade after Earth departure. Wheels and flex are the daily system in cruise. Assist is for the published high-thrust events only.

---

## Crew of 12 — watches

| Role seats (not ranks as government) | Count |
|--------------------------------------|-------|
| Plant / hall watch | 2 |
| Flight / attitude / comms | 2 |
| Life support / hydro | 2 |
| Medical | 1–2 |
| EVA / surface (L or M) | 2–3 |
| Survey or surface-ops | 2 |
| Commander / relief (rotates) | from the above |

Two people can be sick without emptying a watch if the card is written that way. Twelve is the locked cruise number so that is true. A dock shakedown may fly 4; a cruise card that says 12 and sails 7 is a different ship.

Cabins: twelve private volumes on disc 1. No hot-bunking as the default.

---

## Hybrid operations (default)

1. **Dock and Earth orbit.** Magnetorquers + wheels + flex. Assist safed.  
2. **Departure burn.** Assist-firing on the fore flanks. Discs spin-locked or spun down per card. Train straight and locked.  
3. **Cruise.** Electric trim if E0 fitted thrusters; wheels and flex for pointing; solar as house. Assist safed.  
4. **Capture / plane change.** Assist-firing again.  
5. **Abort.** Assist or electric per the card; RCS only if translation has no other path.

Pure electric means skip the chemical burns and stretch the cruise. That is allowed if you name it. It is not the usual setting.

---

## Reorder and reconnection

Cars unmate, swap, remate on the same [IRIS](IRIS_MIDS.md) Stage 0 ring as [Space Dock](SPACE_DOCK.md). Change those numbers in IRIS first.

Moon example: put EVA next to the lander before a surface window; put survey next to aft comms for a radio-quiet map pass.  
Mars example: put long-stores on the lander ring before descent cargo transfer; put medical next to quarters after an injury.

Steps: stop the spin → cut that car’s power and air from the train → open the joint → move the car → close the hooks → air → data and shutdown sense → power. Write down the new car order. The plant stays forward. Do not remate while a disc is still spinning. Prefer Space Dock or two tugs.

### Joints (IRIS I0, copied)

| Item | Ship lock |
|------|-----------|
| Opening | **$1.00\,\mathrm{m}$** |
| Ring outside | **$1.60\,\mathrm{m}$** |
| Hooks | **12** in two sets of 6 |
| Tunnel at a disc hub | **$0.40\,\mathrm{m}$** class (full stack) |
| Ports | Data and power: MIL-DTL-38999 III. Air: 25 mm aerospace QD. Water: 12 mm aerospace QD. |
| Seal | Metal face plus inboard elastomer; hatch inboard |
| Power-loss | Hooks closed; power open |
| Approach box | $\leq 0.05\,\mathrm{m/s}$; offset $\leq 0.10\,\mathrm{m}$; angle and clock $\leq 5^\circ$ |
| Keep-out from an RLC plate | **$1.0\,\mathrm{m}$** or a measured map |
| Mass | $\sim 150\,\mathrm{kg}$ per face magnets off |
| Stuck-mate | Dual mechanical release + hand crank. No pyro on first article. |
| First flights | Stage 0 only. Live blades wait on IRIS I1–I4. |
| IRIS-C ($2.00\,\mathrm{m}$) | Not on first L or M consists |

Every disc hub, fore-stack face, lander ring, and dock remate uses this ring. No third connector. Local undock does not wait on Earth. Either face can be active for a given mate.

---

## Lock Node (primary egress)

Suitports are refused. The ship’s door is a **Lock Node**: a short, non-spinning can the train attaches to. Landers hang on its **waist**, not as the last car. It is a junction, not a cabin.

**Faces (all IRIS Stage 0 — same ring)**

| Face | Default on first L / M | May also be |
|------|------------------------|-------------|
| Fore | Crew train | Always the train on the first article |
| Aft | Cap, or optional reverse-prop module | Vacuum door if no RP-1 is flown |
| Waist Port-1 | Lander-A | Vacuum door |
| Waist Port-2 | Lander-B (or cap on L) | Vacuum door |
| Waist Stbd-1 | Vacuum door (EVA / dock) | Lander |
| Waist Stbd-2 | Vacuum door (EVA / dock) | Lander |

Six faces, one ring type. Every waist and the aft face is **universal**: lander berth or space door. You do not machine a second hatch family. Cap any face you are not using.

**Inside.** One clean vestibule from the train. Each used face has its own pump-down lock (four suited on a lander/EVA face; two minimum). Dirty / dust volume stays on that face. Quarters air never shares it. Cycle **10–20 min**. Power-loss: hatches stay closed.

**Landers.** They remate on a waist face, not behind the node on the train axis. Two waist faces can hold two landers (Mars option). Leaving a lander does not block the two space doors.

**Structure.** The barrel can take mid-train longeron load and an aft braking load from RP-1. It does not spin. Mass planning **$14\text{–}18\,\mathrm{t}$** (six faces).

**Not this node.** Daily walk from quarters to commons. Plant access. Skin-tile work from a cabin panel.

---

## Smart hull

Solar is **in the skin**. No unfolding wings. Gel lives in **bumper tiles**, not under live cell strings. Cabin **viewports are refused** on the first train: they are holes in a pressure hull. Outside view is cameras and optical sensors in the skin, screens in the rim and hubs. A small pressure window on the Lock Node is an E0 exception only, not a rim picture window. Inject from the hub between events; SDS in E0. A failed face is cut off from the rest. Gel is not a weapon shield and does not retire bumpers by announcement. E0-H maps which faces are cells and which are gel.

---

## Attitude, flex, and length

Wheels on every hub and the fore stack. Magnetorquers for Earth-field trim. Flex joints command a curve; fail **locked**. RCS is abort translation and a named desat last resort.

Max consist: E0-A number. Default first flyable max is the Mars consist (nine spinning discs) until someone measures how the train bends. Do not claim a twenty-car train before that.

---

## Lander classes

| | Lander-L | Lander-M |
|--|----------|----------|
| Surface party | 4 of 12 | 6 of 12 |
| Job | Survey, EVA, shallow rig | Habitat window, cargo, ops bench |
| Power | Batteries or small plate | Small plate preferred |
| Second path | 8 on train + dock/stay | 6 on train + stay-aboard / second lander |

Lander remate uses the same IRIS Stage 0 ring and the hotel-bus close-out.

---

## Transit Hotel Bus

The Core Cassette remains the replaceable article. Enterprise uses one or more plates in the hall and, if E0 allows, a small plate on the lander.

| Loop | Path | Crystal role |
|------|------|----------------|
| Heat | Tree → ship radiators | Spreader only |
| Electric (primary) | Stirling → main DC → train | Not a conductor |
| Electric (TE) | Module D → logged TE bus | Housekeeping |
| Buffer | Tier-0 rack; tier-1 per disc | D-class first |

**Bays:** Control (fore), Habitat (crew discs), Life-support electric, Service/gallery, Comms (fore and aft), Lander (its own power). Each bay can isolate. $N$ is cassette count. $n$ is cans in a bay. Do not add those two numbers together.

Remate and reorder use the same close-out: IRIS hooks, thermal reject, data/shutdown sense, then 120 VDC-class power A/B. Ties are bidirectional. Wiring that only works in one consist order is refused.

Electrical isolate is not thermal isolate. Afterheat still needs a reject path.

---

## Life, water, and plants

Wet loops isolate per disc. Plants buffer food and air; they are not the only oxygen path. Water leak-home is tanks. Knowledge and Material Continuity Floors: records, power, and water must survive one dead disc and one dead cassette.

### ECLSS chemistry (planning lock)

Numbers are ISS-class rates for **12 people**. They size tanks and loops. They are not a flight chemistry stamp.

| Flow | Rate (planning) | How it is met |
|------|-----------------|---------------|
| Metabolic O₂ use | $\sim 0.84\,\mathrm{kg}$ / person / day | Water electrolysis (primary). Compressed O₂ bottles as isolate backup only. |
| CO₂ produced | $\sim 1.0\,\mathrm{kg}$ / person / day | Regenerative removal (molecular-sieve or amine bed). LiOH or equivalent canisters as isolate backup. |
| Cabin N₂ / air makeup | Leak-driven | Tanks on the life-support disc. Not dumped to make room. |
| Water use before recycle | $\sim 3.5\,\mathrm{kg}$ / person / day (drink + hygiene + electrolysis feed) | Condensate + urine processor, **90%** recycle planning. |
| Water makeup after recycle | $\sim 0.35\,\mathrm{kg}$ / person / day | 30-day tank $\approx 0.13\,\mathrm{t}$ makeup plus a **$0.5\text{–}1\,\mathrm{t}$** working inventory. |
| Trace contaminants | Continuous | Charcoal / catalytic bed on the LS disc. |
| Humidity | Condensate to the water loop | Not vented as the normal dump. |
| Optional Sabatier | CO₂ + H₂ → water + CH₄ | Allowed later. Methane is not a hotel fuel on this card. |

**Loops.** Each crew disc has a wet stub that can isolate. The life-support disc holds the processors. One dead disc must not dry the train. One dead cassette must not stop electrolysis if the backup bottles and a second power path are up.

**Plants.** Hydroponics count as a buffer and a morale loop. Do not subtract plant O₂ from the electrolysis sizing until a measured campaign says so.

**Refuse.** Venting cabin air as the daily CO₂ plan. Sharing the water loop with ferrofluid, gel, or RLC salt. Putting the only O₂ bottles on the lander.

### Waste

Urine already goes to the water loop (LS-W2). Solids and trash do not.

| Stream | First-article plan |
|--------|-------------------|
| Urine / condensate | Recycle. Already in the ECLSS packet. |
| Fecal / hygiene solids | Dry or stabilize on the LS disc. Bag. Store. Do not dump overboard as the daily plan. |
| Packaging / shop trash | Compact on the stores disc. Store dry. |
| Where it lives | Stores (Moon). Long-stores (Mars). Not in quarters. Not next to O₂ bottles. |

Planning mass after water is pulled: about **$0.12\,\mathrm{kg}$** solids + trash per person per day. Mars transit order: $5280 \times 0.12 \approx 0.6\,\mathrm{t}$ plus cans. Reclaim more water from solids only after E0 names a processor. Compost is a later add, not the first card.

### Fire card

A fire is a disc problem first, then a train problem. You do not vent the whole ship.

1. **Detect** — smoke and heat in every rim sector, every hub, the hall, the Lock Node. Alarm on that car and on the commons watch copy.  
2. **Isolate** — that car’s air stub, power tie, and wet stub close. Neighbors stay closed.  
3. **People** — two spoke paths out of every rim sector to the hub. Hub to tether. Do not block a spoke with stores.  
4. **Kill** — portable extinguishers on the rim. Water mist or a named clean agent in the hall and in the LS processors. No Halon-class dump into a crew rim as the first move.  
5. **Plant** — isolate the cassette. Afterheat still has a radiator path. Do not fight a hall fire by opening the crew air.  
6. **Last resort** — vent **that disc only** if the card says the agent failed. Other discs stay pressurized.  
7. **After** — keep the burnt volume isolated until the yard or a written re-entry card.

O₂ bottles, trash, and batteries do not share a bay. A fire in quarters sends the crew to the commons hub or the aft comms hub — not into the hall.

### Storm shelter

Solar-particle storms last hours to a couple of days. This file does not stop galactic cosmic rays.

**Primary volume:** the **quarters hub**, sized for all 12. Ring it with water tanks, waste cans, and food — mass you already fly. That is the shield. Not a tenth disc.

**Backup volume:** the **aft comms hub**, if quarters is the fire disc or is open to space.

Path: rim → spoke → hub. You do not walk the tether in a storm if you are already on quarters. Watch copy in commons stays up unless that disc is the problem.

Dose numbers wait on E0 (g/cm² of water-equivalent around that hub). The rule does not: twelve people have a named hole to go to.

### Hall noise

Stirling machines and pumps are loud. Sleep is not next to them.

| Place | Planning limit |
|-------|----------------|
| Hall gallery | $\leq 75\,\mathrm{dBA}$ at the rail |
| Hub of the first disc (commons) | $\leq 55\,\mathrm{dBA}$ |
| Quarters rim, sleep | $\leq 45\,\mathrm{dBA}$ |

How: isolator mounts under every kit and pump; liner in the hall; the first tether flex joint is also an acoustic break; commons is the first spinning disc so quarters sits one car farther away. If a kit cannot meet the hall number on isolators, it does not sit in an open gallery — it sits in a lined bay.

Air noise in the hall is one problem. The worse one is **structure-borne** vibration: kits shake the hall, the hall shakes the tether, the tether shakes the first disc. Space does not absorb that path. You manage it in the metal.

**Do not treat the whole hull as one tuning fork.** One big note is what you are trying to avoid. Split the hull into sections that do not share a single ring frequency.

| Layer | What it does |
|-------|----------------|
| Isolator mounts under kits and pumps | Stop the shake at the source |
| Hall liner | Air noise at the gallery |
| Constrained-layer damping in hall and first-disc skins | Kills ring-on after a hit |
| Different stiffness / mass in neighboring panels | So two skins do not sing the same note |
| First tether flex | Breaks the path into the crew train |
| Optional tuned dampers | Small masses aimed at a measured hall mode, after E0 hears the real frequencies |

First article is **passive**: mounts, damping layers, broken paths, sections that disagree. Active “play the hull” (actuators that chase a mode) is a later card, after someone measures the real frequencies. Do not fly a control loop that can drive the skin as a speaker.

Stirling and pumps live in tens of hertz. Rim spin is about $3.3\,\mathrm{rpm}$ ($0.055\,\mathrm{Hz}$) — that is not an acoustic note; it is a slow load. Keep those two families apart. If a kit’s running tone matches a hall skin mode, change the mount or the panel, not the crew schedule.

### ECLSS packet (E0-E)

This is the first-article hardware list for 12 people. Vendor SKUs wait on purchase. Classes do not.

| Kit | What | Where | Planning |
|-----|------|-------|----------|
| LS-O2 | Water electrolysis stack | Life-support disc | Size for $10\,\mathrm{kg}$ O₂ / day. Second power path. |
| LS-O2B | Compressed O₂ bottles | LS disc + one spare set on stores | **2 days** of 12-crew metabolic O₂ if the stack is down |
| LS-CO2 | Regenerative CO₂ bed (sieve or amine) | LS disc | Dual bed so one can isolate |
| LS-CO2B | LiOH or equivalent canisters | Stores | **3 days** of 12-crew CO₂ if both beds are down |
| LS-W1 | Condensate collector + polish | Each crew disc stub + LS | Returns to the water loop |
| LS-W2 | Urine processor | LS disc | 90% recycle planning |
| LS-W3 | Working water inventory | LS + stores | **$0.5\text{–}1\,\mathrm{t}$** |
| LS-W4 | Makeup tank | Stores | 30-day makeup $\approx 0.13\,\mathrm{t}$ |
| LS-N2 | N₂ / air makeup tanks | LS disc | Leak-driven; not a dump tank |
| LS-TCC | Trace-contaminant charcoal / catalytic | LS disc | Continuous |
| LS-HUM | Humidity to condensate | Each crew disc | Not a vent |
| LS-CAB | Cabin sensors (O₂, CO₂, H₂O, P, T) | Every disc + hall | Isolate if a disc is out of band |

**Power.** Electrolysis and processors sit on the hotel bus (inside the 45 kWe band). They do not steal hybrid-assist tanks.

**Isolate.** Close the wet stub on a sick disc. Processors on the LS disc keep running. Bottles and canisters are the days above, not an infinite backup.

**Sabatier.** Not on the first packet. If added later, methane is vented or stored as waste. It is not hotel fuel.

**E0-E closes** when this table has vendor names and tank drawings. Rates above stay the sizing lock.

---

## Materials (dock incoming, orientation)

Aluminum-lithium or equivalent hull; composite/fabric tether restraint; published inflatable bladders; viewports as E0 allows; copper/bus bar; hall steel; IRIS hook and ring metal; counted wheel and bearing sets; magnetorquer bars; solar-in-skin product; ballistic gel with SDS; bumper layers; RLC kits as licensed articles; hybrid-assist tanks and engines as licensed flank kits.

No fuel fabrication from this file. No paddle arrays in the incoming list.

---

## Space Dock (assumed)

### Disc, tether, and boom planning masses

Replace with weighed masses when you have them. The numbers below are planning bands, not CAD.

| Item | Planning lock |
|------|----------------|
| First instrumented disc (structure + hub + wheels) | **$12\text{–}18\,\mathrm{t}$** |
| Outfitted crew disc (12-person capable, wet loops dry) | **$18\text{–}25\,\mathrm{t}$** |
| Tether span (hub to hub) | **$15\text{–}25\,\mathrm{m}$** |
| Tether dry mass each | **$400\text{–}800\,\mathrm{kg}$** |
| Inflatable clear diameter | **$2\,\mathrm{m}$** class |
| IRIS faces per joint | 2 × $\sim 0.15\,\mathrm{t}$ |
| Fore stack (hall + flanks, no tanks) | **$40\text{–}70\,\mathrm{t}$** order, kit-article driven |
| Water buffer (12 crew, high recycle) | **30-day tank** at $\sim 0.5\text{–}1\,\mathrm{t}$ working inventory; makeup from the ECLSS table |
| Food (orientation) | $\sim 1.8\,\mathrm{kg}$ / person / day before packaging; Mars card uses the workbook days |

Spin: $0.3\,g$ at $25\,\mathrm{m}$ remains $\approx 3.3\,\mathrm{rpm}$. Boom stop and shake live in [Space Dock](SPACE_DOCK.md) D0-S.

The neighbor article is [Space Dock](SPACE_DOCK.md) **v1.9**: modular spines, two SD-B01 berths on IRIS Stage 0, SD-1 first yard, Earth / Moon / Mars cards. Altitude, debris, and dock power live there.

E0-D closes when all of these are written and match:

- IRIS I0: $1.00\,\mathrm{m}$ opening, $1.60\,\mathrm{m}$ ring, 12 hooks  
- Space Dock D0-B (berth, approach box, $80\,\mathrm{m}$ keep-out planning, $1.0\,\mathrm{m}$ plate keep-out)  
- Space Dock **D0-E** interface list (plate family, crane/tug, boom, tanker face)  

A different locked opening than the yard is a failed E0-D. A working berth in orbit is later (D3 / E1), not this gate.

---

## Command, agency, and custody

Gallery and disc crew have first-class isolate. Licensed source actions follow the kit article. Ship command is not automatic with plant custody. Agency Interface interruption stays first-class. A disc can be spun down and dropped without a speech about network stability.

---

## E0 manifest (workbook)

Initial outfitting, stores, and the feasibility register are in [ENTERPRISE_E0_MANIFEST.xlsx](ENTERPRISE_E0_MANIFEST.xlsx).

- Hotel kit count is computed: online = CEILING($45\,\mathrm{kWe}$ / $10\,\mathrm{kWe}$) = **5** at the default knobs, plus at least **2** spare (25% with a floor of 1 — check the sheet after recalc). Change the yellow hotel target and the $N$ follows.  
- Disc structure masses in the kit sheets are the **16–25 t outfitted band** from this file. They are still estimates until weigh-in, not CAD.  
- All E0 gates start **OPEN**. Close them with written numbers, not with hope.

## Campaign E0

| Gate | Must name | Fail |
|------|-----------|------|
| E0-K Consist | L or M list, 12 crew, max length | No list = no train |
| E0-P Plant | KP-10-S cluster or FSP-40-S, $N$, reject path, hall isolate | No named article class = no hall |
| E0-T Thrust | Hybrid card, $50\text{–}80\,\mathrm{kN}$ class flank pair (or 4× AJ10-class), longerons, tanks | Thrust through a bladder or a crew disc = dead |
| E0-G Gravity | $r=25\,\mathrm{m}$ default, rpm, spin-down, cabin area for 12 | Unnamed Coriolis = no spin |
| E0-U Tether | Span, layers, leak-home, cut-away, flex cone | Limp joint = no train |
| E0-H Hull | Skin solar map, gel in bumper tiles not under cells, SDS | Folding wing or gel under live strings = no smart hull |
| E0-A Attitude | Wheels per car, torquer band, desat, max consist | Gas-only turn = no long train |
| E0-R Reorder | IRIS Stage 0 ($1.00\,\mathrm{m}$, 12 hooks), **spin-down first**, isolate that car, write the new order | Live-spin remate, live blades on first flight, or wiring that only works in one order = no rebuild |
| E0-C Comms | Fore and aft independent | One array = no outbound watch |
| E0-L Lander | L or M class, party size, second path | Lander as only lifeboat = failed viability |
| E0-B Bus | Bays, $N$ vs $n$, remate, bidirectional ties | Folded numbers = no grid |
| E0-S Stores | Food/water/EVA/spares masses for the variant | Class list with no days = no cruise |
| E0-E ECLSS | Packet above: stack, beds, tanks, 2-day O₂ / 3-day CO₂ backup | Vent as daily CO₂, or bottles only on the lander = no cruise |
| E0-D Dock | Space Dock D0-B + D0-E + IRIS I0 match | No dock interface, or a different opening than the yard = no assembly |

E1: one instrumented disc on a boom. E2: short train, watch of 4. E3: 12-crew L or M consist unmanned or dock-tethered spin. Then a cruise card.

---

## Refused stories

- The hall *is* the reactor  
- Warp, antimatter, or a crystal that stores the voyage  
- Weapons hidden as sensors  
- One hole that is seismic, geothermal, and hotel  
- Gel that retires bumpers by announcement  
- Earth-normal gravity at a $15\,\mathrm{m}$ rim  
- Aft comms as a second government  
- Transit Hotel Bus as the whole ship  
- Unfolding solar  
- RCS as daily steering  
- Flex that fails limp  
- Wiring that forbids a new consist  
- A 12-crew card sailed by 7  
- Suitports as the ship’s door
- Cabin viewports on the first train
- Dumping solids as the daily waste plan
- Venting the whole train to fight a fire  
- EVA through quarters instead of the Lock Node  
- Moon cars copied onto Mars “for symmetry”  
- Pure electric silently replacing hybrid  
- A ship opening that does not match the yard IRIS I0 lock  
- Live iris blades on the first L or M remate  

---

## Naming and family

**Enterprise** — vessel family.  
**Enterprise-L** — Moon consist.  
**Enterprise-M** — Mars consist.  
**Disc-train** — layout.  
**Transit Hotel Bus** — electrical subsection.  
**RLC** — cassette.  
**Space Dock** — neighbor article, not this file.  
**IRIS Stage 0** — joint and remate ring (I0 in that file).  
**Lock Node** — primary egress hub. Not a suitport.

Implementation layer after Regenerative Lattice Core. Not a foundation protocol.

---

## Closing

Enterprise is a train you can count: kits in the hall, six core discs, mission cars for Moon or Mars, twelve people, hybrid burns that are written down. The saucer is a rotating floor. The engineering well is a gallery around licensed kits. The voyage still runs on heat, Stirling, radiators, wheels, and a published abort.

It is meant to be copied during the colony boom after Starship-class flights are ordinary: same ring as the yard, same plate language, Moon and Mars variants from one spine. Fail into a disc that is still just a disc. Do not fail into a myth that the name will fly the ship.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.

This license covers the architectural description. It does not grant rights in third-party standards, reactor kits, solar products, or anyone else’s patents. It does not grant rights in Star Trek or any other fiction franchise. Builders remain responsible for launch, nuclear, and flight licenses in their jurisdiction.

No warranty of merchantability, fitness, voyage endurance, or $0.3\,g$ comfort is offered. The first honest product of an Enterprise train is a measured disc on a measured tether, not a silhouette.
