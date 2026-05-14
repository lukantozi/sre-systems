#include <stdio.h>

int main(void) {
    FILE *fp;
    int x = 32;

    fp = fopen("output.txt", "w");
    //fp = stdout; // to print it out to the console

    fputc('B', fp);
    fputc('\n', fp);
    fprintf(fp, "x = %d\n", x);
    fputs("Hello, world!\n", fp);

    fclose(fp);
}
