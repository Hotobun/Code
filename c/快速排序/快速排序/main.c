# include <stdio.h>

void sort(int array[], int left, int right) {
	if (left > right) {
		return;
	}
	int i, j,t,temp;
	i = left;
	j = right;
	temp = array[i];
	while (i < j) {
		while ( i < j && array[j] >= temp) {
			j--;
		}
		while (i < j && array[i] <= temp) {
			i++;
		}
		if (i < j) {
			t = array[j];
			array[j] = array[i];
			array[i] = t;
		}		
	}
	array[left] = array[i];
	array[i] = temp;
	sort(array, 0, i - 1 );
	sort(array, i + 1, right);
}

void print(int array[], int count) {
	for (int i = 0; i < count; i++) {
		printf("%4d", array[i]);
	}
	printf("\n");
}

int main(void) {
	int a[100] = { 0 };
	int count = 0;
	int i;
	do{
		scanf_s("%d", &i);
		if (i == 0) {
			break;
		}
		a[count++] = i;
	} while (i);
	print(a, count);
	sort(a, 0, count-1);
	print(a, count);

	return 0;
}