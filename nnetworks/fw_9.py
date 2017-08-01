
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

input_data = np.array([1, 2, 3])
weights = np.array([0, 2, 1])
target = 0
# Set the learning rate: learning_rate
learning_rate = 0.01

n_updates = 20
mse_hist = []



def relu(input):
    '''Define your relu activation function here'''
    # Calculate the value for the output of the relu function: output
    output = max(0, input)

    # Return the value just calculated
    return (output)


# Define predict_with_network()
def predict_with_network(input_data_row, weights):
    # Calculate node 0 value
    node_0_input = (input_data_row * weights['node_0']).sum()
    node_0_output = relu(node_0_input)

    # Calculate node 1 value
    node_1_input = (input_data_row * weights['node_1']).sum()
    node_1_output = relu(node_1_input)

    # Put node values into array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])

    # Calculate model output
    input_to_final_layer = (hidden_layer_outputs * weights['output']).sum()
    model_output = relu(input_to_final_layer)

    # Return model output
    return (model_output)


def get_mse(input_data, target, weights):
    mse = (weights * input_data).sum() - target


    return mse


def get_slope(input_data, target, weights):
    # Calculate the predictions: preds
    preds = (weights * input_data).sum()
    # Calculate the error: error
    error = preds - target
    # Calculate the slope: slope
    slope = 2 * input_data * error
    return slope




# Iterate over the number of updates
for i in range(n_updates):
    # Calculate the slope: slope
    slope = get_slope(input_data, target, weights)

    # Update the weights: weights
    weights = weights - slope * 0.01

    # Calculate mse with new weights: mse
    mse = get_mse(input_data, target, weights)

    # Append the mse to mse_hist
    mse_hist.append(mse)

# Plot the mse history
plt.plot(mse_hist)
plt.xlabel('Iterations')
plt.ylabel('Mean Squared Error')
plt.show()