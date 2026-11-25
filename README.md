# Sims 4 Bladder Traits

A custom Sims 4 trait mod adding six selectable bladder-related personality traits.

## Current status

**Development in progress — not yet installable or tested in-game.**

This repository tracks the trait design, tuning research, implementation source, and validation work. A playable release requires valid Sims 4 Trait Tuning and Sim Data resources, localized string tables, and in-game testing.

## Traits

- Weak Bladder
- Incontinence
- Small Bladder
- Bladder Distracted
- Strong Bladder
- Large Bladder

See [the agreed trait specification](design/trait-spec.md) for exact mechanics and compatibility rules.

## Compatibility goals

- The Sims 4 for Windows PC
- No required dependency on Basemental or WickedWhims
- Aim for compatibility with both when installed
- Intended for Teen through Elder Sims, pending tuning validation

## Development notes

The project follows the custom-trait workflow documented by Sims4CommunityLibrary: clone a valid personality Trait Tuning and its matching Sim Data, assign unique FNV32 identifiers, and add an English string-table resource. See [technical notes](research/technical-notes.md).

No file in this repository should be treated as a playable .package or .ts4script until explicitly marked as a tested release.
