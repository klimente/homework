a = int(input("Введите первое значение: "))
b = int(input("Введите второе значение: "))

while 1:
  a, b = b, a % b
  if b ==0:
    print("Наибольший общий делитель = {}".format(a))
    break

