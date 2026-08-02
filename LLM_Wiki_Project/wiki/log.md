---
type: overview
title: "Wiki Log"
description: "Append-only chronological record of ingests, queries, and lint passes."
tags: ["wiki", "log"]
timestamp: "2026-08-01"
sources: ["wiki_system"]
---

# Wiki Log

Append-only chronological record of ingests, queries, and lint passes.

## [2026-07-14] init | Created LLM Wiki structure

## [2026-07-15] ingest | 2027 resume.md (Re-Ingest)
- Ran advanced `/ingest` protocol on `raw/assets/2027 resume.md`
- Created [[University_College_London]]
- Created [[Kwangwoon_University]]
- Created [[University_of_Oklahoma]]
- Created [[Boundary_Spanning]]
- Created [[Meta_Analysis]]
- Created [[Process_Mining]]
- Created [[2027_Resume_Summary]]
- Eradicated all orphans by robust cross-linking.

## [2026-07-15] ingest | Kim Lab Journal Club - Summer 2026.md
- Ran advanced `/ingest` protocol on `raw/assets/Kim Lab Journal Club - Summer 2026.md`
- Created [[Kim_Lab]]
- Created [[Situational_Strength]]
- Created [[Trait_Activation_Theory]]
- Created [[AI_and_Work]]
- Created [[Algorithm_Aversion]]
- Created [[Algorithmic_Management]]
- Created [[Kim_Lab_Journal_Club_Summer_2026]]
- Successfully processed and moved raw file to `_processed`.

## [2026-07-15] ingest | Multi-Agent PDF Ingest (6 Papers)
- Spawned 6 subagents to concurrently read 6 academic PDFs from `raw/assets/`.
- Created summaries: [[Meyer_et_al_2009]], [[Judge_and_Zapata_2015]], [[Calderwood_et_al_2023]], [[Dalal_et_al_2020]], [[DellAcqua_et_al_2026]], [[Yam_et_al_2023]].
- Created concepts: [[Automation_Bias]], [[Extra_Normative_Work]], [[Job_Insecurity]], [[Counterproductive_Work_Behavior]].
- Merged empirical findings seamlessly into [[Situational_Strength]], [[Trait_Activation_Theory]], [[AI_and_Work]], and [[Meta_Analysis]].
- Renamed all 6 PDFs to `_processed.pdf`.

## [2026-07-15] ingest | BCI Domain Expansion
- Processed BCI Roadmap and AR/VR Research PDF using Master-Subagent architecture.
- Created summaries: BCI_Roadmap, BCI_in_AR_VR_Research.
- Created 11 new concepts relating to spatial computing, HCI, and neurotechnology (e.g., Brain_Computer_Interface, Asymmetric_Hybrid_Control, Volume_Conduction).
- Renamed raw assets to _processed.

## [2026-07-15] ingest | BCI Internship Tracker & Networking Data
- Ingested 'Intern summer 2.md' and '2027_BCI_Internship_Tracker.xlsx'.
- Translated and synthesized Korean networking strategies and hackathon details into English according to the new Universal Language Constraint.
- Created 9 Entity pages for Big Tech companies (e.g., Apple, Google_DeepMind, Meta_Reality_Labs).
- Created Concepts: Cold_Email_Strategy, Neurotech_Hackathons.
- Created Summaries: 2027_BCI_Internship_Tracker, Summer_2027_Internship_Networking.
- Renamed raw files to _processed and synced with GitHub.

## [2026-07-18] ingest | Research Methods & Statistics Lectures (14 PDFs)
- Ingested 14 UCL Research Methods lecture PDFs (Lectures 1–9, 11–15) using 3-batch parallel subagent architecture.
- **Housekeeping**: Renamed `2027 resume.md` and `temp_tracker.md` to `_processed` (content already in wiki from prior ingests).
- **Summaries Created** (14): [[Lecture_01_The_Research_Process]], [[Lecture_02_Psychological_Data]], [[Lecture_03_Summarising_Data]], [[Lecture_04_Visualising_Data]], [[Lecture_05_Probability_Theory]], [[Lecture_06_Sampling]], [[Lecture_07_Hypothesis_Testing]], [[Lecture_08_T_Tests]], [[Lecture_09_Correlations]], [[Lecture_11_Linear_Regression]], [[Lecture_12_One_Way_ANOVA]], [[Lecture_13_Categorical_Data_With_Chi_Squared]], [[Lecture_14_Non_Parametric_Tests]], [[Lecture_15_Reproducible_Science]].
- **Concepts Created** (14): [[Research_Process]], [[Variables_and_Measurement]], [[Descriptive_Statistics]], [[Data_Visualization]], [[Probability_Theory]], [[Sampling]], [[Hypothesis_Testing]], [[T_Test]], [[Correlation]], [[Linear_Regression]], [[ANOVA]], [[Chi_Squared_Test]], [[Non_Parametric_Tests]], [[Reproducibility]].
- **Concepts Merged**: Batch B merged new content into [[Research_Process]], [[Descriptive_Statistics]], [[Probability_Theory]].
- Renamed all 14 lecture PDFs to `_processed.pdf`.
- Updated `index.md` and `overview.md` with all new pages.
- Note: Lecture 10 was not present in the raw folder.

