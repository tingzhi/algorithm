/* CS325 - Project 2
 * Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
 * Date: 7/17/2015
 * Solution description: Implementation on different algorithms
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int changeslow(int *v, int *c, int n, int A)
{
	int m = 0;
	m = m + changeslow(v, c, n, A);
	/*
	for (int i = n - 1; i > 0; i++)
	{
		if (A == v[i])
		{
			v[i]++;
			m++;
		}
	}*/
	return m;
}

int changegreedy(int *v, int *c, int n, int A)
{
	int m = 0;
	int temp = A;
	for (int i = n - 1; i >= 0; i--)
	{
		temp = A;
		while (temp > 0)
		{
			temp = temp - v[i];
			if (temp >= 0)
			{
				A = temp;
				c[i]++;
				m++;
			}
		}
	}
	return m;
}

int changedp(int *v, int *c, int n, int A)
{
	int m = 0;

	return m;
}

int main()
{
	int v[5] = { 1, 5, 10, 25, 50 };
	int n = sizeof(v) / sizeof(v[0]);
	int A = 41;
	int c[5] = { 0, 0, 0, 0, 0 };
	int m = changegreedy(v, c, n, A);
	printf("the result array is:\n");
	for (int i = 0; i < n; i++)
		printf("%d\t",c[i]);
	printf("\nThe number of coins for Greedy Algorithm is: %d\n\n", m);
}