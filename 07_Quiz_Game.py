import time
from colorama import Fore, Style, init
init(autoreset=True)


score = 0

questions = [
    {
        "question" : "What is the capital of France?",
        "options" : "A. Paris, B. Rome, C. Madrid, D. Berlin",
        "answer" : "A"
    },
    {
        "question" : "Which language is used for web apps?",
        "options" : "A. Python, B. Java, C. JavaScript, D. All of the above",
        "answer" : "D"
    },
    {
        "question" : "Who developed Python?",
        "options" : "A. Elon Musk, B. Dennis Ritchie, C. Guido van Rossum, D. Bill Gates",
        "answer" : "C"
    }
]

for q in questions:

    time.sleep(0.5)
    print(Fore.YELLOW + f"Q: {q['question']}\n")
    time.sleep(0.3)
    print(f"{q['options']}\n")
    time.sleep(0.3)
    userAns = input("Enter your choice(A/B/C/D): ")

    while userAns.upper() not in ["A", "B", "C", "D"]:
        userAns = input(Fore.YELLOW + "Please enter a valid choice (A/B/C/D): ")

    if userAns.upper() == q["answer"]:
        time.sleep(0.3)
        print(Fore.GREEN + "\nCorrect answer! Well done\n\n")
        score += 1
    else:
        time.sleep(0.3)
        print(Fore.RED + f"\nYour answer is wrong...\nRight answer is {q['answer']}\n\n")

time.sleep(0.3)
print(Fore.CYAN + f"\n\nGame Over! \nYour Total Score = {(score/3)*100}%")