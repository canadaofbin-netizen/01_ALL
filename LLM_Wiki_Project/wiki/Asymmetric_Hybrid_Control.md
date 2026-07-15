---
title: "Asymmetric Hybrid Control"
description: "An HCI paradigm that strategically decouples the degrees of freedom across different biosignals to bypass anatomical limitations."
type: concept
tags: ["HCI", "BCI", "hybrid-systems", "paradigm"]
timestamp: 2026-07-15
sources: ["[[BCI Roadmap.md]]"]
---

# Asymmetric Hybrid Control

Asymmetric Hybrid Control is a paradigm-shifting approach in [[Brain_Computer_Interface]] design that abandons the academic dogma of attempting to resolve both spatial navigation (direction) and execution (click) through a single modality (like EEG).

## Application in Smart Glasses
Because temporal EEG cannot resolve spatial direction due to [[Volume_Conduction]], the [[BCI_Roadmap]] proposes decoupling the Degrees of Freedom (DoF) asymmetrically:
- **Electrooculography (EOG)**: Subtle ocular tremors and eye movements are exclusively assigned to handle 2D spatial navigation (Cursor Direction).
- **EEG + EMG**: Brainwaves combined with facial EMG (e.g., jaw muscle tension from micro-gestures) are strictly allocated to confirm the user's intent (Binary Click/Activation).

This elegant fusion circumvents physical limitations, resolving the chronic "Midas Touch" (unintended activation) flaw of gaze-only systems and moving HCI closer to a flawless [[Zero_UI]].
