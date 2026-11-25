# Technical Notes

## Confirmed custom-trait resource workflow

The Sims4CommunityLibrary custom trait guide describes a workflow that creates all of the following:

1. A Trait Tuning resource.
2. Its matching Sim Data resource.
3. A String Table resource for the displayed trait name and text.

For traits with `trait_type` set to `PERSONALITY`, use FNV32 identifiers for the Trait Tuning, matching Sim Data, and string-table keys. String Table resource instance IDs use FNV64, with the English locale prefix handled by the package tooling.

The guide also warns against using Sims 4 Studio's Duplicate action for these resources; its documented process uses Add and copies the source tuning contents before changing identifiers and references.

Reference: https://github.com/DeviantGameMods/Sims4CommunityLibrary/blob/main/Documents/GitHub/CreateCustomTrait.txt

## Current implementation constraints

- The project does not yet contain a verified EA personality-trait template.
- The draft XML skeletons from earlier prototyping are not validated against the current game schema.
- No playable .package or .ts4script has been produced.
- The game represents bladder need through a normalized motive; do not assume there is a direct physical bladder-capacity property.
- Custom autonomy and accident behavior may require script support or carefully tuned interactions/loot. The exact supported injection points must be verified against the current game build before implementation.
- A successful XML parse is not proof that Sims 4 can load the tuning.
- A successful package build is not proof of in-game behavior; test each trait and all conflict pairs in a clean save.

## Intended build sequence

1. Obtain and inspect a valid current personality-trait tuning template and matching Sim Data.
2. Establish unique FNV32 identifiers and localized string-table keys.
3. Build and validate the six CAS trait resources.
4. Implement motive decay, effective-capacity mapping, autonomy postponement, and control checks using verified game APIs.
5. Package the resources and script together.
6. Test loading, CAS selection, trait conflicts, autonomy, sleep behavior, and interaction with common mods.
