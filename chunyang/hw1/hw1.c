#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int recursivefib(int n)
{
	if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	else
		return (recursivefib(n - 1) + recursivefib(n - 2));
}

long iterativefib(long n)
{
	long fib = 0, a = 1, t = 0;
	for (long k = 0; k < n; k++)
	{
		t = fib + a;
		a = fib;
		fib = t;
	}
	return fib;
}

int main()
{
	clock_t timer;

	/*recursive algorithm*/
	int n = 30;
	int recursivesum;
	timer = clock();
	recursivesum = recursivefib(n);
	timer = clock() - timer;
	printf("The %dth number of this Fibonacci Numbers using recursive algorithm is: %d\n", n, recursivesum);
	printf("recursive algorithm for n = %d ran in %f seconds\n\n", n, (float)timer / (float)CLOCKS_PER_SEC);
	
	/*iterative algorithm*/
	long n = 10000000;
	long iterativesum;
	timer = clock();
	iterativesum = iterativefib(n);
	timer = clock() - timer;
	printf("The %ldth number of this Fibonacci Numbers using iterative algorithm is: %ld\n", n, iterativesum);
	printf("iterative algorithm for n = %ld ran in %f seconds\n\n", n, (float)timer / (float)CLOCKS_PER_SEC);
}