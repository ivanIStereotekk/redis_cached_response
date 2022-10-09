import asyncio
import requests
import json
import redis

client = redis.Redis(host='localhost', port=6379, db=0)

async def make_request(item_id: int, ttl: int):
    """
    :param item_id: ID записи
    :param ttl: "Time To Live"- Время жизни записи в кэше
    :return: Возвращает результат либо из кэша (если есть такая запись) либо идет на эндпоинт
    берет запись там ...
    """
    url_s = [f'https://jsonplaceholder.typicode.com/posts/{item_id}',f'http://188.127.251.4:8240/posts/{item_id}']
    cached_response = client.get(item_id)
    if cached_response is None:
        future = _loop.run_in_executor(None, requests.get,url_s[0])
        url_s[0],url_s[1] = url_s[1],url_s[0]
        response = await future
        client.set(item_id, json.dumps(response.text))
        client.expire(item_id, ttl)
        print("Endpoint Resp:\n\n",response.text)
    else:
        print("Cached Resp:\n\n",json.loads(cached_response))

_loop = asyncio.get_event_loop()
_loop.run_until_complete(make_request(88, 60))
