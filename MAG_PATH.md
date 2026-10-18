# Mag-Path
### *Sealed Liquid EAP Walk Lines, Gait-Following Grip, and Tagged Acoustic Link for Enterprise and Space Dock*
---
by **Bradford James Focht** (The Architect / Aspenth)  
*v1.0 - v1.6 — October 17th, 2026*<br>
*v1.6.1 - v1.6.2 — October 18th, 2026*<br>

---

## Purpose

This document is the article behind the **MP-1** kit named in [Enterprise](ENTERPRISE.md). It specifies a sealed, liquid-filled conductive path that hardens under a tagged boot, a gait-following grip that does not cling, and a short acoustic link along that path.

The path is powered. The boot is passive. Contact with a valid tag is what makes a segment active. There is no open charged surface.

The same article serves [Space Dock](SPACE_DOCK.md) truss and boom-root walk lines. It does not replace the spinning rim. The rim already has about $0.3\,g$. Paths are not laid on the cabin floor. Emergency lots inside a disc stay off unless an emergency or a spin-down calls them.

The document is an architecture and first-article campaign. It is not a flight stamp and not a medical device. Frequencies and force bands below are orientation. Campaign M0 replaces them.

A [Separation Lock](SEPARATION_LOCK.md) is the EVA airlock sibling. It keeps ordinary return inside the seat film. It is not in this file. This file only requires that an EVA shell still walks if a slipper will not seat.

---

## Scope and Limits

**In scope**

- Interior zero- $g$ lots: hub cores, tether pylons, fore-stack gallery, Lock Node clean side, Space Dock spines and boom root
- Exterior EVA walk lines: fore stack, tether restraint webbing, Lock Node barrel, lander waist, yard truss — between gel bumper tiles, not under live solar cells, not across a spinning rim skin
- Emergency lots inside $0.3\,g$ discs: spoke foot, airlock threshold, spin-down refuge band. Default off. Not the cabin floor
- IVA slipper and EVA shell, slipper seating into the shell
- Sealed liquid path, electroactive-polymer skin, pair tag, grip law, force bands, heat loop, acoustic link
- Keep-out from RLC plates, IRIS coils, and a later maglev hub bearing

**Out of scope**

- Gravity plating, $1\,g$ simulation, or paths as the rim floor
- An open electrode or a current through the crew
- A radio replacement for long-range or off-path talk
- IRIS drive coils used as a walk surface
- Trapping a boot on power loss
- A claim that the acoustic link is private against another body on the same path
- [Separation Lock](SEPARATION_LOCK.md). This file does not specify the lock. It only requires a shell that walks if the seat is dirty
- AURA-suit overwatch or high-potential energy beaming

---

## Locked defaults (from Enterprise)

| Item | Lock |
|------|------|
| Rim floor | **No paths.** $0.3\,g$ at the rim is the floor |
| Interior lots | Still spine only |
| Exterior lots | Narrow walk lines, not under solar, not on spinning skin |
| Power loss | Field dies to residual or off. A dead path does not trap a boot |
| Burns and launch | Straps, not the path |
| Keep-out | $1.0\,\mathrm{m}$ from an RLC plate. Not under a maglev hub bearing. No shared driver with IRIS coils |
| Kit | MP-1: interior lots, exterior lots, boot plates |
| Fail posture | **Fail open.** Unlike an IRIS port, which stays latched, a Mag-Path segment releases |

This file does not reopen those locks.

---

## The path

A Mag-Path lot is not a solid metal strip.

It is a sealed channel: a conductive liquid under a dielectric electroactive-polymer skin, with a local driver.

- **Liquid.** The sensing and thermal medium. Pressure under a foot is read as a change in the channel. The liquid also carries low-grade heat.
- **Skin.** Electroactive polymer. Soft when idle. Under a valid contact it stiffens in the patch under the sole. Stiffening is the “draw.” It is reflexive to contact plus tag, not a standing hard floor.
- **No open conductor.** The liquid stays inside. The skin is the face the boot touches. Coupling into the boot is magnetic and mechanical through the skin. No current crosses into the sole. The earlier open-surface problem is closed by enclosure plus local enable, not by insulating an exposed electrode.
- **Local enable.** A segment energizes only under a tagged contact. Neighboring segments stay soft and dark. Power exchange is the grip field in that patch and a tiny tag interrogation. It is isolated to the patch.
- **Driver.** On the ship side. Sees the tag. Commands stiffness and field for that patch. Does not run a ship-wide magnet.
- **Fail-safe.** Driver loss or skin fault $\rightarrow$ patch to soft and field to residual or off. Residual is below the free-band ceiling. A dead path does not trap a boot.

