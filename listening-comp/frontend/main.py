import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.interactive import InteractiveLearning

# Page config
st.set_page_config(
    page_title="Kannada Learning Assistant - Interactive",
    layout="wide"
)

def render_interactive_stage():
    """Render the interactive learning stage"""
    st.header("Interactive Learning")
    
    # Scenario selection
    scenario = st.selectbox(
        "Select Scenario",
        ["1. Daily Conversations", "2. Shopping", "3. Traveling", "4. At the Restaurant"]
    )
    
    # Create an instance of InteractiveLearning
    interactive_learning = InteractiveLearning()

    # Initialize session state for question and options
    if 'question_data' not in st.session_state:
        st.session_state.question_data = None
        st.session_state.selected_option = None
        st.session_state.feedback = None
        st.session_state.correct_count = 0
        st.session_state.incorrect_count = 0
        st.session_state.total_questions = 0

    # Display progress bar in the sidebar
    total_attempts = st.session_state.correct_count + st.session_state.incorrect_count
    progress = (st.session_state.correct_count / total_attempts) * 100 if total_attempts > 0 else 0
    st.sidebar.header("Progress")
    st.sidebar.progress(progress / 100)  # Update progress bar
    st.sidebar.write(f"Correct Answers: {st.session_state.correct_count}")
    st.sidebar.write(f"Incorrect Answers: {st.session_state.incorrect_count}")

    # Get a new question based on the selected scenario
    if st.button("Generate Question"):
        question_data = interactive_learning.get_question_and_options(scenario)
        if question_data:  # Check if question_data is not None
            st.session_state.question_data = question_data
            st.session_state.selected_option = None
            st.session_state.feedback = None
            st.session_state.total_questions += 1  # Increment total questions
        else:
            st.error("No questions available for this scenario.")

    # Display the question and options
    if st.session_state.question_data:
        question = st.session_state.question_data["question"]
        options = st.session_state.question_data["options"]
        st.subheader(question)
        
        # Allow user to select an option
        st.session_state.selected_option = st.radio("Choose your answer:", options)

        # Submit answer and provide feedback
        if st.button("Submit Answer"):
            correct_answer = st.session_state.question_data["correct_answer"]
            if st.session_state.selected_option == correct_answer:
                st.success(f"Correct! The answer is: {correct_answer}")
                st.session_state.correct_count += 1  # Increment correct count
            else:
                st.error(f"Incorrect! The correct answer is: {correct_answer}")
                st.session_state.incorrect_count += 1  # Increment incorrect count

            # Update progress bar
            total_attempts = st.session_state.correct_count + st.session_state.incorrect_count
            progress = (st.session_state.correct_count / total_attempts) * 100 if total_attempts > 0 else 0
            st.sidebar.progress(progress / 100)  # Update progress bar

def main():
    render_interactive_stage()

if __name__ == "__main__":
    main()