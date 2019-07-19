class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems


data_list = []

input_list = input().split(" -> ")

while input_list[0] != "go go go":
    input_object = Exercise(input_list[0],
                            input_list[1],
                            input_list[2],
                            input_list[3].split(", "))
    data_list.append(input_object)
    input_list = input().split(" -> ")

for obj in data_list:
    print(f"Exercises: {obj.topic}")
    print(f'''Problems for exercises and homework for the
        "{obj.course_name}\" course @ SoftUni.''')
    print(f"Check your solutions here: {obj.judge_contest_link}")
    for count, problem in enumerate(obj.problems, 1):
        print(f"{count}. {problem}")
