#!/usr/bin/env python3
"""Generate and validate deterministic FNV-1a identifiers for Bladder Traits.
Compatible with the Sims 4 Python 3.7-era tooling (standard library only).
"""
from __future__ import print_function
import json
import sys

TRAITS = [
    ("Weak Bladder", "WeakBladder"),
    ("Incontinence", "Incontinence"),
    ("Small Bladder", "SmallBladder"),
    ("Bladder Distracted", "BladderDistracted"),
    ("Strong Bladder", "StrongBladder"),
    ("Large Bladder", "LargeBladder"),
]

def fnv1a_32(text):
    value = 0x811C9DC5
    for byte in text.encode("ascii"):
        value ^= byte
        value = (value * 0x01000193) & 0xFFFFFFFF
    return "0x{0:08X}".format(value)

def build_manifest():
    result = []
    seen = {}
    for display_name, slug in TRAITS:
        tuning_name = "Finn1041_BladderTraits_Trait_" + slug
        values = {
            "trait": fnv1a_32(tuning_name),
            "name": fnv1a_32("Finn1041_BladderTraits_String_" + slug + "_Name"),
            "description": fnv1a_32("Finn1041_BladderTraits_String_" + slug + "_Description"),
        }
        for kind, identifier in values.items():
            if identifier in seen:
                raise ValueError("FNV32 collision: {0} and {1}".format(seen[identifier], kind))
            seen[identifier] = display_name + ":" + kind
        result.append({
            "display_name": display_name,
            "tuning_name": tuning_name,
            "trait_and_simdata_instance": values["trait"],
            "name_string_key": values["name"],
            "description_string_key": values["description"],
        })
    return result

if __name__ == "__main__":
    data = {"algorithm": "FNV-1a 32-bit", "traits": build_manifest()}
    output = json.dumps(data, indent=2, sort_keys=True)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as handle:
            handle.write(output + "\\n")
    else:
        print(output)
