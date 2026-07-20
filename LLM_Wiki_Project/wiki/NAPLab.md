---
title: "Neural Acoustic Processing Lab (NAPLab)"
description: "A research lab at Columbia University's Zuckerman Institute led by Professor Nima Mesgarani, pioneering auditory brain-computer interfaces and brain-controlled hearing aids."
type: entity
tags: ["research-lab", "BCI", "auditory-neuroscience", "AAD", "hearing-aids", "AI", "USA"]
timestamp: 2026-07-20
sources: ["[[BCI Research Opportunities Investigation.pdf]]"]
---

# Neural Acoustic Processing Lab (NAPLab)

## Background
The Neural Acoustic Processing Lab (NAPLab), led by Professor Nima Mesgarani at the Department of Electrical Engineering and the Zuckerman Mind Brain Behavior Institute at [[Columbia_University]], is designing the future of auditory [[Brain_Computer_Interface]] systems at the intersection of cognitive neuroscience and advanced artificial intelligence. Their research focuses on uncovering the neurological mechanisms of the "Cocktail Party Effect" — the ability to selectively listen to a specific speaker's voice in a noisy environment — and transplanting this ability into artificial auditory systems.

## Key Attributes

### Auditory Attention Decoding (AAD)
NAPLab has developed [[Auditory_Attention_Decoding]] (AAD) algorithms that decode a user's brain neural signals to identify the sound source they are currently paying attention to, selectively separating and amplifying only that specific source. This addresses the fundamental limitation of traditional hearing aids that indiscriminately amplify both background noise and the target speaker.

### Landmark Nature Neuroscience Study (2026)
The culmination of their AAD technology was a groundbreaking study published in Nature Neuroscience (first author: Vishal Choudhari). The research team:
- Used intracranial EEG (iEEG/ECoG) electrodes implanted on epilepsy patients' brain surfaces.
- Introduced a novel concept called "Spatial Neural Fingerprints" possessing time-invariance, going beyond simple temporal envelope tracking.
- Architecture: A Bidirectional Long Short-Term Memory network (Bi-LSTM) brain signal predictor classifies attended speaker clusters from iEEG, while a Mamba-TasNet speech extractor receives the mixed audio signal. The neural prediction is provided as a conditioning cue via Feature-wise Linear Modulation (FiLM).
- Training uses the LibriTTS speech corpus with K-means clustering for speaker feature classification.
- Achieved up to 90% attention separation accuracy in real-time.
- Recorded as the first instance proving commercial viability of brain-controlled hearing aids at the clinical level.

### LLM & Brain Convergence Research
Published in Nature Machine Intelligence (2024, 2026): Discovered that the contextual features extracted from intermediate layers of LLMs and ASR systems converge with how the human auditory cortex encodes language in a parallel and hierarchical manner. Also contributing to diffusion-based Text-to-Speech generative models like StyleTTS 2.

### Tech Stack & Team
- **Core tools**: PyTorch, TensorFlow, Bi-LSTM, State Space Models (Mamba), Mamba-TasNet, StyleTTS 2, WavLM, x-vector, iEEG/ECoG data preprocessing.
- **Collaborators**: Neurologists Ashesh Mehta and Stephan Bickel.
- **Team profile**: Most PhD students and researchers have backgrounds in electrical engineering, biomedical engineering, or computer science.
- Highly values the ability to design mathematical modeling and deep learning architectures from scratch, not just measuring brainwaves.

## Related Concepts & Entities
[[Auditory_Attention_Decoding]], [[Brain_Computer_Interface]], [[Electroencephalography]], [[Event_Related_Potentials]], [[Columbia_University]], [[Iverson_Lab]]

---
*Provenance: BCI Research Opportunities Investigation.pdf*
