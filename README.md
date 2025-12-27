# Adey Innovations Inc. - Fraud Detection System

## 💼 Business Context

Adey Innovations Inc. operates in a high-velocity financial environment where fraudulent transactions result in immediate capital loss and diminished user trust. As digital transactions scale, manual review becomes impossible, necessitating an automated, real-time detection system.

This project addresses two distinct fraud landscapes:

1. **E-commerce Fraud**: Focuses on behavior-based anomalies such as account takeovers and bot attacks.
2. **Bank Fraud**: Focuses on pattern-based detection in credit card transactions with extreme class imbalance (only **0.17%** fraud rate).

---

## 📌 Project Overview

This project aims to build a robust fraud detection system by analyzing e-commerce transactions and bank credit card activities. By integrating geolocation data and engineering transaction patterns, we develop machine learning models capable of identifying fraudulent behavior with high precision.

## 🎯 Business Objective

* **Geolocation Analysis**: Mapping IP addresses to geographical locations to detect high-risk origins.
* **Behavioral Modeling**: Engineering features that capture user behavior and transaction velocity.
* **Imbalanced Learning**: Utilizing **SMOTE** and **Stratified Cross-Validation** to handle highly skewed data.

---

## 📁 Project Structure

```text
fraud-detection/
├── .github/                # CI/CD pipelines (unittests.yml: Runs tests on push/PR)
├── data/                   # Data storage (Git Ignored)
│   ├── raw/                # Original datasets (Fraud_Data.csv, IpAddress_to_Country.csv, etc.)
│   └── processed/          # Cleaned data and engineered features (X_train, y_train, etc.)
├── notebooks/              # Experimental Analysis
│   ├── eda-fraud-data.ipynb   # E-commerce EDA
│   ├── eda-creditcard.ipynb   # Bank Transaction EDA
│   ├── feature-engineering.ipynb # Preprocessing & SMOTE
│   ├── modeling.ipynb         # Model training (Baseline vs Tuned XGBoost)
│   └── shap-explainability.ipynb # Model interpretation using SHAP
├── src/                    # Core modular logic
│   ├── __init__.py
│   ├── processing.py       # Data cleaning and Geolocation merge functions
│   └── modeling_utils.py   # Reusable evaluation and CV functions
├── tests/                  # Quality assurance
│   ├── __init__.py
│   └── test_preprocessing.py # Unit tests for core processing logic
├── models/                 # Saved artifacts (.joblib files)
├── scripts/                # Utility scripts
├── requirements.txt        # Project dependencies
├── .gitignore              # Prevents large data/models from being uploaded
└── README.md               # Main project documentation

```

---

## 📊 Dataset Description

1. **E-commerce Fraud Data**: 151,112 rows of transaction data including user IDs, purchase values, and device IDs.
2. **IP-to-Country Mapping**: A lookup table used to map numerical IP ranges to specific countries.
3. **Credit Card Fraud Data**: 284,807 bank transactions featuring 28 numerical variables (V1-V28).

---

## 🛠️ Setup and Installation

### 1. Environment Configuration

```bash
conda create -n fraud_detection python=3.11 -y
conda activate fraud_detection

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Running Tests

Ensure the "Green" status of the processing logic:

```bash
python -m unittest discover tests

```

---

## 🚀 Workflow Execution

1. **EDA**: Visualizing distributions in `eda-xxx.ipynb`.
2. **Engineering**: Preparing data in `feature-engineering.ipynb`.
3. **Modeling**: Training tuned models in `modeling.ipynb`.
4. **Explainability**: Interpreting decisions in `shap-explainability.ipynb`.

**Author:** Rufta

**Date:** 2025

---