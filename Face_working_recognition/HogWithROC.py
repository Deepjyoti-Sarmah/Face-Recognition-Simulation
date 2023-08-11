import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from skimage.feature import hog
from sklearn.metrics import confusion_matrix, roc_curve, auc
import seaborn as sns

# Load the digits dataset
digits = load_digits()

# Extract features and labels
X = digits.images
y = digits.target

# Convert images to grayscale
X_gray = [color.rgb2gray(image) for image in X]

# Compute HOG features
hog_features = [hog(image) for image in X_gray]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(hog_features, y, test_size=0.2, random_state=42)

# Train a Support Vector Machine (SVM) classifier
clf = SVC(probability=True)  # Set probability=True for ROC curve
clf.fit(X_train, y_train)

# Predict the probabilities for the testing set
y_probs = clf.predict_proba(X_test)

# Compute ROC curve and AUC
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(len(digits.target_names)):
    fpr[i], tpr[i], _ = roc_curve((y_test == i).astype(int), y_probs[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Plot ROC curve
plt.figure(figsize=(8, 6))
for i in range(len(digits.target_names)):
    plt.plot(fpr[i], tpr[i], label=f'Class {i} (AUC = {roc_auc[i]:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.show()

# Predict the labels for the testing set
y_pred = clf.predict(X_test)

# Compute the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Visualize the confusion matrix using Seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d", xticklabels=digits.target_names, yticklabels=digits.target_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Ma