The path is a walking line, a pressure sensor, a short acoustic medium, and a heat tributary. It is not a power bus and not a data backbone.

---

## Tag and pair link

Simple. No suit overwatch.

- Each sole carries a passive tag. The tag is read on contact. It names the boot. It does not track the wearer off the path.
- A pair is two tags enrolled together. Left and right are known to each other so the grip law can see load leave one foot and arrive on the other.
- Enrollment is a local act on that lot. It is not a ship directory of movement.
- A segment that cannot read a tag does not draw. An untagged contact is a pressure event only. It does not harden the skin and it does not open a link.
- Two pairs on one lot get independent patches. They do not share an envelope.

The tag is an address for the patch under the foot. It is not a location log.

---

## Two boots, one sole law

### IVA slipper

A removable pseudo-sock for interior zero- $g$.

- Soft upper. Passive tag. Thin ferromagnetic interface plate. Tactile and pressure arrays in the sole, reading the path under them.
- Worn alone in a safe interior. Removed for relief. Donned again without tools.
- Seats into the EVA shell. Connect-in is a mechanical seat plus tag and plate align.

### EVA shell

- Receives the slipper. If the slipper seats, the slipper’s plate and tag are the inner stack.
- If dust or damage blocks the seat, the shell walks on its own plate and its own tag. Conversion does not depend on a clean slipper. [Separation Lock](SEPARATION_LOCK.md) is what keeps ordinary EVA inside the film. This file only requires the shell to walk alone.
- Shell adds thermal, dust, and abrasion cover. See Panels.
- Seat tolerance, orientation: the slipper seats with up to $0.2\,\mathrm{mm}$ of film at the plate face. Above that, or if the tag does not read, the shell walks alone. M0 confirms the number. [Separation Lock](SEPARATION_LOCK.md) is what keeps ordinary EVA inside it. The lock idles Mag-Path in that chamber for its cycle. The two do not share a driver.

The law is the same in slipper and shell. A crew member who must exit does not relearn the foot.

---

## Panels

The shell does not wait to be scrubbed, and it does not hot-swap a sole.

Every ablative panel on the shell, not only the sole, refuses the grain before it seats.

- **Repulsion.** A low field and a light acoustic tick in the panel stack. Charged fines are pushed off. Packed grains are kept from keying into the face. It runs during EVA. Intensity stays below what would fight path grip or pin a foot. In the lock, Mag-Path is idle, so the panels may run harder for the cycle, then drop.
- **Sweat.** A metered micro-film from the panel face, the same idea as the Separation Lock wall film. The grit cuts the film, not the panel. Worn film leaves in the lock wash and in the boot well. It is not a seep from a crack. It is not sprayed into the visor. Restored from a small reservoir in the suit. Not the path glycol. Not a cabin-air contaminant.
- **No disassembly.** No retractable sole. No replaceable pad. No internal shutter. A panel that cannot sweat isolates. The boot still walks.
- **Not the closer.** Repulsion and sweat cut the load. They do not promise a clean tread after a long EVA. [Separation Lock](SEPARATION_LOCK.md) wells finish the contact face. The $0.2\,\mathrm{mm}$ check is after the well.

Fail open. A panel field dies with power. It does not trap a foot. Untagged contact still does not harden the path.

---

## Materials and fill

One fill for every lot. The loop keeps the channel in band. Exterior lots are not a second chemistry unless M0 shows the loop cannot hold them.

### First-article fill

Propylene glycol and water, near $40/60$ by volume, with a dilute potassium acetate load for ionic conductivity.

- **Why this.** Low toxicity if a cabin joint weeps. Known freeze depression. High heat capacity. Compatible with common dielectric-elastomer skins. Not a research fluid.
- **Conductivity.** Enough for channel sensing and for the local return inside the sealed path. Not enough to invite corrosion. M0 sets the ceiling.
- **Freeze.** The $40/60$ mix stays liquid well below cabin temperature. The loop, not the mix, covers an exterior cold soak. If the loop cannot, that lot is off. It is not refilled with a harsher liquid in the field.
- **Vapor.** Low enough that a pinhole does not dump the channel into the cabin as a cloud. A weep is a wet joint, isolated, not an atmosphere event.

