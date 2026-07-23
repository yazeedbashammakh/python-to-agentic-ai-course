

# height = input("Enter your height in meters: ")
# weight = input("Enter your weight in kilograms: ")

# print("Your height is: " + height + " meters")
# print("Your weight is: " + weight + " kilograms")


# try:
#     bmi = float(weight) / (float(height) ** 2)
# except ValueError:
#     print("Error: Please enter valid numbers for height and weight.")
#     exit()
# except ZeroDivisionError:
#     print("Error: Height cannot be zero.")
#     exit()
# except:
#     print("Error calculating BMI.")
#     exit()
# else:
#     print("Your BMI is: " + str(bmi))
# finally:
#     print("Thank you for using the BMI calculator.")


# try:
#     # Risky code that may raise an exception
# except ExceptionType:
#     # Handle the exception
# else:
#     # Code to execute if no exception occurs
# finally:
#     # Code that will always execute, regardless of exceptions

class MarksNotAcceptable(ValueError):
    pass


def grade_student(marks: float) -> str:
    """
    Function to grade a student based on their marks.

    Args:
        marks (float): The marks obtained by the student.
    Outputs:
        str: The grade corresponding to the marks.
    Exceptions:
        Raises MarksNotAcceptable if marks are not between 0 and 100.
    """
    marks = float(marks)  # Convert marks to float for comparison
    if marks < 0 or marks > 100:
        raise MarksNotAcceptable("Marks should be between 0 and 100.")

    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

try:
    grade_student("asg")
except MarksNotAcceptable as e:
    print("Error:", e)
except ValueError as e:
    print("Error: Invalid input. Please enter a numeric value for marks.")
    print("Exception details:", e)
except Exception as e:
    print("An unexpected error occurred:", e)




