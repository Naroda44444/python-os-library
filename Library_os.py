import os
import time

print("ДЕМОНСТРАЦІЯ БІБЛІоТЕККИ OS")
print("-" * 30)

current_dir = os.getcwd()
print(f"ЯКИЙ НАШ рабочий каталог -> {current_dir}")
time.sleep(1)

new_folder = "пітон_створив_папку"
print(f"\n2. спроба створити нову папку: '{new_folder}'....")
try:
    os.mkdir(new_folder)
    print(f"папку '{new_folder}' Створенно! перевірте іі у файловому менеджеру!")
except FileExistsError:
    print(f"papka '{new_folder}' вже існує. пропускаємо створення.")
time.sleep(1)

renamed_folder = "Пітон_перейменував"

print(f"\n3. Спроба перейменувати папку: '{new_folder}' на '{renamed_folder}'.")

try:
    os.rename(new_folder, renamed_folder)
    print(f"папку перейменовано! тепер вона називається '{renamed_folder}'.")
except FileNotFoundError:
    print(f"помилка: Папка '{new_folder}'  не знайдена для перейменування.")
time.sleep(1)

print(f"\n4. спроба видалити папку: '{renamed_folder}'...")

try:
    os.rmdir(renamed_folder)
    print(f" папку '{renamed_folder}' успішно видалено.")
except FileNotFoundError:
    print(f"ПОмилка: папка '{renamed_folder}'вже видалено або не уснує")
except OSError:
    print(f"Помилка: папка '{renamed_folder}' не пуста. видаляємо лише пусті папки!")

# python os library