#include <stdio.h>
#include <stdlib.h>

#define SEN_SIZE 100
#define LIMIT 10

void out(FILE *dest, int limit) {
    int line_count = 0;
    // TODO: implement dynamic malloc
    char *s = malloc(SEN_SIZE);
    if (s == NULL) {
        perror("malloc");
        exit(1);
    }
    while (line_count < limit && fgets(s, SEN_SIZE, dest)) {
        fprintf(stdout, "%s", s);
        line_count++;
    } 
    free(s);
}

FILE *file_val(char *arg) {
    FILE *f = fopen(arg, "r");
    if (f == NULL) {
        perror("file");
        exit (1);
    }
    return f;
}

int main(int argc, char *argv[]) {
    if (argc == 1) out(stdin, LIMIT);
    else if (argc == 2 || argc == 3) {
        FILE *f = file_val(argv[1]);
        int limit = (argc == 2) ? LIMIT : atoi(argv[2])
        out(f, limit);
        fclose(f);
    return 0;
}
