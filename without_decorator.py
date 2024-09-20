import requests
import time

print('----------------"without decorator"---------------------------')
def get_req(url):
    r = requests.get(url)
    if r.status_code == 200:
        print(r)
        return r
    else:
        return 'failed to fetch data'
start = time.time()
get_req('https://example.com/')
end = time.time()
print(f'Execution time for "get_req" function  is : {end - start} seconds')

print('================================================')


def say_hello():
    print('hello world')
    time.sleep(1)

start = time.time()
say_hello()
end = time.time()
print(f'Execution time for "say_hello" function  is : {end - start} seconds')
