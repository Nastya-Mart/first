first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
list_ = first + second
first_result = (len(i) - len(x) for i, x in zip(first, second) if len(i) != len(x))
second_result = (len(first[y]) == len(second[y]) for y in range(len(first)) if y < len(second))

print(list(first_result))

print(list(second_result))