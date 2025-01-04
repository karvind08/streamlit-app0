#include <stdio.h>
struct Student
{
    int r;
    char name[20];
    struct Student *p;
};

int main()
{
    struct Student s1;
    s1.r = 1;
    s1.name = "Arvind";
    s1.p = NULL;
    printf("%d%s", s1.r, s1.name);
}