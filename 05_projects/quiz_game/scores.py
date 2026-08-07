def calculate_percentage(score, total):
    if total == 0:
        return 0

    return (score / total) * 100


def display_result( score, total, skipped, incorrect):
    percentage = calculate_percentage(score, total)

    print("=" * 40)
    print("RESULT")
    print("=" * 40)

    print(f"Total Questions : {total}")
    print(f"Correct         : {score}")
    print(f"Incorrect       : {incorrect}")
    print(f"Skipped         : {skipped}")
    print(f"Percentage      : {percentage:.2f}%")

    if percentage == 100:
        print("Outstanding! Perfect score!")
    elif percentage >= 80:
        print("Excellent work!")
    elif percentage >= 60:
        print("Good job!")
    elif percentage >= 40:
        print("Keep practicing!")
    else:
        print("Don't give up. Try again!")
        
