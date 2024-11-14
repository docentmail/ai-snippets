# Metric Classification Methods
**Week 02 Part 01**

## Syllabus


Metric methods classify based on similarity, enabling them to work with complex-structured data as long as distances can be measured between objects. This module introduces the k-Nearest Neighbors method and regression generalization using kernel smoothing.

- Metric Methods
  - Nearest Neighbor Method
  - Parzen Window Method
  - Metric Methods for Regression Tasks
  - Outlier Detection
- **Assignment**: Choosing the Number of Neighbors
- **Assignment**: Choosing the Metric



## Assignment Overview: Machine Learning Technologies

### What Concrete Machine Learning Tasks Were Required to Be Solved in This Assignment
1. Implement the **k-Nearest Neighbors (kNN)** algorithm to classify data into specific categories.
2. Tune the parameter \( k \) (number of neighbors) to optimize classification accuracy using:
   - **Cross-validation** with 5-fold validation.
3. Measure and compare classification accuracy before and after feature scaling.
4. Identify the optimal \( k \) values and evaluate how scaling affects model performance.

### What Input Data Is Used in This Task
- **Dataset**: The Wine dataset from the UCI Machine Learning Repository.
   - **Features**: Results of chemical analyses (e.g., alcohol content, acidity).
   - **Target Classes**: Grape varieties (three distinct categories).
   - **Structure**:
      - The first column contains the target class.
      - Columns 2 through the last include feature values.



### Used Technologies and Packages

- **pandas**: Used for data manipulation and analysis, including loading and processing data in tabular form.
- **numpy**: Utilized for numerical operations, likely for efficient computation of arrays or matrices.
- **sklearn**: A general import indicating usage of scikit-learn functionalities.
  - **sklearn.model_selection**: Used for splitting the dataset into training and testing sets, possibly involving cross-validation methods.
  - **sklearn.neighbors**: Indicates the use of machine learning models based on nearest neighbors, likely for classification or regression tasks.
- **collections**: Standard library module used for specialized container datatypes.