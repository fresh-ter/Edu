import threading, random, time

lock = threading.Lock()

u_1 = 1000
u_2 = 10

# print(lock.locked())

def perevod(a1, a2):
	global u_1
	global u_2

	lock.acquire(timeout=2)
	try:
		u_1 += a1
		u_2 += a2
	finally:
		lock.release()


if __name__ == "__main__":
	t1 = threading.Thread(target=perevod, args=(-1000, 1000))
	t2 = threading.Thread(target=perevod, args=(10, -10))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print(u_1, " ", u_2)
