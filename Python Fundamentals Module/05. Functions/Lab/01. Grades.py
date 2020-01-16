def grade(float_score):
    if 2.00 <= float_score <= 2.99:
        return "Fail"
    elif 3.00 <= float_score <= 3.49:
        return "Poor"
    elif 3.50 <= float_score <= 4.49:
        return "Good"
    elif 4.50 <= float_score <= 5.49:
        return "Very Good"
    elif 5.50 <= float_score <= 6.00:
        return "Excellent"


score = float(input())
print(grade(score))
