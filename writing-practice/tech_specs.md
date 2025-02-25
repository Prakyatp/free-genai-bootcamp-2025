# Technical Specifications

## Project Overview

This project is a web application built using Streamlit that allows users to generate random Kannada sentences, draw them on a canvas, and provide their English translations. The app provides feedback on the user's translation and allows them to download their drawings.

## Pages Overview

### 1. Home Page

- **Title**: Draw the Kannada Sentence and Translate
- **Functionality**: 
  - Users can click the "Generate Random Kannada Sentence" button to fetch a random Kannada sentence from the dataset.
  - The generated Kannada sentence is displayed for the user to draw.

### 2. Drawing Board

- **Functionality**: 
  - A drawing canvas is provided where users can draw the generated Kannada sentence.
  - Users can adjust the stroke color and width while drawing.
  - A "Download Drawing" button allows users to save their drawings as PNG images.

### 3. Translation Input

- **Functionality**: 
  - Users can enter their English translation of the displayed Kannada sentence in a text input field.
  - After entering their translation, users can click the "Rate Translation" button to receive feedback on their translation accuracy.
  - The actual English translation from the dataset is displayed for comparison.

## Dataset Used

The app uses the **Hemanth-thunder/english-to-kannada-mt** dataset, which contains pairs of English and Kannada sentences. The dataset has three columns:
- **Index**: The index of the sentence pair.
- **en**: The English translation.
- **kn**: The Kannada sentence.

This dataset is used to randomly select a Kannada sentence and its corresponding English translation for the user to draw and translate.

## Drawing Board

The drawing board is implemented using the `streamlit-drawable-canvas` library, which provides an interactive canvas for users to draw. Users can:
- Draw the generated Kannada sentence using a mouse or touch input.
- Adjust the stroke color and width for their drawings.
- Download their drawings as PNG images.

## How to Use the Project

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd writing-practice
   ```

2. **Install Required Libraries**:
   Make sure you have Python installed, then install the required libraries:
   ```bash
   pip install streamlit numpy datasets streamlit-drawable-canvas pillow
   ```

3. **Run the Streamlit App**:
   Open a terminal, navigate to the project directory, and run:
   ```bash
   streamlit run app.py
   ```

4. **Access the App**:
   After running the command, Streamlit will provide a local URL (usually `http://localhost:8501`) where you can access the app in your web browser.

5. **Using the App**:
   - Click the "Generate Random Kannada Sentence" button to fetch a sentence.
   - Draw the sentence on the canvas.
   - Enter your English translation in the provided text field.
   - Click "Rate Translation" to see your score and the actual English translation.
   - Download your drawing if desired.

## Conclusion

This app provides an engaging way to practice writing Kannada sentences and translating them into English. It combines drawing and language learning in an interactive format.

