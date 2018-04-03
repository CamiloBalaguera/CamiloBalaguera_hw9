import time

def fibonacci(N):
	if N == 0:
		return 0
	if N == 1:
		return 1
	else:
		return fibonacci(N-1) + fibonacci(N-2)

def get_time(N):
	t0 = time.time()
	fibonacci(N)
	t1 = time.time()-t0
	return t1

for i in range(35):
	print(i , ",", get_time(i))
