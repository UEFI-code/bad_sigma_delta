# BAD SIGMA-DELTA

> "what if we implement sigma-delta modulation with pure bad decisions"

An extremely cursed sigma-delta-ish experiment written in Python.

It is mathematically suspicious.

It is emotionally unstable.

It somehow converges anyway.

## WHAT IS THIS

This repo contains a tiny fake-looking sigma-delta modulator built from:

- accumulated error
- vibes
- clamping
- raw confidence

There is no DSP purity here.

Only a screaming feedback loop trying to approximate energy levels with progressively more deranged bit patterns.

And somehow:

```
it. keeps. working.
```

## FEATURES

- Zero optimization
- Dubious stability
- Questionable control theory
- Debug output that reads like a medical monitor
- Generates bytes that look increasingly concerned

## DEMO

```bash
python3 demo.py
```

or, if you want the slightly more self-aware version:

```bash
python3 demo2.py
```

Sample output:

```text
Last equ energy: 0.243, Error sum: -0.010, Energy sigma bits: 0, This high bits: 3, This equ energy: 0.375
Byte value: 00000111
```

## SERIAL PORT AUDIO MODE

Yes.

THIS THING CAN SCREAM THROUGH A SERIAL PORT.

No DAC.
No amplifier.
No dignity.

```bash
python3 play.py
```

`play.py`:

- generates a 440Hz sine wave
- feeds it into the cursed sigma-delta loop
- converts the resulting bit density into byte patterns
- violently attempts to stream them over UART

Current setup target:

```python
serial.Serial('/dev/ttyUSB0', 115200)
```

Then:

- connect TX directly to a headphone if you fear nothing
- or connect it to a MOSFET
- or connect it to literally whatever conductive object is nearby

And eventually:

```text
WWWWWWWWWWWWWWWWWWWWWWW
```

You will hear a horrible electronic roaring noise.

Not clean audio.

Not signal reproduction.

Just raw sigma-delta panic converted directly into violence on a wire.

Observed waveform fragments:

```text
Byte value: 00000001
Byte value: 00000011
Byte value: 00001111
Byte value: 00001111
Byte value: 00001111
Byte value: 00000111
Byte value: 00000001
Byte value: 00000001
Byte value: 00000011
Byte value: 00001111
Byte value: 00001111
Byte value: 00001111
Byte value: 00000111
Byte value: 00000001
```

You can literally SEE the fake sine wave trying to crawl through the bits.

Like a terrified analog signal trapped inside a UART.

In theory:

```text
sine wave -> sigma-delta chaos -> serial bytes -> hardware -> sound
```

In practice:

```text
terminally possessed industrial machinery
```

## HOW IT FEELS

Imagine a DAC designed by somebody who learned control systems from an arcade machine repair manual.

That.

That's the project.

## TECHNICAL EXPLANATION

We continuously compare a target energy level against a historical approximation.

The resulting error gets integrated into a running value, converted into a rough number of "high bits", then smashed into an 8-bit output state.

No elegant quantizer.
No filtering pipeline.
No adult supervision.

## WHY

Because small chaotic experiments are fun.

And because sometimes the best way to understand a signal-processing concept is to implement it in the worst possible way first.

## STATUS

```
[x] alive
[x] emitting bits
[ ] academically defensible
```