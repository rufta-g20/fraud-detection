import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.metrics import (
    confusion_matrix, classification_report, 
    precision_recall_curve, auc
)

def perform_cross_validation(model, X, y, model_name="Model"):
    """
    Step 1: Reliable estimation using 5-Fold Stratified Cross-Validation.
    """
    print(f"\n--- Running 5-Fold Cross-Validation for {model_name} ---")
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scoring = ['recall', 'f1', 'roc_auc']
    
    cv_results = cross_validate(model, X, y, cv=skf, scoring=scoring, n_jobs=-1)
    
    print(f"Mean Recall: {cv_results['test_recall'].mean():.4f} (+/- {cv_results['test_recall'].std():.4f})")
    print(f"Mean F1-Score: {cv_results['test_f1'].mean():.4f} (+/- {cv_results['test_f1'].std():.4f})")
    print(f"Mean ROC-AUC: {cv_results['test_roc_auc'].mean():.4f} (+/- {cv_results['test_roc_auc'].std():.4f})")

def evaluate_model(y_true, y_pred, y_prob, model_name="Model"):
    """
    Step 2: Detailed visualization of results on the hold-out test set.
    """
    print(f"\n--- {model_name} Final Test Evaluation ---")
    print(classification_report(y_true, y_pred))
    
    # Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'{model_name} Confusion Matrix')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.show()

    # Precision-Recall Curve
    precision, recall, _ = precision_recall_curve(y_true, y_prob)
    pr_auc = auc(recall, precision)
    
    plt.figure(figsize=(5, 4))
    plt.plot(recall, precision, label=f'PR AUC = {pr_auc:.4f}')
    plt.title(f'{model_name} Precision-Recall Curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.legend()
    plt.show()
    
    return pr_auc