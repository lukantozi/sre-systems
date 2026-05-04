#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool isPalindrome(char *s) {
    int l, i;
    l = strlen(s);
    char *st, *en;
    st = s;
    en = s + l - 1;
    while (st < en) {
        while (!isalnum(*st)) {
            st++;
            if (st == en) return 1;
        }
        while (!isalnum(*en)) {
            en--;
            if (st == en) return 1;
        }
        if (tolower(*st) != tolower(*en)) return 0;
        st++;
        en--;
    }
    return 1;
}

int main(void) {
    char *s = "A man, a plan, a canal: Panama";
    printf("%s - %d\n", s, isPalindrome(s));
    char *g = "race a car";
    printf("%s - %d\n", g, isPalindrome(g));
    char *f = " ";
    printf("%s - %d\n", f, isPalindrome(f));
    char *ab = "ab";
    printf("%s - %d\n", ab, isPalindrome(ab));
    char *comma = ".,";
    printf("%s - %d\n", comma, isPalindrome(comma));
    char *tor = "......a.......";
    printf("%s - %d\n", tor, isPalindrome(tor));
    char *con = "0z;z   ; 0";
    printf("%s - %d\n", con, isPalindrome(con));
}
