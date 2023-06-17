import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Load the dataset
dataset = pd.read_csv('heart.csv')

# Separate the features (predictor variables) and the target variable
X = dataset.drop('output', axis=1)  # Adjust 'target_variable_name' to your column name
y = dataset['output']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the logistic regression model
model = LogisticRegression(solver='lbfgs', max_iter=1000)

# Fit the model on the training data
model.fit(X_train, y_train)

# Predict on the testing data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:%.2f"%accuracy)

### Getting user input for various features

age = int(input('Enter Your age: '))
sex = int(input('Enter Gender (0 for Female, 1 for Male): '))
cp = int(input('Enter Chest Pain type (0-3): '))
trestbps = int(input('Enter Resting Blood pressure: '))
chol = int(input('Enter Serum Cholesterol Level: '))
fbs = int(input('Enter Fasting Blood Sugar (0 for <= 120mg/dl, 1 for > 120mg/dl): '))
restecg = int(input('Enter Resting Electrocardiographic results (0-2): '))
thalach = int(input('Enter Maximum Heart Rate achieved: '))
exang = int(input('Enter Exercise Induced Angina (0 for no, 1 for yes): '))
oldpeak = float(input('Enter ST Depression Induced by exercise relative to rest: '))
slope = int(input('Enter Slope of the Peak exercise ST segment (0-2): '))
ca = int(input('Enter No. of major vessels (0-3) colored by Fluoroscopy: '))
thal = int(input('Enter Thalassemia (0-3): '))

# Making predictions using the trained model

new_data = [[age, sex, cp, trestbps, chol, fbs, restecg,thalach, exang, oldpeak, slope, ca, thal]]
prediction = model.predict(new_data)
print()

# Displaying the prediction to the user

if prediction == 1:
    print('The patient is likely to have heart disease.')
else:
    print('The patient is unlikely to have heart disease.')
