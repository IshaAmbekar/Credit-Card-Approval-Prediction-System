# -*- coding: utf-8 -*-
"""ML Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mzPF8w0YMRgAWJ8KQuZrO-5aVuPvxxSH
"""

# Import pandas
import pandas as pd
 
# Load dataset
cc_apps = pd.read_csv("/content/credit_card_approval.data")
cc_apps.columns=['Gender','Age','Debt','Married','BankCustomer','EducationLevel','Ethnicity','YearsEmployed','PriorDefault','Employed','CreditScore','DriversLicense','Citizen','ZipCode','Income','Approved']

# Print summary statistics
cc_apps_description = cc_apps.describe()
print(cc_apps_description)
 
print("\n")
 
# Print DataFrame information
cc_apps_info = cc_apps.info()
print(cc_apps_info)
 
print("\n")
 
# Inspect missing values in the dataset
print(cc_apps.tail(50))
 
 
# Import numpy
import numpy as np# Impute the missing values with mean imputation
cc_apps = cc_apps.fillna(cc_apps.mean())
 
# Count the number of NaNs in the dataset to verify
print(cc_apps.isnull().values.sum())  
 
 
# Inspect missing values in the dataset
print(cc_apps.isnull().values.sum())
 
# Replace the '?'s with NaN
cc_apps = cc_apps.replace("?",np.NaN)
 
# Inspect the missing values again
print(cc_apps.tail(50))
 
# Iterate over each column of cc_apps
 
for col in cc_apps.columns:
    # Check if the column is of object type
    if cc_apps[col].dtypes == 'object':
        # Impute with the most frequent value
        cc_apps[col] = cc_apps[col].fillna(cc_apps[col].value_counts().index[0])
 
# Count the number of NaNs in the dataset and print the counts to verify
print(cc_apps.isnull().values.sum())
 
# Import LabelEncoder
from sklearn.preprocessing import LabelEncoder
 
# Instantiate LabelEncoder
le = LabelEncoder()
 
# Iterate over all the values of each column and extract their dtypes
for col in cc_apps.columns:
    # Compare if the dtype is object
    if cc_apps[col].dtype=='object':
    # Use LabelEncoder to do the numeric transformation
        cc_apps[col]=le.fit_transform(cc_apps[col])
# Import MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
 
# Drop features 10 and 13 and convert the DataFrame to a NumPy array
cc_apps = cc_apps.drop([cc_apps.columns[11],cc_apps.columns[13]], axis=1)
print(cc_apps)
 
cc_apps = cc_apps.values
 
# Segregate features and labels into separate variables
X,y = cc_apps[:,0:13], cc_apps[:,13]
 
# Instantiate MinMaxScaler and use it to rescale
scaler = MinMaxScaler(feature_range=(0,1))
rescaledX = scaler.fit_transform(X)
rescaledX
 
# Import train_test_split
from sklearn.model_selection import train_test_split
 
# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(rescaledX,
                                                    y,
                                                    test_size=0.33,
                                                    random_state=42)
# Import LogisticRegression
from sklearn.linear_model import LogisticRegression
 
# Instantiate a LogisticRegression classifier with default parameter values
logreg = LogisticRegression()
 
# Fit logreg to the train set
logreg.fit(X_train,y_train)
 
# Import confusion_matrix
from sklearn.metrics import confusion_matrix
# Use logreg to predict instances from the test set and store it
y_pred = logreg.predict(X_test)
 
# Get the accuracy score of logreg model and print it
print("Accuracy of logistic regression classifier: ", logreg.score(X_test, y_test))
# Print the confusion matrix of the logreg model
print(confusion_matrix(y_test, y_pred))
 
import seaborn as sns
import matplotlib.pyplot as plt
ax = sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='Blues')
 
ax.set_title('Credit Card Approval Confusion Matrix by Logistic Regression\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');
 
## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])
 
## Display the visualization of the Confusion Matrix.
plt.show()
 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
model = DecisionTreeClassifier(max_depth=12,
                               min_samples_split=8,
                               random_state=1024)
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
 
print('Accuracy Score is {:.5}'.format(accuracy_score(y_test, y_predict)))
print(pd.DataFrame(confusion_matrix(y_test,y_predict)))
ax = sns.heatmap(confusion_matrix(y_test, y_predict), annot=True, cmap='Blues')
 
ax.set_title('Credit Card Approval Confusion Matrix by Decision Tree\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');
 
## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])
 
## Display the visualization of the Confusion Matrix.
plt.show()

!pip install colorama

from colorama import Fore, Back
 
gender=input("Are you male?\n\n")
age=input("\n\nWhat is your age?\n\n")
Debt=input("\n\nWhat is your Debt?\n\n")
Married=input("\n\nAre you married?\n\n")
BankCustomer=input("\n\nAre you a bank customer?\n\n")
EducationLevel=input("\n\nWhat is your Education Level?\n\n")
Ethnicity=input("\n\nWhat is your Ethnicity?\n\n")
YearsEmployed=input("\n\nHow many years were you employed?\n\n")
PriorDefault=input("\n\nDo you have any Prior defaults?\n\n")
Employed=input("\n\nAre you Employed?\n\n")
CreditScore=input("\n\nWhat is your Credit Score?\n\n")
Citizen=input("\n\nWhat is your Citizenship?\n\n")
Income=input("\n\nWhat is your Income?\n\n")
new_input=[[gender, age, Debt, Married, BankCustomer,EducationLevel,Ethnicity,YearsEmployed,PriorDefault,Employed,CreditScore,Citizen,Income]]
 
new_output=logreg.predict(new_input)
print(new_output)
print("By Logistic Regression")
if (new_output==1):
  print(Fore.WHITE, Back.GREEN +"Congratulations your credit card application has been approved")
else:
  print(Fore.RED +"We regret to inform you that your credit card application is declined.")
 
NEW_output=model.predict(new_input)
print(NEW_output)
print("By Decision Tree")
if (NEW_output==1):
  print(Fore.WHITE, Back.GREEN +"Congratulations your credit card application has been approved")
else:
  print(Fore.RED +"We regret to inform you that your credit card application is declined.")