"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

def getAllVariants (l, in_str):
    # print(l)
    if len(in_str) == 2:
        return l.append(in_str[0:])
    for i in range(1,len(in_str)):
        l.append(in_str[i:])
        getAllVariants(l, in_str[i:])
        l.append(in_str[:i])
        getAllVariants(l, in_str[:i])



l = []
getAllVariants(l, "papa")
unique_list = list(set(l))
print(unique_list)
print(len(unique_list))

