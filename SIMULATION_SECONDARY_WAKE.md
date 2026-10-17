# Simulation Model of Secondary Wake
### *Collapse of a Coherent Trail, Skirt On and Skirt Off*
---
by **Bradford James Focht** (The Architect / Aspenth)  
*v1.0 - v1.1 — October 17th, 2026*<br>

---

## Purpose

This document is a runnable model of *[Secondary Wake](SECONDARY_WAKE.md)*. It gives state variables, an update, orientation parameters, and pass tests so a builder can simulate skirt-off against skirt-on before a burn.

It does not replace the theory. A simulation pass is not an M0 pass. M0 replaces every orientation number.

---

## Modeling goals

- Reproduce skirt-off against skirt-on on the four ratios and the harm line.
- Fail cleanly when the ring dies or the source needs the skirt.
- Keep the tributary and the acoustic coupon off the pass line.
- Stay orientation. A burn replaces the rates.

---

## State

At step $k$, for a source that is on or off:

| Symbol | Meaning |
|--------|---------|
| $L_k$ | Core length |
| $A_k$ | Area above the published floor |
| $T_k$ | Peak core temperature |
| $\tau_k$ | Time for the core to fall below the floor after a stop, or time-to-$\Lambda$ on a steady burn |
| $q_k$ | Heat flux or radiance at standoff $d$ |
| $n_{\mathrm{live}}$ | Mixers still in the ring |
| $P_k$ | Tributary watts, if a skin is fitted |

Skirt state is a flag: off or on. A killed mixer decrements $n_{\mathrm{live}}$.

---

## Update

One step is one published interval $\Delta t$. Orientation $\Delta t = 1\,\mathrm{s}$.

With the source burning, skirt off:

$$
L_{k+1} = L_k, \quad A_{k+1} = A_k, \quad T_{k+1} = T_k
$$

A steady uncontrolled core holds. It does not collapse by itself in this model.

Skirt on, source burning, $n_{\mathrm{live}} \ge n_{\min}$:

$$
\begin{aligned}
L_{k+1} &= L_k - c_L\,\phi\,\frac{n_{\mathrm{live}}}{n}\,\Delta t \\
A_{k+1} &= A_k + c_A\,\phi\,\frac{n_{\mathrm{live}}}{n}\,\Delta t \\
T_{k+1} &= T_k - c_T\,\phi\,\frac{n_{\mathrm{live}}}{n}\,\Delta t
\end{aligned}
$$

$c_L$, $c_A$, $c_T$ are orientation rates. They are not physics constants. Floors: $L \ge L_{\min}$, $T \ge T_{\mathrm{amb}}$. $A$ does not shrink while the skirt is on.

If $n_{\mathrm{live}} < n_{\min}$, the skirt is treated as off. The core holds. That is a failed ring, not a collapse.

Source stops at step $k_s$. Then, skirt on and ring live:

$$
\tau = k_{\mathrm{floor}} - k_s
$$

where $k_{\mathrm{floor}}$ is the first step with $T_k$ below the published floor. Skirt off uses the same clock. A pass needs $\tau_{\mathrm{on}} < \tau_{\mathrm{off}}$.

Harm at published $d$, orientation:

$$
q_k = q_0\,\frac{L_k}{L_0}\,\left(\frac{T_k}{T_0}\right)^{4}\,\frac{d_0}{d}
$$

$q$ falls if the core shortens and cools. A rise fails the harm line.

Tributary, if fitted:

$$
P_k = \eta\,c_Q\,(T_k - T_{\mathrm{skin}})
$$

$P_k$ is reported. It is not a pass line.

Continuous form, same law, for a solver that prefers it:

$$
\frac{dL}{dt} = -c_L\,\phi\,\frac{n_{\mathrm{live}}}{n}, \quad
\frac{dA}{dt} = c_A\,\phi\,\frac{n_{\mathrm{live}}}{n}, \quad
\frac{dT}{dt} = -c_T\,\phi\,\frac{n_{\mathrm{live}}}{n}
$$

while the source burns and the ring is live. Skirt off: all three derivatives are zero.

---

## Worked step

Orientation, one second, skirt on, ring full, $\phi = 0.6$, $n_{\mathrm{live}}/n = 1$.

$$
\begin{aligned}
\Delta L &= -2.0 \times 0.6 = -1.2\,\mathrm{m} \\
\Delta A &= 3.0 \times 0.6 = 1.8\,\mathrm{m}^{2} \\
\Delta T &= -40 \times 0.6 = -24\,\mathrm{K}
\end{aligned}
$$

From the worked posture, about eighteen such steps land near $L = 18\,\mathrm{m}$, $A = 55\,\mathrm{m}^{2}$, $T = 1100\,\mathrm{K}$. That is a shape check. It is not a calibration.

---

## Orientation parameters

From the theory’s worked posture and bands. Not pass lines.

| Name | Value |
|------|-------|
| $L_0$ | $40\,\mathrm{m}$ |
| $A_0$ | $20\,\mathrm{m}^{2}$ |
| $T_0$ | $1800\,\mathrm{K}$ |
| $\tau$ off | $12\,\mathrm{s}$ |
| $\phi$ | $0.6$ |
| $n$ | $8$ |
| $n_{\min}$ | $4$ |
| $d$ | $15\,\mathrm{m}$ |
| $\eta$ | $0.04$ |
| $c_L$ | $2.0\,\mathrm{m\,s^{-1}}$ |
| $c_A$ | $3.0\,\mathrm{m}^{2}\,\mathrm{s^{-1}}$ |
| $c_T$ | $40\,\mathrm{K\,s^{-1}}$ |

