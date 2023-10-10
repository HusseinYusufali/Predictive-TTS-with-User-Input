import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import ModelCheckpoint
import sys

# Load the text corpus from a text file
with open('Enhanced-Dasher/Data/AAC/sent_train_aac.txt', 'r', encoding='utf-8') as file:
    corpus = file.read()

# Create a set of unique characters in the corpus
unique_chars = sorted(set(corpus))
char_to_int = {char: i for i, char in enumerate(unique_chars)}
int_to_char = {i: char for i, char in enumerate(unique_chars)}

# Define the maximum sequence length
max_sequence_length = 15  # Adjust this value based on your needs

# Create input sequences and their corresponding target characters
sequences = []
next_chars = []
for i in range(0, len(corpus) - max_sequence_length, 1):
    seq = corpus[i:i + max_sequence_length]
    next_char = corpus[i + max_sequence_length]
    sequences.append(seq)
    next_chars.append(next_char)

# Create X and y
X = np.zeros((len(sequences), max_sequence_length, len(unique_chars)), dtype=np.bool)
y = np.zeros((len(sequences), len(unique_chars)), dtype=np.bool)
for i, sequence in enumerate(sequences):
    for t, char in enumerate(sequence):
        X[i, t, char_to_int[char]] = 1
    y[i, char_to_int[next_chars[i]]] = 1

# Build the LSTM model
model = Sequential()
model.add(LSTM(128, input_shape=(max_sequence_length, len(unique_chars))))
model.add(Dense(len(unique_chars), activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Configure checkpoints to save the model during training
checkpoint = ModelCheckpoint('lstm_model.h5', monitor='loss', save_best_only=True)

# Train the model
model.fit(X, y, epochs=100, batch_size=64, callbacks=[checkpoint])

# Save the model
model.save('final_lstm_model.h5')
