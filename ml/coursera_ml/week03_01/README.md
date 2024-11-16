# Support Vector Machine and Logistic Regression
**Week 02 Part 02**\
[Go to the description of the assignment](_assignment.md)\
[Go to Python notebook for the assignment ](assignment_code/assignment.ipynb)

## Syllabus
This module discusses key linear methods like Support Vector Machines (SVM) and Logistic Regression, their applications, and advantages.

- Support Vector Machines
  - SVM for Nonlinear Cases
- **Assignment**: Support Vector Analysis
- **Assignment**: Text Analysis


## Assignment Overview: 

### FIles and folders

**===== task 1 =======**
- **[_assignment.md](assignment_code_01/_assignment.md)**- description of the tasks that need to be solved in the assignment
- **assignment_code**- folder containing solution Python code, dataset and related files
  - **[assignment.ipynb](assignment_code01/assignment.ipynb)** - the Pyhon Notebook with solution


**===== task 2 =======**
- **[_assignment.md](assignment_code_02/_assignment.md)**- description of the tasks that need to be solved in the assignment
- **assignment_code**- folder containing solution Python code, dataset and related files
  - **[assignment.ipynb](assignment_code02/assignment.ipynb)** - the Pyhon Notebook with solution


## Used Technologies and Packages


### task 1
1. **NumPy**
   - Used for numerical computations and creating arrays.
   - Generated grid of `C` values for parameter tuning in SVM (`np.power`).

2. **Pandas**
   - Loaded data and provided dataframe manipulations.

3. **Scikit-learn**
   - **Datasets**:
     - `fetch_20newsgroups`: Loaded the 20 Newsgroups dataset with specific categories.
   - **Feature Extraction**:
     - `TfidfVectorizer`: Transformed text data into TF-IDF representations.
   - **Support Vector Machines**:
     - `SVC`: Implemented SVM with a linear kernel.
   - **Model Selection**:
     - `GridSearchCV`: Performed grid search for hyperparameter tuning.
   - **Cross-validation**:
     - `KFold`: Split data for cross-validation.

4. **Miscellaneous**
   - Accessed the vocabulary and feature mappings of the `TfidfVectorizer`.
   - Extracted coefficients from the trained SVM model to analyze feature importance.



### task 2
1. **NumPy**
   - Used for numerical computations and data manipulation.

2. **Pandas**
   - Read CSV data from a file using `read_csv`.
   - Selected and prepared feature columns (`[['B', 'C']]`) and target labels (`['A']`) for training.

3. **Scikit-learn**
   - **Support Vector Machines**:
     - `SVC`: Implemented an SVM model with a linear kernel and specific hyperparameter `C=100000`.
   - Extracted:
     - Support vectors using the `support_vectors_` attribute.
     - Indices of support vectors using the `support_` attribute.