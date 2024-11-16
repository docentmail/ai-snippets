<p style="font-size: 26px;"> "Data Analysis and Machine Learning" Coursera.com. 8 weeks. </p>

**[<span style="color: green;">View certificate</span>](https://www.coursera.org/account/accomplishments/certificate/VY63EBXE35FR)**.

** Table of Contents **
- [Syllabus overview](#syllabus-overview)
- [Introduction to Data Analysis and Machine Learning](#introduction-to-data-analysis-and-machine-learning)
- [Logical Classification Methods](#logical-classification-methods)
- [Metric Classification Methods](#metric-classification-methods)
- [Linear Classification Methods](#linear-classification-methods)
- [Support Vector Machine and Logistic Regression](#support-vector-machine-and-logistic-regression)
- [Logistic Regression](#logistic-regression)
- [Classification Quality Metrics](#classification-quality-metrics)
- [Linear Regression](#linear-regression)
- [Dimensionality Reduction and Principal Component Analysis](#dimensionality-reduction-and-principal-component-analysis)
- [Algorithm Ensembles](#algorithm-ensembles)
- [Neural Networks](#neural-networks)
- [Clustering and Visualization](#clustering-and-visualization)
- [Semi-Supervised Learning](#semi-supervised-learning)
- [Machine Learning in Practical Applications](#machine-learning-in-practical-applications)
- [The final task. Subject area: Dota 2 game](#the-final-task-subject-area-dota-2-game)

# Syllabus overview

- **Logical Classification Methods**: Decision Tree  
- **Metric Classification Methods**: Nearest Neighbor, Parzen Window  
- **Linear Classification Methods**:  
  - Stochastic Gradient  
  - Gradient Numerical Minimization Methods  
  - SG6, SAG3 Algorithms  
  - Feature Normalization  
- **Dimension Reduction and Principal Component Analysis**  
- **Linear Regression**:  
  - Singular Value Decomposition  
  - Ridge Regression  
  - LASSO  
- **Compositions of Algorithms**:  
  - Bagging and Random Forest  
  - Gradient Boosting: Modifications and Heuristics  
- **Neural Networks**:  
  - Backpropagation  
  - Standard Heuristics  
- **Clustering and Visualization**:  
  - Hierarchical Clustering  
  - Nonlinear Dimensionality Reduction Methods  
- **Partial Training**: Applying Clustering and Classification to Partial Learning Problems

Python, numpy, pandas, GradientBoostingClassifier, LogisticRegression, sklearn.cross_validation, StandardScaler, json, bz2, AUC-ROC, datetime, scipy.sparse, sklearn.ensemble, sklearn.grid_search, sklearn.linear_model, sklearn.preprocessing, warnings, train_test_split, numpy, log_loss, GradientBoostingClassifier, matplotlib, RandomForestClassifier, RandomForestRegressor, KFold, PCA, DictVectorizer, TfidfVectorizer, hstack, Ridge, SVC, accuracy_score, roc_auc_score, precision_recall_curve, Scikit-learn, Matplotlib, Math, Sys, sklearn.model_selection, sklearn.neighbors, collections, klearn.tree.DecisionTreeClassifier, matplotlib.pyplot, sklearn.metrics.accuracy_score, SciPy.stats.pearsonr, re, collections


# Introduction to Data Analysis and Machine Learning
**Go to [Week 01 Part 01](week01_01/README.md)**

Welcome! In the first module of the course, we will introduce the tasks solved by machine learning, define the basic concepts, and introduce necessary notations. Additionally, we will discuss the main Python libraries for data work (NumPy, Pandas, Scikit-Learn) required for the practical assignments throughout the course.\
Pandas, NumPy, SciPy.stats.pearsonr, re, collections


- **Welcome**
  - Introduction and course overview
- **Introduction**
  - Formal definition of machine learning tasks
  - Examples of machine learning applications
  - Overfitting problem and methodology for solving machine learning tasks
- **Tools Overview**
  - Python for data analysis
  - Working with vectors and matrices in NumPy
  - **Assignment**: Data preprocessing in Pandas

# Logical Classification Methods
**Go to [Week 01 Part 02](week01_02/README.md)**

Logical methods classify objects based on simple rules, making them interpretable and easy to implement. Combined into ensembles, they can solve many tasks with high quality. This module covers decision trees and their combination into ensembles known as random forests.\
numpy, pandas, sklearn.tree.DecisionTreeClassifier, matplotlib.pyplot, sklearn.metrics.accuracy_score


- Decision Trees
- Decision Tree Construction Algorithm
- Handling Missing Values, Advantages, and Disadvantages of Decision Trees
- Addressing Decision Tree Limitations
- **Assignment**: Feature Importance

# Metric Classification Methods
**Go to [Week 02 Part 01](week02_01/README.md)**

Metric methods classify based on similarity, enabling them to work with complex-structured data as long as distances can be measured between objects. This module introduces the k-Nearest Neighbors method and regression generalization using kernel smoothing.\
pandas, numpy, sklearn, sklearn.model_selection, sklearn.neighbors, collections


- Metric Methods
  - Nearest Neighbor Method
  - Parzen Window Method
  - Metric Methods for Regression Tasks
  - Outlier Detection
- **Assignment**: Choosing the Number of Neighbors
- **Assignment**: Choosing the Metric

# Linear Classification Methods
**Go to [Week 02 Part 02](week02_02/README.md)**


Linear models are one of the most studied classes of algorithms in machine learning. They are scalable and widely used for large datasets. This module covers stochastic gradient methods for linear classifier tuning, regularization, and practical nuances of linear methods.\
NumPy, Pandas, Scikit-learn

- Linear Classification Methods
  - Stochastic Gradient Method
  - Gradient Numerical Minimization and SG Algorithms
  - Overfitting Problem
- **Assignment**: Feature Normalization

# Support Vector Machine and Logistic Regression
**Go to [03 Part 01](week03_01/README.md)**

This module discusses key linear methods like Support Vector Machines (SVM) and Logistic Regression, their applications, and advantages.\
NumPy, Pandas, Scikit-learn, 

- Support Vector Machines
  - SVM for Nonlinear Cases
- **Assignment**: Support Vector Analysis
- **Assignment**: Text Analysis

# Logistic Regression
**Go to [Week 03 Part 02](week03_02/README.md)**\
NumPy, Pandas, Scikit-learn, Matplotlib, Math, Sys

- Logistic Regression
- Regularized Logistic Regression
- **Assignment**: Logistic Regression

# Classification Quality Metrics
**Go to [Week 03 Part 03](week03_03/README.md)**

In machine learning, there are numerous quality metrics, each with its own practical interpretation and focus on measuring a specific aspect of a solution. In this module, we will discuss the various metrics for binary and multiclass classification and explore methods for reducing multiclass problems to binary classification tasks.\
pandas, SVC, accuracy_score, roc_auc_score, precision_recall_curve


Quality Metrics

Quality Metrics in Classification
- Resume: Quality Metrics in Classification
- Multiclass Classification 
- Quiz: Classification Quality Metrics
- **Assignment**: Classification Quality Metrics


# Linear Regression
**Go to [Week 04 Part 01](week04_01/README.md)**

This module explores linear models for regression and their connection to singular value decomposition of the object-feature matrix.\
pandas, DictVectorizer, TfidfVectorizer, hstack, Ridge


- Solving Multidimensional Linear Regression with SVD
- Ridge Regression
- LASSO Method
- **Assignment**: Predicting Salary Based on Job Descriptions

# Dimensionality Reduction and Principal Component Analysis
**Go to [Week 04 Part 02](week04_02/README.md)**

Dimensionality reduction is crucial for practical applications, such as speeding up model performance. This module covers feature selection approaches and Principal Component Analysis (PCA).\
pandas, PCA, numpy

- Principal Component Analysis
- **Assignment**: Stock Index Compilation

# Algorithm Ensembles
**Go to [Week 05 Part 01](week05_01/README.md)**

Combining multiple models into ensembles can significantly improve overall quality. This module discusses the basics of ensembles and gradient boosting.\
pandas, train_test_split, numpy, log_loss, GradientBoostingClassifier, matplotlib, RandomForestClassifier, RandomForestRegressor, KFold


- Bagging and Random Forest
- Gradient Boosting
  - Modifications and Heuristics
- **Assignment**: Random Forest Size
- **Assignment**: Gradient Boosting with Decision Trees

# Neural Networks
**Go to [Week 05 Part 02](week05_02/README.md)**

Neural networks solve complex nonlinear tasks, such as image and speech recognition. This module introduces multilayer neural networks, backpropagation, and deep network architectures.

- Introduction to Neural Networks
- Backpropagation
- Standard Heuristics
- **Quiz**: Neural Networks

# Clustering and Visualization
**Go to [Week 06 Part 01](week06_01/README.md)**


Unsupervised learning focuses on identifying patterns in data. This module covers clustering and visualization techniques.

- Clustering
- Hierarchical Clustering
- Nonlinear Dimensionality Reduction Methods
- **Assignment**: Reducing Image Color Count
  Python, numpy, imread, skimage, KMeans, pprint, matplotlib

# Semi-Supervised Learning
**Go to [Week 06 Part 02](week06_02/README.md)**

Semi-supervised learning lies between supervised learning and clustering, handling datasets where the target variable is known for only part of the objects.

- Semi-Supervised Learning Overview
- Applying Clustering and Classification to Semi-Supervised Problems

# Machine Learning in Practical Applications
**Go to [Week 07](week07/README.md)**

This module summarizes the course, reviews data analysis stages, and explores practical tasks to prepare for the final project./
GradientBoostingClassifier, LogisticRegression, sklearn.cross_validation, StandardScaler, numpy, pandas, json, bz2, AUC-ROC, datetime, scipy.sparse, sklearn.ensemble, sklearn.grid_search, sklearn.linear_model, sklearn.preprocessing, warnings



- Data Analysis Stages
- Handling Numerical and Text Features
- Data Preprocessing
- Quality Evaluation
- Algorithm Overview
- **Assignment**: Predicting Winners in Online Games

# The final task. Subject area: Dota 2 game


**What concrete machine learning tasks were required to be solved in this assignment**
- Predict the outcome of a Dota 2 match (which team will win: Radiant or Dire) based on data from the first five minutes of gameplay.

**Technologies and Packages Used**
sklearn.ensemble.GradientBoostingClassifier, sklearn.linear_model.LogisticRegression, sklearn.cross_validation, sklearn.preprocessing.StandardScaler, numpy, pandas, json, bz2