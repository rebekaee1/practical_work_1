# output.py - файл для сохранения данных
def save_info(name, age):
  with open("user_info.txt", "w") as file:
    file.write(f"Имя: {name}\nВозраст: {age}")
