---
title: "Event-Related Potentials (ERP)"
description: "Measured brain responses that are the direct result of a specific sensory, cognitive, or motor event."
type: concept
tags: ["neuroscience", "ERP", "P300", "BCI", "N400", "speech-perception"]
timestamp: 2026-07-20
sources: ["[[BCI in AR_VR Research.pdf]]", "[[BCI Research Opportunities Investigation.pdf]]"]
---

# Event-Related Potentials (ERP)

An Event-Related Potential (ERP) is the measured electrical brain response that is the direct result of a specific sensory, cognitive, or motor event. The P300 component is a widely used ERP in [[Brain_Computer_Interface]] (BCI) spellers.

## LLM Integration & Context Rot
Modern P300 speller paradigms in spatial environments integrate Large Language Models (LLMs) to correct raw, noisy decoding errors. However, this has introduced a phenomenon known as **"Context Rot"** or "Cognitive Divergence." When AI autocomplete becomes too efficient, the user's active neural focus drops. This lack of intense concentration paradoxically degrades the clarity and amplitude of the P300 signal, making it harder for the BCI to read the user's intent.

## Auditory ERPs & Speech Perception
Research from [[Iverson_Lab]] at [[University_College_London]] has demonstrated that N400 lexical processing EEG responses — a negative-going ERP component peaking around 400ms after stimulus onset, associated with semantic processing — and neural entrainment to the target speaker increase when listeners are exposed to non-native (L2) English or unfamiliar accents. This finding implies that speech perception involves a highly dynamic process where high-level top-down cognitive prediction actively intervenes in the acoustic processing stage in real-time, rather than operating as a purely feedforward sensory pipeline. This connects to broader [[Auditory_Attention_Decoding]] research led by [[NAPLab]], where neural decoding of auditory attention is being applied to create brain-controlled hearing aids.

*Provenance: BCI in AR_VR Research.pdf; BCI Research Opportunities Investigation.pdf*
