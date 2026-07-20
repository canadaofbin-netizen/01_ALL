---
title: "Competitive Queuing (CQ)"
description: "A motor control model in which individual action elements are prepared in parallel within the brain, forming a gradient of activation strength according to their execution order."
type: concept
tags: ["motor-control", "neuroscience", "motor-planning", "hippocampus", "BCI"]
timestamp: 2026-07-20
sources: ["[[BCI Research Opportunities Investigation.pdf]]"]
---

# Competitive Queuing (CQ)

## Definition
Competitive Queuing (CQ) is a computational model of motor sequence planning positing that, before a human executes a sequence of movements, individual action elements are prepared in parallel within the brain, forming a gradient of activation strength according to their order. The first movement is activated most strongly, and subsequent movements are gradually activated less strongly. This parallel preparation mechanism is central to understanding how the brain orchestrates complex skilled actions such as playing a musical instrument or typing.

## Key Details

### Hippocampal Involvement in Motor Sequence Planning
The [[Kornysheva_Lab]] at [[University_of_Birmingham]] used multivariate pattern analysis (MVPA) of functional magnetic resonance imaging (fMRI) to make a monumental discovery: the hippocampus — traditionally thought to be limited to episodic memory and spatial navigation — is directly involved in pre-planning the sequences of procedural motor skills (Journal of Neuroscience, 2024; first author: Rhys Yewbrey; 24 participants; custom force-transducer-equipped keyboard). The study clearly distinguished the high-level sequence control role of the anterior body of the hippocampus from the lower-level control of the cortico-striato-cerebellar circuits. This discovery fundamentally questions the dichotomous classification system of procedural and episodic memory.

### Implications for Motor Disorders
In a 2026 study targeting adult patients with Developmental Coordination Disorder (DCD/Dyspraxia), the [[Kornysheva_Lab]] identified that motor planning deficits in DCD patients do not stem from general working memory problems, but rather from a significant degradation in their inherent ability to pre-order sequences of movements — i.e., the ability to form CQ gradients. Additionally, they confirmed that even in kinematically fused actions like continuous handwriting, individual movement elements do not completely merge into a neurologically new "motor primitive" but are still competitively pre-ordered according to their position.

### BCI Design Implications
These findings suggest that new non-invasive motor rehabilitation [[Brain_Computer_Interface]] systems must specifically target the "sequence planning" of individual actions, rather than attempting to decode holistic movement patterns. This principle directly informs the [[Scalable_Neural_Interfaces]] project, which fuses multi-modal neural data with GPT-based foundation models to decode intricate hand and arm movement intentions.

## Related Entities & Concepts
[[Kornysheva_Lab]], [[University_of_Birmingham]], [[Brain_Computer_Interface]], [[Motor_Imagery]], [[Scalable_Neural_Interfaces]], [[Electroencephalography]]

---
*Provenance: BCI Research Opportunities Investigation.pdf*
