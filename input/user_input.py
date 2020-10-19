def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

new_something = ''
something = input('Введите текст: ')
for extra_symbols in range(len(something)):
    if something[extra_symbols] == ',':
        print('')
    else:
        new_something += something[extra_symbols]

print(new_something)

if (is_palindrome(new_something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
