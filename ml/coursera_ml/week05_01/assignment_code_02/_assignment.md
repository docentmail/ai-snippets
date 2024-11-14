# Gradient Boosting over Decision Trees

This task is based on the lecture materials on algorithm compositions.

## You will learn:

- work with gradient boosting and select its hyperparameters
- compare different methods for constructing compositions
- understand in which case it is better to use a random forest, and in which - gradient boosting
- use the log-loss metric

## Introduction

Constructing a composition is an important approach in machine learning, which allows you to combine a large number of weak algorithms into one strong one. This approach is widely used in practice in a variety of tasks.
The lectures discussed the gradient boosting method, which sequentially builds a composition of algorithms, with each subsequent algorithm selected in such a way as to correct the errors of the existing composition. Typically, small-depth trees are used as basic algorithms, since they are fairly easy to construct and, at the same time, they provide nonlinear separating surfaces.

Another method for constructing compositions is a random forest. In it, unlike gradient boosting, individual trees are built independently and without any restrictions on depth - the tree grows until it shows the best quality on the training sample.

In this task, we will deal with a classification problem. As a loss function, we will use log-loss:

![img](_assignment_01.png)

Here, y denotes the true answer, and z denotes the algorithm's prediction. This function is differentiable, and therefore suitable for use in gradient boosting. It can also be shown that
when using it, the final algorithm will approximate the true
class probabilities.

## Implementation in sklearn

In the scikit-learn package, gradient boosting is implemented in the ensemble module in the form of the GradientBoostingClassifier and GradientBoostingRegressor classes. The main parameters that will interest us are: n_estimators, learning_rate.
Sometimes the verbose parameter can be useful for tracking the learning process.
To be able to evaluate the quality of the constructed composition
at each iteration, the class has a staged_decision_function method. For a given sample, it returns an answer at each iteration.
In addition to machine learning algorithms, the scikit-learn package provides a large number of different tools. In this task, we will
suggest using the train_test_split function of the cross_validation module.
It can be used to split samples randomly. Several samples can be passed to the input (provided that they have the same number of rows). Let's say, for example, we have data X and y, where
X is a feature description of objects, y is a target value. Then
the following code will be convenient for splitting this data into training
and test sets:

```Python
X_train , X_test , y_train , y_test =
train_test_split (X,y, test_size =0.33 , random_state=42)
```

Note that with a fixed random_state parameter
the splitting result can be reproduced.
The log-loss metric is implemented in the metrics package.

## Materials

More about gradient boosting and its application to trees

## Data

As part of this task, we will consider a dataset from the Predicting
a Biological Response competition.

## Instructions for implementation

1. Load the sample from the gbm-data.csv file using pandas and convert it to a numpy array (the values ​​parameter of the dataframe).

The first column of the data file records whether a reaction occurred or not.

All other columns (d1 - d1776) contain various characteristics of the molecule, such as size, shape, etc. Split the set
into training and testing using the train_test_split function with the parameters test_size = 0.8 and random_state = 241.
2. Train the GradientBoostingClassifier with the parameters n_estimators=250,
verbose=True, random_state=241 and for each learning_rate
from the list [1, 0.5, 0.3, 0.2, 0.1] do the following:
- Use the staged_decision_function method to predict the quality on the training and test sets at each
iteration.
- Transform the obtained prediction using the formula ![img](_assignment_02.png),
where y_pred is the predicted value.

- Calculate and plot the log-loss values ​​on the training and test samples, and also find the minimum value of the metric and the iteration number at which it is achieved.

3. How does the quality graph behave on the test sample with a decrease in the learning_rate parameter? Note that the smaller the learning_rate, the later the algorithm begins to retrain.

4. On the same data, train RandomForestClassifier with the number of trees equal to the number of iterations at which the best quality is achieved for gradient boosting from the previous point, random_state=241 and the rest of the default parameters.

Round the answer to the third decimal place if necessary.

Note that, although gradient boosting has much weaker base algorithms, it