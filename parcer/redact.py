

info = '''[<a class="post__title_link" href="https://habr.com/ru/news/t/498364/">Вышел <em class="searched-item">Python</em> 2.7.18, последний релиз ветки <em class="searched-item">Python</em> 2.x</a>, <a class="post__title_link" href="https://habr.com/ru/company/itsumma/news/t/490834/">...  начале этого года <em class="searched-item">Python</em> сместил Java и ...</a>, <a class="post__title_link" href="https://habr.com/ru/news/t/505096/">Вышла версия 0.0.2 snakeware — дистрибутива Linux, в котором всё работает через <em class="searched-item">Python</em></a>, <a class="post__title_link" href="https://habr.com/ru/news/t/473926/">Создатель <em class="searched-item">Python</em> Гвидо ван Россум ушел из Dropbox на пенсию</a>, <a class="post__title_link" href="https://habr.com/ru/news/t/519414/">Астрономам порекомендовали меньше использовать суперкомпьютеры и <em class="searched-item">Python</em> из-за вреда экологии</a>, <a class="post__title_link" href="https://habr.com/ru/post/147281/">Мысли о <em class="searched-item">Python</em> 3</a>, <a class="post__title_link" href="https://habr.com/ru/post/161931/">Дружим <em class="searched-item">Python</em> 3 с MS Visual C++. Строим мост в Boost.<em class="searched-item">Python</em> с автоматической перекодировкой</a>, <a class="post__title_link" href="https://habr.com/ru/post/168083/">Объединяя C++ и <em class="searched-item">Python</em>. Тонкости Boost.<em class="searched-item">Python</em>. Часть первая</a>, <a class="post__title_link" href="https://habr.com/ru/post/168827/">Конвертация типов в Boost.<em class="searched-item">Python</em>. Делаем преобразование между привычными типами C++ и <em class="searched-item">Python</em></a>, <a class="post__title_link" href="https://habr.com/ru/post/169639/">Путешествие исключений между C++ и <em class="searched-item">Python</em> или «Туда и обратно»</a>, <a class="post__title_link" href="https://habr.com/ru/post/205944/"><em class="searched-item">Python</em> на Хабре</a>, <a class="post__title_link" href="https://habr.com/ru/post/269411/">10 приложений для изучения <em class="searched-item">Python</em> на Android-устройствах</a>, <a class="post__title_link" href="https://habr.com/ru/company/mailru/blog/337364/">Что за чёрт, <em class="searched-item">Python</em></a>, <a class="post__title_link" href="https://habr.com/ru/company/ods/blog/348260/">Совмещение R и <em class="searched-item">Python</em>: зачем, когда и как?</a>, <a class="post__title_link" href="https://habr.com/ru/company/oleg-bunin/blog/418449/">Бинарные модули для <em class="searched-item">Python</em></a>, <a class="post__title_link" href="https://habr.com/ru/company/otus/blog/425233/"><em class="searched-item">Python</em> 3 в Facebook</a>, <a class="post__title_link" href="https://habr.com/ru/company/mailru/blog/454324/">Указатели в <em class="searched-item">Python</em>: в чём суть?</a>, <a class="post__title_link" href="https://habr.com/ru/post/455796/">Объектно-ориентированное программирование в Java и <em class="searched-item">Python</em>: сходства и отличия</a>, <a class="post__title_link" href="https://habr.com/ru/company/intersystems/blog/486984/"><em class="searched-item">Python</em> Gateway в InterSystems IRIS</a>, <a class="post__title_link" href="https://habr.com/ru/post/46350/">Emacs и <em class="searched-item">Python</em>, <em class="searched-item">Python</em> и Emacs</a>]'''

print(len(info))
i = 0
marker = info[29:34]
stats_list = []
article = ""
print(info[29:34])
print(info[35:69])
while True:
    i += 1
    if info[i:i+5] == marker:
        i += 6
        while info[i] != ">":
            article += info[i]
            i += 1
        stats_list.append(article[0:len(article) - 1])
        article = ""
        i += 150
    if len(stats_list) == 10:
        break

print(stats_list)
