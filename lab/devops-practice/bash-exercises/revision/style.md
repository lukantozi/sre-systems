Section 1 — Error Handling & Environment

    Why should error messages go to stderr instead of stdout?
    
    A: to separate actual output from what went wrong

    What does set -o pipefail do?

    A: will exit the script with exit status if the command in the pipe fails

    In the PIPESTATUS example, why do you need return_codes=( "${PIPESTATUS[@]}" ) instead of just return_codes="${PIPESTATUS[@]}"?

    A: so that we create an array instead of the string, which we later can access via indexing

    Why does the guide say [ is a command and will wipe out PIPESTATUS?

    A: because if we check the pipestatus without saving it's values using [ (which is a synonym to test), i am guessing it will
        clean out it's values due to that reason

Section 2 — Comments

    What are the 4 things every function comment should describe?

    A: local/global variables, arguments, if it's complicated, short description what it does, return values if there

    When do you use TODO(username): comments?

    A: when there is something to come back to and do in a multi person project

    Give an example from the notes of a good function comment.

    A: i will not, because im lazy

Section 3 — Formatting

    Indentation is 2 spaces, never tabs. Why no tabs?

    A: i don't think it matters that much, but i guess, tab has a different value than space, and during parsing the code, there could be
    errors. also different users could have different tab expansions, that could cause some inconsistencies

    Max line length? How do you handle long strings?

    A: 80. if quoted, we can just drop to the next line, use here doc strings...

    How should pipelines be formatted if they do not fit on one line?

    A: separated with `\`

Mini task A — reformat this broken pipeline according to the rules:

bash
ls -la /etc | grep "^d" | awk '{print $9}' | xargs echo

A: i didn't really get there (awk) yet, so ... imn't sure what to really fix

Section 4 — Variable Expansion & Quoting

    When do you not need to quote variables?

    A: when they are bash meta characters? or in mathematical expressions

    What is the key difference between "$@" and "$*"?

    A: $@ makes an array, while $* stringifies the string

    Why does grep -cP '([Ss]pecial|\\|?characters*)$' ${1:+"$1"} use ${1:+"$1"} instead of just "$1"?

    A: i honestly have no clue.

Section 5 — Naming & Structure

    Function names: lowercase with _ or ::? Give example.

    A: lowercase with_, :: defines accessing libraries/packages

    Why main "$@" as the last line of long scripts?

    A: so that we pass the arguments into functions

    Variables inside functions: why local? How do you declare + assign on separate lines?

    A: so that we don't pollute namespace and avoid unintentional accessing to the variables. 
    ```bash
    declare -i num1
    num1=12
    ```

Section 6 — Calling Commands

    Prefer builtins over external commands. Give 2 examples from notes.

    A: to do builtin ${var/abc/xyz} instead of sed. second one i don't remember (remembered during answering question below):
        to do math exprs using (( counter++ )), instead of expr counter + 1

    For unpiped commands, what are the 2 ways to check $??

    A: to first run the command and using `if`, check the literal value of $? (math expr), or do the command inside the
        [[]] expression and if truthy, then continue, if not send the appropriate error message to wherever you need to (stderr)
        

Paste answers when ready.
