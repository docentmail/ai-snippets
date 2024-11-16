# Semi-Supervised Learning
**Week 06 Part 02**\
[Go to the description of the assignment](_assignment.md)\
[Go to Python notebook for the assignment ](assignment_code/assignment.ipynb)

## Syllabus
Semi-supervised learning lies between supervised learning and clustering, handling datasets where the target variable is known for only part of the objects.

- Semi-Supervised Learning Overview
- Applying Clustering and Classification to Semi-Supervised Problems

## Assignment Overview: 

### FIles and folders
- **[_assignment.md](_assignment.md)**- description of the tasks that need to be solved in the assignment
- **assignment_code**- folder containing solution Python code, dataset and related files
  - **[assignment.ipynb](assignment_code/assignment.ipynb)** - the Pyhon Notebook with solution



# Used Technologies and Packages

### Python Libraries and Packages
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