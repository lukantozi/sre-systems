#include <stdio.h>
#include <stdlib.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strs[0][0] == '\0') {
        return "";
    }
    int i = 0;
    int j = 0;
    int buffSize = 201;
    int min = 201;
    char *pref = malloc(sizeof(char)*buffSize);

    for (i = 0; i < strsSize - 1; i++) {
        j = 0;
        while (strs[i][j] == strs[i+1][j] && strs[i][j] != '\0') {
            j++;
        }
        min = j < min ? j : min;
    }
    if (min == 201) {
        free(pref);
        return strs[0];
    }
    else {
        for (i = 0; i < min; i++) {
            pref[i] = strs[0][i];
        }
        pref[min] = '\0';
        return pref;
    }
}

int main(void) {
    char *s[3] = {"flower","flow","flight"};
    char *s1[3] = {"dog","racecar","car"};
    char *s2[1] = {""};
    char *s3[1] = {"a"};
    char *s4[2] = {"", ""};
    printf("flower: %s\n", longestCommonPrefix(s, 3));
    printf("dog: %s\n", longestCommonPrefix(s1, 3));
    printf("'': %s\n", longestCommonPrefix(s2, 0));
    printf("a: %s\n", longestCommonPrefix(s3, 1));
    printf("'', '': %s\n", longestCommonPrefix(s4, 2));
    return 0;
}
