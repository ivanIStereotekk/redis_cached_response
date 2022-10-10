# redis_cached_response

Текст задания:


Тестовое задание для кандидатов “Fullstack разработчик Python+Django”
Есть метод API возвращающий информацию о посте https://jsonplaceholder.typicode.com/posts/<id> где <id> это идентификатор поста.
API имеет ограничение по частоте запросов до 30 раз в минуту, а надо иметь возможность обращаться к нему в несколько раз чаще. При превышении ограничения происходит временная блокировка доступа.
Для этого API уже сделаны зеркала, api_addr = [‘https://jsonplaceholder.typicode.com’, ‘http://188.127.251.4:8240’,]
Надо написать функцию на Python, которая по заданному идентификатору поста будет возвращать ответ метода API.
Требования к функции:
Вызов функции не должен приводить к блокировке со стороны API.
Функция может вызываться одновременно из разных потоков и из разных процессов.
Функция должна эффективно использовать все доступные адреса для доступа к API.
Любой разработчик команды должен иметь возможность вызывать функцию и просто получить результат.


Решение "вариант 1" | main.py  
----------------------------


 Для наглядности ответ пометил sys.stdout так:
 
 Endpoint Resp:

 {
  "userId": 6,
  "id": 55,
  "title": "sit vel voluptatem et non libero",
  "body": "debitis excepturi ea perferendis harum libero optio\neos accusamus cum fuga ut sapiente repudiandae\net ut incidunt omnis molestiae\nnihil ut eum odit"
}


 В случае ответа из кеша:
 
 Cached Resp:

 {
  "userId": 6,
  "id": 55,
  "title": "sit vel voluptatem et non libero",
  "body": "debitis excepturi ea perferendis harum libero optio\neos accusamus cum fuga ut sapiente repudiandae\net ut incidunt omnis molestiae\nnihil ut eum odit"
}



Решение "вариант 2" скрипт | simple_def.py 
---------------------------


КАК ПОЛЬЗОВАТЬСЯ:
Ставим REDIS
Дергаем все что есть в репозитории на локальную машину.
Говорим в терминал - pip install -r requirements.txt ... 
Запускаем скрипт, смотрим вывод в консоли
Если есть вопрос по коду и аргументам то смотрим в main.py docstring  



