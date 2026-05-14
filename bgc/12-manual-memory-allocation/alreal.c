#include <stdio.h>
#include <stdlib.h>

char *readline(FILE *pf) {
    // init buf bufsize ofset char
    char *buf;
    int buffer = 4;
    int offset = 0;
    int c;

    // Error check
    if ((buf = malloc(buffer)) == NULL) return NULL;

    // Main loop--read until newline or EOF
    while (c = fgetc(pf), c != '\n' && c != EOF) {
        // Check if we're out of room in the buffer accounting
        if (offset == buffer - 1) {
            buffer *= 2;
            // for the extra byte for the NUL terminator
            char *new_buf = realloc(buf, buffer);
            if (new_buf == NULL) {
                free(buf);
                return NULL;
            }
            buf = new_buf;
        }
        buf[offset++] = c;
    }
    
    // if at EOF and we read no bytes, free the buffer and return NULL
    // to indicate that we're at EOF
    if (c == EOF && offset == 0) {
        free(buf);
        return NULL;
    }

    // shrink buffer
    if (offset < buffer - 1) {        
        // +1 for null terminator
        char *new_buf = realloc(buf, offset + 1);
        if (new_buf == NULL) return NULL;
        buf = new_buf;
    }
    // add null terminator
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
