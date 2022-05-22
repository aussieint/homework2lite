more_game = None
quetion_amount = 5
while more_game != "Нет":
    right_answer = 0
    year1 = int(input("Год рождения Пушкина: "))  # 1799
    if year1 == 1799:
        right_answer += 1
    year2 = int(input("Год рождения Лермонтова: "))  # 1814
    if year2 == 1814:
        right_answer += 1
    year3 = int(input("Год рождения Горького: "))  # 1868
    if year3 == 1868:
        right_answer += 1
    year4 = int(input("Год рождения Ленина: "))  # 1870
    if year4 == 1870:
        right_answer += 1
    year5 = int(input("Год рождения Достоевского: "))  # 1821
    if year5 == 1821:
        right_answer += 1
    print("Количество правильных ответов: ", right_answer)
    print("Количество ошибок: ", quetion_amount - right_answer)
    print("Процент правильных ответов: ", right_answer * 100 / quetion_amount)
    print("Процент ошибок: ", (quetion_amount - right_answer) * 100 / quetion_amount)
    more_game = input("Начать игру сначала?")
