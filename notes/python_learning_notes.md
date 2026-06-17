# Python Learning Notes

## Day 14 - Log Analyzer

### Main Idea
The program reads scan.log and counts how many lines contain OPEN and CLOSED.

### Flow
1. Start open_count and closed_count at 0.
2. Open scan.log in read mode.
3. Read all lines from the file.
4. Loop through each line.
5. If a line contains OPEN, add 1 to open_count.
6. If a line contains CLOSED, add 1 to closed_count.
7. Print the summary.

### Important Syntax

#### open("scan.log", "r")
Opens scan.log in read mode.

#### with open("scan.log", "r") as log_file:
Opens scan.log safely and refers to it as log_file while the program is using it.

#### lines = log_file.readlines()
Reads all lines from the file and stores them in a list.

#### if "OPEN" in line:
Checks whether the word OPEN exists inside the current line.

#### elif "CLOSED" in line:
Checks whether the word CLOSED exists inside the current line if OPEN was not found.

#### open_count += 1
Adds 1 to open_count.

#### except FileNotFoundError:
Runs when scan.log does not exist and shows a clean message instead of crashing.

### What I Learned
- How to read a log file
- How to count specific words in a file
- How to use counters
- How to use try and except
- Why elif is more specific than else