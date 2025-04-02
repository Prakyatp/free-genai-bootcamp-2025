let currentKannadaWord = null;

async function getNewWord() {
    try {
        // Clear previous content and show loading
        document.getElementById('english-word').textContent = 'Loading...';
        document.getElementById('answer-input').value = '';
        document.getElementById('result-message').textContent = '';

        console.log('Fetching new word...');  // Debug log
        const response = await fetch('/get_word');
        const data = await response.json();
        
        console.log('Received data:', data);  // Debug log
        
        if (data.error) {
            console.error('Error:', data.error);  // Debug log
            document.getElementById('result-message').textContent = 'Error: ' + data.error;
            return;
        }
        
        // Update the UI with new word
        document.getElementById('english-word').textContent = data.english_word;
        currentKannadaWord = data.kannada_word;
        
        console.log('Word displayed:', data.english_word);  // Debug log
        
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result-message').textContent = 'Error getting new word: ' + error.message;
    }
}

async function checkAnswer() {
    const userAnswer = document.getElementById('answer-input').value;
    if (!userAnswer) {
        document.getElementById('result-message').textContent = 'Please enter an answer';
        return;
    }
    
    try {
        const response = await fetch('/check_answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                answer: userAnswer,
                correct_answer: currentKannadaWord
            })
        });
        
        const data = await response.json();
        const resultMessage = document.getElementById('result-message');
        
        if (data.correct) {
            resultMessage.textContent = 'Correct!';
            resultMessage.className = 'correct';
        } else {
            resultMessage.textContent = `Incorrect. The correct answer is: ${data.correct_answer}`;
            resultMessage.className = 'incorrect';
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result-message').textContent = 'Error checking answer: ' + error.message;
    }
}

// Load first word when page loads
document.addEventListener('DOMContentLoaded', () => {
    console.log('Page loaded, getting first word...');  // Debug log
    getNewWord();
}); 