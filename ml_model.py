import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
from sklearn import datasets
from sklearn.model_selection import train_test_split

def rec_dig(image_path):
    digits = datasets.load_digits()
    X = digits.data
    y = digits.target
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state=42, stratify=y)

    print(X_train[0])
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train,y_train)
    print(knn.score(X_test, y_test))
    neighbors = np.arange(1, 9)

    image = Image.open(image_path)

    # Resize the image to 8x8 pixels
    image = image.resize((8, 8), resample=Image.BILINEAR)

    # Convert the image to grayscale
    image = image.convert("L")

    # Extract pixel values into a NumPy array
    numpydata = np.asarray(image)

    # Normalize pixel values to range from 0 to 16
    numpydata = 16 - (numpydata / 255) * 16
    pixel_list = numpydata.flatten()
    # Print the resulting 8x8 array
    pixel_list = [pixel_list]
    print (knn.predict(pixel_list))
    return (knn.predict(pixel_list))

rec_dig('fifthDigit.png')