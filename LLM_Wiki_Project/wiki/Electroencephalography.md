---
title: "Electroencephalography (EEG)"
description: "A non-invasive monitoring method to record electrical activity of the brain."
type: concept
tags: ["neuroscience", "EEG", "BCI", "wearables"]
timestamp: 2026-07-20
sources: ["[[BCI in AR_VR Research.pdf]]", "[[BCI Research Opportunities Investigation.pdf]]"]
---

# Electroencephalography (EEG)

Electroencephalography (EEG) measures the electrical activity of the brain through electrodes placed on the scalp or within the ears.

## Wearables & Dry Electrodes in Spatial Computing
According to recent research (2023-2026), EEG has become the dominant modality for XR (Extended Reality) integration due to its high temporal resolution and miniaturization potential compared to alternatives like fNIRS. 

Recent form factors are embedding dry or semi-dry electrodes directly into:
- VR facial interfaces
- Smart glasses temples
- True Wireless Stereo (TWS) earbuds (e.g., Apple's AirPods architecture utilizing dynamic electrode selection to optimize signal-to-noise ratios amidst movement).

However, it still faces anatomical challenges such as [[Volume_Conduction]], leading researchers to propose [[Asymmetric_Hybrid_Control]] paradigms.

## Ecological Wearable EEG & Language Research
[[Iverson_Lab]] at [[University_College_London]] is developing a proprietary wearable, head-mounted EEG recorder based on dry-electrodes combined with a microphone-array, funded by the UK ESRC (Project No: ES/Z503630/1). The device integrates gel-free dry EEG electrodes to real-time synchronize auditory and lexical neural processing signals in naturalistic settings — for instance, measuring how 9-month-old infants in multilingual households or adult migrants process everyday conversations and podcasts. The hardware blueprints and signal processing code will be open-sourced to the scientific community.

## Multi-Modal Foundation Datasets
The [[Scalable_Neural_Interfaces]] project, funded by ARIA, combines high-density EEG and MEG signals with kinematic behavioral data to construct massive multi-modal foundation datasets. These are fed into GPT-based foundation models developed by [[Kornysheva_Lab]] at [[University_of_Birmingham]] to decode intricate hand and arm movement intentions at high resolution, aiming to break through the accuracy bottlenecks of traditional motor cortex signal decoding.

*Provenance: BCI in AR_VR Research.pdf; BCI Research Opportunities Investigation.pdf*
