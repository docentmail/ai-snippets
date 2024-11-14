# Data Preprocessing in Pandas

This assignment is designed to introduce you to tools that will be useful in future practical assignments.  

You will learn to:  
- Work with data using Python and the Pandas package  
- Perform data preprocessing  
- Find simple patterns in data  

## Introduction  

Currently, Python is one of the most widely used programming languages. One of its advantages is the large number of packages available to solve a wide range of tasks. In our course, we recommend using the **Pandas**, **NumPy**, and **SciPy** libraries, which simplify reading, storing, and processing data. In future work, you will also become familiar with the **Scikit-Learn** package, which implements many machine learning algorithms.  

## Getting Started  

To start working with data, you must first load it from a file. In this assignment, we will work with data in **CSV format**, which is intended for storing tabular data: columns are separated by commas, and the first row contains the column names.  

**Example of loading data into Pandas**:  

```python
import pandas

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
