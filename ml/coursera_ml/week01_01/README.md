# Introduction to Data Analysis and Machine Learning
**Week 01 Part 01**
ass


## Syllabus

Welcome! In the first module of the course, we will introduce the tasks solved by machine learning, define the basic concepts, and introduce necessary notations. Additionally, we will discuss the main Python libraries for data work (NumPy, Pandas, Scikit-Learn) required for the practical assignments throughout the course.

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


## The Assignment

### What Concrete Machine Learning Tasks Were Required to Be Solved in This Assignment

1. **Survival Analysis**:
   - Calculate the proportion of passengers who survived.
2. **Class Distribution**:
   - Determine the percentage of passengers in the first class.
3. **Correlation Analysis**:
   - Compute the Pearson correlation coefficient between `SibSp` (number of siblings/spouses) and `Parch` (number of parents/children).
4. **Feature Extraction**:
   - Extract and identify the most common female name from the passenger dataset.

### What Input Data Is Used in This Task

- **Dataset**: Titanic passenger data (`titanic.csv`) sourced from Kaggle.
- **Key Features Used**:
  - `Sex`: Gender of passengers.
  - `Survived`: Survival status (0 or 1).
  - `Pclass`: Passenger class.
  - `Age`: Age of passengers.
  - `SibSp`: Number of siblings or spouses aboard.
  - `Parch`: Number of parents or children aboard.
  - `Name`: Full name of passengers.

### Technologies and Packages Used

1. **Pandas**:
   - For loading and analyzing tabular data.
2. **NumPy**:
   - Used for numerical calculations and array operations.
3. **SciPy**:
   - Utilized the `pearsonr` function for calculating Pearson correlation.
4. **Regular Expressions**:
   - Applied for parsing and extracting first names from the `Name` column.
   
### Used Technologies and Packages (and Their Specific Parts)

The **Lesson1_1.ipynb** notebook file specifically uses the following packages and components for data analysis:

1. **NumPy (`import numpy as np`)**  
   - Used for numerical operations on arrays, facilitating data manipulation within the notebook.

2. **Pandas (`import pandas`)**  
   - Employed to load, structure, and analyze tabular data in DataFrames.

3. **SciPy (`from scipy.stats import pearsonr`)**  
   - Utilizes `pearsonr` to calculate the Pearson correlation coefficient between two variables.

4. **re (`import re`)**  
   - Applied for regular expressions, lto parse or clean text data.

5. **collections (`import collections`)**  
   - Utilized for data structures that count occurrences or frequencies, supporting data analysis tasks.









