# Handwritten Digit Recogniser

This project is a **Machine Learning based Handwritten Digit Recognition System** built using Python and Scikit-learn.

The model is trained to recognize handwritten digits from **0 to 9** using image data. It takes an image of a handwritten digit and predicts which number it represents.

The project uses the **MNIST dataset**, one of the most popular datasets for image classification tasks in machine learning.

---

## Dataset

The model is trained using the MNIST dataset which contains:

- 70,000 handwritten digit images
- Each image is 28 × 28 pixels
- Digits from 0 to 9

Dataset split used in this project:

- Training data: 60,000 images
- Testing data: 10,000 images

---

## Technologies Used

- Python
- NumPy
- Matplotlib
- Scikit-learn

---

## Machine Learning Type

This project uses:

- **Supervised Learning**
- **Classification Algorithm**

Algorithm used:

- Logistic Regression

---

## How the System Works

1. Load the handwritten digit dataset
2. Split the dataset into training and testing data
3. Shuffle the training data
4. Train the Logistic Regression model
5. Select a test image
6. Predict the digit
7. Display the image with the predicted number

---

## Example

The program asks the user to choose an image from the test dataset.

Example input:

```
Select a number between 0 and 9999 to select an image: 120
```

The program will:

- Display the handwritten digit image
- Predict the number shown in the image

---

## Project Structure

```
handwritten-digit-recogniser
│
├── digit_recogniser.py
└── README.md
```

---

## Future Improvements

- Implement deep learning using Convolutional Neural Networks (CNN)
- Create a web interface where users can draw digits
- Improve model accuracy
- Deploy the model as a web application

---

## Author

Mayank Rana
