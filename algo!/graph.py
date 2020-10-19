from collections import deque



graph = {}

graph['you'] = ['alice', 'bob','claire']
graph['bob'] = ['anyjm','peggi']
graph['alice'] = ['peggi']
graph['claire'] = ['tom','jonny']
graph['anyjm'] = []
graph['peggi'] = []
graph['jonny'] = []
graph['tom'] = []



def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph [ "you"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person ,"  is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search('you')
