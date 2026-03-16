import sklearn
from sklearn.datasets import fetch_openml
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# Load MNIST dataset
mnist = fetch_openml('mnist_784', version=1)
x, y = mnist['data'], mnist['target']

# Randomly select a digit image
#random_digit_index = random.randint(0, 69999)  # Adjust the range to the dataset size
#random_digit = x.iloc[random_digit_index].to_numpy()  # Use .iloc to access row, then convert to numpy array
#some_random_digit = random_digit.reshape(28, 28)
#plt.imshow(some_random_digit, cmap=matplotlib.cm.binary)
#plt.show()

# Train-test split
x_train, x_test = x[:60000], x[60000:70000]
y_train, y_test = y[:60000], y[60000:70000]

# Shuffle the training set
shuffle_index = np.random.permutation(60000)
x_train, y_train = x_train.iloc[shuffle_index], y_train.iloc[shuffle_index]

# Train a Logistic Regression model
model = LogisticRegression(tol=0.1, max_iter=2000)
model.fit(x_train, y_train)

# Select a test image based on user input
test_num = int(input("Select a number between 0 and 9999 to select an image: "))
test_image_data = x_test.iloc[test_num].to_numpy()  # Use .iloc for row access
test_image = test_image_data.reshape(28, 28)

# Make a prediction
prediction = model.predict([test_image_data])

# Display the test image and its prediction
plt.imshow(test_image, cmap=matplotlib.cm.binary)
plt.title(f"Selected image number: {test_num}")
plt.xlabel(f"The image has been classified as: {prediction[0]}")
plt.show()
