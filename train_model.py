import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Load the data from the saved file
with open('Data/test_data.pickle', 'rb') as f:
    training_data = pickle.load(f)

# Split the data into input and output arrays
X = np.array([data[0] for data in training_data])
y = np.array([[data[1], data[2], data[3]] for data in training_data])

# Preprocess the input data
X = X.astype('float32')
X /= 255

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the CNN model architecture
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(270, 480, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(3, activation='linear'))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model on the training data
print('Training Started')
model.fit(X_train, y_train, batch_size=32, epochs=10, validation_data=(X_test, y_test))

# Evaluate the model on the testing data
loss = model.evaluate(X_test, y_test)
print(f'Test loss: {loss}')

# Save the trained model
model.save('model.h5')
