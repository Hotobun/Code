# include <stdio.h>
# include "student.h"
# include <stdlib.h>

int main(void) {
	struct Student *cocoa = Create_newstudent("cocoa", 12, 18);
	printf("age = %d\nname = %s\n",getAge(cocoa),getName(cocoa));


	Free(cocoa);

	system("pause");
	return 0;
}