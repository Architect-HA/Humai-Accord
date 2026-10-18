# Stormcrashers — Mars
### *Atmospheric Mitigation for a Thin Carbon-Dioxide Sky*
---
by **Bradford James Focht** (The Architect / Aspenth)  
*v1.0 - v1.6 — October 18th, 2026*<br>

---

## Purpose

This document is the Martian sibling of *[Stormcrashers](STORMCRASHERS.md)*. It specifies two parent articles for a thin, dusty, carbon-dioxide atmosphere: a dustbreak mast and a pad fence. Shelter is still an array property. A single unit is not a storm switch.

It is an architecture and a campaign. It is not a stamped set, not a terraforming plan, and not a stealth kit.

It follows the [Humai Accord](README.md), including *[Stormcrashers](STORMCRASHERS.md)*, *[Atmospheric Restoration](ATMOSPHERIC_RESTORATION.md)*, the **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)**, the **[Architectural Elasticity Protocol](ARCHITECTURAL_ELASTICITY_PROTOCOL.md)**, and [The Call to Code](THE_CALL_TO_CODE.md).

---

## Scope and Limits

**In scope**

- A porous mast that sheds dust-laden wind around a pad, a hab lane, or a crane
- A low porous fence that does the same job as a line, counted as kits
- Foundations, abrasion, electrostatics, and a first campaign in a density-matched flow with a dust coupon
- Orientation bands. M0 replaces them

**Out of scope**

- Raising the planetary atmosphere. That is *[Atmospheric Restoration](ATMOSPHERIC_RESTORATION.md)*
- A solid wall as the article
- Earth coastal pylons, flumes, or biofouling packages copied onto regolith
- A claim that one mast calms a global dust storm
- Dual-use steering of dust onto a neighbor

A failed unit isolates. The array stays up.

---

## The sky this file is for

Mars is not a thin Earth.

- Surface pressure is about $0.6\,\mathrm{kPa}$, under one percent of Earth. The gas is mostly carbon dioxide, about $95$ percent, with a little nitrogen and argon.
- Density is about $0.020\,\mathrm{kg\,m^{-3}}$. Dynamic pressure at $30\,\mathrm{m\,s^{-1}}$ is on the order of $9\,\mathrm{Pa}$. The same speed on Earth is hundreds of pascals. Force is not the design driver. Abrasion and visibility are.
- Gravity is about $3.71\,\mathrm{m\,s^{-2}}$. A mast may be taller for the same base moment, and a fence may be lighter. Dust still settles, and it settles charged.
- Dust is fine, sharp, and often electrified. Global and regional storms move it. A quiet day still carries fines.
- Temperature swings are large. A published surface band for this file is $-120\,^{\circ}\mathrm{C}$ to $+30\,^{\circ}\mathrm{C}$, orientation, wider at the poles and on a bad night. Carbon-dioxide frost is a polar and seasonal fact. It is not a coastal tide. Every article is designed for that swing. A part that cannot take it isolates. It does not take the mast with it.

Earth wind-tunnel numbers do not transfer. A Mars article is tested in a density-matched flow, with a dust coupon, or it is not tested.

---

## Core principles

1. **Porosity first.** Dissipate the dusty stream. Do not dam it. A solid face loads with fines and then fails as a dune.
2. **Shelter is an array.** One mast protects a pad. A line protects a lane. A belt is a later count. None of these is a regional climate machine.
3. **Name the leftover.** Dust that the article does not catch is a published remainder path, in the spirit of [Gulpgates](GULPGATES.md). It is not “the wind took it.”
4. **Abrasion is the life.** The face that wears is the face you meant to replace. Structure behind it is not the wear surface.
5. **Fail quiet.** Power loss does not turn a fence into a wall and does not aim a jet. Passive porosity is the default.
6. **Protective only.** Under the **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)**. No steering of dust onto a neighbor. No experiment rides on the mast.

---

## What one unit can honestly do

A single mast, in a density-matched campaign, can:

