import csv
import sys
import os

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
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    if not data: 
        print("CSV file is empty")
        return data
    
    # TODO: a) Check if all scores are percentage based (0-100)
    for assignment in data: 
        if not 0 < assignment["score"] < 100:
            print("ERROR: Invalid Score; Score must be between 0 and 100")
            sys.exit(1)
    print("Great!! Lets Continue")
        
    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
     
    formative_total = 0
    summative_total = 0    

    for assignment in data:
        if assignment["group"] == "Formative":
            formative_total += assignment["weight"]

        elif assignment["group"] == "Summative":
            summative_total += assignment["weight"]
        else: 
            print(f"WARNING: {assignment["group"]} is an UNKNOWN GROUP. Expected Group(Formative or Summative)")

    total_weight = formative_total + summative_total

    if formative_total != 60:
        print(f"ERROR: The formative total sums up to {formative_total}, but they must add up to 60")
        sys.exit(1)
    if summative_total != 40: 
        print(f"ERROR: The Summative total sums up to {summative_total}, but they must add up to 40")
        sys.exit(1)
    if total_weight != 100:
        print(f"ERROR: The total_weight sums up to {total_weight}, but they must add up to 100")
        sys.exit(1)

    print()
    # TODO: c) Calculate the Final Grade and GPA
    formative_grades = 0 
    summative_grades = 0 

    for assignment in data: 
        total_contribution = (assignment["score"] * assignment["weight"]) / 100 
        if assignment["group"] == "Formative": 
            formative_grades += total_contribution
        elif assignment["group"] == "Summative":
            summative_grades += total_contribution

    total_contribution = formative_grades + summative_grades

    print(f"The Formative grades are: {formative_grades}")
    print()
    print(f"The Summative grades are: {summative_grades}")
    print()
    print(f"The Final grades are: {total_contribution}")
    print("-------------------")

    GPA =  (total_contribution / 100) * 5
    print(f"The GPA is: {GPA}")



    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    
    pass

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)