# 📄 Project Summary Report: Fraud Detection for Adey Innovations Inc.

## 1. Executive Summary
This project developed a high-precision fraud detection system to mitigate financial losses for Adey Innovations Inc. By analyzing behavior in E-commerce and pattern-based anomalies in Bank transactions, we transitioned from a low-performing baseline to an optimized **XGBoost ensemble**. 

The final models achieve significant lift in **Recall**, ensuring that nearly **82% of bank fraud** and **56% of e-commerce fraud** is captured before processing.

---

## 2. Modeling & Performance Metrics
We compared a Logistic Regression (LR) baseline against a tuned XGBoost model using **Stratified 5-Fold Cross-Validation**.

| Dataset | Baseline (LR) Recall | Best Model | Final PR-AUC Score |
| :--- | :--- | :--- | :--- |
| **E-commerce** | 0.2513 | XGBoost (Tuned) | **0.6993** |
| **Bank (Credit Card)** | 0.9210 | XGBoost (Tuned) | **0.7994** |

> **Model Selection**: XGBoost was selected for its superior ability to handle non-linear relationships and the extreme class imbalance (**0.17%**) present in the bank dataset.

---

## 3. Key Fraud Drivers (SHAP Analysis)
Using **SHAP (SHapley Additive exPlanations)**, we identified the top 5 factors driving fraud at Adey Innovations:

1.  **Velocity Indicators**: High frequency of a single device or IP address across multiple accounts.
2.  **Account Age**: Transactions occurring immediately after account creation (low "time-to-purchase").
3.  **Geographic Risk**: Specific country origins and "Unknown" IP locations identified via mapping.
4.  **Behavioral Identity**: Use of specific browser headers (e.g., Opera/IE) and direct traffic sources.

---

**Author:** Rufta  
**Date:** 2025