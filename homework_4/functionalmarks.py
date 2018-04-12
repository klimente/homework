"""Functional marks"""
from operator import itemgetter


def get_data():
    """A function to return massive of data.

    :returns: list -- data about students.
    """
    return [
        {'name': 'Alexey', 'rate': 2, 'course': 'python'},
        {'name': 'Andrey', 'rate': 3, 'course': 'python'},
        {'name': 'Oleg', 'rate': 1, 'course': 'python'},
        {'name': 'Alexey', 'rate': 6, 'course': 'js'},
        {'name': 'Senya', 'rate': 4, 'course': 'js'},
        {'name': 'Alex', 'rate': 7, 'course': 'js'},
        {'name': 'Greg', 'rate': 3, 'course': 'c#'},
        {'name': 'Regi', 'rate': 6, 'course': 'c#'},
        {'name': 'Regg', 'rate': 3, 'course': 'c#'},
        {'name': 'Gerg', 'rate': 9, 'course': 'c#'},
        {'name': 'Lena', 'rate': 7, 'course': 'c#'}
    ]


def get_course(data):
    """A function to get courses from data.

    :param data: handle data.
    :type data: list.
    :returns: set -- of courses.
    """
    return {item['course'] for item in data}


def get_students(data, course):
    """A function to get list of students by courses.

    :param data: handle data.
    :type data: list.
    :returns: list of tuple -- name and rate of student.
    """
    return sorted([(item['name'], item['rate']) for item in data if item['course'] == course],
                  key=itemgetter(1), reverse=True)


def get_table(course):
    """A function to create table.

    :param course: course.
    :type course: str.
    :returns: str -- table representation for some course.
    """
    return f'Course {course}\n' + \
        '\n'.join(f'{student[0]+1:2}: Name: {student[1][0]:6} --> Rate:{student[1][1]:2}'
                  for student in enumerate(get_students(get_data(), course)))

if __name__ == '__main__':
    print('\n'.join(get_table(course) for course in get_course(get_data())))
