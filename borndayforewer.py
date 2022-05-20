pushkin_born_year = int(input("Год рождения А.С. Пушкина?"))   #1799
while pushkin_born_year != 1799:
    print("Неверно!")
    pushkin_born_year = int(input("Год рождения А.С. Пушкина?"))
pushkin_birthday = input("Дата рождения:")  # 6 июня
while pushkin_birthday != "6 июня":
    pushkin_birthday = input("Дата рождения:")
print("Верно!")