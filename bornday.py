pushkin_born_year = int(input("Год рождения А.С. Пушкина?"))  # 1799
if pushkin_born_year == 1799:
    pushkin_birthday = input("Дата рождения:")  # 6 июня
    if pushkin_birthday == "6 июня":
        print("Верно!")
    else:
        print("Неверная день рождения!")
else:
    print("Неверный год рождения!")
