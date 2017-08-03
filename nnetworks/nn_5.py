# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
import pandas as pd

from nnetworks.nn_t import predictors
n_cols = predictors.shape[1]
df = pd.read_csv('titanic.csv')

# Convert the target to categorical: target
target = to_categorical(df.survived)

# Set up the model
model = Sequential()

# Add the first layer
model.add(Dense(32, activation='relu', input_shape = (n_cols,)))

# Add the output layer
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='sgd',loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(predictors, target)

