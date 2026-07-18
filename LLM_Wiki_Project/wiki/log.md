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
