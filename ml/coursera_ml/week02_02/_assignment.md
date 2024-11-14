# Normalization of features

This task is based on the materials of the lecture on linear classification methods.

## You will learn:

- work with a perceptron, the simplest version of a linear classifier
- improve the quality of a linear model by normalizing features

## Introduction

Linear algorithms are a common class of models that are distinguished by their simplicity and speed of operation. They can be trained in a reasonable time on very large volumes of data, and they can work with any type of features - real, categorical, sparse. In this task, we suggest that you use a perceptron, one of the simplest versions of linear models.
As in the case of metric methods, the quality of linear algorithms depends on some properties of the data. In particular, the features
must be normalized, that is, have the same scale. If this is not the case, and the scale of one feature greatly exceeds the scale of others, then the quality can drop sharply.
One of the ways of normalization is to standardize features. To do this, a set of feature values ​​is taken on all objects, their mean value and standard deviation are calculated. After that, the mean is subtracted from all feature values, and then the resulting difference is divided by the standard deviation.

## Implementation in Scikit-Learn

In the scikit-learn library, linear methods are implemented in the sklearn.linear_model package.
We will work with the perceptron implementation sklearn.linear_model.Perceptron.
As with most models, training is performed using the fit function, and predictions are made using the predict function.
Example of usage:

```python
import numpy as np
from sklearn.linear_model import Perceptron

X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 0])

clf = Perceptron()
clf.fit(X, y)
predictions = clf.predict(X)

```

As a quality metric, we will use the proportion of correct
answers (accuracy). To calculate it, you can use the sklearn.metrics.accuracy_score function, the first argument of which is the vector of correct answers, and the second is the vector of algorithm responses.
To standardize features, it is convenient to use the sklearn.preprocessing.StandardScaler class.
Example of usage:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = np.array([[100.0, 2.0], [50.0, 4.0], [70.0, 6.0]])
X_test = np.array([[90.0, 1.0], [40.0, 3.0], [60.0, 4.0]])

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

```

## Instructions for execution

1. Load the training and test samples from the perceptron-
train.csv and perceptron-test.csv files. The target variable is written in the first column, the features in the second and third.
2. Train the perceptron with standard parameters and random_state=241.

3. Calculate the quality (the proportion of correctly classified objects, accuracy) of the resulting classifier on the test set.

4. Normalize the training and test sets using the
StandardScaler class.

5. Train the perceptron on new sets. Find the proportion of correct answers on the test set.

6. Find the difference between the quality on the test set after normalization and the quality before it. This number will be the answer to the task.

If the answer is a non-integer number, then the integer and fractional parts
must be separated by a period, for example, 0.421. If necessary, round the fractional part to three digits.
The answer to each task is a text file containing the answer in
the first line. Please note that the files you submit must not contain a line break at the end. This is a limitation of the Coursera platform. We are working to remove this limitation.