from questions import load_questions
from utils import display_welcome
from game import QuizGame
import time

def main():
    start = time.time()
    display_welcome()

    questions = load_questions()

    game = QuizGame(questions)

    game.start()

    end = time.time()

    seconds = int(end - start)

    print(f"Time Played : {seconds} seconds")

if __name__ == "__main__":
    main()