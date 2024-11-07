# Задача "Записать и запомнить":

def custom_write(file_name, strings):
    strings_positions = {} # словарь
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings: # Записывать в файл file_name все строки из списка strings, каждая на новой строке.
        start = file.tell() # для получения номера байта начала строки
        file.write(string + '\n') # символ перехода на следующую строку в конце
        strings_positions[(len(strings_positions) + 1, start)] = string # кортеж (<номер строки>, <байт начала строки>), а значение - записываемая строка
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
