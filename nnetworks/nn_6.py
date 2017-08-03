# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
import pandas as pd

from nnetworks.nn_t import pred_data,predictors
n_cols = predictors.shape[1]
df = pd.read_csv('titanic.csv')

# Convert the target to categorical: target
target = to_categorical(df.survived)


def get_model():
    # Specify, compile, and fit the model
    model = Sequential()
    model.add(Dense(32, activation='relu', input_shape=(n_cols,)))
    model.add(Dense(2, activation='softmax'))
    return model


model = get_model()
model.compile(optimizer='sgd',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(predictors, target)

# Calculate predictions: predictions
predictions = model.predict(pred_data)

# Calculate predicted probability of survival: predicted_prob_true
predicted_prob_true = predictions[:,1]

# print predicted_prob_true
print(predicted_prob_true)