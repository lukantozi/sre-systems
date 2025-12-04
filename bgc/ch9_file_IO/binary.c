#include <stdio.h>

int main(void) {
    FILE *fp;
    unsigned char bytes[6] = {5, 37, 0, 88, 255, 12};

    fp = fopen("output.bin", "wb");

    fwrite(bytes, sizeof(char), 6, fp);
}
