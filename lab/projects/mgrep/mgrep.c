#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SENTENCE_SIZE 100

void match(FILE *f, char* pattern, int size) {
    // TODO: implement dynamic allocation
    char *buffer = (char *)malloc(size);
    while (fgets(buffer, size, f)) {
        if (strstr(buffer, pattern) != NULL) {
            printf("%s", buffer);
        }
    }
    free(buffer);
}

int main(int argc, char *argv[]) {
    if (argc == 1) {
        printf("Usage: mgrep PATTERN [FILE]\n");
    } else if (argc == 2) {
        match(stdin, argv[1], SENTENCE_SIZE);
    } else if (argc == 3) {
       FILE *f = fopen(argv[2], "r"); 
       if (f == NULL) {
           printf("File could not open\n");
           return 1;
       }
       match(f, argv[1], SENTENCE_SIZE);
        fclose(f);
    }
    return 0;
}
