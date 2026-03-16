# MNIST Digit Classifier

This project is a **Machine Learning based Handwritten Digit Recognition System** built using Python and Scikit-learn.

The model is trained on the famous **MNIST dataset**, which contains thousands of handwritten digit images from 0–9.

The system classifies a handwritten digit image and predicts which number it represents.

---

## Dataset

This project uses the **MNIST Dataset**, a popular dataset used in machine learning and computer vision research.

The dataset contains:

- 70,000 handwritten digit images
- Each image is 28 × 28 pixels
- Digits range from 0 to 9

Split used in this project:

- Training set: 60,000 images
- Test set: 10,000 images

---

## Technologies Used

- Python
- NumPy
- Matplotlib
- Scikit-learn

---

## Machine Learning Algorithm

This project uses:

- **Supervised Learning**
- **Classification Algorithm**

Algorithm used:

- Logistic Regression

---

## How the Model Works

1. Load the MNIST dataset using Scikit-learn
2. Split the dataset into training and testing sets
3. Shuffle the training data
4. Train a Logistic Regression model
5. Select a test image
6. Predict the digit using the trained model
7. Display the image and predicted label

---

## Example

The program allows the user to select an image index from the test dataset.

Example:

```
Select a number between 0 and 9999 to select an image: 145
```

The system will:

- Display the handwritten digit image
- Predict the digit value

---

## Project Structure

```
mnist-digit-classifier
│
├── digit_classifier.py
└── README.md
```

---

## Future Improvements

- Use Convolutional Neural Networks (CNN)
- Build a web interface for drawing digits
- Improve accuracy with deep learning models
- Deploy the model as a web application

---

## Author

Mayank Rana