Rates are chosen so a short run lands near the worked posture. A bench replaces them.

---

## Scenarios

1. **Skirt off, steady.** $L$, $A$, $T$ hold. This is the denominator.
2. **Skirt on, ring live.** $L$ falls, $A$ rises, $T$ falls. Compute $\Lambda$, $\alpha$, $\theta$.
3. **One mixer killed.** $n_{\mathrm{live}} = 7$. Collapse continues. Source still “runs.”
4. **Ring below minimum.** $n_{\mathrm{live}} = 3$. Skirt counts as off. Card fails.
5. **Skirt isolated.** Source still runs. If the model requires the skirt flag to keep the source on, the card is zero.
6. **Shutdown clock.** Source stops. $\tau_{\mathrm{on}} < \tau_{\mathrm{off}}$ or the pass fails.
7. **Harm.** $q_{\mathrm{on}}(d) < q_{\mathrm{off}}(d)$ at $15\,\mathrm{m}$.
8. **Atmosphere and vacuum.** Same update. Vacuum uses a larger $c_A$ and a smaller $c_T$ contact term, published per instance. Do not average a pass and a fail.
9. **Acoustic coupon.** A harvester term may add watts. Killing it does not change $\Lambda$, $\alpha$, $\theta$, or $\tau$.

---

## Pass test

$$
\Lambda < 1,\;\alpha > 1,\;\theta < 1,\;\tau_{\mathrm{on}} < \tau_{\mathrm{off}},\;q_{\mathrm{on}} < q_{\mathrm{off}}
$$

and the source flag stays on when the skirt flag is off, and $n_{\mathrm{live}} \ge n_{\min}$ is not required for the source to run.

A lower $S \propto A T^{4}$ is printed. It is not the test.

---

## What this model refuses

- A solid shroud ($\phi = 0$) counted as a collapse
- Averaging atmosphere and vacuum
- Treating $P_k$ as a pass
- A baffle between the trail and the recorded $q$
- Citing the residual layer as a source term

The layer is the sink. It is not in the update as a fuel.

---

## Success criteria

A reference run on the orientation parameters produces a pass shape near $\Lambda \approx 0.45$, $\alpha \approx 2.8$, $\theta \approx 0.6$, with $\tau$ down and $q$ down, and fails cleanly when the ring drops below $n_{\min}$ or the source flag depends on the skirt.

Agreement with a later burn is not claimed. The burn replaces the rates.

---

## Adversarial checks

- A solid shroud ($\phi = 0$) produces no collapse. Counting it as a pass fails the check.
- Averaging an atmosphere pass and a vacuum fail fails the check.
- A run that needs the skirt flag to keep the source on is a zero card.
- A baffle that lowers recorded $q$ without lowering $L$ and $T$ fails the check.
- A tributary term added into $\Lambda$ fails the check.
- Citing a layer source term fails the check. The layer is not in the update as a fuel.

---

## Implementation notes

State is a small struct. Skirt flag, source flag, $n_{\mathrm{live}}$. One function steps it. Print $\Lambda$, $\alpha$, $\theta$, $\tau$, $q$, and $S$. Do not print a pass on $S$. Seed nothing. The orientation parameters are the scenario. A later code file ships under Apache-2.0 or MIT. This document does not.

---

## Open modeling questions

- Is the linear rate enough, or does collapse need a core-fraction term?
- Shutdown clock or time-to-$\Lambda$ on a steady burn?
- How should vacuum differ from atmosphere beyond a larger $c_A$?
- Does a thermoelectric skin belong in the thermal derivative at all?

---

## Closing

This model is a bench before the bench. It shows the shape of a pass and the shape of a cheat. It does not fly, and it does not replace M0.

---

## Relation

Implements *[Secondary Wake](SECONDARY_WAKE.md)*. Does not modify it. A campaign card may cite a run. A run may not cite itself as M0.

Runner: [`simulations/secondary_wake_sim.py`](simulations/secondary_wake_sim.py). Apache-2.0. No dependencies beyond Python 3.

```bash
python3 simulations/secondary_wake_sim.py
```

Clone the repository, or open the file from GitHub and save it, then run that command in the folder that contains `simulations/`. Do not paste the script into a page. The file is the source. A page that copies it will drift.

### Orientation run

Not an M0 result. Reference instance, eighteen steps:

| | Off | On |
|--|-----|-----|
| $L$ | $40\,\mathrm{m}$ | $18.4\,\mathrm{m}$ |
| $A$ | $20\,\mathrm{m}^{2}$ | $52.4\,\mathrm{m}^{2}$ |
| $T$ | $1800\,\mathrm{K}$ | $1368\,\mathrm{K}$ |
| $\tau$ | $24\,\mathrm{s}$ | $9\,\mathrm{s}$ |

$\Lambda = 0.46$, $\alpha = 2.62$, $\theta = 0.76$, harm ratio $0.15$. Pass shape. Atmosphere and vacuum are printed separately and not averaged. A shroud and a dead ring do not collapse.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

Reference implementations and software derived from this model should use Apache-2.0 or MIT. This document does not.
