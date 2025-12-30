#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void) {
    // allocate aligned space
    char *p = aligned_alloc(64, 256); // 64 byte alignment with total of 256 bytes (256 = 64 * 4)

    // copy the string into the aligned memory
    strcpy(p, "Hello, World!");
    printf("%s\n", p);

    free(p);
}
