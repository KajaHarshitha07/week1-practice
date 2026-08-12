# Problem 8: Student Skill Matcher

def match_skills(student_skills, required_skills):
    matched_skills = student_skills & required_skills
    missing_skills = required_skills - student_skills
    extra_skills = student_skills - required_skills
    
    if len(required_skills) > 0:
        match_percentage = (len(matched_skills) / len(required_skills)) * 100
    else:
        match_percentage = 0.0
        
    return matched_skills, missing_skills, extra_skills, match_percentage

# Take input from user
student_input = input("Enter Student Skills: ")
required_input = input("Enter Required Job Skills: ")

student_skills = set(student_input.split())
required_skills = set(required_input.split())   

matched_skills, missing_skills, extra_skills, match_percentage = match_skills(student_skills, required_skills)

if match_percentage >= 70:
    status = "Eligible"
else:
    status = "Needs More Skills"

print(f"Student Skills: {student_skills}")
print(f"Required Skills: {required_skills}")
print(f"Matched Skills: {matched_skills}")
print(f"Missing Skills: {missing_skills}")
print(f"Extra Skills: {extra_skills}")
print(f"Match Percentage: {match_percentage:.2f}%")
print(f"Status: {status}")
