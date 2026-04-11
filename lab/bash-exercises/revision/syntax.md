These are targeted directly at your weak spots from the quiz — not random exercises.

***

## Syntax Muscle Memory

These tripped you up repeatedly. Write and run each one in your terminal.

**E1.** Assign the string `hello world` to a variable `msg` and print it. Then try adding a space around `=` and observe the error.

**E2.** Write a script that sets a variable `name` but never uses it. Run it once normally, then again with `set -u`. Observe the difference.

**E3.** Write a script with a deliberate error on line 3 (e.g. `cat nonexistent.txt`), then a `echo "still running"` on line 4. Run it twice — once with `set -e`, once without.

**E4.** Add `set -x` to any small script you have and run it. Just observe what it prints — understand what "expanding commands" actually looks like in practice.

***

## String Manipulation

**E5.** Given `path=/var/log/nginx/access.log`, extract just `access.log` using `##`. Then extract just `access` (no extension) using `%`.

**E6.** Given `str=aabbccbbaa`, write the substitutions to:
- replace the first `bb` with `XX`
- replace all `bb` with `XX`
- delete all occurrences of `aa`

**E7.** Given `stringZ=Hello_World_2024`, extract:
- characters at position 6, length 5
- everything after the first `_`
- everything before the last `_`

***

## Exit Codes

**E8.** Run these one by one, check `$?` after each, and write down what you get:
```bash
ls /nonexistent
/bin/ls            # valid but try running a directory
notacommand
chmod 000 /tmp/testfile && /tmp/testfile
```

**E9.** Write a script that runs three commands in a pipe where the middle one fails. Print `${PIPESTATUS[@]}` and observe which position has the non-zero code. Then modify the middle command to succeed and compare.

***

## Parameter Substitution

**E10.** Open a fresh shell. Without setting any variable, test each of these and write down what prints:
```bash
echo ${x-"not set"}
echo ${x:-"not set or null"}
x=
echo ${x-"not set"}
echo ${x:-"not set or null"}
```

**E11.** Write a script that accepts a filename as `$1` and uses `${1:-default.txt}` as the actual filename. Run it with and without an argument.

**E12.** Write a one-liner using `${var:+extra}` that prints `--verbose` only when a variable `DEBUG` is non-empty, and nothing otherwise.

***

## Conditions and Loops

**E13.** Fix this broken script:
```bash
#!/bin/bash
counter = 1
while [[ counter -le 5 ]]; do
    echo $counter
    (( counter ++ ))
done
```

**E14.** Write an `until` loop that keeps prompting the user with `read` for a password until they type `secret`. Print "Access granted" when they get it right.

**E15.** Write a `case` statement that takes `$1` and handles: `start`, `stop`, `restart`, and a default `*` that prints usage.

***

## Functions

**E16.** Write a function `greet` that takes a name as `$1` and a greeting as `$2`, both with defaults (`World` and `Hello` respectively) using `:-`. Call it four ways: both args, one arg, no args, and with an empty first arg.

**E17.** Write a function that intentionally uses a variable without `local`, then calls it and checks whether the variable leaked into the outer script scope. Repeat with `local` and compare.

**E18.** Write a function `divide` that takes two numbers, returns `1` if the second is zero (with an error message to stderr), otherwise echoes the result. Check `$?` after calling it both ways.

***

## Redirection

**E19.** Run `java -version` (or any command that writes to stderr). Redirect stderr and stdout separately to two different files. Then use `&>` to merge them into one. Compare the three files.

**E20.** Write a here document that generates a simple config file with at least 4 lines, using a variable inside it. Then write the same content using a here string — note where it becomes impractical.

**E21.** Use `tee` to run `ls -la`, display output in the terminal, and write it to `listing.txt` simultaneously. Then verify the file was written.

***

Start with E1–E4 (syntax), then E13 (fixing a broken script) — those directly target your most repeated mistakes. Come back with code or output whenever you want it reviewed.