### Variable modes

The fill does not change. The loop mode does.

| Mode | Channel | Loop |
|------|---------|------|
| Idle | Soft, dark, no tag | Trickle, or stopped if the lot is emergency-off |
| Walk | Patch under the tag only | Slow recirculation, centimetres per second |
| Heat-feed | As walk | Tributary open to the cabin bus |
| Heat-reject | As walk | Tributary to the radiator path |
| Cold-hold | Soft | Loop holds the channel above freeze. No grip. A lot that cannot be held is isolated, not refilled |
| Emergency | Zero- $g$ bands, and only below half published spin | As heat-feed or heat-reject. Warmth is not the reason the lot is on |

### Skin, plate, tag

- **Skin.** Dielectric elastomer, silicone- or polyurethane-class, rated for the fill. Soft when idle. Stiffens in the patch under drive. A skin that swells, clouds, or cracks in the fill is a failed material, not a maintenance item.
- **Channel wall.** Laminated barrier. The liquid does not touch structure. A wall breach isolates that lot.
- **Sole interface.** Thin ferromagnetic stainless, or a plated polymer with a stainless face. Not bare iron. Not a metal that attacks the fill.
- **Tag.** Passive. No cell in the sole. Silent off the path.

### Refuse list

- Mercury, gallium alloys, or any liquid metal
- Strong acid, strong base, or ammonia
- A fill with high vapor pressure
- A fill that swells or embrittles the skin
- A field change of chemistry. One fill. A lot that cannot hold it is isolated
- An exterior “special” fill that the cabin crew cannot safely weep

M0-L is the materials card: soak, freeze, weep, conductivity, and skin mass change. It picks the acetate load and confirms $40/60$, or it publishes the nearest mix that passes. It does not open the refuse list.

---

## Grip law

Hard cling is refused. The patch draws, then eases, on the walker’s own phase.

**What the path and the sole see**

- Channel pressure under the contact: load, edge, and shift.
- Sole tactile and center-of-pressure arrays: lateral travel, heel–toe roll.
- Pair state: load arriving on the other foot.

Lateral intent is center-of-pressure travel. Vertical intent is unload rate. A shift onto the other foot plus a rising unload is the release cue. A planting contact with a falling center of pressure is the draw cue.

**Phases**

1. **Plant.** Tagged contact, load rising. Patch stiffens toward the draw band. The foot is seated, not locked.
2. **Stance.** Load stable. Patch holds in the walk band.
3. **Roll.** Pressure center travels. The unloading zone eases. The loaded zone holds.
4. **Release.** Unload crosses the threshold, or the other foot takes the load. Patch drops to free before the foot leaves.
5. **Swing.** No contact. That segment returns to soft and dark.

Predictive lead is one phase. The path reacts to the motion already in the foot. It does not commit the next step.

---

## Force bands

Orientation for a $75\,\mathrm{kg}$ crew member. M0 replaces them.

At the rim, $0.3\,g$ is $0.3 \times 9.81 = 2.94\,\mathrm{m\,s^{-2}}$. Weight is about $220\,\mathrm{N}$. One foot in stance carries about $110\,\mathrm{N}$. A deliberate lift on Earth exceeds $70\,\mathrm{N}$ without effort. The bands stay under that so a lift always wins.

### Zero- $g$ (spine, tether, gallery, exterior line)

| Band | Force | Intent |
|------|-------|--------|
| Free | $\le 8\,\mathrm{N}$ | Swing, or power-loss residual. Below lift-off of an unloaded boot |
| Walk | $25\text{–}40\,\mathrm{N}$ | Loose seat. A small push does not float the foot. A deliberate lift succeeds |
| Draw | $50\text{–}70\,\mathrm{N}$, decay to walk within one stance | Brief plant. Not a hold |

$40\,\mathrm{N}$ is the weight of about $4\,\mathrm{kg}$ on Earth. Noticeable. Not a trap.

### $0.3\,g$ disc

| State | Command |
|-------|---------|
| Published spin | **Off.** Emergency lots are neutral. They do not add force on top of rim weight |
| Emergency or spin-down, below half published spin | Zero- $g$ bands above. At $3.3\,\mathrm{rpm}$ that gate is $1.65\,\mathrm{rpm}$. The floor’s own weight is already falling. Do not stack |
| Any state | No band that prevents lift. No command above $70\,\mathrm{N}$ |

