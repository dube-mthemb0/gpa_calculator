print("Welcome to the Grade Point Average calculator")
print("") #blank line
print("Please enter all your letter grades, one per line. ")
print("Enter a blankline to designate the end. ")

# Map from letter grade to point value
#review the scale accuracy!!!!!!!
#fix
points = {"A+":4.0, "A":4.0, "B+":3.3, "B":3.0, "B-":2.67, "C+":2.33, "C":2.0, "D+":1.33, "D":1, "F":0}
num_courses = 0
total_grade_points = 0

#We don’t know how many grades the user will enter,
# so we loop forever and break when a blankline is entered.
while True:
    grade = input().strip().upper() #read line from user
    if grade == "": #blankline to designate the end
        break

    elif grade not in points:
        print(f"Unknown grade '{grade}' being ignored")
    else:
        num_courses += 1
        total_grade_points += points[grade]

if num_courses > 0:
    print(f"Your GPA is {total_grade_points/ num_courses:.2f}")
else:
    print("No valid grades were entered.")
