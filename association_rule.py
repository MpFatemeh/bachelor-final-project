from apyori import apriori

class association_rule:
    def __init__(self, items, items_base, support, repeat_count, confidence):
        self.items, self.items_base = items, items_base
        self.support, self.repeat_count, self.confidence = support, repeat_count, confidence
    def print_association_rule(self):
        print("items : " + '، '.join(self.items) + "\titems_base : " + '، '.join(self.items_base) 
            + "\tsupport : " + str(self.support) + "\trepeat_count : " + str(self.repeat_count) 
            + "\tconfidence : " + str(self.confidence))

def extract_association_rules(student_courses_list, min_repeat, students_count ,course_id_name_map):    
    min_support = min_repeat / students_count
    association_rules = apriori(student_courses_list, min_support=min_support)
    association_results = list(association_rules)
    rules_object_list = []
    for relation_record in association_results:
        items_course_name = []
        for item in relation_record.items:
            course_name = course_id_name_map[item]
            items_course_name.append(course_name)
        for ordered_statistic in relation_record.ordered_statistics:
            if len(items_course_name) > 1:
                items_all = items_course_name
                support = float(relation_record.support)
                repeat_count = int(support * students_count)
                confidence = float(ordered_statistic.confidence)
                items_base_course_names = []
                for item in ordered_statistic.items_base:
                    course_name = course_id_name_map[item]
                    items_base_course_names.append(course_name)
                items_base = items_base_course_names
                rule_object = association_rule(items_all, items_base, support, repeat_count ,confidence)
                rules_object_list.append(rule_object)
    rules_object_list = list(set(rules_object_list))
    rules_object_list = sorted(rules_object_list, key=lambda x: x.support, reverse=True)
    
    return rules_object_list