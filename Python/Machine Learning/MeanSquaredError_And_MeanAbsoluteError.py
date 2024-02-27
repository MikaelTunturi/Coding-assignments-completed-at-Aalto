# Course: Machine Learning Supervised Methods
# Quiz 1, Assignment 2

# In this exercise, we want to determine which line is a better fit for the 
# given data points (X,Y) based on Mean Squared Error and Mean Absolute Error.

from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

X = [1,0,0,1,2,2.5,3,4,4,5,5]
Y = [7,1,2,1,2,2,3.5,3.5,5,4,6]
line1 = lambda x: [element + 1 for element in x]
line2 = lambda x: [element + 0.5 for element in x]

# A function for Mean Squared Error.
def my_mse(y_true, y_pred):
    res = 0
    for ii in range(len(y_pred)):
        res += (y_true[ii]-y_pred[ii])**2
    return res/len(y_pred)

# A function for Mean Absolute Error.
def my_mae(y_true, y_pred):
    res = 0
    for ii in range(len(y_pred)):
        res += np.abs(y_true[ii]-y_pred[ii])
    return res/len(y_pred)

# Let's calculate MSE for lines 1 and 2.
mse_res1 = my_mse(Y, line1(X))
mse_res2 = my_mse(Y, line2(X))
if mse_res1 < mse_res2:
    print(f"\033[91mLine1: {mse_res1:.3f}, Line2: {mse_res2:.3f}\033[0m")
    print("\033[1mLine 1 is a better fit for the data w.r.t. Mean Squared Error!\033[0m")
else:
    print("Line 2 is a better fit for the data w.r.t. Mean Squared Error!")

# Let's calculate MAE for lines 1 and 2.
mae_res1 = my_mae(Y, line1(X))
mae_res2 = my_mae(Y, line2(X))
if mae_res1 < mae_res2:
    print("Line 1 is a better fit for the data w.r.t. Mean Absolute Error!")
elif mae_res2 < mae_res1:
    print(f"\033[91mLine1: {mae_res1:.3f}, Line2: {mae_res2:.3f}\033[0m")
    print("\033[1mLine 2 is a better fit for the data w.r.t. Mean Absolute Error!\033[0m")
