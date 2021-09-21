import random

def benchmark(algo, list, passes):
    import time
    start = time.time()
    for i in range(0, passes+1):
        algo(list)
    end = time.time()
    time = end-start
    print(f"{algo.__name__} completed {passes} passes in {round(time, 1)} seconds.")

def gen_random_list(len):
    list = []
    for i in range(0, len):
        list.append(random.randrange(1, 101))
    return list