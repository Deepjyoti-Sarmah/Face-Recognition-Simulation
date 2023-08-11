import cv2
import numpy as np
import sklearn.metrics as metrics
import seaborn as sns

def hog_features(image):
    """Extract HOG features from an image."""

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    width, height = image.shape
    cell_size = 8
    block_size = 2
    n_bins = 9
    hog_descriptors = []
    for y in range(0, height, cell_size):
        for x in range(0, width, cell_size):
            cell = image[y:y + cell_size, x:x + cell_size]
            gradients = cv2.calcOpticalFlowFarneback(
                np.zeros_like(image), cell, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            magnitude, direction = cv2.cartToPolar(gradients[..., 0], gradients[..., 1])
            hog_descriptor = np.zeros(n_bins * 2 * 2)
            for i in range(cell_size):
                for j in range(cell_size):
                    bin = int(direction[i, j] / (2 * np.pi) * n_bins)
                    hog_descriptor[2 * bin] += magnitude[i, j]
                    hog_descriptor[2 * bin + 1] += 1
            hog_descriptors.append(hog_descriptor)
    return np.array(hog_descriptors)

def train_dnhfaces(hog_features, labels):
    """Train a DnHFaces model on HOG features."""

    dnhfaces = DnHFaces(hog_features.shape[1])
    dnhfaces.fit(hog_features, labels)
    return dnhfaces

def test_dnhfaces(dnhfaces, test_hog_features, test_labels):
    """Test a DnHFaces model on HOG features."""

    predictions = dnhfaces.predict(test_hog_features)
    accuracy = np.mean(predictions == test_labels)
    print("Accuracy:", accuracy)

    # Get the confusion matrix
    confusion_matrix = metrics.confusion_matrix(test_labels, predictions)

    # Plot the confusion matrix
    plt.figure(figsize=(10, 10))
    sns.heatmap(confusion_matrix, annot=True, cmap="Blues")
    plt.show()

if __name__ == "__main__":
    # Load the training data
    training_images = []
    training_labels = []
    for i in range(10):
        image = cv2.imread("face_{}.jpg".format(i))
        training_images.append(image)
        training_labels.append(i)

    # Extract HOG features from the training images
    training_hog_features = np.array([hog_features(image) for image in training_images])

    # Train the DnHFaces model
    dnhfaces = train_dnhfaces(training_hog_features, training_labels)

    # Load the test data
    test_images = []
    test_labels = []
    for i in range(10, 20):
        image = cv2.imread("face_{}.jpg".format(i))
        test_images.append(image)
        test_labels.append(i)

    # Extract HOG features from the test images
    test_hog_features = np.array([hog_features(image) for image in test_images])

    # Test the DnHFaces model
    test_dnhfaces(dnhfaces, test_hog_features, test_labels)