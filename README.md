# Med-Track South-West

## Pharmaceutical Supply Chain Analysis & Stock-Out Prediction System

This project demonstrates a complete data science pipeline for predicting pharmaceutical stock-outs in health facilities across South-West Cameroon, addressing critical medicine shortages in resource-limited settings.

### Project Overview

**Problem:** Health facilities in Cameroon experience frequent stock-outs of essential medicines (9–50%+ of facilities), compromising patient care and treatment outcomes.

**Solution:** Machine learning-based predictive system that:
- Generates realistic synthetic supply chain data (3,840 records)
- Analyzes stock-out patterns across 5 facilities and 8 drug types
- Predicts critical shortages 1 month ahead with **97.63% accuracy**

### Key Features

✓ **Synthetic Data Generation**
- 24-month timeline (Jan 2023 – Dec 2024)
- 5 health facilities × 8 essential drugs
- Realistic consumption patterns, supply shocks, and replenishment behavior
- Overall stock-out rate: ~32% (matches Cameroon's reported range)

✓ **Exploratory Data Analysis**
- Stock-out risk by drug type (Bar chart)
- Stock trend visualization with critical threshold detection
- Facility-level and drug-level insights

✓ **Machine Learning Model**
- **Algorithm:** Random Forest Classifier (100 trees, optimized hyperparameters)
- **Accuracy:** 97.63%
- **Key Features:** 
  - Stock trend (60.5% importance) – most predictive feature
  - Previous stock level (20.5%)
  - Consumption patterns and seasonality
- **Output:** Binary classification (stock-out / no stock-out)

### Files Included

**Data:**
- `synthetic_medtrack_data_v2.csv` – 3,840 records with facility, drug, month, consumption, stock, and stock-out flag

**Visualizations:**
- `stock_out_by_drug_v2.png` – Bar chart of stock-out risk by drug
- `example_trend_v2.png` – Time series with critical threshold (50 units)
- `confusion_matrix.png` – Model performance matrix
- `sample_predictions_table.png` – Example predictions with features

**Code:**
- `med-track-analysis.ipynb` – Complete Jupyter notebook with all analysis and modeling

### How to Use

1. **Load and Explore:**
   ```python
   import pandas as pd
   df = pd.read_csv('synthetic_medtrack_data_v2.csv')
   print(df.head())
   ```

2. **View Visualizations:**
   - Open the PNG files to see stock-out patterns and predictions

3. **Run Model:**
   - Execute the notebook to retrain the model and generate predictions
   - Model retraining takes ~2-3 seconds

### Use Cases

- **Supply Chain Optimization:** Identify drugs at highest risk and prioritize replenishment
- **Policy Planning:** Data-driven evidence for medicine supply policy in health systems
- **Early Warning System:** Alert facility managers 1 month before predicted stock-outs
- **Resource Allocation:** Target interventions to highest-risk facilities/drugs

### Model Performance

| Metric | Value |
|--------|-------|
| Accuracy | 97.63% |
| True Negatives | ~97% of non-stock-out months correctly identified |
| True Positives | ~98% of stock-out months correctly predicted |
| Key Predictor | Stock trend (declining stock = higher risk) |

### Technologies

- **Python 3.13**
- **pandas, numpy** – Data manipulation
- **scikit-learn** – Machine learning
- **matplotlib, seaborn** – Visualization

### Context

This project supports pharmaceutical supply chain resilience in Cameroon's health system, where stock-outs of essential medicines remain a critical barrier to achieving Universal Health Coverage (UHC) and sustainable development goals.

---

**Author:** Sumbele Serge  
**Date:** January 2026  
**License:** MIT
