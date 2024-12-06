import csv
class Student:
    def __init__(self, name,subjects_file ):
        self.__setattr__('name', name)
        self.subjects = {}
        self.load_subjects(subjects_file)
    def __setattr__(self, name, value):
        if name == 'name':
            if not (value and value[0].isupper() and value.replace(" ","").isalpha()):
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name,value)
    def __getattr__(self, name):
       if name in self.subjects:
           return self.subjects[name]
       raise ValueError(f"Предмет {name} не найден")
    def __str__(self):
        predmet = ', '.join(self.subjects.keys())
        return f"Студент: {self.name}\nПредметы: {predmet}"
        
    def load_subjects(self, subjects_file):
        try:
            with open(subjects_file, newline="", encoding='utf-8') as file_cvs:
                reading = csv.reader(file_cvs)
                for row in reading:
                    strings = [subjckt for subjckt in row]
                    for srt in strings:
                        if srt:
                            self.subjects[srt] = {'grades': [], 'test_scores': []}
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {subjects_file} не найден")

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return
        if not (isinstance(grade,int) and 2<= grade <= 5):
            print("Оценка должна быть целым числом от 2 до 5")
            return
        self.subjects[subject]['grades'].append(grade)
    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return
        if not (isinstance(test_score,int) and 0<= test_score <= 100):
            print("Результат теста должен быть целым числом от 0 до 100")
            return
        self.subjects[subject]['test_scores'].append(test_score)
    def get_average_test_score(self, subject):
       if subject not in self.subjects:
           print(f"Предмет {subject} не найден")
           return
       result = self.subjects[subject]['test_scores']
       if not result:
           return 0.0
       return sum(result) / len(result)
    def get_average_grade(self):
        result = [grede for sun in self.subjects.values() for grede in sun['grades']]
        if not result:
           return 0.0
        return sum(result) / len(result)
    # Пример использования
if __name__ == "__main__":
  
    student = Student("Иван Иванов", "subjects.csv")
    # Добавляем оценки и результаты тестов
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)
    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    # Получаем средний балл и результат по тестам
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")
    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")
    # Выводим информацию о студенте
    print(student)