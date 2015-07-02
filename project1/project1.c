/* CS325 - Project 1
 * Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
 * Date: 7/1/2015
 * Solution description: Implementation on different algorithms
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdlib.h>
#include <time.h>

int Enumeration(int *a, int n, int *x, int *y)
{
	int i, j, sum, max;
	max = a[0];
	for (i = 0; i < n; i++)
	{
		for (j = i; j < n; j++)
		{
			sum = 0;
			for (int z = i; z <= j; z++)
			{
				if (j > i)
					sum = sum + a[z];
				else sum = a[i];
			}
			if (sum > max)
			{
				max = sum;
				*x = i;
				*y = j;
			}
		}
	}
	return max;
}

int betterEnumeration(int *a, int n, int *x, int *y)
{
	int i, j, sum, max;
	max = a[0];
	for (i = 0; i < n; i++)
	{
		sum = 0;
		for (j = i; j < n; j++)
		{
			sum = sum + a[j];
			if (sum > max)
			{
				max = sum;
				*x = i;
				*y = j;
			}
		}
	}
	return max;
}

int main()
{
	int i, j, n, maxsum;
	clock_t timer;

	/*a small test*/
	int a[4] = { -1, 1, 2, 3 };
	n = sizeof(a) / sizeof(a[0]);				//get the size of the array

	timer = clock();
	maxsum = Enumeration(a, n, &i, &j);
	timer = clock() - timer;
	printf("For the enumeration, the maxsum is %d\nthe start index is %d, and the finish index is %d\n", maxsum, i, j);
	printf("This algorithm ran in %f seconds\n\n", (float)timer / (float)CLOCKS_PER_SEC);

	timer = clock();
	maxsum = betterEnumeration(a, n, &i, &j);
	timer = clock() - timer;
	printf("For a better enumeraton, the maxsum is %d\nthe start index is %d, and the finish index is %d\n", maxsum, i, j);
	printf("This algorithm ran in %f seconds\n\n", (float)timer / (float)CLOCKS_PER_SEC);
	/*end of the test*/
}