from multiprocessing.dummy import Pool
import numpy as np
import time

# calculus thread

def my_function(i, param1, param2, param3):
    result = param1 ** 2 * param2 + param3
    time.sleep(2)
    return (i, result)


def get_result(result):
    global results
    results.append(result)


# Returning name thread

def worker(nome):
    return nome

def callback(nome):
    print(nome)

def main_thread(nome):
    pool_threads= 8
    div = 10
    try:
        with Pool(pool_threads) as pool:
            # for i in range(1 , div):
            re = pool.apply_async(worker, args=[nome])
            re.get()

        pool.close()
        pool.join()

    except Exception as error:
        print(error)

if __name__ == "__main__":
    params = "Johnatas"
    main_thread(params)

    params = np.random.random((10, 3)) * 100.0
    results = []
    ts = time.time()
    for i in range(0, params.shape[0]):
        get_result(my_function(i, params[i, 0], params[i, 1], params[i, 2]))
    print('Time in serial:', time.time() - ts)
    print(results)

    results = []
    ts = time.time()
    pool = mp.Pool(mp.cpu_count())
    for i in range(0, params.shape[0]):
        pool.apply_async(my_function, args=(i, params[i, 0], params[i, 1], params[i, 2]), callback=get_result)
    pool.close()
    pool.join()
    print('Time in parallel:', time.time() - ts)
    print(results)

    print(mp.cpu_count())