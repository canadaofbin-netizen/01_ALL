---
title: "Beyond the Spatial Horizon: An Asymmetric Hybrid Biosignal Interface"
description: "A detailed research roadmap proposing an EOG-EEG-EMG hybrid interface for all-in-one smart glasses."
type: summary
tags: ["BCI", "Spatial Computing", "Smart Glasses", "Research Proposal", "HCI"]
timestamp: 2026-07-15
sources: ["[[BCI Roadmap.md]]"]
---

# BCI Roadmap: Beyond the Spatial Horizon

## Overview
This document summarizes the research proposal for constructing an **Asymmetric Hybrid Biosignal (EOG-EEG-EMG) Interface** designed explicitly for All-in-One Smart Glasses. It aims to overcome the current bottleneck in spatial computing interfaces, where optical tracking induces physical fatigue (e.g., Gorilla Arm) and voice recognition causes social friction.

## Core Problem
While [[Brain_Computer_Interface]] (BCI) technology is seen as the ultimate alternative, temporal EEG sensors embedded in smart glasses suffer from [[Volume_Conduction]], causing an extreme loss of spatial resolution. Furthermore, relying on secondary devices like Meta's HD-EMG wristband results in [[Form_Factor_Fragmentation]], breaking the seamless ambient computing experience.

## Proposed Solution
The proposal introduces [[Asymmetric_Hybrid_Control]], an elegant circumvention of physical EEG limitations. It asymmetrically assigns Degrees of Freedom (DoF):
- **EOG (Eye Movements)**: Assigned for 2D spatial navigation.
- **EEG + EMG (Jaw/Micro-gestures)**: Assigned for confirming intent (Binary Click).
This achieves a flawless [[Zero_UI]] experience within a standalone eyewear form factor.

## Research Roadmap (4 Phases)
1. **Verifying Temporal Limits (*In-vitro*)**: Quantifying accuracy degradation when reducing 64-channel EEG to 4 temporal channels, and using extreme engineering to recover accuracy to the 70% threshold.
2. **UX Optimization**: Abandoning directional decoding from the temporal lobe in favor of extracting a highly reliable 'Binary Click' via Micro-gestures, massively reducing cognitive fatigue.
3. **Multi-modal AI Fusion**: Fusing EOG, EEG, and facial EMG using a CNN+LSTM network, and validating usability against Fitts' Law to solve the "Midas Touch" problem.
4. **Ecological Validity (*In-the-wild*)**: Proving robustness in real-world environments (walking, talking) by using [[Adaptive_Noise_Canceling]] with the smart glasses' built-in IMU to subtract motion artifacts in real-time.
