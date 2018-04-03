#include <ctime>
#include <iostream>
using namespace std;

int fibonacci(int N);
float get_time(int N);
int main()
{
	for(int i = 0; i<35 ; i++)
	{
		float t = get_time(i);
		cout << t << "," << i << endl;
	}	
	return 0;
}


int fibonacci(int N)
	{
		int fib = 0;
		if (N == 0)
			{
				return 0;
			}
		if (N == 1)
			{
				return 1;
			}
		else
			{
				return fibonacci(N-1) + fibonacci(N-2);
			}
	}

float get_time(int N)
	{
		clock_t t;
		t = clock();
		fibonacci(N);
		t = clock() - t;
		float time = ((float)t)/CLOCKS_PER_SEC;
		return time;
	}
