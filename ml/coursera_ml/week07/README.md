# The final task. Subject area: Dota 2 game


# Machine Learning in Practical Applications
**Week 07 Part 01**


## Syllabus

This module summarizes the course, reviews data analysis stages, and explores practical tasks to prepare for the final project.

- Data Analysis Stages
- Handling Numerical and Text Features
- Data Preprocessing
- Quality Evaluation
- Algorithm Overview
- **Assignment**: Predicting Winners in Online Games



## What concrete machine learning tasks were required to be solved in this assignment
- Predict the outcome of a Dota 2 match (which team will win: Radiant or Dire) based on data from the first five minutes of gameplay.

## What input data is used in this task
- The dataset is provided in compressed JSON format (`matches.jsonlines.bz2`) with structured match details.
- Features include:
  - Player statistics (e.g., experience, gold, kills, deaths, items).
  - Team statistics (e.g., first blood events, hero selection).
  - Match meta-data (e.g., start time, lobby type).
- Additional datasets include pre-processed feature tables (`features.csv`) and a test dataset (`features_test.csv`).

## Used Technologies
- **Gradient Boosting** (via `sklearn.ensemble.GradientBoostingClassifier`): Used for modeling nonlinear relationships and initial predictions.
- **Logistic Regression** (via `sklearn.linear_model.LogisticRegression`): Employed for faster linear modeling with regularization.
- **Cross-Validation** (via `sklearn.cross_validation`): Applied to evaluate models' performance and select optimal hyperparameters.
- **Feature Scaling** (via `sklearn.preprocessing.StandardScaler`): Used to normalize features for logistic regression.
- **Python Standard Libraries**:
  - `numpy`: For numerical computations and "bag of words" transformations for hero encodings.
  - `pandas`: For handling feature tables.
  - `json` and `bz2`: For reading and processing JSON-based match data.
- **Performance Metric**: AUC-ROC was used to evaluate prediction quality across all models.

## Used Packages

- **datetime**: Used for managing and manipulating date and time data.
- **numpy**: Utilized for array operations and numerical computations.
- **pandas**: Used for handling and processing tabular data with DataFrames.
- **scipy.sparse**: Applied for working with sparse matrix structures.
- **sklearn.cross_validation**: For splitting datasets into training and validation sets.
- **sklearn.ensemble**: Used for ensemble machine learning methods such as RandomForest.
- **sklearn.grid_search**: For hyperparameter tuning and optimization.
- **sklearn.linear_model**: Used for building linear models, like Logistic Regression.
- **sklearn.preprocessing**: For preprocessing datasets, such as scaling and normalization.
- **warnings**: For managing and suppressing warning messages during execution.

## Folders and files structure

- files **_assignment.pdf _assignment.mhtml _About.txt** - Assignment 
- file **dota_kaggle_data.zip** - Dota2 Kaggle dataset 
  - The dataset is provided in compressed JSON format (`matches.jsonlines.bz2`) with structured match details.
  - Features include:
    - Player statistics (e.g., experience, gold, kills, deaths, items).
    - Team statistics (e.g., first blood events, hero selection).
    - Match meta-data (e.g., start time, lobby type).
  - Additional datasets include pre-processed feature tables (`features.csv`) and a test dataset (`features_test.csv`).

- folder **dota_kaggle_features** - Additional datasets include pre-processed feature tables (`features.csv`) and a test dataset (`features_test.csv`).



