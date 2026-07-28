# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 2
# Topic: Conditional Logic (if / elif / else) and Functions
# =============================================================================
#
# TASK: Student Grade System
#
# Write a Python program that reads a student's score and outputs the
# corresponding letter grade based on the scale below.
#
# Grading Scale:
#   Score 80 – 100  →  Grade A
#   Score 70 – 79   →  Grade B
#   Score 60 – 69   →  Grade C
#   Score 50 – 59   →  Grade D
#   Score below 50  →  Grade F
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter student score (0-100): 85
#   Grade: A
#
#   Enter student score (0-100): 73
#   Grade: B
#
#   Enter student score (0-100): 45
#   Grade: F
#
#   Enter student score (0-100): 110
#   Error: Score must be between 0 and 100.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST use functions (see scaffold below).
# - Validate that the score is within the range 0–100 inside get_grade().
#   If it is not, return None and let main() print the error message.
# - Use if / elif / else to determine the grade.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
grade=(input("What was your grade? "))
while grade.isdigit()==False:
	print("It seems you do understand the instructions. Enter your Grade in Digits")
	grade=(input("What was your grade? "))
def grade_assessment(x):	
	if int(x) in range(80,101):
		return "You had Grade A,you're a brilla "
	elif int(x) in range(70,80):
		return "You had Grade B,you're not mid"
	elif int(x)  in range(60,70):
		return "You had Grade C , you're an average student"
	elif int(x) in range(50,60):
		return "You had a Grade D, looks like its time to hit the books bro "
	elif int(x) < 50:
		return "I'm sorry to be the bearer of bad news but um...you failed💀.You had a Grade F"
	else:
		return "Your number isn't in the range"
print(grade_assessment(grade))


