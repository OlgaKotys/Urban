import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Новое слово №{i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()

write_words(15, 'example1.txt')
write_words(30, 'example2.txt')
write_words(75, 'example3.txt')
write_words(150, 'example4.txt')

end_time = time.time()
print(f"Время выполнения функций: {end_time - start_time:.2f} секунд")

threads = [
    threading.Thread(target=write_words, args=(15, 'example5.txt')),
    threading.Thread(target=write_words, args=(30, 'example6.txt')),
    threading.Thread(target=write_words, args=(75, 'example7.txt')),
    threading.Thread(target=write_words, args=(150, 'example8.txt'))
]

start_time = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Время выполнения потоков: {end_time - start_time:.2f} секунд")
