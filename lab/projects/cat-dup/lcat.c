#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    if (argc == 1) {
        char c;
        while (c != EOF) {
            scanf("%c", &c);
            //printf("%c", c);
            putchar(c);
        }
    }

    for (int i = 1; i < argc; i++) {
        FILE *fp = fopen(argv[i], "r");

        if (fp == NULL) {
            return 1;
        }

        char *ch = malloc(sizeof(ch));
        while ((*ch = fgetc(fp)) != EOF) {
            putchar(*ch);
        }

        free(ch);
        fclose(fp);
    }
}