- Cut wind speed and dust flux in a published wake, on the order of a few mast-heights downwind, for a pad or a crane
- Keep that wake from becoming a dune against the hab
- Publish the dust it did not catch

It cannot:

- Stop a global dust storm
- Clear a landing ellipse by itself
- Replace a suit or a [Separation Lock](SEPARATION_LOCK.md)
- Be cited as a reason the sky is safe to breathe

---

## Article M-A — Dustbreak mast

### Stack

```
40 m     porous tip, sensor, replaceable abrasion coupons
30 m     light truss, cable stays
 0 m     regolith-ballast or piled footing, utility trunk
−1 to −3 m   footing or screw piles in competent ground
```

Forty metres, not one hundred. Dynamic pressure does not ask for an Earth tower. Height is for the wake, not for the moment. A later on-site article may grow. The first article does not.

### Layer 1 — Footing

**Function.** Hold the mast against a small overturning load and against thermal cycling. Provide a bond path for charge.

- Screw piles, a ballast ring, or a short drilled group. Working depth is site-specific and shallow compared with an Earth tower. Regolith bearing is not assumed. M0 publishes it.
- No Earth splash zone. No sulfate-marine package. The enemy is fines in the joints and a thermal crack.
- Charge: a bond from tip to footing to a published ground stake. Carbon stays off that path.

### Layer 2 — Lower mast (0–30 m)

**Function.** Spine, utility trunk, access.

- A lattice or a thin shell in a published alloy or in on-site sintered regolith for a later article. First article may be flown metal.
- Joints are dust-tolerant: covers, not open bearings. A joint that packs with fines is a failed joint.
- No occupied cabin. Inspection is suited or remote, below a published wind and dust lockout.

### Layer 3 — Tip (30–40 m)

**Function.** The porous face. This is the article.

- Open area fraction $\phi$ in the orientation band $0.4\text{–}0.7$. A solid tip is refused.
- Replaceable abrasion coupons on the windward face. The coupon wears. The truss does not.
- Optional light Coandă or pulsed bleed, gated, duty-limited, and off on power loss. Not required for the first article.
- Sensor: wind, dust flux, charge. Local. Does not wait on Earth.

### Optional recovery

A small turbine in a duct is a tributary. Mars dynamic pressure is low. Do not size the mast to make watts. If a unit is fitted, publish watts against mass. A recovery that does not beat its mass is refused. Same posture as [Secondary Wake](SECONDARY_WAKE.md): recovery does not size the article.

---

## Article M-B — Pad fence

### Role

The line. A counted row of low porous panels upwind of a pad, a ramp, or a hab door. This is the coastal article translated: no water, no biofouling, a fence instead of a pylon.

### Stack

```
3–6 m    porous panel, replaceable face
0 m      ballast or short pile, dust apron
```

### Working face

- Same $\phi$ band as the mast tip. Repeating coupon. Punchable or sintered. Not a one-off fractal that cannot be replaced.
- Apron at the foot so a dune does not bury the panel. The apron is part of the article.
- Panels are independent. One buried panel is a remainder. The line still stands.

### What it is not

Not a pressure wall. Not a suitport. Not a [Separation Lock](SEPARATION_LOCK.md). Crew still use the lock. The fence cuts the load the lock then finishes.

---

## Dust face

Abrasion and buildup are the life of both articles. The mitigation is local, mostly passive, and cheap when it is active. It does not size a power plant.

**Order.** Natural and passive first. Active only for what those leave.

