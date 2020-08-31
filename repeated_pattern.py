from apyori import apriori
class repeated_pattern:
    def __init__(self, items, support, repeat_count):
        self.items, self.support, self.repeat_count = items, support, repeat_count

    def print_repeated_pattern(self):
        print("items : " + '، '.join(self.items) + "\tsupport : " + 
                    str(self.support) + "\trepeat_count : " + str(self.repeat_count) )

def extract_repeated_patterns(student_courses_list, min_repeat, students_count, course_id_name_map):    
    min_support = min_repeat / students_count
    print("min_support = " + str(min_support))
    association_rules = apriori(student_courses_list, min_support=min_support)
    association_results = list(association_rules)
    repeated_patterns_object_list = []
    for relation_record in association_results:
        course_names = []
        for item in relation_record.items:
            course_name = course_id_name_map[item]
            course_names.append(course_name)
        
        if len(course_names) > 1:
            items = course_names
            support = float(relation_record.support)
            repeat_count = int(support * students_count)
            repeated_pattern_object = repeated_pattern(items, support, repeat_count)
            repeated_patterns_object_list.append(repeated_pattern_object)
    repeated_patterns_list = list(set(repeated_patterns_object_list))
    repeated_patterns_list = sorted(repeated_patterns_object_list, key=lambda x: x.support, reverse=True)

    return repeated_patterns_list