A lot that is on while the disc is still at published spin is a failure. The cap exists so a fault cannot pin a foot the floor is already holding. $30\%$ of one-foot rim load is about $33\,\mathrm{N}$. The walk band sits near that and does not exceed it while any rim weight remains. Draw is allowed only once spin is below the published fraction.

---

## Frequencies and the liquid path

Two channels. They do not share a tone.

### Grip and stiffening

- The patch is amplitude-shaped.
- Fundamental **$40\text{–}120\,\mathrm{Hz}$**. Slow enough for a foot. Fast enough to avoid cogging.
- 3rd and 5th kept below **$600\,\mathrm{Hz}$** and off any channel mode M0 measures.
- Only the segment under a tag runs. Adjacent segments stay soft.

### Acoustic link

The medium is a polymer skin over liquid, not a metal plate. A $40\,\mathrm{kHz}$ Lamb wave was the solid-strip guess. It is retired.

The planted sole is the coupler. The path is the wire. Two boots on the same continuous lot can exchange a short acoustic signal through that shared surface. A boot in swing is silent. A boot on another lot is silent unless a published coupler bridges the gap.

**First-article window**

- Attempt a guided tone in the skin/liquid stack, center **$20\text{–}40\,\mathrm{kHz}$**.
- If M0 finds no clean window there, pick the wall band **$2\text{–}8\,\mathrm{kHz}$**, which the sole arrays already read.
- M0 publishes one window. Both are not in service together.
- Grip harmonics stay out of that window. If a channel mode sits in it, move the center. Do not raise power to punch through a mode.
- Recirculation is slow. It does not wash out a kilohertz tone.

**What the circuit can carry**

Local, on one continuous path, between tagged soles that are planted.

- Identity confirm and “on path.”
- A distress bit. Local. It does not replace the suit radio.
- A lot-end chirp, so a walker knows the path stops.
- A short paired confirm between an enrolled left and right, or between a lead and a follower on the same lot.
- Later, a low-rate symbol stream: a heading cue, a hold, a “path ends.” Still not voice. Still not a file.

The signal is in the skin and the liquid under the feet. It does not need a radio hop between two crew on the same strip. It dies at an uncoupled joint, a gel-tile gap, or a lot end. That limit is the feature. A transmission cannot wander onto a deck that is not this path.

**What it cannot carry**

- Voice, on the first article or as a quiet upgrade. A voice channel is a different system.
- A file, a map, or a backbone. The path is not a data bus.
- Privacy. A body on the same continuous path can hear the tone. Say so on the suit checklist.
- Off-path reach. Swing is silent. A different lot is silent without a coupler.
- A trail. Tones are not retained as movement. The tag remains an address for the patch, not a tracker.

**Couplers**

A published coupler may bridge two lots. It is a joint in the channel, not a radio. Without it, the link ends. Couplers are named on the lot drawing. A builder does not assume continuity across a gap.

**Separation Lock**

The lock and the path are not in one ear. Lock pulses and the lock’s light acoustic shed stay off this window. During a lock cycle, Mag-Path in that chamber is idle, so the path circuit is quiet while the lock works.

The lock borrows the idea, not the circuit. After its shed it chirps its own floor, walls, and drain cartridges and matches the return to a published particulate library. A hazard class holds that lock’s inner hatch. Unknown is a result. The lock’s dust face is a metered gel film on a hard wall, so the grit does not cut structure. That film is a known library signature, not a path fluid. The sniff is a cycle result for the hatch count. It is not a tone on this path, and it is not a trail. See [Separation Lock](SEPARATION_LOCK.md).

This is a local surface telephone for feet on the same line. It is not a comms system, and it is not a log.

---

## Heat

A solid strip’s eddy loss is not the problem here. The losses are driver heat, liquid resistance under the patch, and EAP switching. They are low-grade.

The liquid is already a loop.

- Slow recirculation carries patch heat out of the lot.
- When the cabin loop wants warmth, the tributary may feed it. Foot contact and grip loss become a small internal gain instead of a local dump.
- When the cabin does not want heat, the same loop rejects to the ship’s ordinary radiator path.
- The path does not replace heaters. It is a recoverable tributary. Heaters remain the primary. A cold ship does not depend on people walking.
- Keep-out from RLC plates stands. This loop is not an RLC cassette and does not share an RLC driver. It may hand low-grade heat to the same cabin bus RLC already knows how to feed or to reject.

