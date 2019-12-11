# include <stdio.h>
# include <stdlib.h>
# define N 6
# define W 21

int B[N][W] = { 0 };
int w[6] = { 0,2,3,4,5,20};
int v[6] = { 0,3,4,5,8,999 };

void knapsack() {
	int k, C;
	for (k = 1; k < N; k++) {
		for (C = 1; C < W; C++) {
			if (w[k] > C) {
				B[k][C] = B[k - 1][C];
			}
			else {
				int value1 = B[k - 1][C - w[k]] + v[k];
				int value2 = B[k - 1][C];
				if (value2 > value1) {
					B[k][C] = value2;
				}
				else {
					B[k][C] = value1;
				}
			}
		}

	}

}

void show(int * arr) {
	int i;
	for (i = 0; i < 21; i++) {
		printf("%d|", i);
	}
	printf("  \n");
	for (i = 0; i < 21; i++) {
		printf(":--:|");
	}
	printf("  \n");
	for (i = 0; i < N; i++) {
		printf("%d|", i);
		for (int j = 1; j < W; j++) {
			printf("%d|", B[i][j]);
		}
		printf("\n");
	}
}

int main(void) {
	knapsack();
	printf("%d \n", B[5][20]);
	show(B);
	system("pause");
	return 0;
}