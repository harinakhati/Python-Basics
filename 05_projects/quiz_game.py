import random
import time

#Questions
quiz = [
    {
        "question": "What is the output of print(2 + 3)?",
        "options": {
            "A": "23",
            "B": "5",
            "C": "Error",
            "D": "None"
        },
        "answer": "B"
    },

    {
        "question": "Which data type is mutable?",
        "options": {
            "A": "Tuple",
            "B": "String",
            "C": "List",
            "D": "Integer"
        },
        "answer": "C"
    },

    {
        "question": "Which keyword creates a function?",
        "options": {
            "A": "class",
            "B": "return",
            "C": "lambda",
            "D": "def"
        },
        "answer": "D"
    },
    {
    "question": "Which symbol is used for comments in Python?",
    "options":{
        "A":"//",
        "B":"#",
        "C":"/* */",
        "D":"--"
    },
    "answer":"B"
},
{
    "question":"Which function displays output?",
    "options":{
        "A":"input()",
        "B":"show()",
        "C":"print()",
        "D":"display()"
    },
    "answer":"C"
},
{
    "question":"Which function accepts user input?",
    "options":{
        "A":"scan()",
        "B":"input()",
        "C":"read()",
        "D":"print()"
    },
    "answer":"B"
},
{
    "question":"Which data type stores True or False?",
    "options":{
        "A":"int",
        "B":"float",
        "C":"bool",
        "D":"list"
    },
    "answer":"C"
},
{
    "question":"Which keyword creates a loop?",
    "options":{
        "A":"loop",
        "B":"repeat",
        "C":"for",
        "D":"next"
    },
    "answer":"C"
},
{
    "question":"Which collection uses curly braces {}?",
    "options":{
        "A":"List",
        "B":"Tuple",
        "C":"Dictionary",
        "D":"String"
    },
    "answer":"C"
},
{
    "question":"What does len() return?",
    "options":{
        "A":"Largest value",
        "B":"Length",
        "C":"Type",
        "D":"Index"
    },
    "answer":"B"
},
{
    "question":"Which keyword exits a loop immediately?",
    "options":{
        "A":"stop",
        "B":"continue",
        "C":"exit",
        "D":"break"
    },
    "answer":"D"
},
{
    "question":"Which operator checks equality?",
    "options":{
        "A":"=",
        "B":"==",
        "C":"!=",
        "D":"<>"
    },
    "answer":"B"
},
{
    "question":"What does append() do?",
    "options":{
        "A":"Removes an item",
        "B":"Sorts a list",
        "C":"Adds an item to a list",
        "D":"Copies a list"
    },
    "answer":"C"
},
{
    "question":"Which keyword defines a class?",
    "options":{
        "A":"object",
        "B":"class",
        "C":"struct",
        "D":"new"
    },
    "answer":"B"
},
{
    "question":"Which exception occurs when dividing by zero?",
    "options":{
        "A":"ValueError",
        "B":"TypeError",
        "C":"ZeroDivisionError",
        "D":"NameError"
    },
    "answer":"C"
}
]

random.shuffle(quiz)

messages = [
    "Excellent!",
    "Great job!",
    "Keep it up!",
    "Nice work!",
    "Awesome!",
    "Fantastic!"
]

def display_welcome():
    print("=" * 40)
    print("        PYTHON QUIZ GAME")
    print("=" * 40)
    print("Choose the correct option (A, B, C, or D).")
    print()    
    

def ask_question(question):
    print(question["question"])
    print()

    for key, value in question["options"].items():
        print(f"{key}. {value}")

    print()
    
    while True:
        
        answer = input("\nEnter A/B/C/D (S= Skip, Q= Quit):").strip().upper()
        
        if answer == "":
            print("Answer cannot be empty.")
            continue
        
        if answer == "Q":
            confirm = input(
                "Are you sure you want to quit? (Y/N): "
            ).strip().upper()

            if confirm == "Y":
                return "quit"

            continue
        
        if answer == "S":
            return "skip"
        
        if answer not in ["A", "B", "C", "D"]:
            print("Please enter A,B,C,D,S or Q.")
            continue
        
        if answer == question["answer"]:
            print(random.choice(messages))
            return True
    
        print("Incorrect!")
        correct_option = question['answer']
        correct_text = question["options"][correct_option]
        
        print(f"Correct Answer: {correct_option}. {correct_text}\n")
        
        return False


def calculate_percentage(score, total):
    return (score/total)*100


def display_result(score, total, skipped, incorrect):
    
    print("=" * 40)
    print("RESULT")
    print("=" * 40)

    
    print(f"Total Questions : {total}")
    print(f"Correct         : {score}")
    print(f"Incorrect       : {incorrect}")
    print(f"Skipped         : {skipped}")
    
    percentage = calculate_percentage(score, total)

    print(F"Percentage: {percentage:.2f}%")
    
    if percentage == 100:
        print("Outstanding! Perfect score!")
    elif percentage >=80:
        print("Excellent work!")
    elif percentage >=60:
        print("Good job!")
    elif percentage >= 40:
        print("Keep practicing!")
    else:
        print("Don't give up. Try again!")

def retry_questions(question_list):

    score = 0

    for question in question_list:

        if ask_question(question):
            score += 1

    return score

def main():
    start = time.time()
    skipped_questions = []
    incorrect_questions = []
    
    display_welcome()
    
    if len(quiz) == 0:
        print("No questions available.")
        return

    score = 0
    total_questions = len(quiz)
        
    for number, question in enumerate(quiz, start=1):

        print(f"\nQuestion {number} of {len(quiz)}")
        print("-" * 30)

        result = ask_question(question)

        if result is True:
            score += 1
        elif result is False:
            incorrect_questions.append(question)
        elif result == "skip":
            skipped_questions.append(question)
        elif result == "quit":
            break
    
                
    if skipped_questions:      
        choice = input("\nRetry skipped question? (Y/N):").strip().upper()
        
        if choice == "Y":
            score += retry_questions(skipped_questions)
 
                    
    if incorrect_questions:
        choice = input(
            "\nRetry incorrect questions? (Y/N): "
        ).strip().upper()

        if choice == "Y":
            score += retry_questions(incorrect_questions)
                
    display_result(score, total_questions, len(skipped_questions), len(incorrect_questions))
    
    end = time.time()

    seconds = int(end - start)

    print(f"Time Played : {seconds} seconds")


main()

