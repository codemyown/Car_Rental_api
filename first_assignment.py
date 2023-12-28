import time

def custom_random():
  
    seed = int(time.time() * 1000)  
    seed = (seed % 1000) + 1  
    while True:
        seed = (seed * 387420489) % 99999999977  
        yield seed % 100 

random_generator = custom_random()
for _ in range(10):
    print(next(random_generator))
