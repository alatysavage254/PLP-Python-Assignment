import time

def ask_question(question, options, correct_answer):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= len(options):
                return answer == correct_answer
            else:
                print("Invalid choice. Please choose a number from the options.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_quiz():
    questions = [
        {
            "question": "What is the output of print(2**3)?",
            "options": ["5", "8", "6", "9"],
            "correct": 2
        },
        {
            "question": "Which movie won Best Picture at the 2020 Oscars?",
            "options": ["Joker", "Parasite", "1917", "Once Upon a Time in Hollywood"],
            "correct": 2
        },
        {
            "question": "Who is the creator of Python?",
            "options": ["Elon Musk", "Guido van Rossum", "Dennis Ritchie", "Mark Zuckerberg"],
            "correct": 2
        }
    ]

    score = 0

    for q in questions:
        if ask_question(q["question"], q["options"], q["correct"]):
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong answer.")
    
    print("\n🎉 Quiz Over! Your final score is:", score, "out of", len(questions))

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    return play_again == "yes"

while True:
    if not play_quiz():
        print("Thanks for playing! 👋")
      
