def select_candidates():
    # Ввод списка кандидатов
    candidates = []
    num_candidates = int(input("Введите количество кандидатов: "))

    for i in range(num_candidates):
        print(f"\nКандидат {i+1}")
        name = input("ФИО: ")
        age = int(input("Возраст: "))
        programming_languages = input("Освоенные языки программирования (через запятую): ")
        experience = int(input("Опыт работы (лет): "))
        education_level = input("Уровень образования (Среднее/Высшее): ")
        stress_tolerance = int(input("Стрессоустойчивость (от 1 до 10): "))
        teamwork_ability = int(input("Работа в команде (от 1 до 10): "))

        # Проверка данных
        if not name or not programming_languages or not education_level:
            print("Ошибка! Введите все данные.")
            return
        if age <= 0 or experience <= 0 or stress_tolerance < 1 or stress_tolerance > 10 or teamwork_ability < 1 or teamwork_ability > 10:
            print("Ошибка! Некорректные данные.")
            return

        candidate = {
            'name': name,
            'age': age,
            'programming_languages': programming_languages.split(","),
            'experience': experience,
            'education_level': education_level,
            'stress_tolerance': stress_tolerance,
            'teamwork_ability': teamwork_ability
        }

        candidates.append(candidate)

    # Ввод критериев
    print("\nВведите критерии для выбора кандидатов:")
    preferred_languages = input("Освоенные языки программирования: ")
    preferred_education_level = input("Уровень образования: ")
    preferred_experience = int(input("Опыт работы: "))
    preferred_stress_tolerance = int(input("Стрессоустойчивость (от 1 до 10): "))
    preferred_teamwork_ability = int(input("Работа в команде (от 1 до 10): "))

    # Ранжируем кандидатов по сумме критериев
    for candidate in candidates:
        candidate['score'] = len(set(candidate['programming_languages']).intersection(set(preferred_languages.split(",")))) + \
                             (candidate['education_level'] == preferred_education_level) + \
                             (candidate['experience'] // preferred_experience) + \
                             (candidate['stress_tolerance'] // preferred_stress_tolerance) + \
                             (candidate['teamwork_ability'] // preferred_teamwork_ability)

    # Сортировка кандидатов по очкам (в порядке убывания)
    ranked_candidates = sorted(candidates, key=lambda x: x['score'], reverse=True)

    # Вывод трех лучших кандидатов
    print("\nТри лучших кандидата:")

    for i in range(min(3, len(ranked_candidates))):
        candidate = ranked_candidates[i]
        print(f"\nКандидат {i+1}:")
        print(f"ФИО: {candidate['name']}")
        print(f"Возраст: {candidate['age']}")
        print(f"Освоенные языки программирования: {', '.join(candidate['programming_languages'])}")
        print(f"Опыт работы: {candidate['experience']} лет")
        print(f"Уровень образования: {candidate['education_level']}")
        print(f"Стрессоустойчивость: {candidate['stress_tolerance']}")
        print(f"Работа в команде: {candidate['teamwork_ability']}")


# Пример вызова функции
select_candidates()