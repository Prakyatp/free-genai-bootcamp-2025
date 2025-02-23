import random

class InteractiveLearning:
    def __init__(self):
        self.scenarios = {
            "1. Daily Conversations": [
                {
                    "question": "ನೀವು ಯಾರನ್ನು ಭೇಟಿಯಾದಾಗ ಏನು ಹೇಳುತ್ತೀರಿ?",  # What do you say when you meet someone?
                    "options": [
                        "ನಮಸ್ಕಾರ",  # Hello
                        "ನೀವು ಹೇಗಿದ್ದೀರಿ?",  # How are you?
                        "ನಾನು ಚೆನ್ನಾಗಿದ್ದೇನೆ",  # I am fine
                        "ಧನ್ಯವಾದಗಳು"  # Thank you
                    ],
                    "correct_answer": "ನಮಸ್ಕಾರ"  # Correct answer
                },
                {
                    "question": "ನೀವು ದಿಕ್ಕು ಕೇಳಲು ಹೇಗೆ ಕೇಳುತ್ತೀರಿ?",  # How do you ask for directions?
                    "options": [
                        "ಈಗ ಎಲ್ಲಿದೆ?",  # Where is it now?
                        "ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡುತ್ತೀರಾ?",  # Can you help me?
                        "ನಾನು ಇಲ್ಲಿಗೆ ಹೇಗೆ ಹೋಗಬಹುದು?",  # How can I get here?
                        "ನೀವು ನನ್ನನ್ನು ಕರೆದರೆ?"  # Will you call me?
                    ],
                    "correct_answer": "ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡುತ್ತೀರಾ?"  # Correct answer
                },
                {
                    "question": "ನೀವು ಏನು ಮಾಡುತ್ತೀರಿ?",  # What will you do?
                    "options": [
                        "ನಾನು ಓಡುತ್ತೇನೆ",  # I will run
                        "ನಾನು ಓದುತ್ತೇನೆ",  # I will read
                        "ನಾನು ನಗುತ್ತೇನೆ",  # I will laugh
                        "ನಾನು ನಿದ್ರಿಸುತ್ತೇನೆ"  # I will sleep
                    ],
                    "correct_answer": "ನಾನು ಓದುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಊಟ ಮಾಡುತ್ತೀರಿ?",  # When do you eat?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಊಟ ಮಾಡುತ್ತೇನೆ",  # I eat breakfast in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಊಟ ಮಾಡುತ್ತೇನೆ",  # I eat lunch in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಊಟ ಮಾಡುತ್ತೇನೆ",  # I eat dinner at night
                        "ನಾನು ಯಾವಾಗಲೂ ಊಟ ಮಾಡುತ್ತೇನೆ"  # I eat anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಊಟ ಮಾಡುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಕೆಲಸಕ್ಕೆ ಹೋಗುತ್ತೀರಿ?",  # When do you go to work?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಕೆಲಸಕ್ಕೆ ಹೋಗುತ್ತೇನೆ",  # I go to work in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಕೆಲಸಕ್ಕೆ ಹೋಗುತ್ತೇನೆ",  # I go to work in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಕೆಲಸಕ್ಕೆ ಹೋಗುತ್ತೇನೆ",  # I go to work at night
                        "ನಾನು ಯಾವಾಗಲೂ ಕೆಲಸಕ್ಕೆ ಹೋಗುತ್ತೇನೆ"  # I go to work anytime
                    ],
                    "correct_answer": "ನಾನು ಬೆಳಿಗ್ಗೆ ಕೆಲಸಕ್ಕೆ ಹೋಗುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಮನೆಗೆ ಹೋಗುತ್ತೀರಿ?",  # When do you go home?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಮನೆಗೆ ಹೋಗುತ್ತೇನೆ",  # I go home in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಮನೆಗೆ ಹೋಗುತ್ತೇನೆ",  # I go home in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಮನೆಗೆ ಹೋಗುತ್ತೇನೆ",  # I go home at night
                        "ನಾನು ಯಾವಾಗಲೂ ಮನೆಗೆ ಹೋಗುತ್ತೇನೆ"  # I go home anytime
                    ],
                    "correct_answer": "ನಾನು ರಾತ್ರಿ ಮನೆಗೆ ಹೋಗುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಸ್ನಾನ ಮಾಡುತ್ತೀರಿ?",  # When do you take a bath?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಸ್ನಾನ ಮಾಡುತ್ತೇನೆ",  # I take a bath in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಸ್ನಾನ ಮಾಡುತ್ತೇನೆ",  # I take a bath in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಸ್ನಾನ ಮಾಡುತ್ತೇನೆ",  # I take a bath at night
                        "ನಾನು ಯಾವಾಗಲೂ ಸ್ನಾನ ಮಾಡುತ್ತೇನೆ"  # I take a bath anytime
                    ],
                    "correct_answer": "ನಾನು ಬೆಳಿಗ್ಗೆ ಸ್ನಾನ ಮಾಡುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಓದುತ್ತೀರಿ?",  # When do you read?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಓದುತ್ತೇನೆ",  # I read in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಓದುತ್ತೇನೆ",  # I read in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಓದುತ್ತೇನೆ",  # I read at night
                        "ನಾನು ಯಾವಾಗಲೂ ಓದುತ್ತೇನೆ"  # I read anytime
                    ],
                    "correct_answer": "ನಾನು ರಾತ್ರಿ ಓದುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ನಿದ್ರಿಸುತ್ತೀರಿ?",  # When do you sleep?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ನಿದ್ರಿಸುತ್ತೇನೆ",  # I sleep in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ನಿದ್ರಿಸುತ್ತೇನೆ",  # I sleep in the afternoon
                        "ನಾನು ರಾತ್ರಿ ನಿದ್ರಿಸುತ್ತೇನೆ",  # I sleep at night
                        "ನಾನು ಯಾವಾಗಲೂ ನಿದ್ರಿಸುತ್ತೇನೆ"  # I sleep anytime
                    ],
                    "correct_answer": "ನಾನು ರಾತ್ರಿ ನಿದ್ರಿಸುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಸ್ನಾನ ಮಾಡುತ್ತೀರಿ?",  # When do you take a bath?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಸ್ನಾನ ಮಾಡುತ್ತೇನೆ",  # I take a bath in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಸ್ನಾನ ಮಾಡುತ್ತೇನೆ",  # I take a bath in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಸ್ನಾನ ಮಾಡುತ್ತೇನೆ",  # I take a bath at night
                        "ನಾನು ಯಾವಾಗಲೂ ಸ್ನಾನ ಮಾಡುತ್ತೇನೆ"  # I take a bath anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಸ್ನಾನ ಮಾಡುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಚಲನಚಿತ್ರ ನೋಡುತ್ತೀರಿ?",  # When do you watch movies?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಚಲನಚಿತ್ರ ನೋಡುತ್ತೇನೆ",  # I watch movies in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಚಲನಚಿತ್ರ ನೋಡುತ್ತೇನೆ",  # I watch movies in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಚಲನಚಿತ್ರ ನೋಡುತ್ತೇನೆ",  # I watch movies at night
                        "ನಾನು ಯಾವಾಗಲೂ ಚಲನಚಿತ್ರ ನೋಡುತ್ತೇನೆ"  # I watch movies anytime
                    ],
                    "correct_answer": "ನಾನು ರಾತ್ರಿ ಚಲನಚಿತ್ರ ನೋಡುತ್ತೇನೆ"  # Correct answer
                },
            ],
            "2. Shopping": [
                {
                    "question": "ನೀವು ಒಂದು ವಸ್ತುವಿನ ಬೆಲೆಯನ್ನು ಕೇಳಲು ಹೇಗೆ ಕೇಳುತ್ತೀರಿ?",  # How do you ask for the price of an item?
                    "options": [
                        "ಇದು ಎಷ್ಟು?",  # How much is this?
                        "ನೀವು ಇದನ್ನು ಮಾರಾಟ ಮಾಡುತ್ತೀರಾ?",  # Do you sell this?
                        "ನೀವು ನನಗೆ ಬೆಲೆಯನ್ನು ಹೇಳುತ್ತೀರಾ?",  # Can you tell me the price?
                        "ನೀವು ನನಗೆ ಇತರ ಆಯ್ಕೆಗಳು ನೀಡುತ್ತೀರಾ?"  # Can you give me other options?
                    ],
                    "correct_answer": "ಇದು ಎಷ್ಟು?"  # Correct answer
                },
                {
                    "question": "ನೀವು ಖರೀದಿಸಲು ಏನು ಬೇಕು?",  # What do you want to buy?
                    "options": [
                        "ನಾನು ಹಣ್ಣು ಖರೀದಿಸುತ್ತೇನೆ",  # I want to buy fruits
                        "ನಾನು ತರಕಾರಿ ಖರೀದಿಸುತ್ತೇನೆ",  # I want to buy vegetables
                        "ನಾನು ಬಟ್ಟೆ ಖರೀದಿಸುತ್ತೇನೆ",  # I want to buy clothes
                        "ನಾನು ಆಟಿಕೆ ಖರೀದಿಸುತ್ತೇನೆ"  # I want to buy toys
                    ],
                    "correct_answer": "ನಾನು ಹಣ್ಣು ಖರೀದಿಸುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಖರೀದಿಸಿದ ವಸ್ತುಗಳನ್ನು ಹೇಗೆ ಪಾವತಿಸುತ್ತೀರಿ?",  # How do you pay for the items you bought?
                    "options": [
                        "ನಾನು ನಗದು ಪಾವತಿಸುತ್ತೇನೆ",  # I pay in cash
                        "ನಾನು ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ ಬಳಸುತ್ತೇನೆ",  # I use a credit card
                        "ನಾನು ಡೆಬಿಟ್ ಕಾರ್ಡ್ ಬಳಸುತ್ತೇನೆ",  # I use a debit card
                        "ನಾನು ಆನ್‌ಲೈನ್ ಪಾವತಿಸುತ್ತೇನೆ"  # I pay online
                    ],
                    "correct_answer": "ನಾನು ನಗದು ಪಾವತಿಸುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಖರೀದಿಸಿದ ವಸ್ತುಗಳನ್ನು ಹೇಗೆ ಸಾಗಿಸುತ್ತೀರಿ?",  # How do you carry the items you bought?
                    "options": [
                        "ನಾನು ಬ್ಯಾಗ್‌ನಲ್ಲಿ ಸಾಗಿಸುತ್ತೇನೆ",  # I carry them in a bag
                        "ನಾನು ಕೈಯಲ್ಲಿ ಸಾಗಿಸುತ್ತೇನೆ",  # I carry them in my hands
                        "ನಾನು ಕಾರಿನಲ್ಲಿ ಸಾಗಿಸುತ್ತೇನೆ",  # I carry them in a car
                        "ನಾನು ಬೈಕಿನಲ್ಲಿ ಸಾಗಿಸುತ್ತೇನೆ"  # I carry them on a bike
                    ],
                    "correct_answer": "ನಾನು ಬ್ಯಾಗ್‌ನಲ್ಲಿ ಸಾಗಿಸುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಖರೀದಿಸುತ್ತೀರಿ?",  # When do you shop?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಖರೀದಿಸುತ್ತೇನೆ",  # I shop in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಖರೀದಿಸುತ್ತೇನೆ",  # I shop in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಖರೀದಿಸುತ್ತೇನೆ",  # I shop at night
                        "ನಾನು ಯಾವಾಗಲೂ ಖರೀದಿಸುತ್ತೇನೆ"  # I shop anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಖರೀದಿಸುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೀರಿ?",  # When do you look for sales?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ",  # I look for sales in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ",  # I look for sales in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ",  # I look for sales at night
                        "ನಾನು ಯಾವಾಗಲೂ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ"  # I look for sales anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಖರೀದಿಸುತ್ತೀರಿ?",  # When do you shop?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಖರೀದಿಸುತ್ತೇನೆ",  # I shop in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಖರೀದಿಸುತ್ತೇನೆ",  # I shop in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಖರೀದಿಸುತ್ತೇನೆ",  # I shop at night
                        "ನಾನು ಯಾವಾಗಲೂ ಖರೀದಿಸುತ್ತೇನೆ"  # I shop anytime
                    ],
                    "correct_answer": "ನಾನು ಬೆಳಿಗ್ಗೆ ಖರೀದಿಸುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೀರಿ?",  # When do you look for sales?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ",  # I look for sales in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ",  # I look for sales in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ",  # I look for sales at night
                        "ನಾನು ಯಾವಾಗಲೂ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ"  # I look for sales anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಖರೀದಿಸುತ್ತೀರಿ?",  # When do you shop?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಖರೀದಿಸುತ್ತೇನೆ",  # I shop in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಖರೀದಿಸುತ್ತೇನೆ",  # I shop in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಖರೀದಿಸುತ್ತೇನೆ",  # I shop at night
                        "ನಾನು ಯಾವಾಗಲೂ ಖರೀದಿಸುತ್ತೇನೆ"  # I shop anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಖರೀದಿಸುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೀರಿ?",  # When do you look for sales?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ",  # I look for sales in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ",  # I look for sales in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ",  # I look for sales at night
                        "ನಾನು ಯಾವಾಗಲೂ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ"  # I look for sales anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಮಾರಾಟವನ್ನು ನೋಡುತ್ತೇನೆ"  # Correct answer
                },
            ],
            "3. Traveling": [
                {
                    "question": "ನೀವು ಹೋಟೆಲ್ ಬುಕ್ಕಿಂಗ್‌ಗಾಗಿ ಹೇಗೆ ಕೇಳುತ್ತೀರಿ?",  # How do you ask for a hotel reservation?
                    "options": [
                        "ನೀವು ನನಗೆ ಒಂದು ಕೋಣೆ ಬೇಕು",  # I need a room
                        "ನೀವು ನನಗೆ ಬೆಲೆಯನ್ನು ಹೇಳುತ್ತೀರಾ?",  # Can you tell me the price?
                        "ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡುತ್ತೀರಾ?",  # Can you help me?
                        "ನೀವು ನನ್ನನ್ನು ಕರೆದರೆ?"  # Will you call me?
                    ],
                    "correct_answer": "ನೀವು ನನಗೆ ಒಂದು ಕೋಣೆ ಬೇಕು"  # Correct answer
                },
                {
                    "question": "ನೀವು ಸ್ಥಳೀಯ ಆಕರ್ಷಣೆಗಳ ಬಗ್ಗೆ ಕೇಳಲು ಹೇಗೆ ಕೇಳುತ್ತೀರಿ?",  # How do you ask about local attractions?
                    "options": [
                        "ನೀವು ನನಗೆ ಸ್ಥಳೀಯ ಆಕರ್ಷಣೆಗಳ ಬಗ್ಗೆ ಹೇಳುತ್ತೀರಾ?",  # Can you tell me about local attractions?
                        "ನೀವು ನನಗೆ ಬೆಲೆಯನ್ನು ಹೇಳುತ್ತೀರಾ?",  # Can you tell me the price?
                        "ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡುತ್ತೀರಾ?",  # Can you help me?
                        "ನೀವು ನನ್ನನ್ನು ಕರೆದರೆ?"  # Will you call me?
                    ],
                    "correct_answer": "ನೀವು ನನಗೆ ಸ್ಥಳೀಯ ಆಕರ್ಷಣೆಗಳ ಬಗ್ಗೆ ಹೇಳುತ್ತೀರಾ?"  # Correct answer
                },
                {
                    "question": "ನೀವು ಊಟವನ್ನು ಆರ್ಡರ್ ಮಾಡಲು ಹೇಗೆ ಕೇಳುತ್ತೀರಿ?",  # How do you ask to order food?
                    "options": [
                        "ನಾನು ಊಟವನ್ನು ಆರ್ಡರ್ ಮಾಡುತ್ತೇನೆ",  # I will order food
                        "ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡುತ್ತೀರಾ?",  # Can you help me?
                        "ನೀವು ನನ್ನನ್ನು ಕರೆದರೆ?",  # Will you call me?
                        "ನೀವು ನನಗೆ ಬೆಲೆಯನ್ನು ಹೇಳುತ್ತೀರಾ?"  # Can you tell me the price?
                    ],
                    "correct_answer": "ನಾನು ಊಟವನ್ನು ಆರ್ಡರ್ ಮಾಡುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಸ್ಥಳೀಯ ಆಹಾರವನ್ನು ಕೇಳಲು ಹೇಗೆ ಕೇಳುತ್ತೀರಿ?",  # How do you ask for local food?
                    "options": [
                        "ನೀವು ನನಗೆ ಸ್ಥಳೀಯ ಆಹಾರವನ್ನು ಹೇಳುತ್ತೀರಾ?",  # Can you tell me about local food?
                        "ನೀವು ನನಗೆ ಬೆಲೆಯನ್ನು ಹೇಳುತ್ತೀರಾ?",  # Can you tell me the price?
                        "ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡುತ್ತೀರಾ?",  # Can you help me?
                        "ನೀವು ನನ್ನನ್ನು ಕರೆದರೆ?"  # Will you call me?
                    ],
                    "correct_answer": "ನೀವು ನನಗೆ ಸ್ಥಳೀಯ ಆಹಾರವನ್ನು ಹೇಳುತ್ತೀರಾ?"  # Correct answer
                },
                {
                    "question": "ನೀವು ಪ್ರವಾಸದ ಸಮಯದಲ್ಲಿ ಏನು ಮಾಡುತ್ತೀರಿ?",  # What do you do during the trip?
                    "options": [
                        "ನಾನು ಪ್ರವಾಸಕ್ಕೆ ಹೋಗುತ್ತೇನೆ",  # I go on a trip
                        "ನಾನು ಓದುತ್ತೇನೆ",  # I read
                        "ನಾನು ನಗುತ್ತೇನೆ",  # I laugh
                        "ನಾನು ನಿದ್ರಿಸುತ್ತೇನೆ"  # I sleep
                    ],
                    "correct_answer": "ನಾನು ಪ್ರವಾಸಕ್ಕೆ ಹೋಗುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಹಾರುತ್ತೀರಿ?",  # When do you fly?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಹಾರುತ್ತೇನೆ",  # I fly in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಹಾರುತ್ತೇನೆ",  # I fly in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಹಾರುತ್ತೇನೆ",  # I fly at night
                        "ನಾನು ಯಾವಾಗಲೂ ಹಾರುತ್ತೇನೆ"  # I fly anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಹಾರುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಪ್ರಯಾಣಿಸುತ್ತೀರಿ?",  # When do you travel?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಪ್ರಯಾಣಿಸುತ್ತೇನೆ",  # I travel in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಪ್ರಯಾಣಿಸುತ್ತೇನೆ",  # I travel in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಪ್ರಯಾಣಿಸುತ್ತೇನೆ",  # I travel at night
                        "ನಾನು ಯಾವಾಗಲೂ ಪ್ರಯಾಣಿಸುತ್ತೇನೆ"  # I travel anytime
                    ],
                    "correct_answer": "ನಾನು ಬೆಳಿಗ್ಗೆ ಪ್ರಯಾಣಿಸುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಹಾರುತ್ತೀರಿ?",  # When do you fly?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಹಾರುತ್ತೇನೆ",  # I fly in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಹಾರುತ್ತೇನೆ",  # I fly in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಹಾರುತ್ತೇನೆ",  # I fly at night
                        "ನಾನು ಯಾವಾಗಲೂ ಹಾರುತ್ತೇನೆ"  # I fly anytime
                    ],
                    "correct_answer": "ನಾನು ರಾತ್ರಿ ಹಾರುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಪ್ರಯಾಣಿಸುತ್ತೀರಿ?",  # When do you travel?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಪ್ರಯಾಣಿಸುತ್ತೇನೆ",  # I travel in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಪ್ರಯಾಣಿಸುತ್ತೇನೆ",  # I travel in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಪ್ರಯಾಣಿಸುತ್ತೇನೆ",  # I travel at night
                        "ನಾನು ಯಾವಾಗಲೂ ಪ್ರಯಾಣಿಸುತ್ತೇನೆ"  # I travel anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಪ್ರಯಾಣಿಸುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಹಾರುತ್ತೀರಿ?",  # When do you fly?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಹಾರುತ್ತೇನೆ",  # I fly in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಹಾರುತ್ತೇನೆ",  # I fly in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಹಾರುತ್ತೇನೆ",  # I fly at night
                        "ನಾನು ಯಾವಾಗಲೂ ಹಾರುತ್ತೇನೆ"  # I fly anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಹಾರುತ್ತೇನೆ"  # Correct answer
                },
            ],
            "4. At the Restaurant": [
                {
                    "question": "ನೀವು ಆಹಾರವನ್ನು ಆರ್ಡರ್ ಮಾಡಲು ಹೇಗೆ ಕೇಳುತ್ತೀರಿ?",  # How do you ask to order food?
                    "options": [
                        "ನಾನು ಆಹಾರವನ್ನು ಆರ್ಡರ್ ಮಾಡುತ್ತೇನೆ",  # I will order food
                        "ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡುತ್ತೀರಾ?",  # Can you help me?
                        "ನೀವು ನನ್ನನ್ನು ಕರೆದರೆ?",  # Will you call me?
                        "ನೀವು ನನಗೆ ಬೆಲೆಯನ್ನು ಹೇಳುತ್ತೀರಾ?"  # Can you tell me the price?
                    ],
                    "correct_answer": "ನಾನು ಆಹಾರವನ್ನು ಆರ್ಡರ್ ಮಾಡುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಆಹಾರವನ್ನು ಆರ್ಡರ್ ಮಾಡುತ್ತೀರಿ?",  # When do you order food?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಆಹಾರವನ್ನು ಆರ್ಡರ್ ಮಾಡುತ್ತೇನೆ",  # I order food in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಆಹಾರವನ್ನು ಆರ್ಡರ್ ಮಾಡುತ್ತೇನೆ",  # I order food in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಆಹಾರವನ್ನು ಆರ್ಡರ್ ಮಾಡುತ್ತೇನೆ",  # I order food at night
                        "ನಾನು ಯಾವಾಗಲೂ ಆಹಾರವನ್ನು ಆರ್ಡರ್ ಮಾಡುತ್ತೇನೆ"  # I order food anytime
                    ],
                    "correct_answer": "ನಾನು ರಾತ್ರಿ ಆಹಾರವನ್ನು ಆರ್ಡರ್ ಮಾಡುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಬಿಲ್ ಕೇಳುತ್ತೀರಿ?",  # When do you ask for the bill?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಬಿಲ್ ಕೇಳುತ್ತೇನೆ",  # I ask for the bill in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಬಿಲ್ ಕೇಳುತ್ತೇನೆ",  # I ask for the bill in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಬಿಲ್ ಕೇಳುತ್ತೇನೆ",  # I ask for the bill at night
                        "ನಾನು ಯಾವಾಗಲೂ ಬಿಲ್ ಕೇಳುತ್ತೇನೆ"  # I ask for the bill anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಬಿಲ್ ಕೇಳುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೀರಿ?",  # When do you eat food?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ",  # I eat food in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ",  # I eat food in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ",  # I eat food at night
                        "ನಾನು ಯಾವಾಗಲೂ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ"  # I eat food anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಆಹಾರವನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತೀರಿ?",  # When do you share food?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಆಹಾರವನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತೇನೆ",  # I share food in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಆಹಾರವನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತೇನೆ",  # I share food in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಆಹಾರವನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತೇನೆ",  # I share food at night
                        "ನಾನು ಯಾವಾಗಲೂ ಆಹಾರವನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತೇನೆ"  # I share food anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಆಹಾರವನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೀರಿ?",  # When do you eat food?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ",  # I eat food in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ",  # I eat food in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ",  # I eat food at night
                        "ನಾನು ಯಾವಾಗಲೂ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ"  # I eat food anytime
                    ],
                    "correct_answer": "ನಾನು ರಾತ್ರಿ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಬಿಲ್ ಕೇಳುತ್ತೀರಿ?",  # When do you ask for the bill?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಬಿಲ್ ಕೇಳುತ್ತೇನೆ",  # I ask for the bill in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಬಿಲ್ ಕೇಳುತ್ತೇನೆ",  # I ask for the bill in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಬಿಲ್ ಕೇಳುತ್ತೇನೆ",  # I ask for the bill at night
                        "ನಾನು ಯಾವಾಗಲೂ ಬಿಲ್ ಕೇಳುತ್ತೇನೆ"  # I ask for the bill anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಬಿಲ್ ಕೇಳುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಆಹಾರವನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತೀರಿ?",  # When do you share food?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಆಹಾರವನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತೇನೆ",  # I share food in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಆಹಾರವನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತೇನೆ",  # I share food in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಆಹಾರವನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತೇನೆ",  # I share food at night
                        "ನಾನು ಯಾವಾಗಲೂ ಆಹಾರವನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತೇನೆ"  # I share food anytime
                    ],
                    "correct_answer": "ನಾನು ರಾತ್ರಿ ಆಹಾರವನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತೇನೆ"  # Correct answer
                },
                {
                    "question": "ನೀವು ಯಾವಾಗ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೀರಿ?",  # When do you eat food?
                    "options": [
                        "ನಾನು ಬೆಳಿಗ್ಗೆ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ",  # I eat food in the morning
                        "ನಾನು ಮಧ್ಯಾಹ್ನ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ",  # I eat food in the afternoon
                        "ನಾನು ರಾತ್ರಿ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ",  # I eat food at night
                        "ನಾನು ಯಾವಾಗಲೂ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ"  # I eat food anytime
                    ],
                    "correct_answer": "ನಾನು ಮಧ್ಯಾಹ್ನ ಆಹಾರವನ್ನು ತಿನ್ನುತ್ತೇನೆ"  # Correct answer
                },
            ],
        }

    def get_question_and_options(self, scenario):
        if scenario in self.scenarios:
            questions = self.scenarios[scenario]
            return random.choice(questions)  # Return a random question
        else:
            return None  # Return None if scenario not found
