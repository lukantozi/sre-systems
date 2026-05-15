# mhead

Minimal clone of `head(1)` in C.

- Prints the first N lines from stdin or a file (default 10)
- Uses `fgets` into a fixed-size buffer (`SEN_SIZE == 100`)
- `mhead FILE [N]` reads from `FILE` and prints N lines; with no args, reads from stdin
- On error (`fopen`, `malloc`) prints with `perror` and exits

Next:
- Replace fixed buffer with `fgetc` + dynamic `realloc` to support arbitrarily long lines
- Add proper `-n N` flag parsing instead of positional `N`
