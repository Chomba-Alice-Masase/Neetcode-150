import pandas as pd

def calculate_year_gpa(courses, year_label):
    gpv_mapping = {
        'A+': 5.00, 'A': 4.00, 'B+': 3.50, 'B': 3.00,
        'C+': 2.37, 'C': 1.00, 'S': 1.00, 'IN': 0.00
    }
    
    total_credits = 0
    total_grade_points = 0
    
    print(f"\n{year_label} Courses")
    print("=" * 80)
    print(f"{'Course':<12} {'Credits':<10} {'Grade':<8} {'GPV':<8} {'Grade Points':<15}")
    print("-" * 80)
    
    for course in courses:
        credits = course['credits']
        grade = course['grade']
        gpv = gpv_mapping[grade]
        grade_points = credits * gpv
        
        print(f"{course['course']:<12} {credits:<10} {grade:<8} {gpv:<8.2f} {grade_points:<15.2f}")
        
        total_credits += credits
        total_grade_points += grade_points
    
    gpa = total_grade_points / total_credits if total_credits > 0 else 0
    print("-" * 80)
    print(f"Year Total: Credits = {total_credits}, Grade Points = {total_grade_points:.2f}, GPA = {gpa:.2f}")
    print("=" * 80)
    
    return {
        'gpa': round(gpa, 2),
        'credits': total_credits,
        'grade_points': total_grade_points
    }

# First Year Courses
year1 = [
    {'course': 'MAT1100', 'credits': 30, 'grade': ''},    # Foundation Mathematics
    {'course': 'BIO1412', 'credits': 15, 'grade': ''},   # Molecular Biology
    {'course': 'BIO1401', 'credits': 15, 'grade': ''},   # Cells and Biomolecules
    {'course': 'CHE1000', 'credits': 30, 'grade': ''},   # Introductory Chemistry
    {'course': 'PHY1010', 'credits': 30, 'grade': ''}     # Introductory Physics
]

# Second Year Courses
year2 = [
    {'course': 'CSC2912', 'credits': 15, 'grade': ''},    # Numerical Analysis
    {'course': 'CSC2000', 'credits': 30, 'grade': ''},   # Computer Programming
    {'course': 'CSC2202', 'credits': 15, 'grade': ''},   # Operating Systems
    {'course': 'CSC2702', 'credits': 15, 'grade': ''},    # Database Management
    {'course': 'CSC2111', 'credits': 15, 'grade': ''},   # Computer Architecture
    {'course': 'CSC2101', 'credits': 15, 'grade': ''},   # Computer Systems
    {'course': 'CSC2901', 'credits': 15, 'grade': ''}    # Discrete Structures
]

# Third Year Courses
year3 = [
    {'course': 'CSC3402', 'credits': 15, 'grade': ''},   # AI Fundamentals
    {'course': 'CSC3011', 'credits': 15, 'grade': ''},   # Algorithm and Complexity
    {'course': 'CSC3712', 'credits': 15, 'grade': ''},    # Advanced Databases
    {'course': 'CSC3120', 'credits': 30, 'grade': ''},    # Digital Electronics
    {'course': 'CSC3301', 'credits': 15, 'grade': ''},    # Programming Languages
    {'course': 'CSC3801', 'credits': 15, 'grade': ''},    # Data Communication
    {'course': 'CSC3612', 'credits': 15, 'grade': ''}    # IT Project Management
]

# Fourth Year Courses
year4 = [
    {'course': 'CSC4792', 'credits': 15, 'grade': ''},    # Data Mining
   # {'course': 'CSC3009', 'credits': 30, 'grade': 'S'},    # Industrial Training
    {'course': 'CSC4722', 'credits': 15, 'grade': ''},   # Distributed Systems
    {'course': 'CSC4130', 'credits': 30, 'grade': ''},    # Hardware Design
    {'course': 'CSC4004', 'credits': 15, 'grade': ''},    # Projects
    {'course': 'CSC4745', 'credits': 15, 'grade': ''},   # Multimedia & HCI
    {'course': 'CSC4835', 'credits': 15, 'grade': ''},    # Wireless & Mobile
    {'course': 'CSC4812', 'credits': 15, 'grade': ''}     # Cloud Computing
]

# Calculate GPAs with detailed breakdown
print("\nDETAILED GPA CALCULATION")
print("=" * 80)

y1_result = calculate_year_gpa(year1, "First Year")
y2_result = calculate_year_gpa(year2, "Second Year")
y3_result = calculate_year_gpa(year3, "Third Year")
y4_result = calculate_year_gpa(year4, "Fourth Year")

# Calculate Cumulative GPA
total_credits = y1_result['credits'] + y2_result['credits'] + y3_result['credits'] + y4_result['credits']
total_grade_points = y1_result['grade_points'] + y2_result['grade_points'] + y3_result['grade_points'] + y4_result['grade_points']
cumulative_gpa = round(total_grade_points / total_credits, 2)

print("\nFINAL RESULTS")
print("=" * 80)
print(f"Cumulative Grade Points: {total_grade_points:.2f}")
print(f"Total Credits: {total_credits}")
print(f"Cumulative GPA: {cumulative_gpa}")
print(f"Degree Classification: {'Distinction' if cumulative_gpa >= 3.75 else 'Merit' if cumulative_gpa >= 3.25 else 'Credit' if cumulative_gpa >= 2.68 else 'Pass'}")
print("=" * 80)
