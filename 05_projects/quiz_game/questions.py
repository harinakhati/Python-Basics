import json


def load_questions():
    """Load quiz questions from a JSON file."""

    with open("data/python_questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)

    return questions

if __name__ == "__main__":
    questions = load_questions()
    print(questions)