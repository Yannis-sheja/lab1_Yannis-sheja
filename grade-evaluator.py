import csv
import sys
import os
print("===============================")
print("        GRADE EVALUATOR        ")
print("===============================")
def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not all([
                    row["assignment"].strip(),
                    row["group"].strip(),
                    row["score"].strip(),
                    row["weight"].strip()
                ]):
                    print("ERROR: Empty or Incomplete row detected ")
                    sys.exit(1)
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data=[]):
    """
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")

    if not data: 
        print("CSV file is empty")
        return data
    
    # PART 1: CHECK IF ALL SCORES ARE PERCENTAGE BASED(0-100)

    for assignment in data: 
        # We go through the assignment and make sure that the score is between 0 and 100
        if not 0 <= assignment["score"] <= 100: # if it is not between 0 and 100 it will return an error 
            print("ERROR: Invalid Score; Score must be between 0 and 100")
            print(f"Invalid Score, {assignment["score"]} for {assignment["assignment"]}")
            sys.exit(1)#to exit the code 

    print("True") 
    print("Great!! Lets Continue")
        
    # PART 2: VALIDATING TOTAL WEIGHTS (Total=100, Summative=40, Formative=60)
     
    formative_total = 0
    summative_total = 0    

    for assignment in data:
        #Adds up the weight where the group is the formative
        if assignment["group"] == "Formative": #Where the group = formative 
            formative_total += assignment["weight"]
        #Adds up the weight where the group is the summative
        elif assignment["group"] == "Summative":
            summative_total += assignment["weight"]
        #Other than that it will display the error below 
        else: 
            print(f"WARNING: {assignment['group']} is an UNKNOWN GROUP. Expected Group(Formative or Summative)")

    total_weight = formative_total + summative_total
    #Here we need to check if the formative = 60, summative = 40 and the total weight = 100 
    if formative_total != 60:  #!= : simply means not equal to 
        print(f"ERROR: The formative total sums up to {formative_total}, but they must add up to 60")
        sys.exit(1) 

    if summative_total != 40: 
        print(f"ERROR: The Summative total sums up to {summative_total}, but they must add up to 40")
        sys.exit(1)

    if total_weight != 100:
        print(f"ERROR: The total_weight sums up to {total_weight}, but they must add up to 100")
        sys.exit(1)

    print()
    # PART 3: CALCULTING THE FINAL GRADE AND GPA 

    formative_grades = 0 
    summative_grades = 0 
    # Here we want to know the final grades and The GPA. 
    for assignment in data: 
        #Final grade = (Score * weight) / 100
        final_grade = (assignment["score"] * assignment["weight"]) / 100 

        if assignment["group"] == "Formative": 
            formative_grades += final_grade

        elif assignment["group"] == "Summative":
            summative_grades += final_grade

    final_grade = formative_grades + summative_grades

    print(f"The Formative grades are: {formative_grades}")
    print("----------")
    print(f"The Summative grades are: {summative_grades}")
    print("-------------------")
    print(f"The Final grades are: {final_grade}")
    print("-------------------")

    #GPA = (Final grade / 100) * 5 
    GPA =  (final_grade / 100) * 5.00
    print(f"The GPA is: {GPA:.2f}")

    # PART 4: DETERMATING THE STATUS(PASS/FAIL) IN BOTH CATEGORIES(>= 50% in BOTH categories)

    #We are going to use the percentage below for getting the Pass/Fail status 
    formative_percentage = (formative_grades / 60) * 100
    summative_percentage = (summative_grades / 40) * 100
    total_percentage = (final_grade * 100) / 100 

    #if the formative_percentage and summative_percentage is greater than 50% then will print 'PASS' or else 'FAIL' 
    if formative_percentage >= 50: 
        print(f"The Formative Percentage is: {formative_percentage:.2f} %")# :.2f means from 2 decimal places 
        print("PASS")
    else:
        print(f"Your Formative percentage is: {formative_percentage:.2f} %")
        print("FAIL. Your Percentage is below 50 ")

    if summative_percentage >= 50: 
         print(f"The Summative Percentage is: {summative_percentage:.2f} %")
         print("PASS")
    else:
         print(f"Your Summative percentage is: {summative_percentage:.2f} %")
         print("FAIL. Your Percentage is below 50 ")

    if total_percentage >= 50: 
        print(f"The Percentage is: {total_percentage:.2f} %")
        print("PASS")
    else:
        print(f"Your total percentage is: {total_percentage:.2f} %")
        print("FAIL. Your Percentage is below 50 ")

    # PART 5: FAILED_FORMATIVES

    #Here we are trying to find the formatives that a person failed(Below 50) and determine the one that has highest weight. 

    assignment_failed = {} #We using dictionaries because we need keys and values 

    for assignment in data:
        if assignment["group"] == "Formative" and assignment["score"] < 50:
            assignment_failed[assignment["assignment"]] = assignment["weight"] #assignment["assignment"] is the key 
            # assignment["weight"] is the value
    # Create an empty list to store the assignment with the highest weight 
    assignment_with_highest_weight = []
    #Variable to keep track of the highest weight found so far 
    highest_weight = 0

    #If there is no failed assignments
    if not assignment_failed:
        print("There are zero lessons failed!")

    else:
        #It loops through each failed assignment and weight
        for key, value in assignment_failed.items():# assignment_failed.items() is for both th keys and values 

            #If list is empty, store the first failed assignments 
            if not assignment_with_highest_weight:
                assignment_with_highest_weight.append(key)
                highest_weight = value

            else:
                #If the asssignment has a higher weight than the current highest, then
                #replace the old with the new one. 
                if value > highest_weight:
                    assignment_with_highest_weight = [key]
                    highest_weight = value

                #Otherwise, if assignment has the same highest weight,
                #add it to list
                elif value == highest_weight:
                    assignment_with_highest_weight.append(key)

    print("\nAssignment(s) recommended for resubmission:")

    for assignment in assignment_with_highest_weight:
        print(f"- {assignment} (Weight: {highest_weight}%)")

    # PART 6:THE FINAL DECISION
    #  Print the final decision (PASSED / FAILED) and resubmission options
    print()
    print("==============================================================================")
    print()
    print("================REPORT===================")
    print()
    print(f"Formative grades(60): {formative_grades:.2f} with Formative Percentage: {formative_percentage:.2f}%")
    print(f"Summative grades(40): {summative_grades:.2f} with Summative Percentage: {summative_percentage:.2f}%")
    
    print(f"Total grade: {final_grade} with Percentage: {total_percentage:.2f}% ")
    print()
    print("----------Category Status------------")
    print(f"Formative:{'PASS' if formative_percentage >= 50 else 'FAIL'}")
    print(f"Summative:{'PASS' if summative_percentage >= 50 else 'FAIL'}")
    print()
    print("-----------Final Decision---------------")
    if formative_percentage >= 50 and summative_percentage >= 50: 
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")
    print()
    print("-------------Resubmission----------------")
    print("\nELigible for resubmission:")
    
    for assignment in assignment_with_highest_weight:
            print(f"- {assignment}")
    print()
    print("--------THE END----------")
    print()
    print("===============================================================================")
    print()
    
if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)