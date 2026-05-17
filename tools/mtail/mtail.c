#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: ./mtail FILE\n");
        exit(1);
    }
    // open file
    FILE *f;
    if ((f = fopen(argv[1], "r")) == NULL) {
        perror("open error");
        exit(1);
    }
    /*
    // check if the file's empty
    fseek(f, 0, SEEK_END);
    if (ftell(f) == 0) {
        return 0;
    }
    fseek(f, 0, SEEK_SET);
    */
    // initialize variables
    size_t offsetSize = 10;
    size_t lineCount = 0;
    size_t bufferSize = 80;
    size_t *offsets;
    size_t *new_offsets;
    size_t ofst = 0;
    int c;
    char *buffer;
    char *new_lines;
    // allocate buffer
    if ((buffer = malloc(bufferSize)) == NULL) {
        perror("buffer malloc");
        fclose(f);
        exit(1);
    }
    // allocate offsets
    if ((offsets = malloc(sizeof(size_t)*offsetSize)) == NULL) {
        perror("offset malloc");
        free(buffer);
        fclose(f);
        exit(1);
    }
    offsets[0] = 0;
    // write chars into buffer
    while ((c = fgetc(f)) != EOF) {
        if (ofst == bufferSize - 1) { // grow buffer if at the second last
            new_lines = realloc(buffer, bufferSize*2);
            if (new_lines == NULL) {
                free(buffer);
                fclose(f);
                perror("buffer realloc");
                exit(1);
            } 
            bufferSize *= 2;
            buffer = new_lines;
        }
        // detect end of line
        if (c == '\n') {
            if (lineCount == offsetSize - 1) {
                if ((new_offsets = realloc(offsets, sizeof(size_t)*offsetSize*2)) == NULL) {
                    free(offsets);
                    free(buffer);
                    fclose(f);
                    perror("offsets realloc");
                    exit(1);
                }
                offsets = new_offsets;
                offsetSize *= 2;
            }
            offsets[++lineCount] = (size_t)(ofst+1);
        }
        buffer[ofst++] = c;
    }

    if (ofst < bufferSize - 1 && ofst != 0) { // free up unused memory
        new_lines = realloc(buffer, ofst);
        if (new_lines != NULL) {
            buffer = new_lines;
            bufferSize = ofst;
        }
    }

    if (lineCount < offsetSize - 1) { // free up unused mem
        new_offsets = realloc(offsets, sizeof(size_t)*(lineCount+1));
        if (new_offsets != NULL) {
            offsets = new_offsets;
        }
    }
    size_t requested = 10;
    size_t printFrom = lineCount < requested ? lineCount : requested;
    size_t st = offsets[lineCount-printFrom];
    while (st < ofst) {
        putchar(buffer[st++]);
    }
    free(offsets);
    free(buffer);
    fclose(f);
}
