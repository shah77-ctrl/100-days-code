## Day 1 to Day 100 - Review Notes

### Day 1 - GitHub Setup and Python Basics
Main idea:
- Set up GitHub and started learning Python basics.

Important reminders:
- GitHub is used to store projects online.
- A repository is a project folder on GitHub.
- Commit means saving a change.
- Push means uploading the commit to GitHub.

---

### Day 2 - Calculator
Main idea:
- Built a simple calculator using input, float, and if/elif/else.

Important syntax:
- input() asks the user to type something.
- float() converts input into a decimal number.
- if / elif / else is used to choose different actions.
- b != 0 checks that the user is not dividing by zero.

Reminder:
- int() is for whole numbers.
- float() is for decimal numbers.

---

### Day 3 - Port Scanner Loop
Main idea:
- Checked a list of ports and printed whether each port is open or closed.

Important syntax:
- for port in ports: loops through each port one by one.
- if port in open_ports: checks whether the current port exists inside the open_ports list.

Reminder:
- in checks whether something exists inside a list.

---

### Day 4 - Log Writer
Main idea:
- Saved scan results into a log file.

Important syntax:
- open("scan_log.txt", "w") opens a file in write mode.
- "w" overwrites the old file.
- log.write(hasil + "\n") writes the result into the file with a new line.
- log.close() closes the file.

Reminder:
- "\n" means new line.

---

### Day 5 - Interactive Scanner
Main idea:
- Asked the user to enter a port and checked whether it was open or closed.

Important syntax:
- int(port_input) converts user input into a whole number.
- if port in open_ports checks whether the entered port is in the open_ports list.
- open("scan_log.txt", "a") opens the file in append mode.
- "a" keeps old content and adds new content at the bottom.

Reminder:
- "w" overwrites.
- "a" appends.

---

### Day 6 - Multi-Port Scanner
Main idea:
- Allowed the user to enter multiple ports at once.

Important syntax:
- ports_input.split(",") splits text into a list.
- for p in ports_list: checks each port one by one.
- int(p) converts each port from string into integer.

Example:
- "22,80,443".split(",") becomes ["22", "80", "443"]

Reminder:
- split() separates text based on a symbol.

---

### Day 7 - Fake Scanner With Log
Main idea:
- Added target IP, datetime, strip(), and log reading.

Important syntax:
- datetime.datetime.now() gets the current date and time.
- p.strip() removes extra spaces.
- open("scan.log", "a") appends scan results.
- open("scan.log").read() reads the log file.

Reminder:
- Day 7 was still a fake scanner because it checked ports using our own open_ports list.

---

### Day 8 - Real Socket Scanner
Main idea:
- Used socket to actually try connecting to a target IP and port.

Important syntax:
- import socket imports the networking module.
- socket.socket() creates a socket.
- s.settimeout(1) limits the waiting time.
- s.connect_ex((target, port)) tries to connect to the target IP and port.
- result == 0 means the connection succeeded, so the port is open.

Reminder:
- Day 7 = fake scanner.
- Day 8 = real connection attempt using socket.

---

### Day 9 - Range Scanner
Main idea:
- Scanned a range of ports from start to end.

Important syntax:
- range(start, end + 1) includes the final port.
- open_found = [] creates an empty list.
- open_found.append(port) adds open ports into the list.
- len(open_found) counts how many open ports were found.

Reminder:
- range(start, end) stops before the end number.
- Use end + 1 to include the final number.

---

### Day 10 - Fast Scanner
Main idea:
- Used threading to scan ports faster.

Important syntax:
- ThreadPoolExecutor allows multiple ports to be scanned at the same time.
- def scan_port(port): creates a function.
- return port sends the open port number back.
- return None means no open port was found.
- [p for p in results if p] removes None values and keeps real port numbers.

Reminder:
- Day 9 scans one by one.
- Day 10 scans many ports at the same time.

---

### Day 11 - Service Detection
Main idea:
- Added a dictionary to identify common services like SSH, HTTP, and HTTPS.

Important syntax:
- services = {22: "SSH", 80: "HTTP"} creates a dictionary.
- services.get(port, "Unknown") searches for the port in the dictionary.
- If the port exists, it returns the service name.
- If the port does not exist, it returns "Unknown".

Reminder:
- Dictionary = key and value.
- 22 is the key.
- "SSH" is the value.

---

### Day 12 - Fast Service Scanner
Main idea:
- Combined fast scanning, service detection, threading, and time duration.

Important syntax:
- return (port, service) returns two values as a tuple.
- port, svc = result unpacks the tuple.
- open_list.append(result) stores open port results.
- duration = (datetime.datetime.now() - start_time).total_seconds() calculates scan duration.

Reminder:
- Tuple example: (22, "SSH")
- Unpacking means splitting tuple values into variables.

---

### Day 13 - Password Strength Checker
Main idea:
- Checked whether a password is weak, medium, or strong.

Important syntax:
- len(password) checks password length.
- char.isupper() checks uppercase letters.
- char.islower() checks lowercase letters.
- char.isdigit() checks numbers.
- char.isalnum() checks letters or numbers.
- not char.isalnum() checks symbols.
- score += 1 adds 1 point to the score.

Reminder:
- isdigit() = number only.
- isalnum() = letter or number.
- not isalnum() = not letter and not number, treated as symbol.
- Do not test using real passwords.

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

## Day 15 - Simple Login System

### Main Idea
The program checks whether the username and password are correct. The user has 3 login attempts.

### Important Syntax

#### login_successful = False
The program assumes the login has not succeeded yet.

#### for attempt in range(3):
Gives the user 3 login attempts.

#### if username == correct_username and password == correct_password:
Checks whether both username and password are correct.

#### break
Stops the loop when login is successful.

#### if not login_successful:
Checks whether the login never succeeded after all attempts. If still False, the program prints Account locked.

### What I Learned
- How to check username and password
- How to use and
- How to limit login attempts
- How to use break
- How to use a True / False flag