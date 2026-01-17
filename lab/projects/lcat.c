#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *fp1 = fopen("feed_cat_1.txt", "r");
    FILE *fp2 = fopen("feed_cat_2.txt", "r");

    if (fp1 == NULL || fp2 == NULL) {
        return 1;
    }

    char *ch = malloc(sizeof(ch));
    while ((*ch = fgetc(fp1)) != EOF) {
        putchar(*ch);
    }

    while ((*ch = fgetc(fp2)) != EOF) {
        putchar(*ch);
    }

    free(ch);
    fclose(fp1);
    fclose(fp2);
}
