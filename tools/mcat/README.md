# mcat

Simple `cat(1)`-style file printer in C.

- With no arguments: reads characters from stdin and echoes them to stdout
- With file arguments: opens each file in order and writes all characters to stdout using `fgetc`/`putchar`
- Exits with status 1 if a file cannot be opened

Next:
- Handle binary files correctly and avoid using `scanf` for stdin
- Add basic `cat` flags later if needed