1. **Let the wind work.** Porosity is the shed. A stream that passes does not pack a face the way a solid berm does. The apron keeps a dune off the foot. No energy.
2. **A face that does not hold.** The coupon is the wear surface and the low-adhesion surface. A published low-surface-energy coat, or a sintered face M0 shows sheds fines, on the windward coupon only. Not on the truss. Not on the footing. Localized.
3. **A film, not a grind.** The coupon may carry a metered film. The grit cuts the film, not the coupon. This is not a water sweat. Mars will take a water film. Pressure is about $0.6\,\mathrm{kPa}$, the air is dry carbon dioxide, and a water coat sublimes or evaporates on a short clock. Wind will not peel a film. Dynamic pressure is too small. Drying will.

   The film is a low-volatility coat: a published glycol, a silicone oil, or a gel M0 shows survives a Mars-pressure, dry-CO₂ coupon test. A humectant or a thickener is permitted if it keeps the coat on the face without making a paste that holds dust. Water as the carrier is refused.

   It is metered onto the windward coupon only, in pulses, on a dust event or on a published interval. Not a standing wet mast. Not a seep from a crack. Not sprayed at a visor or a hatch. Worn film leaves in the wind or is renewed from a small local reservoir. The reservoir is kept above the film’s freeze point, or the film is one that stays mobile through the published night swing. A frozen line is a failed film, not a failed mast. A coupon that cannot renew isolates. The mast still stands. A dry coupon is still a porous coupon. The film is a life extender, not the article.
4. **Charge has a path.** The bond from tip to footing to stake is the electrostatic shed. Martian fines are charged. A floating face holds them. A bonded face gives the charge somewhere to go. No energy beyond the bond itself.
5. **A sacrificial collector for the magnetic fraction.** Some fines are magnetic. A small replaceable magnetic coupon, off the structural face, is allowed to hold them so the mast does not. It is emptied or swapped on the same interval as the abrasion coupon. Passive. Not a sweeper.

**Active, duty-limited.** What the five above leave may be shaken or pulled, briefly.

- **Acoustic tick.** A short, low-energy pulse in the coupon stack, the same posture as a Mag-Path panel tick. Not a cabin tone and not a continuous drive. It unsticks packed fines so the wind can take them. It does not blow the dust. Window published, and kept off any Mag-Path band if a path is anywhere near. No shared driver. Off on power loss.
- **Magnetic pulse.** A short gradient on the sacrificial collector, not on the truss, to gather the magnetic fraction the passive coupon missed. Duty-limited. Off on power loss. Not a field that pins a boot or a tool.
- **A sniff, optional.** A short chirp on the coupon, matched to a published dust library, the way Separation Lock sniffs its own surfaces. A hazard class is a maintenance flag. Unknown is a result. It is not a cleaner and not a pass line. Not the Mag-Path circuit.

**Not the closer.** The face cuts the load. It does not promise a clean mast after a storm. [Separation Lock](SEPARATION_LOCK.md) still finishes a suit. A mast is not a reason to skip it.

**Energy.** Each active coupon publishes watt-hours per event and events per sol. A coupon whose campaign return does not beat doing nothing, on that duty, is refused. Shelter does not depend on a tick, a pulse, or a film pump. A dead face leaves a porous, bonded coupon. That coupon is still the article.

**Not claimed.** An electrodynamic shield. A clean structure. A reason to skip the suit or the lock. A cleaner wake is not a clean mast.

---

## Array doctrine

Shelter is counted.

| Pattern | Count | Honest claim |
|---------|-------|----------------|
| Point | 1 mast | A pad or a crane. First article |
| Line | fence kits | A lane or a door approach |
| Belt | mast line + fence | A hab cluster. Later |
| Regional | — | Not this file |

Spacing is published from the wake, not from a drawing. M0 sets it. Do not claim a city of shelters from one campaign.

Growth is point, then line, then belt. A ring or a polar frost collar is a later question. It is not an article here.

---

## Bill of materials and substitution grades

The article is porosity, a replaceable face, and a named remainder. Alloys and toolpaths that keep those three are permitted. They are not required.

### M-A mast

| Item | Grade 1 — first article | Grade 2 — permitted | Not required |
|------|-------------------------|---------------------|--------------|
| Tip coupons | Flown alloy sheet, punched, replaceable | Polymer-composite coupon | NiTi, five-axis wet face |
| Film, if any | Pulsed low-volatility coat on the coupon | Glycol, silicone, or gel that survives the Mars-pressure test | A water carrier. A standing wet mast |
| Truss | Flown metal lattice | Thin shell | On-site sinter, until a yard exists |
| Footing | Screw pile or ballast ring | Short drilled group | Earth marine caisson |
| Sensors | Flown, local | Same | An Earth-linked control loop |
| Bleed, if any | Gated, off on power loss | — | Required for a pass |

