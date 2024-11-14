# Selection of the Number of Neighbors

This task is based on lectures on metric methods and is dedicated to selecting the number of neighbors in the kNN method.

## You will learn to:
- Work with the k-nearest neighbors method
- Select the parameter \( k \)
- Properly prepare data before using this method

---

## Introduction

Metric methods are based on the compactness hypothesis, which states that objects with similar feature descriptions have similar target variable values. If this hypothesis holds, predictions for a new object can be built based on objects close to it from the training sample — for example, by averaging their responses (for regression) or by selecting the most common class among them (for classification). Such methods are called metric methods and have several characteristics:

- The training procedure is essentially absent — it is sufficient to remember all objects in the training sample.
- It is possible to use a metric that accounts for the specific features of the dataset — for instance, the presence of categorical (nominal) features.
- With the correct metric choice and a sufficiently large training sample, metric algorithms demonstrate quality close to optimal.

Metric methods are sensitive to feature scales. For example, if the scale of one feature significantly exceeds the scales of other features, its values will have little impact on the algorithm's predictions. Therefore, feature scaling is essential. Usually, this is done by subtracting the mean feature value and dividing by the standard deviation.

---

## Implementation in Scikit-Learn

The k-nearest neighbors method is implemented in the `sklearn.neighbors.KNeighborsClassifier` class. The main parameter is `n_neighbors`, which defines the number of neighbors to consider for predictions.

### Cross-Validation

You will need to perform block-based cross-validation. Cross-validation involves splitting the dataset into \( m \) non-overlapping blocks of approximately equal size, followed by \( m \) steps. At the \( i \)-th step, the \( i \)-th block serves as the test sample, while the union of all other blocks serves as the training sample. On each step, the algorithm trains on a specific training sample and computes its quality on the test sample. After \( m \) steps, \( m \) quality metrics are obtained, and their average gives the cross-validation score. For more details, refer to the video "Overfitting Problem. Machine Learning Task Methodology" from the first module or consult Wikipedia (in Russian or English) or the Scikit-Learn documentation.

Cross-validation is performed in two stages:

1. Create a split generator using `sklearn.cross_validation.KFold`, which sets up training and validation splits. The number of blocks is defined by the `n_folds` parameter. Note that the order of objects in the dataset may not be random, potentially biasing the cross-validation score. To address this, shuffle the objects before splitting by passing the `shuffle=True` parameter to the `KFold` generator.

2. Compute the error for all splits using the `sklearn.cross_validation.cross_val_score` function. The `estimator` parameter specifies the classifier, and the `cv` parameter specifies the split generator from the previous step. Use the `scoring` parameter to define the quality metric; by default, classification tasks use accuracy. The function returns an array of scores that should be averaged.

---

## Feature Scaling

Feature scaling can be performed using the `sklearn.preprocessing.scale` function. Provide the feature matrix as input to obtain a scaled matrix where each column has a mean of zero and a standard deviation of one.

---

## Task Instructions

In this task, you need to select the optimal value of \( k \) for the kNN algorithm. Use the Wine dataset, where the goal is to predict the grape variety from which the wine is made based on chemical analysis results.

### Steps to Complete:

1. Download the Wine dataset from [this link](https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data).

2. Extract features and classes from the data. The class is recorded in the first column (three variants), and features are in the columns from the second to the last. More details about the features are available [here](https://archive.ics.uci.edu/ml/datasets/Wine).

3. Perform quality assessment using 5-fold cross-validation. Create a split generator that shuffles the dataset before forming blocks (`shuffle=True`). To ensure reproducibility, create the `KFold` generator with the fixed parameter `random_state=42`. Use accuracy as the quality metric.

4. Compute classification accuracy for kNN (using `sklearn.neighbors.KNeighborsClassifier`) for \( k \) values from 1 to 50. What value of \( k \) gives the optimal quality? What is the quality score (a number between 0 and 1)? These are the answers to questions 1 and 2.

5. Perform feature scaling using the `sklearn.preprocessing.scale` function. Recompute the optimal \( k \) value after scaling.

6. What value of \( k \) is optimal after feature scaling? How did the quality score change? Provide answers to questions 3 and 4.

**Note:** If the answer is a non-integer, separate the integer and fractional parts with a dot (e.g., 0.5). Round the fractional part to two decimal places if necessary.

**Output Requirements:** Submit a text file with the answer in the first line. Ensure the file does not contain an empty line at the end, as this is a platform limitation in Coursera.
