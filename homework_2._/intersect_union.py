""""Intersect and union"""

def intersect(*args: iter):
    """A function to implement a intersection function through   'in' operator.
    """
    if len(args) > 1:
        list_t = list(args)
        minim = list_t.pop(list_t.index(min(args, key=len)))
        result = set()
        for i in minim:
            have = True
            for j in list_t:
                if i not in j:
                    have = False
            if have:
                result.add(i)
        return list(result)
    return "В функции должно быть минимум 2 аргумента"

F = (1, 2, 3, 4, 5, 6, 7, 8)
C = [1, 2, 3, 4, "asd", "as", "ds", 8]
R = {1, 2, 3, "kek", 8, 3}
D = {(3, 2), 5, 1, 2}
print(intersect(R, C, F, D))

def union(*args: iter):
    """A function to implement a union function through  'in' operator.
    """
    tmp_list = list(args)
    result = set(tmp_list.pop(tmp_list.index(max(args, key=len))))
    for i in tmp_list:
        for j in i:
            if j not in result:
                result.add(j)
    return result

print(union(F, C, R, D))

