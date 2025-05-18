# Meeseeks OCR

![image](https://github.com/user-attachments/assets/bf8d39f3-25c5-448c-b669-8130326e26df)

A docker-based, single-purpose microservice to OCR scanned PDFs into readable text files — and vanish. Inspired by *Mr. Meeseeks* from Rick and Morty.

---

## What It Does

- Accepts a **scanned PDF file** from a user
- Converts it to images
- Applies OCR (Tesseract)
- Saves the text to a local `.txt` file and prints it to the terminal
- This is accomplished in docker

---

### MVP Workflow

1. **Upload your PDF**

2. Run `meeseeks-ocr -i/--input /your_log.pdf` OR `meeseeks-ocr -i/--input /your_log.pdf -o output.txt`

- If the output is short (≤ 500 lines), it prints to the screen.
- If longer, Meeseeks will ask you to specify an output file.

3. Copy the results

---

## Installation

1. Clone the repo
2. Build the docker image
3. If using *nix - Add a CLI alias (optional but recommended)
4. Now you can run: meeseeks-ocr -i scanned_log.pdf

```bash
git clone https://github.com/matoblac/meeseeks_ocr.git # Step 1
cd meeseeks_ocr # Step 1
docker build -t meeseeks-ocr . # Step 2 - wait 5-10 minutes for this process to complete
alias meeseeks-ocr='docker run --rm -v $(pwd):/data meeseeks-ocr' # Step 3 If using ~/.bashrc or ~/.zshrc
source ~/.bashrc # Step 3 If using ~/.bashrc or ~/.zshrc
meeseeks-ocr -i scanned_log.pdf # Step 4
```

### Windows Users
use `%cd%` for native `CMD`
```cmd
docker run --rm -v %cd%:/data meeseeks-ocr -i /data/log.pdf
```
---

### Example

#### With alias(*nix)

```bash
meeseeks-ocr -i /printer_dump.pdf
```

#### Without alias(*nix)

```bash
docker run --rm -v $(pwd):/data meeseeks-ocr -i /data/log.pdf
```

#### With Windows (CMD)

```bash
docker run --rm -v %cd%:/data meeseeks-ocr -i /data/log.pdf
```

---

#### Output
```
=== OCR Output ===
2025-05-17 08:14:23,583 INFO [com.example.MainService] - Application starting up with
environment: PRODUCTION
2025-05-17 08:14:23,742 INFO [com.example.config.AwsConfiguration] - Initializing AWS
client with accessKey: AKIA23XYZJKLMNOPQRST [REDACTED]
2025-05-17 08:14:24,005 INFO [com.example.db.ConnectionPool] - Database connection
pool initialized with 10 connections
```

---

## Summary of Project Setup Choices

| Aspect | Current MVP | Scalable Later |
|--------|-------------|----------------|
| **Input** | Local file path | Web App |
| **Output** | Local `.txt` file | Web App |
| **Auth** | None | Sign with Web App |
| **Infra** | Container | Web App |
| **Install** | Docker | SignUp for Web App |
| **User Interface** | CLI only | Could be web UI with advance options + ML + wider impact + automated error detection with read ability on codebase |


