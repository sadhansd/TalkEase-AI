import tensorflow as tf
from tensorflow.keras import layers, models
import pickle

# Create and train a CNN model (replace this with your actual model)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model (replace X_train and y_train with your data)
model.fit(X_train, y_train, epochs=10)

# Save the trained model to a pickle file
with open('model.pickle', 'wb') as model_file:
    pickle.dump(model, model_file)
