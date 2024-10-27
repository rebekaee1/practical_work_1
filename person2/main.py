# main.py - основной файл
from input import read_name, read_age
from output import save_info


def main():
    print("Версия 2.0 - Обновленная!")  # Добавили эту строку
    name = read_name()
    age = read_age()
    save_info(name, age)
    print("Информация сохранена!")

if __name__ == "__main__":
    main()
