Section 1 — awk Basics

    What is awk's primary purpose in one sentence?

    A: to process the text line by line, performing operations on them

    What does $0 represent in awk? What about $1, $2?

    A: $0 represents the whole line the awk is on currently while processing the text.
        $1 is the first field of the line, $2 - second. field, that is, two strings separated by
        whitespace (default separator of awk).

    What is the default field separator in awk, and how do you change it?

    A: it's a whitespace, and you can modify it by FS="some character"

    What is the structure of an awk program? Write the skeleton with BEGIN, a pattern rule, and END.

    A: awk 'BEGIN {action} END {action}'

    If no input file is specified, where does awk read from?

    A: stdin

Section 2 — awk Built-in Variables

    What is the difference between NR and NF?

    A: NR counts the number of Rows, and NF counts number of Fields while processing the input

    What does $NF give you and why?

    A: last field of the line, because it is the maximum number of fields, in the current line

    What is OFS and when does it apply?

    A: OFS is the output field separator, and it applies to how awk prints the processed text out
        (whitespace by default)

    What is RS and what is its default value?

    A: it's a record separator character and it's default value is `newline` (i peeked into notes)

Mini task A — given this file:

text
alice engineer backend 95000
bob manager frontend 120000
carol designer backend 80000

Write awk commands to:

    print only the name and salary (columns 1 and 4)

    A: awk '{print $1,$NF}' text

    print each line prefixed with its line number
    
    A: awk '{print $NR $0}' text

    print only lines where the department is backend

    A: awk '{print /backend/}' text

Section 3 — sed Basics

    sed does not modify the original file by default — true or false? How do you make it modify in place?

    A: true. by specifying option `-i`

    What does -n flag do in sed?

    A: does not append space/whitespace at the end of the each output

    What is the general syntax of a sed command including the address part?

    A: sed [addr]command[options]

Section 4 — sed Addresses

    What is the difference between these two sed commands?

bash
sed '5s/hello/world/' input.txt
sed '/apple/s/hello/world/' input.txt

    A: in the first command, we are replacing the hello -> world on the 5th line
        in the second command, we are replacing hello with world, on all lines
        where we have word apple

    What does ! do when appended to a sed address?

    A: not sure, but assuming exclusion.

    Why would you use \\%pattern% instead of /pattern/ as a sed address?

    A: to specify that it does not have to start or end with that pattern (i may be wrong)

Section 5 — sed Commands

    What is the difference between a, i, and c commands in sed?

    A: a is append, meaning that the text will be inserted below specified line
        i is insert, meaning that the text will be inserted above specified line
        c is replace, meaning that the text will be replaced on that specified line with the text

    What does the y command do? How is it different from s?

    A: y transliterates characters; y/abc/123 would replace all a's into 1, b's into 2....

    What does p do, and why is it usually paired with -n?

    A: don't remember. assuming that when writing -n, we tell said not to add space at the end of the
        processed chunk, so maybe p allows us to specify what to add at the end of the processed chunk

Mini task B — write sed commands to:

    delete lines 5 through 10 from a file

    A: sed -i '5,10d' file

    replace all occurrences of error with warning case-insensitively

    A: sed -i 's/error/warning' file (don't remember case-insens flag/option)

    replace foo with bar only on lines that contain the word debug

    A: sed -i '/debug/s/foo/bar' file

    insert the line # header above line 1

    A: sed -i '1i "# header" ' file

Section 6 — awk vs sed

    When would you reach for awk over sed, and vice versa?

    A: i would choose awk when i need to deal with text with many columns and i know that they are separated with same chars
        i would choose sed over awk, when i need to make pattern changes in the file

    Both tools can do substitution. What makes awk more powerful for structured data?

    A: as mentioned above, it can parse a lot of text, if the character delimiter is present and consistent

Paste answers when ready.
Prepared using Claude Sonnet 4.6 Thinking
