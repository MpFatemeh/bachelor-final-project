import sys
import numpy as np 
from association_rule import extract_association_rules, association_rule
from repeated_pattern import extract_repeated_patterns, repeated_pattern
from records_analyze import extract_records, extract_term_courses, student_term_count, extraxt_course_id_name_map

fild_map = {
    "field" : 0,
    "term_id" : 1,
    "course_id" : 2,
    "class_id" : 3,
    "course_name": 4,
    "units_number": 5,
    "course_type": 6,
    "student_id": 7,
}
MIN_STUDENT_COUNT = 100 #the term is valid when we have at lease this number of students take courses in that term
MIN_REPEAT = 15 #minimum number of repeat for patterns
records = extract_records()

original_stdout = sys.stdout
with open('out.txt' , 'a+', newline='',encoding="utf-8") as csv_file:
    sys.stdout = csv_file
    #student_term_count(records, fild_map)
    course_id_name_map = extraxt_course_id_name_map(records, fild_map)
    term_courses = extract_term_courses(records, fild_map)

    valid_term_count = 0
    for t in term_courses:
        student_courses_list = term_courses[t]
        students_count = len(student_courses_list)
        print("\nterm ==> " + t + "\nstudent_count ==>" + str(students_count))
        
        if students_count < MIN_STUDENT_COUNT or t[3] == '3':
            continue

        valid_term_count = valid_term_count + 1
        repeated_patterns_list = extract_repeated_patterns(student_courses_list, MIN_REPEAT, students_count, course_id_name_map)
        for repeated_pattern in repeated_patterns_list:
            repeated_pattern.print_repeated_pattern()

    term_courses_all = list(term_courses.values())
    courses_all = [item for sublist in term_courses_all for item in sublist]
    students_count = len(courses_all)
    print("\nfor all records\n" + "students_count ==>" + str(students_count))
    min_repeat_all = valid_term_count * MIN_REPEAT
    repeated_patterns_list = extract_repeated_patterns(courses_all, min_repeat_all, students_count, course_id_name_map)
    for repeated_pattern in repeated_patterns_list:
        repeated_pattern.print_repeated_pattern()
    association_rules = extract_association_rules(courses_all, min_repeat_all, students_count, course_id_name_map)
    for association_rule in association_rules:
        association_rule.print_association_rule()

    sys.stdout = original_stdout