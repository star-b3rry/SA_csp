//SA financial calculator
#include <stdio.h>

int main () {
    int income;

    int rent;

    int utilities;

    int groceries;

    int transportation;
    
    printf("What is your monthly income? ");
    scanf("%d", &income);
    printf("What is your monthly rent? ");
    scanf("%d", &rent);
    printf("What is your monthly utilities? ");
    scanf("%d", &utilities);
    printf("What is your monthly groceries? ");
    scanf("%d", &groceries);
    printf("What is your monthly transportation? ");
    scanf("%d", &transportation);

}
    float divide(int income, int rent){
        return (float) income/rent;
        }
    
    float divide(int income, int utilities){
        return (float) income/utilities;
       }
     float divide(int income, int groceries){
        return (float) income/groceries;
       }
      float divide(int income, int transportation){
        return (float) income/transportation;
       }

       