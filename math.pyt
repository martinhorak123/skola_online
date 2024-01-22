class Student:

    def __init__(self, student_jmeno):
        
        self._student_jmeno = student_jmeno
        self._clazz = None
    @property
    def student_jmeno(self):
        
        return self._student_jmeno

    def set_class(self, tridaa):
        
        self._tridaa = tridaa
students = []
clazzes = [] 
subjects = [] 
class Tridaa:
    
    def __init__(self, tridaa_jmeno):
        
        self._tridaa_jmeno = tridaa_jmeno
        self._students = [] # list

    def pridat_student(self, student):
        
        self._students.append(student)

    def odstranit_student(self, student):
        
        self._students.remove(student)

class Subject:
    
    def __init__(self, trida_jmeno):
        
        self._trida_jmeno = trida_jmeno
        self._grades = {} # dict

    def add_grade(self, student, grade):
        
        self._grades[student] = grade

    def get_average_grade(self):
        
        if not self._grades:
            return 0
        return sum(self._grades.values()) / len(self._grades) 



def vytvor_student(name):
    
    student = Student(name)
    students.append(student)
    return student


def vytvor_tridaa(tridaa_name):
    
    tridaa = Tridaa(tridaa_name)
    tridaa.append(tridaa)
    return tridaa

def odstranit_student(student):
    
    if student in students:
        students.remove(student)
    else:
        print("student nenalezen")
def remove_subject(subject):
    
    if subject in subjects:
        subjects.remove(subject)
    else:
        print("předmět nenalezen")
        subjects.remove(subject)

def edit_student(student, name):
    
    student._student_name = name

def remove_clazz(clazz):
    
    if clazz in clazzes:
        clazzes.remove(clazz)
    else:
        print("třída nenalezena")

def create_subject(subject_name):
    
    subject = Subject(subject_name)
    subjects.append(subject)
    return subject



def display_total_grades(subject):
   
    for student, grade in subject._grades.items():
        print(f"{student._student_name}: {grade}")
    total_grade = subject.get_average_grade()
    print(f"finální známka z {subject._subject_name}: {total_grade}")

if __name__ == "__main__":
    while True:
        print()
        print("škola online menu:")
        print("1. vytvoč studentta")
        print("2. smaž studenta")
        print("3. uprav studenta")
        print("4. vytvoř třídu")
        print("5. smaž třídu")
        print("6. vytvoř předmět")
        print("7. smaž předmět")
        print("8. přidej známku")
        print("9. Zobrazit celkové průměrné známky za předmět")
        print("10. Zpět")

        choice = input("vyber možnost (1-10): ")

        if choice == "1":
            name = input("zadej jméno studenta: ")
            vytvor_student(name)

        elif choice == "2":
            name = input("zadej jméno studenta pro vymazání: ")
            for student in students:
                if student._student_name == name:
                    odstranit_student(student)
                    break
            else:
                print("student nenalezen")

        elif choice == "3":
            name = input("zadej jméno studenta pro upravení: ")
            for student in students:
                if student._student_name == name:
                    new_name = input("zadej ový jméno studenta: ")
                    edit_student(student, new_name)
                    break
            else:
                print("student nenalezen")

        elif choice == "4":
            clazz_name = input("zadej jméno třídy: ")
            vytvor_tridaa(clazz_name)

        elif choice == "5":
            clazz_name = input("zadej jméno třídy pro vymazání: ")
            for clazz in clazzes:
                if clazz._clazz_name == clazz_name:
                    remove_clazz(clazz)
                    break
            else:
                print("třída nenalezena")

        elif choice == "6":
            subject_name = input("zadej jméno předmětu: ")
            create_subject(subject_name)

        elif choice == "7":
            subject_name = input("zadejjméno předmětu pro vymazání: ")
            for subject in subjects:
                if subject._subject_name == subject_name:
                    remove_subject(subject)
                    break
            else:
                print("předmět nenalezen")

        elif choice == "8":
            student_name = input("Zadej jméno studenta: ")
            subject_name = input("Zadej jméno předmětu: ")
            grade = int(input("Zadej známku: "))
            for student in students:
                if student._student_name == student_name:
                    for subject in subjects:
                        if subject._subject_name == subject_name:
                            subject.add_grade(student, grade)
                            break
                    else:
                        print("Předmět nebyl nalezen")
                    break
            else:
                print("Student se nenašel")

        elif choice == "9":
            subject_name = input("Zadej jméno předmětu: ")
            for subject in subjects:
                if subject._subject_name == subject_name:
                    display_total_grades(subject)
                    break
            else:
                print("předět nebyl nalezen")

        elif choice == "10":
            break

        else:
            print("špatný výběr, vyber z čísel 1-10")