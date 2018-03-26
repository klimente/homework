numbers_of_students = int(input("Введите количество студентов: "))
numbers_of_tasks = int(input("Введите количество заданий: "))

students = {} #Словарь с оценками
students_rate = {} #Словарь с суммой оценок

tasks = dict.fromkeys([x for x in range(1,numbers_of_tasks+1)],0)  #Словарь для задач
tasks_hardness = tasks.copy()  #Словарь с суммой баллов для каждой задачи

for i in range(1,numbers_of_students+1): #Заполняю имя для каждого студента
  name = input(f"Введите имя {i}-го студента -").title()
  students[name] = tasks.copy()   #Добавляю словарь оценко к каждому студенту
  students_rate[name] = 0 # Инициализирую словарь с рейтингом

for key,value in students.items():
  for j in value:  #Заполняю оценки по каждому заданию к каждому студенту
    mark = int(input(f"Введите оценку по шкале от 0 до 10 для студента {key} в задании {j} -"))
    if mark<=10 and mark>=0:
      students[key][j] = mark
      students_rate[key] += mark #Заполняю рейтинг студентов и задач
      tasks_hardness[j] += mark
    else:
      print("Оценка не в интервале от 0 до 10 попробуйте еще.".upper())
      break

top_s = 3 if len(students_rate)>3 else len(students_rate) #Количество элементов в топе для студентов
top_t = 3 if len(tasks_hardness)>3 else len(tasks_hardness) #Количество элементов в топе для задач

print()
print("-"*30)
print(f"Топ {top_s} студента")
print("-"*30)

top_stud = {}
while len(top_stud)<top_s: #Сортирую и достаю максимальные элементы из рейтинга студентов
  for k,v in students_rate.copy().items():
    if v==max(students_rate.values()) and len(top_stud)<3:
      top_stud[k] = students_rate.pop(k)
      print("{} c баллами {}".format(k, v))

print()
print("-"*30)
print("Топ {} задачи по сложности".format(top_t))
print("-"*30)

top_tasks = {}
while len(top_tasks)<top_t: #Сортирую и достаю минимальные элементы из рейтинга задач
  for k,v in tasks_hardness.copy().items():
    if v==min(tasks_hardness.values()) and len(top_tasks)<3:
      top_tasks[k] = tasks_hardness.pop(k)
      print(" Задание - {} c общей суммой баллов {} ".format(k,v))

