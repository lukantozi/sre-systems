#include <stdio.h>

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Please specify the file to operate on.\n");
        return 0;
    }

    int c;
    int line_count = 0;
    int char_count = 0;
    int word_count = 0;
    int space_flag = 0;

    FILE *pf = fopen(argv[1], "r");
    if (pf == NULL) {
        fprintf(stderr, "Error: cannot open file\n");
        return 1;
    }
    while ((c = fgetc(pf)) != EOF) {
        char_count++;
        if (!((c >= 0x09 && c <= 0x0D) || c == 0x20)) {
            if (space_flag == 1) {
                word_count++;
                space_flag = 0;
            }
        }
        if (c == '\n') {
            line_count++;
        }
        if ((c >= 0x09 && c <= 0x0D) || c == 0x20) {
                space_flag = 1;
        }
    }
    fclose(pf);
    printf("total lines = %d\n", line_count);
    printf("total words = %d\n", word_count);
    printf("total characters = %d\n", char_count);
}
