# NASA Battery Capacity Prediction using Machine Learning

## Project Overview

This project focuses on predicting battery capacity using machine learning regression algorithms.

The project uses the NASA Battery Dataset and performs data preprocessing, feature engineering, exploratory data analysis, model training, hyperparameter tuning, and model evaluation.

The main objective is to predict battery capacity based on battery cycle information and other battery-related measurements.

---

## Dataset

The project uses the NASA Battery Dataset.

The dataset contains battery measurement data collected across different battery cycles. It includes a metadata file and individual battery data files.

The data is processed before training the machine learning models.

After preprocessing and cleaning, the final machine learning dataset contains:

- **2,769 samples**
- **17 features**
- **80% training data**
- **20% testing data**

The final train-test split contains:

- **Training samples:** 2,215
- **Testing samples:** 554

---

## Machine Learning Models

A total of 10 regression algorithms are implemented and evaluated in this project.

### Linear Regression Models

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. ElasticNet
5. Polynomial Regression

### Non-Linear and Other Regression Models

6. Decision Tree Regressor
7. Random Forest Regressor
8. Gradient Boosting Regressor
9. Support Vector Regressor (SVR)
10. KNN Regressor

---

## Regression Algorithms

### 1. Linear Regression

Linear Regression predicts the target value by finding a linear relationship between the input features and battery capacity.

### 2. Ridge Regression

Ridge Regression is a regularized version of Linear Regression. It uses L2 regularization to reduce the effect of large coefficients and help prevent overfitting.

### 3. Lasso Regression

Lasso Regression uses L1 regularization. It can reduce some feature coefficients to zero, which can also help with feature selection.

### 4. ElasticNet

ElasticNet combines both L1 and L2 regularization. It combines the advantages of Lasso and Ridge Regression.

### 5. Polynomial Regression

Polynomial Regression extends linear regression by creating polynomial features so that non-linear relationships between features and battery capacity can be modeled.

### 6. Decision Tree Regressor

Decision Tree Regressor predicts battery capacity by recursively splitting the dataset based on feature values.

### 7. Random Forest Regressor

Random Forest combines multiple decision trees and averages their predictions to produce a more robust prediction.

### 8. Gradient Boosting Regressor

Gradient Boosting builds decision trees sequentially. Each new tree attempts to reduce the errors made by the previous trees.

### 9. Support Vector Regressor

Support Vector Regression predicts a continuous target value using a regression function. The project uses the RBF kernel to model non-linear relationships.

### 10. KNN Regressor

KNN Regressor predicts the target value using the values of the nearest training samples.

---

## Data Preprocessing

The following preprocessing steps are performed:

1. Dataset loading
2. Data cleaning
3. Feature selection
4. Feature engineering
5. Handling missing values
6. Outlier processing
7. Feature scaling
8. Train-test splitting

The features are standardized using `StandardScaler` before model training.

---

## Model Training

The models are trained using the same training and testing split so that their performance can be compared consistently.

The overall workflow is:

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Prediction
   ↓
Model Evaluation
# Project Structure
NASA-Battery-Capacity-Prediction/
│
├── README.md
├── requirements.txt
│
├── app/
│   └── app.py
│
├── data/
│   └── dataset files
│
├── notebooks/
│   └── ML_Regression_Final00.ipynb
│
└── results/
    └── model results and visualizations

 ##workflow
NASA Battery Dataset
        ↓
Data Loading
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Feature Selection
        ↓
Train-Test Split
        ↓
Feature Scaling
        ↓
10 Regression Models
        ↓
Hyperparameter Tuning
        ↓
Predictions
        ↓
R² / RMSE / MAE
        ↓
Model Comparison
        ↓
Battery Capacity Prediction