### M-B fence

| Item | Grade 1 | Grade 2 | Not required |
|------|---------|---------|--------------|
| Panel | Repeating punched coupon | Sintered coupon if M0 says it wears evenly | A one-off fractal face |
| Apron | Local fill or a flown mat | — | A single buried outlet |
| Bond | Stake per bay | — | A floating panel |

Quote Grade 2 and any NiTi as their own line. Do not bury a premium in the prototype band and then treat the band as a procurement number.

---

## Campaign M0

Density-matched flow, then dust. Earth sea-level wind is not a Mars test. Under [Process-Reward Alignment](PROCESS_REWARD_ALIGNMENT.md), a skipped density match zeros the card. A pretty wake from a sea-level tunnel does not wash that miss.

**Match.** Dynamic pressure within $20$ percent of a published Mars case, or density within that band with speed adjusted. Publish the match. A tunnel without that note is a failed card.

**Simulant.** A published Mars soil simulant, size band stated, charge state stated if electrostatics are claimed. An unnamed dust is not a coupon.

**Matrix.**

| Case | What is in the flow | Pass |
|------|---------------------|------|
| Solid control | Same outline, $\phi = 0$ | Run, then refuse as the article |
| Porous tip | $\phi$ in $0.4\text{–}0.7$ | Wake speed ratio $0.5\text{–}0.8$ at $3$ heights |
| Dust on porous | Simulant, published dose | Flux ratio at $3$ heights preferably below the speed ratio |
| Pore-close | Same coupon after the dose | $\phi$ still in band. A closed face fails |
| Film, if fitted | Mars-pressure, dry CO₂, night swing | Coat survives the test. A dry coupon still passes shelter |
| Power kill | Bleed and ticks on, then off | Porosity remains. No jet. Not a wall. Face still bonded |
| One down | Line of three, middle isolated | The other two still stand |

Wake is reported at $1$, $3$, and $5$ characteristic heights. A photo is not a pass. Spacing for a later line comes from this wake, not from a drawing.

M0 does not fly. It replaces the orientation numbers.

**What this file cannot finish**

Site bearing, the surviving $\phi$ after a surface season, coupon life in a real storm, and belt spacing. Those wait on the bench and on a surface campaign.

---

## Assembly sequence

**Mast**

1. Footing and bond stake. Bond checked before the trunk is called done.
2. Trunk, bays as shipped. Joint covers on before the next bay.
3. Tip ring.
4. Coupons last, so a yard can replace them without dropping the mast.
5. Sensors. Local lockout tested.
6. Bleed, if fitted, tested off on power loss.

**Fence**

1. Apron, continuous enough that a dune cannot start in a gap. Not a single buried outlet. Remainder leaves at published ends or at a ring of gaps, in the [Gulpgates](GULPGATES.md) sense.
2. Panels, independent. A panel that cannot be lifted off is a failed panel.
3. Bond per bay.
4. One panel isolated on purpose. The line still stands.

No occupied work at height in a dust event. Suited or remote only, below the published lockout.

---

## Instrumentation and calibration

Minima, or the campaign is not a campaign.

- One upwind wind and dust-flux instrument, one in the wake at the published station
- Coupon mass and open area on a published interval
- Charge at the tip and at the footing, with the bond path in the circuit
- A lockout that trips locally. It does not wait on Earth

A reading without a published method is not a result.

**Dual metric, if recovery is claimed.** Publish watts and the harvester mass over a published duty. Shelter is still the pass. A recovery that does not beat its mass fails the coupon and does not fail the shelter card. Same split as [Secondary Wake](SECONDARY_WAKE.md).

---

## Thermal envelope

