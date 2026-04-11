Based on your mistakes, here are targeted exercises — nothing else.

***

## awk Field Variables

**E1.** Given this file `data.txt`:
```
london uk europe 8000000
tokyo japan asia 14000000
cairo egypt africa 10000000
```
Write awk to:
- print line number + city name (fix your `$NR` mistake)
- print only lines where continent is `asia`
- print city and population only

A:
```bash
awk '{print NR,$1}' data.txt
awk '/asia/ {print}' data.txt
awk '{print $1 $NR}' data.txt
```

**E2.** What is wrong with this and fix it:
```bash
awk '{print $NR, $0}' data.txt
```
A:
NR tries to acess the last column, when we just want to get the number of lines, i assume
```bash
awk '{print NR,$0}'
```
***

## awk Pattern Filtering

**E3.** What does each of these actually print, and which one is correct for filtering lines?
```bash
# a)
awk '{print /europe/}' data.txt

# b)
awk '/europe/ {print}' data.txt
```
A:
a) print the outcome of the search, (0 or 1)
b) print lines where "europe" was found

***

## sed `-n` and `p`

**E4.** Given `log.txt` with 20 lines, some containing `ERROR`. Explain what each does and what the output difference is:
```bash
# a)
sed 's/ERROR/FIXED/' log.txt

# b)
sed -n 's/ERROR/FIXED/' log.txt

# c)
sed -n 's/ERROR/FIXED/p' log.txt
```

A:
a) here all the newlines are output after processing
b) here automatic writing of newlines is disabled
c) here, automatic writing of newlines is disabled, but we tell sed to print the lines that were modified

**E5.** Write a sed one-liner that prints **only** lines containing `WARNING` from a file, without modifying anything. Use `-n` and `p`.
A:
```bash
sed -n '/WARNING/p' text
```
***

## sed Flags and Delimiters

**E6.** Fix both bugs:
```bash
sed -i 's/error/warning' file.txt
```
A:
```bash
sed -i 's/error/warning/' file.txt
```

**E7.** You want to replace `/usr/local/bin` with `/usr/bin` in a file. Write it two ways:
- using `/` as delimiter (with proper escaping)
- using `|` as delimiter (cleaner)

sed -i 's/\/usr\/local\/bin/\/usr\/bin/' file
sed -i 's/%/usr/local/bin%/%usr/bin$/' file (wrong) -> sed -i 's|/usr/local/bin|/usr/bin|g' file
***

## sed Address Negation

**E8.** Write a sed command that replaces `foo` with `bar` on every line **except** lines containing `skip`.


```bash
sed -i '!/skip/s/foo/bar' file
```
***

## awk Field Separator

**E9.** Given `/etc/passwd` where fields are separated by `:`, write an awk command to print only the username (field 1) and home directory (field 6).

```bash
awk -F: '{print $1 $6}' /etc/passwd
```
