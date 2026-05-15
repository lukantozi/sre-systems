# mgrep

Simplified `grep(1)` in C.

- Usage:
  - `mgrep PATTERN` reads from stdin
  - `mgrep PATTERN FILE` reads from `FILE`
- Reads each line with `fgets` into a fixed-size buffer (`SENTENCE_SIZE == 100`)
- Prints lines where `strstr(buffer, pattern) != NULL`

Next:
- Switch to dynamically growing buffers to handle longer lines safely
- Add basic flags (e.g. case-insensitive search)
