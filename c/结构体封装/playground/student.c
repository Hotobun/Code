# include <malloc.h>

struct Student {
	char *name;
	int age;
	int student_id;
};

struct Student *Create_newstudent(char *name, int age, int student_id) {
	struct Student * new = (struct Student *)malloc(sizeof(struct Student));
	new->name = name;
	new->age = age;
	new->student_id = student_id;
	return new;
}

char * getName(struct Student * student) {
	return student->name;
}

int getAge(struct Student * student) {
	return student->age;
}

int getId(struct Student * student) {
	return student->student_id;
}

void Free(struct Student *student) {
	free(student);
}