Unused heat is not scored as a failure. Forcing the path on to manufacture warmth is.

---

## Sensing, records, and the person

In the spirit of the *[Declaration of Cognitive Liberty](DECLARATION_OF_COGNITIVE_LIBERTY.md)* and the **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)**:

- Sole arrays and channel pressure exist to run the grip law. They are purpose-scoped to the step under the foot.
- Raw sole data stay on the boot unless the wearer affirms a share. The path does not copy them into a ship log.
- The tag is an address for the patch. It is not a tracker. Off-path, it is silent.
- The acoustic tone is not retained as a movement record. “On path” is a momentary confirm, not a trail.
- No secondary inference from gait into health, mood, or standing. That would be a harmony-class signal without a grant, and it is refused. See *[Predictive Harmony Metrics](PREDICTIVE_HARMONY_METRICS.md)*.
- A wearer may scope the optional confirm and the distress bit under *[Selective Ignorance](SELECTIVE_IGNORANCE.md)*. The grip law still runs. The link does not have to.
- Nothing here is a surveillance bus. A lot that stores a trail is an integrity failure under the **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)**.

Higher capability does not license a richer log. It raises the duty to keep the patch local and the record empty.

---

## Where it is used

| Place | Lot | Boot | Default |
|-------|-----|------|---------|
| Enterprise hub, tether, fore-stack gallery, Lock Node clean side | Interior path | IVA slipper | On, local enable |
| Space Dock spine, boom root | Interior or truss path | IVA slipper or EVA shell | On, local enable |
| Exterior walk lines | Exterior path | EVA shell, slipper seated if it will | On, local enable |
| $0.3\,g$ disc emergency | Spoke foot, airlock threshold, spin-down refuge | IVA slipper | **Off** until emergency or spin-down |
| Rim cabin floor | **None** | — | — |
| Spinning rim skin | **None** | — | — |
| Under live solar | **None** | — | — |
| Within $1.0\,\mathrm{m}$ of an RLC plate, or on an IRIS coil | **None** | — | — |

Emergency lots activate only when the disc is in a declared emergency or below the published spin fraction. Otherwise they are neutral. They are not a second floor.

---

## Further functions

Named. Not required for M0.

- **Buddy confirm.** “On path” between an enrolled pair. Not a locator.
- **Distress bit.** One reserved symbol. Local. Does not replace the suit radio.
- **Dust-shed tick.** Later, on the EVA sole, after [Separation Lock](SEPARATION_LOCK.md) has run. Not on the IVA slipper. Not a substitute for the lock.
- **Weak-side assist.** A slightly higher draw on a declared side. Crew-affirmed. Default off.
- **Lot-end chirp.** One tone at a path end.

Refused: grip as restraint, the link as a stealth intercom, emergency lots as ordinary floor, and walking the path to harvest heat.

---

## Failures

- Patch stays in draw or walk after a lift command.
- Power loss leaves a boot trapped.
- An open conductor or a current into the sole.
- Untagged contact hardens a segment.
- Emergency lot on during published spin.
- Grip tone read as an acoustic symbol, or the reverse.
- Path on a cabin floor, a spinning skin, under solar, or inside the RLC / IRIS keep-out.
- Shell that will not walk without the slipper.
- Acoustic link treated as private, or retained as a trail.
- Heat loop run as a reason to force traffic onto the path.

A failed lot isolates. Adjacent lots stay up. Isolation is elasticity, not abandonment. See the **[Architectural Elasticity Protocol](ARCHITECTURAL_ELASTICITY_PROTOCOL.md)**.

---

## Campaign M0

Bench, then a vacuum channel. M0 replaces every orientation number in this file. M0-L is the materials card inside it.

1. Show the skin holds the liquid. No exposed conductor. A contact does not complete a current into a sole.
2. M0-L: soak, freeze, weep, conductivity, skin mass change. Confirm $40/60$ propylene glycol–water with dilute potassium acetate, or publish the nearest mix that passes. Refuse list stays closed.
3. Map channel modes. Place grip harmonics off them. Pick **one** acoustic window: $20\text{–}40\,\mathrm{kHz}$ if it is clean, otherwise $2\text{–}8\,\mathrm{kHz}$. Publish the center. Do not fly both.
4. Tagged plant $\rightarrow$ stance $\rightarrow$ release. Forces inside the bands. A deliberate lift succeeds in every phase.
5. Untagged contact does not harden.
6. Kill the driver. The boot leaves. Residual under $8\,\mathrm{N}$.
7. Two tagged boots on one path exchange the confirm. A boot off the path does not. A gap without a coupler stops the tone.
8. Seat the slipper at $0.2\,\mathrm{mm}$ film. Above that, unseat it. The shell still walks.
9. Emergency lot stays off at or above half published spin ($1.65\,\mathrm{rpm}$ against $3.3$). It accepts zero- $g$ bands only below that gate.
10. Run the loop through idle, walk, heat-feed, heat-reject, and cold-hold. Show heat leaving the patch. Show a lot that cannot stay above freeze is isolated, not refilled.
11. Publish the bands, the center, the mix, and the seat number that survived.

