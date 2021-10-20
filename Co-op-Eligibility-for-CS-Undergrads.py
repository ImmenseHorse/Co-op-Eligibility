# Duc Manh Nguyen
# DOB: 23 Feb 2002

# Prior to the deadline of co-op program applications, students will be preparing much time for final exams, honing resumes, and preparing for interviews.

# Since the work load is hefty, I have written a program to help fellow undergraduates who seek co-op designation to simulate their CGPA, based on their entered expecting grades. The program then determines if the student is possibly met the minimum CGPA requirement at the time of application.

# This program is exclusive for undergraduates majoring in Computer Science.

# "The minimum CGPA requirement at the time of application" complies with Ryerson"s website: https://www.ryerson.ca/career-coop/students-alumni/coop/how-to-apply/

# The grading scale system and GPA calculation comply with Ryerson"s websites: https://www.ryerson.ca/studentguide/grades/#academic_standing and https://www.ryerson.ca/current-students/grades-standings/gpa-calculation/#accordion-1616785862084-sample-gpa-calculation


def GPA(num):
    """
    GPA converts numeric grade into Ryerson GPA
    """
    if num >= 90:
        return 4.33
    elif num >= 85:
        return 4.00
    elif num >= 80:
        return 3.67
    elif num >= 77:
        return 3.33
    elif num >= 73:
        return 3.00
    elif num >= 70:
        return 2.67
    elif num >= 67:
        return 2.33
    elif num >= 63:
        return 2.00
    elif num >= 60:
        return 1.67
    elif num >= 57:
        return 1.33
    elif num >= 53:
        return 1.00
    elif num >= 50:
        return 0.67   
    return 0.00


def retrieveGrades(num):
    """
    retrieveGrades asks the user the grades of a number num of courses and then returns the corresponding CGPA.
    """
    grds = 0
    weights = 0
    grd = 0
    indx = 1
    while num > 0:
        while True:
            gd = float(input("What is your expecting numeric grade for course No. {no:} ? ".format(no = indx)))
            if 0 <= gd <= 100:
                grd = GPA(gd)
                indx += 1
                break
            else:
                print("Your input is not a valid numeric grade.")
                print()

        while True:
            weigh = input("What is the weight for this course? ")
            if weigh == "1" or weigh == "2":
                weigh = float(weigh)
                break
            else:
                print("Your input is not a valid weight.")
                print()

        print()

        grds += grd * weigh
        weights += weigh
        num -= 1

    return round(grds / weights,2)

def main():
    """
    The main function for the CGPA simulator Tool
    """
    print("Welcome to CGPA simulator Tool, designed by Duc Manh Nguyen, exclusively for full-time CS Undergraduates. \n")
    print('Already posted on https://github.com/ImmenseHorse')

    print('Your numeric marks entered are secured and private. \n')

    while True:
        sem = input("What semester are you currently in? Enter 0 if you want to terminate the program. ")
        if sem == "0":
            print("Thank you!")
            return
        if sem > "8" or sem < "1" or len(sem) >= 2:
            print("The entered semester is invalid. Please try again!")
        elif sem <= "8" and sem >= "1" and sem != "2" and sem != "3":
            print("Unfortunately, you are not eligible for the co-op program.")
            return
        else:
            while True:   
                numCourse = int(input("How many courses have you been taken? "))
                print()
                if sem == "2" and 14 >= numCourse >= 6:             
                    break
                elif sem == "3" and 21 >= numCourse >= 9:
                    break
                else:
                    print("Invalid number of courses. \n")
            break
    cgpa = retrieveGrades(numCourse)
    print("Your CGPA is {n:}.".format(n = cgpa))
    if cgpa < 2.8:
        print("You are not eligible for co-op program.")
    elif cgpa >= 3.0:
        print("You met the minimum CGPA requirement for co-op program.")
    else:
        print("You will need at least 3.0 CGPA to remain in the co-op program.")


if __name__ == "__main__":
    main()