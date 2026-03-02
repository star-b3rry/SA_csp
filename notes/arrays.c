#include <stdio.h>

int main(){
    // Example 1
    int grades[] = {84,74,99,78,97};
    printf("%d\n", grades[2]); //single item from the array based on index number
    grades[2] = 85;
    printf("%d\n", grades[2]);
    grades[4] = NULL;
    return 0;
}