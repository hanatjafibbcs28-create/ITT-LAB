#include <stdio.h>
#include <stdbool.h>

int main() {
    int year;
    // Read the year from standard input
    if (scanf("%d", &year) != 1) return 0;

    // Transition year case
    if (year == 1918) {
        printf("26.09.1918\n");
    }
    // Julian Calendar case
    else if (year < 1918) {
        if (year % 4 == 0) {
            printf("12.09.%d\n", year); // Julian Leap Year
        } else {
            printf("13.09.%d\n", year); // Julian Regular Year
        }
    }
    // Gregorian Calendar case
    else {
        bool is_leap = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
        if (is_leap) {
            printf("12.09.%d\n", year); // Gregorian Leap Year
        } else {
            printf("13.09.%d\n", year); // Gregorian Regular Year
        }
    }

    return 0;
}
