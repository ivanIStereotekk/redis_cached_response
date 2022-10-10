import random
import json
import requests
import redis

client = redis.Redis(host='localhost', port=6379, db=0)
urls = ['https://jsonplaceholder.typicode.com/posts/','http://188.127.251.4:8240/posts']



def get_data(user_id,urls):
    random.shuffle(urls)
    result = client.get(user_id)
    if result is None:
        response = requests.get(urls[0] )
        if response.status_code == 200:
            for item in response.json():
                try:
                    client.set(item['id'], json.dumps(item))
                    client.expire(user_id, 30)
                except ConnectionAbortedError:
                    result = f"Can't connect with :\n{client}"
                    return result
        result = client.get(user_id)
    return result



print(get_data(58,urls))