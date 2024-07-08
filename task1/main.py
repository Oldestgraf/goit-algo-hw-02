from queue import Queue
import random
import string

# Створюємо чергу
q = Queue()

def generate_request():
    # Створити нову заявку
    request = "".join([random.choice(string.ascii_letters) for i in range(10)]) 
    # Додати заявку до черги
    q.put(request)

def process_request():
    # Якщо черга не пуста:
    if not q.empty():
        # Видалити заявку з черги
        # Обробити заявку
        return(q.get())
    # Вивести повідомлення, що черга пуста
    return 'Queue is empty'


def main():
    message = 'Press any key to run the process or print "exit" to finish: '
    while True: # Поки користувач не вийде з програми:
        user_input = input(message)
        user_input = user_input.strip().lower()
        if user_input == 'exit':
            break
        generate_request() # Виконати generate_request() для створення нових заявок
        print(process_request()) # Виконати process_request() для обробки заявок

if __name__ == "__main__":
    main()
