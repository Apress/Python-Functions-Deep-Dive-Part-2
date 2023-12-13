def change_age():
    age = 25
    print('age, inside change_name, after change ', age)
    age = 30
    print('age, inside change_name, changed once more', age)


age = 20
print('age, in main code, before calling change_name', age)

change_age()
print('age, in main code, after calling change_name', age)