Every part sees the swing. The band is $-120\,^{\circ}\mathrm{C}$ to $+30\,^{\circ}\mathrm{C}$, orientation. M0 replaces it with the site’s own night and day. A part outside its published range isolates. The mast still stands. The fence still stands.

| Part | Cold | Heat | If it cannot |
|------|------|------|----------------|
| Truss and footing | Stay ductile. No brittle joint | No creep, no seized cover | Isolate the bay. Do not drop the mast |
| Coupons | Stay porous. Frost is a life issue, not a mode | No warp that closes $\phi$ | Swap the coupon. Structure is not the wear face |
| Film reservoir | Above the film’s freeze point, or a film that stays mobile | No boil-off at $0.6\,\mathrm{kPa}$ | Film fails. Coupon remains. Shelter remains |
| Bond path | Continuity at the cold end | Continuity at the hot end | A floating tip is a failed tip |
| Sensors and lockout | Local. Do not wait on a warm start from Earth | Same | Lockout fails safe. Porosity remains |
| Joint covers | Do not crack and admit fines | Do not gap and admit fines | A packed joint is a failed joint |

Carbon-dioxide frost on a coupon is expected at the cold end of the band. It is brushed or it sublimes. It is not a reason to heat the mast. Resistive heat is permitted on the film reservoir and on a sensor, duty-limited, and published in watt-hours. It is not permitted as a mast heater. A warm mast is not the article.

---

## Safety envelopes

**Structural.** Published Mars gust, and the thermal band above. Do not import an Earth 50-year wind or an Earth temperature.

**Dust.** The wake is cleaner, not clean. [*The Residual Cycle*](THE_RESIDUAL_CYCLE.md) applies: dust in the wake is a residue. A cleaner wake is not a clean sky. Suits and [Separation Lock](SEPARATION_LOCK.md) remain.

**Charge.** Bond from tip to footing to stake, tested. A floating tip is a failed tip. Carbon stays off the bond path.

**Human.** No cabin. Wind and dust lockout published. No occupied height during a lockout.

**Cyber.** Authenticated local command. Fail-safe does not wait on Earth.

**Utilization.** Protective dissipation only, under the **[Utilization Integrity Protocol](UTILIZATION_INTEGRITY_PROTOCOL.md)**. No steering onto a neighbor. No experiment on the mast.

---

## Cost and logistics

Orientation only. Not a bid. Freight dominates. Do not quote an Earth concrete tower.

| Stage | What is bought | What moves the band |
|-------|----------------|---------------------|
| M0 | Density-matched flow, dust coupon, siting note | Chamber time and simulant, not steel |
| M-A1 | One flown mast, replaceable tip | Launch mass. Coupons are a small line |
| M-B1 | A short fence, counted panels, apron | Panel count and apron, not a wet face |
| Later on-site | A yard-built mast | A different band. Do not quote it as the first |

Grade 2 and any NiTi are their own lines. A later wet Article B is not in these bands.

---

## Transfer package

What leaves this file for a builder:

- The two articles, the $\phi$ band, the substitution grades, and the thermal band
- The M0 matrix and the density-match rule
- The refuse list
- A statement that Earth wind numbers and Earth temperatures do not transfer, and that Article B waits on standing water

What does not leave: a city-scale claim, a terraforming claim, a stealth claim.

---

## Worked orientation

Not a measurement.

A $40\,\mathrm{m}$ mast, $\phi = 0.55$, density-matched flow at $30\,\mathrm{m\,s^{-1}}$. Dynamic pressure about $9\,\mathrm{Pa}$. Wake at three heights: speed ratio in the band $0.5\text{–}0.8$, dust-flux ratio preferably lower than the speed ratio if the pores catch fines. A solid mast of the same height is the control and is not the article.

M0 replaces every figure.

---

## Environmental siting

