immutable_var = ("собака" , "кошка" , "капибара")
print(immutable_var)
immutable_var_2 =tuple(["собака" , "кошка" , "капибара"])
print(type(immutable_var_2))
# immutable_var[0] = ("тигр") 2. Объясните, почему нельзя изменить значения элементов кортежа.
# print(immutable_var)
mutable_list = ["лев" , "пантера" , "чайка"]
print(mutable_list)
mutable_list[0] = "корги"
mutable_list[-1] = "ворона"
print(mutable_list)
mutable_list.extend(["скунс", "муравей"])
print(mutable_list)
