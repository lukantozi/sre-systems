# mtail

Minimal clone of `tail(1)` in C.

- Prints the last N lines from a file (currently fixed at 10)
- Reads the whole file into a growable buffer
- Tracks line-start offsets in a dynamic `size_t` array
- `mtail FILE` prints the last 10 lines of `FILE`

Next:
- Add `-n N` flag to choose how many lines to print
- Support stdin when no file is given
- Refactor variable names and structure for clarity
- Consider a seek-from-end version for very large files
