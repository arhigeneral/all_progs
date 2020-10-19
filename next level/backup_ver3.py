import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\Documents"', 'C:\\Code']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\Backup' # Подставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
# Проверяем комментарий на особые символы
bad_symbols = 0
for extra_symbols in range(len(comment)):
    if comment[extra_symbols] == '/':
        print ('Недопустимый символ / в комментарии')
        bad_symbols = 1
    elif comment[extra_symbols] == "\\":
        print('Недопустимый символ \ в комментарии')
        bad_symbols = 1

if len(comment) == 0: # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
elif bad_symbols == 0:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print('Каталог успешно создан', today)

# 5. Используем команду "zip" для помещения файлов в zip-архив
# Запускаем создание резервной копии
if (bad_symbols == 0):
    zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
