def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding= 'utf-8')
    for test in strings:
        fl = file.tell()
        file.write(test + '\n')
        strings_positions[(len(strings_positions) + 1, fl)] = test
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




