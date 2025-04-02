## Technical Requirements

- Create a flash card website which will take random Kannada words and generate an image representing the meaning of the word
- The user needs to guess the Kannada word from the image
- Below the image, the English meaning of the word should be displayed
- If the user guesses the word correctly, the word should be added to the list of words the user knows
- If the user guesses the word incorrectly, the word should be added to the list of words the user does not know
- The user should be able to view their known and unknown word lists

## Tech Stack

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Python
- Flask
- SQLite (Database)

AI/ML:
- Ollama Mistral 7B - For word generation and processing
- Gemini 2.0 - For image generation

## API Integration

- Ollama API - For language model interactions
- Gemini API - For image generation

## Database Schema (Suggested)

Users:
- user_id (Primary Key)
- username
- created_at

Words:
- word_id (Primary Key)
- kannada_word
- english_meaning
- image_url

UserProgress:
- progress_id (Primary Key)
- user_id (Foreign Key)
- word_id (Foreign Key)
- is_known (Boolean)
- last_attempted




