---
title: "Volume Conduction"
description: "The scattering and blurring of electrical signals as they pass through biological tissue, severely reducing spatial resolution in non-invasive EEG."
type: concept
tags: ["neuroscience", "EEG", "physics", "signal-processing"]
timestamp: 2026-07-15
sources: ["[[BCI Roadmap.md]]"]
---

# Volume Conduction

Volume conduction is an anatomical and physical phenomenon where minute electrical signals generated in the cerebral cortex scatter, blur, and spread out as they pass through the cerebrospinal fluid, skull, and scalp before reaching external sensors.

## Impact on Brain-Computer Interfaces
In the context of [[Brain_Computer_Interface]] technology, volume conduction represents a fatal limitation for compact form factors like smart glasses. As noted in the [[BCI_Roadmap]]:
- It causes an extreme loss of spatial resolution.
- It makes it physically impossible to decode precise directional motor intent (e.g., flicking a single thumb "left" vs. "right") using only the limited EEG channels available on the temples of an eyewear frame.

This limitation forces engineers to either rely on wrist-worn peripherals (causing [[Form_Factor_Fragmentation]]) or fundamentally redesign the UX using paradigms like [[Asymmetric_Hybrid_Control]].
