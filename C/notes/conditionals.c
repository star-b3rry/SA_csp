// SA Conditionals
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(){
    int grade = 97;
    bool isProgramming = true;

    if (grade > 90){
        printf("Your grade is %d percent, that is an A!\n", grade);
    }else if (grade >=80){
        printf("Your grade is %d percent, that is a B.\n", grade);
    }else if (grade >= 70){
         printf("Your grade is %d percent, that is a C.\n", grade);
    }else if (grade >= 60){
         printf("Your grade is %d percent, that is a D.\n", grade);
    }else{ 
         printf("Your grade is %d percent, youre failing..\n", grade);
    }








    int num = 4;

    if (num < 10){
            printf("Your number is %d, that is a single didgit number\n", num);
    }else if (num < 100){
            printf("Your number is %d, that is a double didgit number\n", num);
    }else if (num < 1000){
            printf("Your number is %d, that is a triple didgit number\n", num);
    }else if (num < 1000){
            printf("Your number is %d, that is a large number\n", num);
        return 0;
    }

    char name[] = "Andrew";

    if (strcmp(name, "Andrew")) {
    }else{ 
        printf("Welcome %s!", name);
    }

