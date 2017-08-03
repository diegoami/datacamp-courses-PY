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

def get_new_model():
    # Specify, compile, and fit the model
    model = Sequential()
    model.add(Dense(32, activation='relu', input_shape=(n_cols,)))
    model.add(Dense(2, activation='softmax'))
    return model

# Import the SGD optimizer
from keras.optimizers import SGD


# Create list of learning rates: lr_to_test
lr_to_test = [0.000001, 0.01, 1]

# Loop over learning rates
for lr in lr_to_test:
    print('\n\nTesting model with learning rate: %f\n' % lr)

    # Build new model to test, unaffected by previous models
    model = get_new_model()

    # Create SGD optimizer with specified learning rate: my_optimizer
    my_optimizer = SGD(lr=lr)

    # Compile the model
    model.compile(optimizer=my_optimizer,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Fit the',l
    model.fit(predictors, target)