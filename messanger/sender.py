import requests

print('Input your name)')
username = input()
print('Input your password)')
password = input()

while True:
    text = input()
    response = requests.post(
        'http://127.0.0.1:5000/send',
        json={'username':username,'password':password, 'text':text}
    )
    if response.status_code == 200:
        print('Message sent')
        print()
