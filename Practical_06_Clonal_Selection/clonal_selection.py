import numpy as np

# Generate Dummy Data
def generate_dummy_data(samples=100, features=10):

    data = np.random.rand(samples, features)

    labels = np.random.randint(0, 2, size=samples)

    return data, labels


# AIRS Algorithm
class AIRS:

    def __init__(self,
                 num_detectors=10,
                 hypermutation_rate=0.1):

        self.num_detectors = num_detectors

        self.hypermutation_rate = hypermutation_rate


    # Training
    def train(self, X, y):

        self.detectors = X[
            np.random.choice(
                len(X),
                self.num_detectors,
                replace=False
            )
        ]


    # Prediction
    def predict(self, X):

        predictions = []

        for sample in X:

            distances = np.linalg.norm(
                self.detectors - sample,
                axis=1
            )

            prediction = int(np.argmin(distances))

            predictions.append(prediction)

        return predictions


# Generate Data
data, labels = generate_dummy_data()

# Split Data
split_ratio = 0.8

split_index = int(split_ratio * len(data))

train_data = data[:split_index]

test_data = data[split_index:]

train_labels = labels[:split_index]

test_labels = labels[split_index:]


# Initialize AIRS
airs = AIRS(
    num_detectors=10,
    hypermutation_rate=0.1
)

# Train Model
airs.train(train_data, train_labels)

# Prediction
predictions = airs.predict(test_data)

# Accuracy
accuracy = np.mean(
    predictions == test_labels
)

print(f"Accuracy: {accuracy}")