#include <stdio.h>

int main() {
    int budget = 5000;
    int *b_ptr = &budget;
    int price;
    int total = 0;
    int bonus_given = 0;

    for(int i = 0; i < 3; i++) {
        printf("Enter price: ");
        scanf("%d", &price);
        total = total + price;

        if (total > 2500 && bonus_given == 0) {
            *b_ptr = *b_ptr + 1000;
            bonus_given = 1;
        }
    }

    printf("Final Total: %d\n", total);
    printf("Final Budget: %d\n", budget);

    return 0;
}
