# Import necessary modules
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd


# Read the CSV file into a DataFrame: df
df = pd.read_csv('../data/diabetes.csv')
X = df.drop('diabetes', axis=1).values
y = df['diabetes']
df_columns = df.drop('diabetes', axis=1).columns

# Create training and test set
X_train, X_test, y_train, y_test = train_test_split(X,y , test_size = 0.4, random_state=42)


# Instantiate a k-NN classifier: knn
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Predict the labels of the test data: y_pred
y_pred = knn.predict(X_test)

# Generate the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
