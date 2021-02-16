import time
import rpa as r
import concurrent.futures


def get_rpa(timeout=10):
    r.init()
    r.url('https://www.google.com')
    r.type('//*[@name="q"]', 'decentralization[enter]')
    print(r.read('result-stats'))
    r.snap('page', 'results.png')
    r.close()

print("Running threaded:")
threaded_start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for i in range(1, 4):
        futures.append(executor.submit(get_rpa))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
print("Threaded time:", time.time() - threaded_start)
