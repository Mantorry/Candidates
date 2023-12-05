class Candidate:
    def __init__(self, name, age, programming_languages, experience, education_level,
                 communication, stress_tolerance, teamwork_ability):
        self.name = name
        self.age = age
        self.programming_languages = programming_languages
        self.experience = experience
        self.education_level = education_level
        self.communication = communication
        self.stress_tolerance = stress_tolerance
        self.teamwork_ability = teamwork_ability

    def validate(self):
        if not self.name or not self.programming_languages or not self.education_level:
            print("Ошибка! Введите все данные.")
            return False
        if (self.age <= 0 or self.experience <= 0 or
                self.communication < 1 or self.communication > 10 or
                self.stress_tolerance < 1 or self.stress_tolerance > 10 or
                self.teamwork_ability < 1 or self.teamwork_ability > 10):
            print("Ошибка! Некорректные данные.")
            return False
        return True

    def calculate_score(self, age_weight, experience_weight, education_weight,
                        communication_weight, stress_tolerance_weight, teamwork_weight):
        score = 0

        # Оценка возраста кандидата
        if self.age >= 20 and self.age <= 30:
            score += 5 * age_weight
        elif self.age > 30 and self.age <= 40:
            score += 3 * age_weight
        elif self.age > 40:
            score += 1 * age_weight

        # Оценка опыта работы
        if self.experience >= 2 and self.experience <= 5:
            score += 5 * experience_weight
        elif self.experience > 5 and self.experience <= 10:
            score += 8 * experience_weight
        elif self.experience > 10:
            score += 10 * experience_weight

        # Оценка уровня образования
        if self.education_level == "Высшее":
            score += 5 * education_weight
        elif self.education_level == "Среднее":
            score += 2 * education_weight

        # Оценка стрессоустойчивости, работы в команде и коммуникабельности
        score += (self.stress_tolerance + self.teamwork_ability + self.communication) * (
            stress_tolerance_weight + teamwork_weight + communication_weight
        )

        return score

    def __str__(self):
        return (f"Имя: {self.name}\nВозраст: {self.age}\nОсвоенные языки программирования: "
                f"{self.programming_languages}\nОпыт работы: {self.experience}\nУровень образования: "
                f"{self.education_level}\nКоммуникабельность: {self.communication}\nСтрессоустойчивость: "
                f"{self.stress_tolerance}\nРабота в команде: {self.teamwork_ability}")

def select_candidates():
    candidates = []
    num_candidates = int(input("Введите количество кандидатов: "))

    for i in range(num_candidates):
        print(f"\nКандидат {i+1}")
        name = input("ФИО: ")
        age = int(input("Возраст: "))
        programming_languages = input("Освоенные языки программирования (через запятую): ")
        experience = int(input("Опыт работы: "))
        education_level = input("Уровень образования (Среднее/Высшее): ")
        communication = int(input("Коммуникация (от 1 до 10): "))
        stress_tolerance = int(input("Стрессоустойчивость (от 1 до 10): "))
        teamwork_ability = int(input("Работа в команде (от 1 до 10): "))

        candidate = Candidate(name, age, programming_languages, experience, education_level, communication,
                              stress_tolerance, teamwork_ability)
        if candidate.validate():
            candidates.append(candidate)

    return candidates

def main():
    age_weight = float(input("Введите вес для оценки возраста (0-1): "))
    experience_weight = float(input("Введите вес для оценки опыта работы (0-1): "))
    education_weight = float(input("Введите вес для оценки уровня образования (0-1): "))
    communication_weight = float(input("Введите вес для оценки коммуникации (0-1): "))
    stress_tolerance_weight = float(input("Введите вес для оценки стрессоустойчивости (0-1): "))
    teamwork_weight = float(input("Введите вес для оценки работы в команде (0-1): "))

    candidates = select_candidates()
    print("\n====== Результаты отбора ======")
    if candidates:
        best_candidate = max(candidates, key=lambda x: x.calculate_score(age_weight, experience_weight,
                                                                        education_weight, communication_weight,
                                                                        stress_tolerance_weight, teamwork_weight))
        print(f"\nЛучший кандидат: {best_candidate}")
        print(f"Оценка: {best_candidate.calculate_score(age_weight, experience_weight, education_weight, communication_weight, stress_tolerance_weight, teamwork_weight)}")
    else:
        print("Не найдено ни одного кандидата.")

if __name__ == "__main__":
    main()