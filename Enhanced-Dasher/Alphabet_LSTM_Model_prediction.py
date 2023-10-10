import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Define the maximum sequence length (the same value used during training)
max_sequence_length = 15

# Load the trained model
model = load_model('/Users/husseinyusufali/Desktop/PhD/Main PhD Folder/PhD - Year 2/Technical System Implementation/Predictive TransformerTTS/Enhanced-Dasher/Alphabet_Model/final_lstm_model.h5')

# Read your training data from a text file and extract unique characters
with open('/Users/husseinyusufali/Desktop/PhD/Main PhD Folder/PhD - Year 2/Technical System Implementation/Predictive TransformerTTS/Enhanced-Dasher/Data/AAC/sent_train_aac.txt', 'r') as file:
    training_text = file.read()

# Extract unique characters from the training text
unique_chars = list(set(training_text))

# Define the character mappings (char_to_int and int_to_char)
char_to_int = {char: i for i, char in enumerate(unique_chars)}
int_to_char = {i: char for i, char in enumerate(unique_chars)}

# Function to predict the next character
def predict_next_character(input_sequence):
    # Ensure the input sequence has a length of max_sequence_length
    if len(input_sequence) < max_sequence_length:
        input_sequence = ' ' * (max_sequence_length - len(input_sequence)) + input_sequence
    elif len(input_sequence) > max_sequence_length:
        input_sequence = input_sequence[-max_sequence_length:]

    x = np.zeros((1, max_sequence_length, len(unique_chars)), dtype=np.bool)

    for t, char in enumerate(input_sequence):
        x[0, t, char_to_int[char]] = 1

    prediction = model.predict(x)[0]

    # Get the index of the predicted character
    next_char_index = np.argmax(prediction)
    
    # Map the index back to the character using int_to_char
    next_character = int_to_char[next_char_index]

    return next_character

# Real-time character prediction
input_sequence = "wo"  # Input sequence of varying length
next_character = predict_next_character(input_sequence)
print(f"Input: {input_sequence}, Predicted Next Character: {next_character}")
