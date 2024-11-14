# Support objects

This task is based on the materials of lectures on support vector
methods.

## You will learn:

- work with the support vector machine (SVM)
- find the most important objects of the sample

## Introduction

The support vector machine (SVM) is one of the types of linear classifiers. The functionality that it optimizes is aimed at maximizing the width of the dividing band between classes. From the theory of statistical learning, it is known that this width is closely related to the generalizing ability of the algorithm, and its maximization
allows you to combat overfitting.
The support vector machine has another feature. If we transform its optimization problem, it turns out that the final classifier can be represented as a weighted sum of scalar products of a given object with objects of the training sample:
In essence, the algorithm makes predictions based on the similarity of a new
object with objects of the training sample. At the same time, as a rule, not all coefficients are non-zero. This means that
classification is made based on similarity with only a part of the training
objects. Such objects are called support.

## Implementation in Scikit-Learn

The support vector method is implemented in the sklearn.svm.SVC class.
The main parameters of this class are the coefficient C and the
kernel type kernel. In this task, we will use a linear kernel
- to do this, set the parameter value kernel=’linear’ The indices of the trained classifier’s support objects are stored in the support_ field

## Instructions for execution

1. Load the sample from the svm-data.csv file. It contains a two-dimensional sample (the target variable is specified in the first column, the features are in the second and third).

2. Train the classifier with a linear kernel, parameter C = 100000
and random_state=241. This parameter value should be used to ensure that SVM works with the sample as linearly separable. With lower parameter values, the algorithm will be tuned taking into account the term in the functional that penalizes for small indents, due to which the result may not coincide with the solution of the classic SVM problem for a linearly separable sample. 3. Find the numbers of the objects that are the reference (numbering from one). They will be the answer to the task. Please note that the answer must be the numbers of the objects in ascending order, separated by commas. The numbering starts with 1. The answer to each task is a text file containing the answer in the first line. Please note that the files sent must not contain a line break at the end. This nuance is a limitation of the Coursera platform. We are working to remove this limitation.