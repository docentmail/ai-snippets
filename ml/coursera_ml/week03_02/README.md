# Logistic Regression
**Week 02 Part 02**\
[Go to the description of the assignment](_assignment.md)\
[Go to Python notebook for the assignment ](assignment_code/assignment.ipynb)

## Syllabus
- Logistic Regression
- Regularized Logistic Regression
- **Assignment**: Logistic Regression

## Assignment Overview: 

### FIles and folders
- **[_assignment.md](_assignment.md)**- description of the tasks that need to be solved in the assignment
- **assignment_code**- folder containing solution Python code, dataset and related files
  - **[assignment.ipynb](assignment_code/assignment.ipynb)** - the Pyhon Notebook with solution



## Used Technologies and Packages

### Python Libraries and Packages
1. **NumPy**
   - Array creation and manipulation.
   - Mathematical operations like `dot`, `sqrt`, `exp`.

2. **Pandas**
   - Reading CSV files (`read_csv`).
   - Dataframe manipulations such as selecting columns and applying transformations.

3. **Scikit-learn**
   - **Linear Models**:
     - `SGDClassifier` for logistic regression.
     - `LogisticRegression` for L1 and L2-penalized logistic regression.
   - **Support Vector Machines**:
     - `SVC` for classification tasks.
   - **Metrics**:
     - `roc_auc_score` for computing AUC-ROC metrics.
   - **Cross-validation**:
     - `KFold` for splitting data into training and testing sets.

4. **Matplotlib**
   - `pyplot` for plotting the ROC curve.

5. **Math**
   - Core mathematical functions like `sqrt` and `pow`.

6. **Other Modules**
   - `sys`: Used, but the exact functionality implemented in this notebook is unclear.

### Additional Functionalities and Algorithms
1. **Gradient Descent**
   - Custom implementation for logistic regression optimization.
   - Iterative weight updates based on gradients.

2. **Sigmoid Function**
   - Defined explicitly for calculating probabilities.

3. **Manual Logistic Regression**
   - Direct implementation of logistic regression using mathematical formulas and iterations.