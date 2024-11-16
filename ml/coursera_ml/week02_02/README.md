# Linear Classification Methods
**Week 02 Part 02**\
[Go to the description of the assignment](_assignment.md)\
[Go to Python notebook for the assignment ](assignment_code/assignment.ipynb)

## Syllabus

Linear models are one of the most studied classes of algorithms in machine learning. They are scalable and widely used for large datasets. This module covers stochastic gradient methods for linear classifier tuning, regularization, and practical nuances of linear methods.

- Linear Classification Methods
  - Stochastic Gradient Method
  - Gradient Numerical Minimization and SG Algorithms
  - Overfitting Problem
- **Assignment**: Feature Normalization


## Assignment Overview: 

### FIles and folders
- **[_assignment.md](_assignment.md)**- description of the tasks that need to be solved in the assignment
- **assignment_code**- folder containing solution Python code, dataset and related files
  - **[assignment.ipynb](assignment_code/assignment.ipynb)** - the Pyhon Notebook with solution



## Used Technologies and Packages

### Python Libraries and Packages
1. **NumPy**
   - Utilized for numerical operations and data handling.

2. **Pandas**
   - Loaded training and testing datasets from CSV files using `read_csv`.
   - Selected specific columns for features and labels.

3. **Scikit-learn**
   - **Preprocessing**:
     - `StandardScaler`: Standardized features by removing the mean and scaling to unit variance.
   - **Linear Models**:
     - `Perceptron`: Implemented a perceptron model for binary classification.
   - **Metrics**:
     - `accuracy_score`: Evaluated model accuracy on the test set.