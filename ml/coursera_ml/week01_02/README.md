# Logical Classification Methods
**Week 01 Part 02**

## Syllabus

Logical methods classify objects based on simple rules, making them interpretable and easy to implement. Combined into ensembles, they can solve many tasks with high quality. This module covers decision trees and their combination into ensembles known as random forests.

- Decision Trees
- Decision Tree Construction Algorithm
- Handling Missing Values, Advantages, and Disadvantages of Decision Trees
- Addressing Decision Tree Limitations
- **Assignment**: Feature Importance


## Assignment: Feature Importance

### What Concrete Machine Learning Tasks Were Required to Be Solved in This Assignment
- Train decision tree models for a classification task.
- Compute and interpret feature importance for the trained decision trees.
- Identify the two most important features based on feature importance scores.

### What Input Data Is Used in This Task
- **Dataset**: Titanic passenger data.
  - Features used: 
    - Passenger class (Pclass)
    - Ticket fare (Fare)
    - Passenger age (Age)
    - Passenger gender (Sex)
  - Target variable: Survival status (Survived).
  - Missing data handling: Remove rows with missing values.

### Technologies and Packages Used
- **Scikit-Learn**:
  - `sklearn.tree.DecisionTreeClassifier` for classification.
  - Feature importance computation via `feature_importances_` attribute.
- **Pandas** for data handling:
  - Used for loading and preprocessing the Titanic dataset (e.g., handling missing values and extracting target/feature columns).
- **NumPy** for handling numerical operations, such as checking for NaN values.


### Used Technologies and Packages (and Their Specific Parts)

The notebook file includes the following technologies and packages:

- `import numpy as np`
- `import pandas as pd`
- `from sklearn.tree import DecisionTreeClassifier`
- `import matplotlib.pyplot as plt`
- `from sklearn.metrics import accuracy_score`