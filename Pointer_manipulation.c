#include <stdio.h>

int main() {
     int VIP_item = 777;
     int *target = &VIP_item;
     int itm1;
     int item = 0;

     for(int i=0; i<5; i++) {
          printf("Enter item value: %d", i);
          scanf("%d", &itm1);
          item = item + itm1;

          if (itm1 == *target) {
              printf("item found: %d (limit: %d\n) ",*target, item);
          } else {
               printf("item not found\n");
             }
     }

     printf("total item: %d\n", item);

return 0;
}
