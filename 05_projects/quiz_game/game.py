import random

from scores import display_result


class QuizGame:

    MESSAGES = [
        "Excellent!",
        "Great job!",
        "Keep it up!",
        "Nice work!",
        "Awesome!",
        "Fantastic!"
    ]

    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.skipped_questions = []
        self.incorrect_questions = []
        self.total_questions = len(questions)

    def ask_question(self, question):

        print(question["question"])
        print()

        for key, value in question["options"].items():
            print(f"{key}. {value}")

        print()

        while True:

            answer = input(
                "\nEnter A/B/C/D (S=Skip, Q=Quit): "
            ).strip().upper()

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
                print("Please enter A, B, C, D, S or Q.")
                continue

            if answer == question["answer"]:
                print(random.choice(self.MESSAGES))
                return True

            print("Incorrect!")

            correct_option = question["answer"]
            correct_text = question["options"][correct_option]

            print(f"Correct Answer: {correct_option}. {correct_text}")

            return False

    def retry_questions(self, question_list):

        score = 0
        remaining_questions = []

        for question in question_list:

            result = self.ask_question(question)

            if result is True:
                score += 1

            elif result == "quit":
                return score, True

            else:
                remaining_questions.append(question)

        question_list.clear()
        question_list.extend(remaining_questions)

        return score, False

    def start(self):

        random.shuffle(self.questions)

        for number, question in enumerate(self.questions, start=1):

            print(f"\nQuestion {number} of {self.total_questions}")
            print("-" * 40)

            result = self.ask_question(question)

            if result is True:
                self.score += 1

            elif result is False:
                self.incorrect_questions.append(question)

            elif result == "skip":
                self.skipped_questions.append(question)

            elif result == "quit":
                display_result(
                    self.score,
                    self.total_questions,
                    len(self.skipped_questions),
                    len(self.incorrect_questions)
                )
                return


        if self.skipped_questions:

            choice = input(
                "\nRetry skipped questions? (Y/N): "
            ).strip().upper()

            if choice == "Y":

                gained_score, quit_game = self.retry_questions(
                    self.skipped_questions
                )

                self.score += gained_score

                if quit_game:
                    display_result(
                        self.score,
                        self.total_questions,
                        len(self.skipped_questions),
                        len(self.incorrect_questions)
                    )
                    return


        if self.incorrect_questions:

            choice = input(
                "\nRetry incorrect questions? (Y/N): "
            ).strip().upper()

            if choice == "Y":

                gained_score, quit_game = self.retry_questions(
                    self.incorrect_questions
                )

                self.score += gained_score

                if quit_game:
                    display_result(
                        self.score,
                        self.total_questions,
                        len(self.skipped_questions),
                        len(self.incorrect_questions)
                    )
                    return

        display_result(
            self.score,
            self.total_questions,
            len(self.skipped_questions),
            len(self.incorrect_questions)
        )