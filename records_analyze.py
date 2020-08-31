import pandas as pd 
def extract_records():
    data = pd.read_excel('CEstudents.xlsx') 
    data_len = len(data)

    records = []
    for i in range(0, data_len):
        element = []
        for j in range(0, 8):
            element.append(str(data.values[i,j]))
        records.append(element)
    #print("len of records ===> ", len(records))
    return records

def extract_term_courses(records, fild_map):
    term_courses = {}
    for record in records:
        term_id = record[fild_map["term_id"]]
        student_id = record[fild_map["student_id"]]
        course_id = record[fild_map["course_id"]]

        if term_id not in term_courses:
            term_courses[term_id] = {}       
        if student_id not in term_courses[term_id]:
            term_courses[term_id][student_id] = []

        term_courses[term_id][student_id].append(course_id)

    for k in term_courses:
        term_courses[k] = list(term_courses[k].values())

    return term_courses

def extraxt_course_id_name_map(records, fild_map):
    course_id_name_map = {}
    for record in records:
        if record[fild_map["course_id"]] in course_id_name_map:
            continue
        course_id_name_map[record[fild_map["course_id"]]] = record[fild_map["course_name"]]

    return course_id_name_map

def student_term_count(records, fild_map):
    terms = []
    students = []
    for record in records:
        term_id = record[fild_map["term_id"]]
        student_id = record[fild_map["student_id"]]
        if term_id not in terms:
            terms.append(term_id)

        if student_id not in students:
            students.append(student_id)

    #print(terms, end="\n\n")
    print("len of terms ==>", len(terms), end="\n\n")
    #print(students, end="\n\n")
    print("len of students ==>", len(students), end="\n\n")