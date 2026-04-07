#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[50];
    int id;
    float capability_score;
} Developer;

void update_score(Developer *d, float new_score) {
    if (d != NULL) {
        d->capability_score = new_score;
        printf("System: Logic score for %s updated to %.2f\n", d->name, d->capability_score);
    }
}

int main() {
    Developer *dev1 = (Developer *)malloc(sizeof(Developer));

    if (dev1 == NULL) {
        fprintf(stderr, "Memory allocation failed!\n");
        return 1;
    }

    strcpy(dev1->name, "0xblackout");
    dev1->id = 2026;
    dev1->capability_score = 85.0;

    printf("--- INITIALIZING LOGIC VAULT ---\n");
    printf("Dev Name: %s\n", dev1->name);
    printf("Dev ID: %d\n", dev1->id);

    update_score(dev1, 99.9);

    printf("Cleaning up memory pointers...\n");
    free(dev1);
    
    printf("Vault Secure. System Offline.\n");

    return 0;
}
