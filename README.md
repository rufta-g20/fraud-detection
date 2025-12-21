# Adey Innovations Inc. - Fraud Detection System

## 📌 Project Overview
This project aims to build a robust fraud detection system for Adey Innovations Inc. by analyzing e-commerce transactions and bank credit card activities. By integrating geolocation data and engineering transaction patterns, we develop machine learning models capable of identifying fraudulent behavior with high precision.

## 🎯 Business Objective
The primary goal is to minimize financial losses due to fraudulent activities while ensuring a seamless experience for legitimate users. We achieve this by:
* Mapping IP addresses to geographical locations to detect high-risk origins.
* Engineering features that capture user behavior and transaction velocity.
* Building scalable models that handle highly imbalanced datasets.

## 📁 Project Structure
- `data/`: Contains raw datasets and processed features (categorized into `raw/` and `processed/`).
- `notebooks/`: Jupyter notebooks for EDA, Feature Engineering, and Model Training.
- `src/`: Reusable Python modules for data processing and utility functions.
- `models/`: Storage for trained model artifacts and evaluation results.
- `requirements.txt`: List of dependencies required to run the project.

## 📊 Dataset Description
The project utilizes three distinct datasets to capture a holistic view of fraud:

1. **E-commerce Fraud Data (`Fraud_Data.csv`)**: Contains 151,112 rows of transaction data including user IDs, purchase values, device IDs, and IP addresses.
2. **IP-to-Country Mapping (`IpAddress_to_Country.csv`)**: A lookup table used to map numerical IP ranges to specific countries.
3. **Credit Card Fraud Data (`creditcard.csv`)**: A dataset of 284,807 bank transactions, anonymized via Principal Component Analysis (PCA), featuring 28 numerical variables (V1-V28).

## 🛠️ Setup and Installation

### 1. Environment Configuration
Ensure you have **Conda** installed. Create a clean environment with Python 3.11 to avoid version conflicts:
```bash
conda create -n fraud_detection python=3.11 -y
conda activate fraud_detection

```

### 2. Install Dependencies

Install the required libraries (optimized for compatibility with NumPy 1.26.4):

```bash
pip install -r requirements.txt

```

### 3. Register Kernel

Make the environment accessible within Jupyter Notebooks:

```bash
python -m ipykernel install --user --name=fraud_detection

```

## 🚀 Workflow Execution

1. **Exploratory Data Analysis (EDA)**:
* Run `notebooks/eda-fraud-data.ipynb` for e-commerce analysis.
* Run `notebooks/eda-creditcard.ipynb` for bank transaction analysis.


2. **Feature Engineering**:
* Execute `notebooks/feature-engineering.ipynb` to transform raw data, handle class imbalance via SMOTE, and scale numerical features.


3. **Modeling**:
* Train and evaluate models using the processed datasets.

## 🔧 Core Utilities

The project uses a modular `src/processing.py` script which includes:

* `ip_to_int`: Secure conversion of IP strings to integers.
* `merge_with_geo`: Range-based merge logic for geolocation mapping.
* `clean_data`: Standardized cleaning and duplicate removal with structured logging.


**Author:** Rufta

**Date:** 2025
