# linear regression projects

this is a collection of linear regression projects exploring different real world scenarios and datasets. each project demonstrates how linear regression can be applied to predict continuous values based on input features.

## what is this repo?

this repository contains multiple linear regression projects. the goal is to explore and understand linear regression by building models on different types of data. we're learning how to preprocess data, train models, evaluate them, and visualize results.

each project is self contained with its own data, code, and documentation. some use plain python scripts while others use jupyter notebooks for interactive exploration.

## the projects

### 1. student score prediction

predicts exam scores based on study hours, sleep, attendance, and previous performance.

- **type**: plain python script
- **features**: study hours, sleep hours, attendance percentage, previous scores
- **target**: exam score
- **location**: `student_score_prediction/`
- **how to run**: `python main.py` or `./init.sh`

### 2. salary prediction based on experience

predicts salary based on years of work experience with input validation and formatted output.

- **type**: plain python script
- **features**: years of experience
- **target**: salary
- **location**: `salaray_experiance/`
- **how to run**: `python main.py` or `./init.sh`
- **special features**: input validation to ensure valid numbers, salary formatted in thousands

### 3. auto mpg prediction

predicts miles per gallon using multiple car features. this project focuses on data preprocessing and handling messy real world data.

- **type**: jupyter notebook
- **features**: horsepower, weight, cylinders, displacement, acceleration, origin, model year
- **target**: mpg (miles per gallon)
- **location**: `autompg/`
- **how to run**: `jupyter notebook notebook.ipynb` or `./init.sh`
- **special features**: handles corrupt data with `?` values, scaling with StandardScaler, r-squared evaluation

## general structure

each project follows the same structure:

- `main.py` or `notebook.ipynb` - the main script or notebook
- `*_data.csv` or `*.csv` - the dataset
- `req.txt` - list of dependencies
- `init.sh` - setup and run script
- `README.md` - project specific documentation

## common concepts

### data preprocessing

across the projects we learn:
- detecting and handling missing values
- dealing with corrupt or messy data (like `?` marks instead of numbers)
- filling missing values with mean or other strategies
- converting data types when needed

### scaling and normalization

when working with multiple features:
- use StandardScaler from sklearn to scale features
- always fit_transform on training data, then only transform on test data
- never re-fit on test data as it will re-learn from test data

### model evaluation

- **r-squared (r²)**: explains how much variance in the target is explained by the model
- train and test splits: typically 80/20 or 75/25
- comparing actual vs predicted values helps visualize model performance

### visualization

scatter plots and line plots help us:
- compare predictions vs actual values
- see if the model is over or underfitting
- identify outliers or problematic data points

## how to set up a new project

1. create a new folder with a descriptive name
2. add the dataset CSV file
3. write your analysis code (script or notebook)
4. create `req.txt` with all dependencies
5. create `init.sh` to automate setup
6. write a `README.md` explaining the project
7. follow the lowercase, plain language style for documentation

## dependencies (common across projects)

- numpy
- pandas
- scikit-learn
- matplotlib
- jupyter (for notebook based projects)

## future projects

more projects will be added to explore:
- different types of datasets
- different preprocessing techniques
- more complex relationships between features and targets
- visualization techniques

each new project will follow the same structure and documentation style.

## notes

- read the individual project READMEs for specific details about each project
- run the notebooks or scripts to see the models in action
- experiment with the data and try to improve the models
- understand the preprocessing steps as they're often the most important part
