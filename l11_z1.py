import csv

# Шляхи до файлів
input_file = "D:/lab11/inflation_data.csv"
output_file = "D:/lab11/inflation_results.csv"

try:
    # Читаємо дані з  файлу
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Читаємо заголовок
        data = [(int(row[0]), float(row[1])) for row in reader]  # Рік, Значення

    # Виведення вмісту файлу на екран
    print("     Зміст файлу\n"
          "  Рік      Значення")
    for row in data:
        print(row)

    # Пошук найвищого та найнижчого значень
    max_inflation = max(data, key=lambda x: x[1])
    min_inflation = min(data, key=lambda x: x[1])

    # Запис результатів у новий файл
    with open(output_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Description", "Year", "Value"])
        writer.writerow(["Highest Inflation", max_inflation[0], max_inflation[1]])
        writer.writerow(["Lowest Inflation", min_inflation[0], min_inflation[1]])

    print(f"\nРезультати обробки:")
    print(f"Найвищий показник: Рік {max_inflation[0]}, Значення {max_inflation[1]}%")
    print(f"Найнижчий показник: Рік {min_inflation[0]}, Значення {min_inflation[1]}%")
    print(f"\nРезультати записано у файл: {output_file}")

except FileNotFoundError:
    print(f"Помилка: Файл {input_file} не знайдено!")
except ValueError:
    print("Помилка: Некоректний формат даних у файлі!")
except Exception as e:
    print(f"Сталася помилка: {e}")