M0 does not fly. It replaces the orientation numbers.

**What this file cannot finish**

Channel modes, the surviving acoustic center, the acetate load, lift-off residual on a real sole, and heat returned to a cabin bus. Those wait on the bench.

Separation Lock M0 may share the bench. The path card does not replace the lock card. See [Separation Lock](SEPARATION_LOCK.md).

---

## Relation to existing work

- [Enterprise](ENTERPRISE.md) — this file is MP-1. Interior spine, exterior walk lines, no cabin-floor paths, power-loss release, RLC and IRIS keep-out. Fail open, not IRIS-latched.
- [Separation Lock](SEPARATION_LOCK.md) — the EVA lock this path required. It keeps the seat inside $0.2\,\mathrm{mm}$. It idles Mag-Path in the lock for its cycle. No shared driver. A lock pulse is not a path draw. Harmonics stay apart. The shell still walks if the lock misses the film.
- [Jamline](JAMLINE.md) — same fail-open posture. Loss of jam is a soft line, not a trap. No shared driver. A line is not a walk path. A tick on the line stays off this band.
- [Secondary Wake](SECONDARY_WAKE.md) — heat is a tributary there as it is here. It does not size the article. No shared driver. A skirt is not a walk line.
- [Space Dock](SPACE_DOCK.md) — same kit on truss and boom root.
- [IRIS / MIDS](IRIS_MIDS.md) — no shared driver. A port may fail latched. A path fails open.
- [Regenerative Lattice Core](REGENERATIVE_LATTICE_CORE.md) — $1.0\,\mathrm{m}$ keep-out. Heat may join the cabin bus. The path is not a cassette.
- **[Architectural Elasticity Protocol](ARCHITECTURAL_ELASTICITY_PROTOCOL.md)** — a failed lot isolates. A dead path releases.
- **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)** — attachment and a short link only. Not a restraint, not a trail, not a heat-harvest pretext.
- *[Declaration of Cognitive Liberty](DECLARATION_OF_COGNITIVE_LIBERTY.md)* and **[Agency Interface Protocol](AGENCY_INTERFACE_PROTOCOL.md)** — sole data stay local. Tag is an address. Share is affirmed.
- *[Predictive Harmony Metrics](PREDICTIVE_HARMONY_METRICS.md)* — no gait-to-harmony inference.
- *[Selective Ignorance](SELECTIVE_IGNORANCE.md)* — confirm and distress may be scoped out. The grip law remains.
- *[Necessary Entropy](NECESSARY_ENTROPY.md)* — gait variance is preserved. One optimized cling is not the goal.

---

## Refuse

- Paths on the rim cabin floor
- An open charged surface or a current through the boot
- A field or a stiffness that traps a boot on power loss or against a lift
- Hard cling as the normal step
- Emergency lots on during published spin
- An audible cabin link, or voice on the first-article tone
- Shared driver with IRIS
- Path under live solar or on spinning rim skin
- Claiming the path link is private, or keeping it as a movement log
- Forcing traffic onto the path to harvest heat
- A retractable or replaceable sole
- A panel field that pins a foot

---

## Closing

Mag-Path is a sealed line that wakes under a tagged foot, not a gravity floor and not an open rail.

The rim already stands. The spine and the outer skin do not. The liquid feels the step. The skin stiffens only there, then eases. The boot is passive. The pair is two tags, not a suit. Heat that must leave the patch may warm a cabin that wants it, and may leave a cabin that does not. The slipper is the foot. The shell is the outside. Either walks. The foot is never the lock.

---

## License

Text of this document is released under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Implementation is invited under [The Call to Code](THE_CALL_TO_CODE.md).

This license covers the architecture and the campaign. It does not certify a flown boot, a filled channel, or a suited crew.
