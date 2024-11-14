# Feature Importance

This assignment is based on materials from lectures on logical methods and focuses on familiarizing with **Decision Trees**.

## Objectives:
- Train decision trees.
- Identify the most important features for decision trees.

## Introduction:
Decision trees belong to the class of logical methods. Their main idea is to combine several simple decision rules, making the final algorithm interpretable. A decision tree is a binary tree where each node contains a rule of the form \"the \( j \)-th feature has a value less than \( b \).\" Leaves of the tree contain predictions. To get a result, you start at the root and traverse to the left or right subtree depending on whether the rule at the current node holds.

One of the unique characteristics of decision trees is the ability to compute the **importance of all features used**. Feature importance is determined based on how much a feature improves the quality criterion at tree nodes.

## Dataset:
The dataset used in this task is the Titanic passenger data. The goal is to solve a **classification problem**: predict who survived the shipwreck based on various passenger characteristics.

## Implementation in Scikit-Learn:
- Scikit-learn provides decision tree implementations in:
  - `sklearn.tree.DecisionTreeClassifier` (for classification).
  - `sklearn.tree.DecisionTreeRegressor` (for regression).
- Training a model is done using the `fit` method.

### Example:
```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier

X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 0])

clf = DecisionTreeClassifier()
clf.fit(X, y)
```

- To compute feature importance after training:
  ```python
  importances = clf.feature_importances_
  ```
  The `importances` variable contains an array of feature importances, where the index corresponds to the feature index in the data.

## Handling Missing Data:
- The dataset may contain missing values, represented as `NaN` in Pandas.
- Use `np.isnan()` to check if a value is `NaN`:
  ```python
  np.isnan(X)
  ```

## Assignment Instructions:

1. Load the dataset from `titanic.csv` using Pandas.
2. Keep only the following four features:
   - Passenger class (`Pclass`).
   - Ticket fare (`Fare`).
   - Passenger age (`Age`).
   - Passenger gender (`Sex`).
3. Note that the `Sex` feature contains string values.
4. Extract the target variable (`Survived`).
5. Handle missing values:
   - Identify rows with missing features.
   - Remove rows with any `NaN` values from the dataset.
6. Train a decision tree with the parameter `random_state=241` and default values for other parameters.
7. Compute feature importances and find the **two most important features**. Provide their names as the answer (comma-separated, no spaces).

## Materials:
- Detailed documentation for decision trees in scikit-learn.
- Handling missing values in Pandas.
- Advanced resources on decision trees and their construction.

## Submission Instructions:
Each answer should be in a text file with the answer on the first line. The submitted files should not contain a newline character at the end, as this is a Coursera platform limitation." > feature_importance_assignment.md
