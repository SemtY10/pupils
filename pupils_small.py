class Pupil: # Створення класу Pupil
    def __init__(self, surname, name, mark):
        self.name = name # Ім'я учня
        self.mark = int(mark) # Оцінка учня
        self.surname = surname # Прізвище учня
        
        
pupils = [] # Створення списку учнів

def print_class(pupils): 
    for p in pupils: # Перебираємо всіх учнів в спискум
        print(p.surname, p.name, "-", p.mark)
    print("\n") # Друкуємо прізвище, ім'я та оцінку кожного учня
    
def print_the_best(pupils): 
    print("Відмінники:")
    for p in pupils:
        if p.mark == 5: 
            print(p.surname)
    print("\n") # Якщо оцінка учня дорівнює 5 друкуємо його прізвище 
    
def find_average(pupils): # Функція, яка обчислює та друкує середню оцінку класу
    average = 0
    for p in pupils:
        average += p.mark                #Визначаємо середню оцінку
    average = average / len(pupils)
    print("Середня оцінка класу:", average) #Друкуємо середню оцінку
    
with open ("pupils_txt.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.split(" ")
        pupil = Pupil(data[0], data[1], data[2]) # Створюємо об'єкт класу Pupil з даними з рядка
        pupils.append(pupil)
        
print_class(pupils)
print_the_best(pupils)    # Викликаємо функції для друку інформації про клас
find_average(pupils)
    
        