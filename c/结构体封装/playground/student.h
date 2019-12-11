# pragma once
struct Student;
struct Student * Create_newstudent(char *name, int age, int student_id);
void Free(struct Student* student);

char * getName(struct Student * student);
int getAge(struct Student * student);
int getId(struct Student * student);
