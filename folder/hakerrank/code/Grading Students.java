import sys

def gradingStudents(grades: list[int]) -> list[int]:
    rounded_grades = []
    
    for grade in grades:
        # Rules state: no rounding for grades less than 38
        if grade < 38:
            rounded_grades.append(grade)
        else:
            remainder = grade % 5
            # If the remainder is 3 or 4, the difference to the next multiple of 5 is less than 3
            if remainder >= 3:
                rounded_grades.append(grade + (5 - remainder))
            else:
                rounded_grades.append(grade)
                
    return rounded_grades

def main():
    # Read all space/newline separated inputs from stdin efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    grades = [int(x) for x in input_data[1:]]
    
    result = gradingStudents(grades)
    
    # Print each rounded grade on a new line
    for grade in result:
        print(grade)

if __name__ == "__main__":
    main()
