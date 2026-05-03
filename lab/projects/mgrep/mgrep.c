#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc == 1) {
        printf("Usage: mgrep PATTERN [FILE]\n");
    } else if (argc == 2) {
        int size = (int)strlen(argv[1]);
        char pattern[size];
        strcpy(pattern, argv[1]);
        while (true) {
            char *sdi = (char *)malloc((sizeof(char) * 100));
            int c;
            int ind = 0;
            while ((c = getchar()) != EOF) {
                sdi[ind++] = c;
                if (c == '\n') {
                    printf("%s", sdi);
                }
            }
            //sdi[ind+1] = '\0';
            //if (strncmp(pattern, sdi, (size_t)size) == 0) {
            //    printf("Match: %s\n", sdi);
            //}
        }
    }
}
    /*
    int c;
    FILE *f = fopen("text", "r");
    if (f == NULL) {
        printf("File could not open\n");
        return 1;
    }
    while ((c = fgetc(f)) != EOF) {
        putchar(c);
    }
    */