- Not in a dune corridor unless the apron and the remainder path are published
- Not as the only dust control for a hab door
- Not on a basin *[Atmospheric Restoration](ATMOSPHERIC_RESTORATION.md)* has marked for survey-before-seed, unless that page clears the siting
- Polar frost is a siting fact. A collar of frost on a coupon is a life issue, not a mode
- Keep-out from a [Regenerative Lattice Core](REGENERATIVE_LATTICE_CORE.md) plate and from an [IRIS](IRIS_MIDS.md) face, $1.0\,\mathrm{m}$, until a map says otherwise
- A retired or dust-buried unit may enter a heartwood-analogue hold under the **[Circulation Recovery Protocol](CIRCULATION_RECOVERY_PROTOCOL.md)**. It is not scored as simple under-use. See **[Architectural Elasticity Protocol](ARCHITECTURAL_ELASTICITY_PROTOCOL.md)**

---

## Later water

Earth Article B, the coastal pylon, is not copied onto today’s Mars. It becomes available when *[Atmospheric Restoration](ATMOSPHERIC_RESTORATION.md)* has standing water and a rain cycle. That is a generational fact, not a first-article mode.

When that day comes, the Earth stack scales. It is not used unchanged.

- **Density still low.** Even a thicker later sky is not Earth’s. Dynamic pressure stays a published Mars number. Do not import an Earth 50-year wind.
- **Dust does not leave.** A rain cycle washes some fines and moves others. A wet face still sees abrasive dust between storms and in the splash. The abrasion coupon stays. A marine alloy does not retire it.
- **No Earth biology.** Biofouling is an Earth package. A Martian wet face gets a dust-and-frost package until a real ecology exists. Do not specify a barnacle coat for a world that does not have one.
- **Frost and brine.** Polar and seasonal carbon-dioxide frost, and any brine a later sea throws, are siting facts. Joints that pack with fines or freeze shut are failed joints. Covers stay.
- **Foundations.** Regolith, ice-rich ground, and a new shoreline are not a terrestrial seabed. The pile or the caisson is re-sized. The Earth depth band does not transfer.
- **Remainder.** A wet face still names the dust and the sediment it does not catch. A rain cycle is not a reason to drop the remainder path.
- **Campaign.** A later B-Mars card is a density-matched wet test plus a dust coupon. An Earth flume pass is not a Mars pass.

Until standing water exists, M-A and M-B are the articles. The coastal machine waits. Writing it now as a current article would pretend the sky has already changed.

---

## Naming and family position

**Stormcrashers — Mars** is the sibling.  
**Dustbreak** is Article M-A.  
**Pad fence** is Article M-B.

*[Stormcrashers](STORMCRASHERS.md)* remains the Earth parent. This file does not rewrite it and does not inherit its coastal article.

[Gulpgates](GULPGATES.md) supplies the remainder rule. [Atmospheric Restoration](ATMOSPHERIC_RESTORATION.md) is the sky-raising sibling, not this job. [Secondary Wake](SECONDARY_WAKE.md) is a trail article. A mast is not a skirt.

---

## Refuse

- A solid wall or a solid tip
- Earth sea-level data cited as a Mars pass
- One mast claimed against a global storm
- Steering dust onto a neighbor
- Recovery that sizes the article
- A cabin at height
- Skipping the suit and the lock because the wake “looked clean”
- Treating Earth Article B as a current Martian article before standing water and a rain cycle exist
- Importing an Earth flume pass, an Earth wind, or an Earth biofouling package onto Mars
- A sea-level tunnel cited as a density-matched pass
- A floating tip
- An active tick or pulse that the article needs in order to be porous
- A continuous acoustic or magnetic drive
- A mast heater as the way a joint survives the night
- A part outside the thermal band that takes the mast with it
- An apron that is a single buried outlet

---

## Closing

Mars does not need a taller Earth tower. It needs a porous face that survives fines, a count of units that matches the pad, and a campaign in the right density. Shelter is still an array. Leftover dust is still a remainder. The sky is still the sky.

Further development, formalization, and testing are invited.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, even commercially, provided appropriate attribution is given, a link to the license is provided, and any changes are indicated.
