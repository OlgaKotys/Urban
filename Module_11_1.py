import requests
import numpy as np
from PIL import Image
import os



url = "https://urban-university.ru/"
response = requests.get(url)

if response.status_code == 200:
   print(response.text)
else:
   print(f"Ошибка при запросе данных: {response.status_code}")




data = np.array([15.55, 18.81, 12.33, 11.9, 15.75, 17.2, 16.12, 17.0, 16.99, 20.2])

average = np.average(data)
print(f"Среднее значение: {average:.2f}")

median_value = np.median(data)
print(f"Медиана: {median_value:.2f}")

std_deviation = np.std(data)
print(f"Стандартное отклонение: {std_deviation:.2f}")

min_value = np.min(data)
max_value = np.max(data)
print(f"Минимальное значение: {min_value:.2f}")
print(f"Максимальное значение: {max_value:.2f}")




def convert_image(input_path, output_path):
    with Image.open(input_path) as img:
        grayscale_img = img.convert("L")
        grayscale_img.save(output_path, "JPEG")

input_path = "Freelancer.png"
output_path = "Freelancer_gray.jpeg"

if os.path.exists(input_path):
    convert_image(input_path, output_path)
    print(f"Новое изображение сохранено как {output_path}")
else:
    print(f"Файл {input_path} не найден.")