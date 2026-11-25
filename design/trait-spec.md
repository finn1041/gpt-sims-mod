# Bladder Traits — Agreed Mechanics

This document records the mechanics agreed with the user. Implementation must preserve these values unless the user approves a change.

## Weak Bladder — moderate negative

- Bladder decay: 1.5x normal (50% faster).
- Effective capacity: normal.
- Discomfort begins earlier than normal.
- Bathroom autonomy: normal.
- Ordinary bladder control; accidents are possible but not an inherent trait effect.

## Incontinence — severe negative

- Bladder decay: normal.
- Effective capacity: normal.
- Bladder control: significantly reduced.
- Earlier discomfort and increased accident likelihood.
- Use both urgency-dependent checks and independent random control failures, including sleep vulnerability.
- Target accident chance per eligible urgency-based control check:

| Bladder fullness | Chance |
| --- | ---: |
| 50–60% | 2% |
| 60–70% | 5% |
| 70–80% | 12% |
| 80–90% | 25% |
| 90–99% | 40% |
| 100% | 60% |

These are per-check probabilities, not per-minute odds. The implementation must include cooldown/state protection so checks cannot fire repeatedly in rapid succession. Sleep and independent checks must be separately calibrated to avoid unintentionally multiplying risk.

## Small Bladder — severe negative

- Effective capacity: 0.5x normal.
- Natural bladder decay: normal.
- Fluid sensitivity: increased; the same drink should produce a larger fraction of effective capacity.
- Earlier discomfort.
- Normal control; no independent accident modifier.

Because the game's bladder motive is normalized, this should be simulated through drink-related motive effects and urgency mapping rather than assuming a physical capacity field exists.

## Bladder Distracted — moderate negative

- Normal decay, capacity, and control.
- While occupied in eligible activities, sometimes postpones or skips a bathroom decision.
- Skip chances:

| Bladder fullness | Chance to skip |
| --- | ---: |
| 30–50% | 60% |
| 50–70% | 50% |
| 70–80% | 40% |
| 80–90% | 20% |
| 90–99% | 5% |

At 90% and above, the 5% skip chance remains. This is only an autonomy/postponement effect while occupied; it is not itself an accident modifier. If not occupied, bathroom autonomy remains normal.

## Strong Bladder — positive

- Bladder decay: 0.65x normal (35% slower).
- Effective capacity: normal.
- Discomfort begins later.
- Improved resistance to urgency-related control failures.
- Normal fluid effects; bathroom needs are not eliminated.

## Large Bladder — positive

- Effective capacity: 1.4x normal.
- Natural bladder decay: normal.
- Normal fluid sensitivity in absolute terms; the same fluid produces a smaller fraction of effective capacity.
- Discomfort begins later.
- Normal control.

## Trait conflicts

- Weak Bladder and Strong Bladder are mutually exclusive.
- Small Bladder and Large Bladder are mutually exclusive.
- Other combinations are allowed, including Weak Bladder + Incontinence + Small Bladder.

## Shared implementation requirements

- All six traits should be selectable in Create-a-Sim as personality traits.
- Target age range: Teen through Elder, subject to confirmation against current trait tuning schema.
- Basemental and WickedWhims must not be required dependencies.
- Avoid hard conflicts with either mod when present.
- Tune autonomy, cooldowns, and event checks to prevent repeated or runaway effects.
