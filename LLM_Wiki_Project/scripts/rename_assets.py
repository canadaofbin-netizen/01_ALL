import os
import shutil

RAW_DIR = r"g:\My Drive\UCL\AI Lab\01_ALL\LLM_Wiki_Project\raw\assets"

# Full rename mapping: old_name -> new_name
# All files keep _processed suffix since they've already been ingested
RENAME_MAP = {
    # === Academic Papers (PDFs) ===
    "1-s2.0-S0191886922000599-main_processed.pdf": "Lee_et_al_2022_Negatively_Keyed_Statements_MFC_processed.pdf",
    "1-s2.0-S0749597825000172-main_processed.pdf": "Schilke_Reimann_2025_AI_Disclosure_Erodes_Trust_processed.pdf",
    "2023-78874-001_processed.pdf": "Tang_et_al_2023_Consequences_Interacting_With_AI_processed.pdf",
    "EBSCO-FullText-07_24_2026_processed.pdf": "Tang_et_al_2022_Conscientious_Employees_Intelligent_Machines_processed.pdf",
    "EBSCO-FullText-08_01_2026 (1)_processed.pdf": "Cameron_2024_Making_Good_Bad_Job_processed.pdf",
    "EBSCO-FullText-08_01_2026_processed.pdf": "Jia_et_al_2024_AI_Augments_Employee_Creativity_processed.pdf",
    "How Perceived Lack of Benevolence Harms Trust of Artificial Intelligence Management_processed.pdf": "Li_Bitterly_2024_Benevolence_Harms_AI_Trust_processed.pdf",
    "Slow drift rate predicts ADHD symptomology over and above executive dysfunction_processed.pdf": "Feldman_Huang-Pollock_2021_Slow_Drift_Rate_ADHD_processed.pdf",
    "s10802-013-9715-2_processed.pdf": "Karalunas_Huang-Pollock_2013_Integrating_RT_Impairments_processed.pdf",
    "s10869-023-09911-w_processed.pdf": "Lee_et_al_2024_Detecting_Careless_MFC_Data_processed.pdf",
    "kupffer-et-al-2024-detecting-careless-responding-in-multidimensional-forced-choice-questionnaires_processed.pdf": "Kupffer_et_al_2024_Careless_Responding_MFC_processed.pdf",
    # Already partially well-named but need format cleanup
    "Calderwood et al. - 2023 - Situational Strength as a Lens to Understand the Strain Implications of Extra-Normative Work_processed.pdf": "Calderwood_et_al_2023_Situational_Strength_Extra_Normative_Work_processed.pdf",
    "Dalal et al. - 2020 - Extending Situational Strength Theory to Account for Situation-Outcome Mismatch_processed.pdf": "Dalal_et_al_2020_Situational_Strength_Situation_Outcome_Mismatch_processed.pdf",
    "Dell'Acqua et al. - 2026 - Navigating the Jagged Technological Frontier_processed.pdf": "DellAcqua_et_al_2026_Jagged_Technological_Frontier_processed.pdf",
    "Judge and Zapata - 2015 - The Person\u2013Situation Debate Revisited Effect of Situation Strength and Trait Activation on the Vali_processed.pdf": "Judge_Zapata_2015_Person_Situation_Debate_Revisited_processed.pdf",
    "Meyer et al. - 2009 - A meta\u2010analytic investigation into the moderating effects of situational strength on the conscientio_processed.pdf": "Meyer_et_al_2009_Situational_Strength_Conscientiousness_processed.pdf",
    "Yam et al. - 2023 - The Rise of Robots Increases Job Insecurity and Maladaptive Workplace Behaviors_processed.pdf": "Yam_et_al_2023_Rise_Of_Robots_Job_Insecurity_processed.pdf",
    "BCI Research Opportunities Investigation_processed.pdf": "BCI_Research_Opportunities_Investigation_processed.pdf",
    "BCI in AR_VR Research_processed.pdf": "BCI_in_AR_VR_Research_processed.pdf",

    # === Lecture Notes (PDFs) ===
    "Lecture 1. The Research Process - notes_processed.pdf": "siromahov_lecture_01_research_process_processed.pdf",
    "Lecture 2. Psychological data - notes_processed.pdf": "siromahov_lecture_02_psychological_data_processed.pdf",
    "Lecture 3. Summarising data - notes_processed.pdf": "siromahov_lecture_03_summarising_data_processed.pdf",
    "Lecture 4. Visualising data - notes_processed.pdf": "siromahov_lecture_04_visualising_data_processed.pdf",
    "Lecture 5. Probability theory - notes_processed.pdf": "siromahov_lecture_05_probability_theory_processed.pdf",
    "Lecture 6. Sampling - notes_processed.pdf": "siromahov_lecture_06_sampling_processed.pdf",
    "Lecture 7. Hypothesis Testing - notes_processed.pdf": "siromahov_lecture_07_hypothesis_testing_processed.pdf",
    "Lecture 8. T-tests - slides_processed.pdf": "siromahov_lecture_08_t_tests_processed.pdf",
    "Lecture 9. Correlations - notes_processed.pdf": "siromahov_lecture_09_correlations_processed.pdf",
    "Lecture 11. Linear Regression - notes_processed.pdf": "siromahov_lecture_11_linear_regression_processed.pdf",
    "Lecture 12. One-way ANOVA - slides_processed.pdf": "siromahov_lecture_12_one_way_anova_processed.pdf",
    "Lecture 13. Categorical data with chi squared - notes_processed.pdf": "siromahov_lecture_13_categorical_data_chi_squared_processed.pdf",
    "Lecture 14. Non-parametric tests - notes_processed.pdf": "siromahov_lecture_14_non_parametric_tests_processed.pdf",
    "Lecture 15. Reproducible science_processed.pdf": "siromahov_lecture_15_reproducible_science_processed.pdf",

    # === Scratch Text Files ===
    "scratch_0_processed.txt": "siromahov_lecture_11_linear_regression_notes_processed.txt",
    "scratch_1_processed.txt": "siromahov_lecture_12_one_way_anova_notes_processed.txt",
    "scratch_2_processed.txt": "siromahov_lecture_13_categorical_data_notes_processed.txt",
    "scratch_3_processed.txt": "siromahov_lecture_14_non_parametric_tests_notes_processed.txt",
    "scratch_4_processed.txt": "siromahov_lecture_15_reproducible_research_notes_processed.txt",

    # === Other Files ===
    "2027 resume_processed.md": "2027_resume_processed.md",
    "2027_BCI_Internship_Tracker_processed.xlsx": "2027_bci_internship_tracker_processed.xlsx",
    "BCI Roadmap_processed.md": "bci_roadmap_processed.md",
    "Intern summer 2_processed.md": "intern_summer_2_journal_processed.md",
    "Kim Lab Journal Club - Summer 2026_processed.md": "kim_lab_journal_club_summer_2026_processed.md",
    "temp_tracker_processed.md": "temp_tracker_processed.md",
}

def main():
    renamed = 0
    skipped = 0
    errors = []
    
    for old_name, new_name in RENAME_MAP.items():
        old_path = os.path.join(RAW_DIR, old_name)
        new_path = os.path.join(RAW_DIR, new_name)
        
        if old_name == new_name:
            skipped += 1
            print(f"[SKIP] Already correct: {old_name}")
            continue
            
        if not os.path.exists(old_path):
            errors.append(f"[NOT FOUND] {old_name}")
            print(f"[NOT FOUND] {old_name}")
            continue
        
        if os.path.exists(new_path):
            errors.append(f"[CONFLICT] Target already exists: {new_name}")
            print(f"[CONFLICT] Target already exists: {new_name}")
            continue
        
        try:
            os.rename(old_path, new_path)
            renamed += 1
            print(f"[RENAMED] {old_name} -> {new_name}")
        except Exception as e:
            errors.append(f"[ERROR] {old_name}: {e}")
            print(f"[ERROR] {old_name}: {e}")
    
    print(f"\n--- Summary ---")
    print(f"Renamed: {renamed}")
    print(f"Skipped: {skipped}")
    print(f"Errors:  {len(errors)}")
    for e in errors:
        print(f"  {e}")

if __name__ == "__main__":
    main()
