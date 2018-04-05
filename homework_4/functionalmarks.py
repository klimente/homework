"""Functional marks"""


def get_data():
    return [
        {'name': 'Alexey', 'rate': 2, 'course': 'python'},
        {'name': 'Andrey', 'rate': 3, 'course': 'python'},
        {'name': 'Oleg', 'rate': 1, 'course': 'python'},
        {'name': 'Alexey', 'rate': 6, 'course': 'js'},
        {'name': 'Senya', 'rate': 4,'course': 'js'},
        {'name': 'Alex', 'rate': 7, 'course': 'js'},
        {'name': 'Greg', 'rate': 3, 'course': 'c#'},
        {'name': 'Regi', 'rate': 6, 'course': 'c#'},
        {'name': 'Regg', 'rate': 3, 'course': 'c#'},
        {'name': 'Gerg', 'rate': 9, 'course': 'c#'},
        {'name': 'Lena', 'rate': 7, 'course': 'c#'}
    ]


def get_course(data):
    return {item['course'] for item in data}

def get_students(data,course):
    return sorted([(item['name'],item['rate']) for item in data if item['course'] == course],key=lambda x: x[1],reverse=True)[:3]

def get_table(students):
    return 'Course {}\n'.format(students) + \
        '\n'.join('{:10} ---> {:4}'.format(*student)
                  for student in get_students(get_data(),students))

if __name__ == '__main__':
    print('\n'.join(get_table(course) for course in get_course(get_data())))
