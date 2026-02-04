#include <stdio.h>
#include <stdlib.h>


char *readline(FILE *pf) {
    char *buf;
    int buffsize = 4;
    int offset = 0;
    int c;

    // Error check
    buf = malloc(buffsize);
    if (buf == NULL) {
        return NULL;
    }

    // Main loop--read until newline or EOF
    while (c = fgetc(pf), c != '\n' && c != EOF) {
        // Check if we're out of room in the buffer accounting
        // for the extra byte for the NUL terminator
        if (offset == buffsize - 1) {
            buffsize *= 2; 
            char *new_buff = realloc(buf, buffsize);

            if (new_buff == NULL) {
                free(buf);
                return NULL;
            }
            buf = new_buff;
        }
        buf[offset++] = c;
    }

    
    // if at EOF and we read no bytes, free the buffer and return NULL
    // to indicate that we're at EOF
    if (c == EOF && offset == 0) {
        free(buf);
        return NULL;
    }

    if (offset < buffsize - 1) {
        char *new_buff = realloc(buf, offset + 1); // +1 for null terminator

        if (new_buff != NULL) {
            buf = new_buff;
        }
    }

    buf[offset] = '\0';
    return buf;
}


int main(void) {
    FILE *fp = fopen("foo.txt", "r");
    char *line;
    while ((line = readline(fp)) != NULL) {
        printf("%s\n", line);
        free(line);
    }
}