## [2026-07-20] ingest | BCI Research Opportunities Investigation (17-page PDF)
- Ingested `raw/assets/BCI Research Opportunities Investigation.pdf` — an in-depth analysis report on four next-generation BCI/neurotech research ecosystems.
- **Summaries Created** (1): [[BCI_Research_Opportunities_Investigation]].
- **Entities Created** (6): [[Kornysheva_Lab]], [[NAPLab]], [[Iverson_Lab]], [[Cambridge_NeuroWorks]], [[University_of_Birmingham]], [[Columbia_University]].
- **Concepts Created** (3): [[Auditory_Attention_Decoding]], [[Competitive_Queuing]], [[Scalable_Neural_Interfaces]].
- **Pages Merged** (4): New content merged into [[University_College_London]], [[Brain_Computer_Interface]], [[Electroencephalography]], [[Event_Related_Potentials]].
- Renamed raw PDF to `_processed.pdf`.
- Updated `index.md` and `overview.md` with all 10 new pages.

## [2026-07-27] ingest | Human-AI Interaction Papers (2 PDFs)
- Ingested 2 academic PDFs using parallel subagent architecture:
  - `raw/assets/2023-78874-001.pdf` — Tang et al. (2023), *Journal of Applied Psychology*: "No Person Is an Island" (AI interaction, social affiliation, loneliness).
  - `raw/assets/EBSCO-FullText-07_24_2026.pdf` — Tang, Koopman, McClean et al. (2022), *Academy of Management Journal*: "When Conscientious Employees Meet Intelligent Machines" (complementarity theory, role theory).
- **Summaries Created** (2): [[Tang_et_al_2023]], [[Tang_Koopman_McClean_et_al_2022]].
- **Concepts Created** (6): [[Attachment_Anxiety]], [[Complementarity_Theory]], [[Conscientiousness]], [[Role_Theory]], [[Social_Affiliation_Model]], [[Workplace_Loneliness]].
- **Entities Created** (1): [[Pok_Man_Tang]].
- **Pages Merged** (2): New empirical findings and thematic content merged into [[AI_and_Work]] and [[Job_Insecurity]].
- Renamed both raw PDFs to `_processed.pdf`.
- Updated `index.md` and `overview.md` with all 9 new pages.


## Ingest Log - 2026-08-01 18:52:34
- Processed `1-s2.0-S0191886922000599-main.pdf`: created/updated 3 entities and 3 concepts.
- Processed `scratch_0.txt`: created/updated 4 entities and 8 concepts.
- Processed `scratch_1.txt`: created/updated 3 entities and 7 concepts.
- Processed `scratch_2.txt`: created/updated 3 entities and 10 concepts.
- Processed `scratch_3.txt`: created/updated 3 entities and 8 concepts.
- Processed `1-s2.0-S0749597825000172-main.pdf`: created/updated 1 entities and 4 concepts.
- Processed `scratch_4.txt`: created/updated 6 entities and 7 concepts.


## Ingest Log - 2026-08-01 18:52:34
- Processed `1-s2.0-S0191886922000599-main.pdf`: created/updated 3 entities and 3 concepts.
- Processed `scratch_0.txt`: created/updated 4 entities and 8 concepts.
- Processed `scratch_1.txt`: created/updated 3 entities and 7 concepts.
- Processed `scratch_2.txt`: created/updated 3 entities and 10 concepts.
- Processed `scratch_3.txt`: created/updated 3 entities and 8 concepts.
- Processed `1-s2.0-S0749597825000172-main.pdf`: created/updated 1 entities and 4 concepts.
- Processed `scratch_4.txt`: created/updated 6 entities and 7 concepts.
- Processed `EBSCO-FullText-08_01_2026 (1).pdf`: created/updated 5 entities and 5 concepts.
- Processed `How Perceived Lack of Benevolence Harms Trust of Artificial Intelligence Management.pdf`: created/updated 3 entities and 4 concepts.
- Processed `Slow drift rate predicts ADHD symptomology over and above executive dysfunction.pdf`: created/updated 5 entities and 4 concepts.
- Processed `kupffer-et-al-2024-detecting-careless-responding-in-multidimensional-forced-choice-questionnaires.pdf`: created/updated 4 entities and 6 concepts.
- Processed `s10802-013-9715-2.pdf`: created/updated 4 entities and 5 concepts.
- Processed `EBSCO-FullText-08_01_2026.pdf`: created/updated 2 entities and 3 concepts.
- Processed `s10869-023-09911-w.pdf`: created/updated 3 entities and 4 concepts.

## [2026-08-01] lint | Full 6-step health check
- **Schema Integrity**: 5 issues (3 structural pages missing frontmatter, 1 YAML parse error, 1 empty sources field). 225/230 pages valid.
- **Staleness**: No contradictions. 10 oldest pages (2026-07-15) remain consistent.
- **Coverage Gaps**: index.md and overview.md contain stale references to old filenames.
- **Overview Drift**: RED — "Recent Additions" sections reference pre-rename filenames (~130 broken links).
- **Orphan Check**: 134/227 content pages (59%) have zero inbound cross-links from other content pages.
- **Duplicate Detection**: 12 duplicate groups identified (25 files affected). Top priorities: Diffusion Model, TIRT, Drift Rate, Non-Parametric Tests, Cynthia Huang-Pollock, MFC pages.
- **Overall Status**: 🟡 Yellow. Bulk ingest created granular pages without sufficient cross-linking. Duplicate merging and orphan remediation recommended.
