import streamlit as st
import random
import numpy as np
from datasets import load_dataset
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io

# Load the dataset
@st.cache_data
def load_kannada_dataset():
    return load_dataset("Hemanth-thunder/english-to-kannada-mt")

# Load the dataset
dataset = load_kannada_dataset()

# Function to fetch a random Kannada sentence and its English translation
def fetch_random_sentence():
    random_index = random.randint(0, len(dataset['train']) - 1)
    kannada_sentence = dataset['train'][random_index]['kn']  # Kannada sentence
    english_sentence = dataset['train'][random_index]['en']  # English translation
    return kannada_sentence, english_sentence

# Function to rate the user's translation
def rate_translation(user_translation, correct_translation):
    if user_translation.strip().lower() == correct_translation.strip().lower():
        return 5, "Excellent! Your translation is perfect."
    elif user_translation.strip().lower() in correct_translation.lower():
        return 4, "Good job! You got most of it right."
    elif len(user_translation.strip()) > 0:
        # Simple scoring based on character match
        score = int((len(set(user_translation.lower()) & set(correct_translation.lower())) / len(correct_translation)) * 5)
        return score, "Not bad! Keep practicing."
    else:
        return 0, "No translation provided. Please try again."

# Streamlit app layout
st.title("Draw the Kannada Sentence and Translate")

# Generate a random Kannada sentence and its English translation
if st.button("Generate Random Kannada Sentence"):
    kannada_sentence, english_sentence = fetch_random_sentence()
    st.session_state.kannada_sentence = kannada_sentence
    st.session_state.english_sentence = english_sentence

# Display the generated Kannada sentence if it exists
if 'kannada_sentence' in st.session_state:
    st.subheader("Generated Kannada Sentence:")
    st.write(st.session_state.kannada_sentence)

    # Create a drawing board
    st.write("Draw the above sentence below:")
    canvas = st_canvas(
        fill_color="white",  # Background color
        stroke_color="black",  # Drawing color
        stroke_width=5,
        height=600,  # Increased height
        width=800,  # Increased width
        key="canvas"
    )

    # Button to download the drawing
    if st.button("Download Drawing"):
        if canvas.image_data is not None:
            # Convert the image data to a PIL image
            image = Image.fromarray((canvas.image_data * 255).astype(np.uint8))  # Convert to 8-bit image
            
            # Save the image to a BytesIO object
            img_buffer = io.BytesIO()
            image.save(img_buffer, format='PNG')
            img_buffer.seek(0)

            # Create a download link
            st.download_button(
                label="Download Image",
                data=img_buffer,
                file_name="drawing.png",
                mime="image/png"
            )
        else:
            st.warning("Please draw something before downloading.")

    # Text field for user translation
    user_translation = st.text_input("Enter your English translation:")

    # Button to rate the user's translation
    if st.button("Rate Translation"):
        if user_translation:
            score, feedback = rate_translation(user_translation, st.session_state.english_sentence)
            st.write(f"Your Score: {score}/5")
            st.success(feedback)
            st.subheader("Actual English Translation:")
            st.write(st.session_state.english_sentence)  # Display the actual English translation
        else:
            st.warning("Please enter your translation before rating.")
else:
    st.warning("Click the button to generate a random Kannada sentence.")
