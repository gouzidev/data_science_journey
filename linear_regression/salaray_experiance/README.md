# salary prediction based on experience

this project uses linear regression to predict salary based on years of work experience.

## what is this?

we're building a model that estimates how much salary someone should get based on how many years of experience they have. we use historical salary data with corresponding experience levels to train the model, then we can input any years of experience and get a predicted salary back.

## how to run it

first install the dependencies:

```
pip install -r req.txt
```

then just run the main script:

```
python main.py
```

or simply use the init script:

```
./init.sh
```

the script will load the salary data, train a linear regression model on experience vs salary, and then prompt you to enter years of experience. it validates your input and keeps asking until you enter a valid number. it will give you a salary prediction based on the trained model, formatted nicely in thousands.

## the data

the CSV file contains salary information with the following columns:
- `YearsExperience`: the number of years of work experience
- `Salary`: the corresponding salary amount

the model learns the relationship between experience and salary to make predictions.

## how it works

1. load the salary dataset from CSV
2. split the data into training (80%) and testing (20%) sets
3. scale the training and testing data using StandardScaler
4. train a linear regression model on the scaled training data
5. make predictions on the test data
6. prompt the user to input years of experience with input validation
7. keep asking for valid input if the user enters something that's not a number
8. predict the salary and format it nicely in thousands

the model helps understand how salary grows with experience and can estimate what salary someone should expect at a given experience level.

## dependencies

- numpy
- pandas
- scikit-learn
- matplotlib

## files

- `main.py` - the main script that trains the model and makes predictions
- `Salary_Data.csv` - dataset with years of experience and salary data
- `req.txt` - list of dependencies
- `init.sh` - setup and run script
