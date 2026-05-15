# mwc

Minimal clone of `wc(1)` in C.

- Usage: `mwc FILE`
- Counts lines, words, and characters by scanning the file with `fgetc`
- Treats spaces and ASCII whitespace as separators; tracks word boundaries with a flag

Next:
- Support multiple input files and a stdin mode
- Match the exact `wc` output format and flags gradually
