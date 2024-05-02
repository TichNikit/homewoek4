immutable_var = (1, 1.5, 'a', True)
print(immutable_var)

#immutable_var[0] = 2

#print(immutable_var)  Ловим ошибку TypeError, т.к. tuple не поддерживаем возможность изменения

mutable_list = [1, 1.5, 'a', True]
mutable_list[0] = 2
mutable_list[1] = mutable_list[1] +0.5
mutable_list[2] = mutable_list[2] * 5
mutable_list.append(False)

print(mutable_list)

