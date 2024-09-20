import time
import requests
 
print('----------------"with decorator"-----------------------')   
def afra(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        x = f(*args, **kwargs)
        end = time.time()
        print(f'Execution time for {f} is : {end - start} seconds')
        return x
    return wrapper

@afra
def get_req(url):
    r = requests.get(url)
    if r.status_code == 200:
        print(r)
        return r
    else:
        return 'failed to fetch data'
get_req('https://example.com/')


print('==================================================')

@afra
def say_hello():
    print('hello world')
    time.sleep(1)
say_hello()      
