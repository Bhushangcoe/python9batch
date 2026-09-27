# Python 9 Batch

This repository contains standalone Python practice examples covering basic conditions, exception handling, text files, CSV files, PDF generation, and MySQL database operations. It is a collection of lessons rather than an installable Python package; run one script at a time from the repository folder.

## Folder Overview

All lesson scripts and their sample data are currently in the repository root. There are no Python package or application source subfolders.

| Entry | Purpose |
| --- | --- |
| `.vscode/` | Visual Studio Code workspace settings. `settings.json` selects the Python extension's system environment manager. |
| `.git/` | Git's internal repository data. It is managed by Git and is not lesson content. |
| `26.2.1` | Empty file with no extension; currently a placeholder with no documented role. |
| `9.0.0` | Empty file with no extension; currently a placeholder with no documented role. |
| `python` | Empty file with no extension; currently a placeholder with no documented role. |

## Python Examples

### Basics and Exceptions

| File | What it demonstrates |
| --- | --- |
| `demo.py` | An `if`/`else` condition that checks voting age. |
| `exceptiondemo.py` | A function, integer input, division, and handling invalid input and division by zero. |
| `exceptiondemo2.py` | `try`/`except`/`else`/`finally`, string indexing, and string case conversion. |
| `exceptiondemo3.py` | A broad exception handler around reading a file. It currently tries to open `data.text`; the sample file in this repository is named `data.txt`. |
| `customeexception.py` | Defines and raises a custom age exception when the entered age is below 16. |
| `customeexception2.py` | Defines a custom marks exception and checks that marks are between 0 and 100. |

### Text Files

| File | What it demonstrates |
| --- | --- |
| `createtext.py` | Opens `abc1.txt` in read/write mode, prints its contents, then writes `bye` at the current file position (after the read). |
| `readtext.py` | Reads and prints the first 15 characters from `data.txt`. |
| `writetext.py` | Opens `data.txt` in write mode and writes sample lines. Write mode replaces the existing contents. |
| `appendtext.py` | Opens `data.txt` in append mode and adds a line without replacing its current contents. |
| `read.py` | Connects to MySQL and selects employee rows ordered by name; despite its short filename, it is a database example, not a text-file reader. |

### CSV and PDF

| File | What it demonstrates |
| --- | --- |
| `readcsv.py` | Opens `employee.csv` and creates a CSV reader. The loop that would print rows is commented out, so it currently does not display the records. |
| `writecsv.py` | Appends several employee rows to `employee.csv`. The `data` list is an example; the active calls write separate rows directly. |
| `employee.csv` | Sample employee data. It currently contains repeated header rows and employee records. |
| `pdffilewrite.py` | Uses ReportLab to create `first.pdf` with a short line of text. Running it overwrites that output file. |
| `first.pdf` | Generated PDF output from `pdffilewrite.py`. |

### MySQL Database

These scripts use the MySQL Connector/Python package and connect to a local server as `root`. Most expect a database named `python9` and a table named `employee`.

| File | What it demonstrates |
| --- | --- |
| `data.py` | Connects to the MySQL server and creates the `python9` database. |
| `createtable.py` | Creates the `employee` table with employee ID, name, department, and salary columns. |
| `insertrecord.py` | Inserts multiple employee records into the table. |
| `selectusingwhere.py` | Selects and displays employee records; its active query orders all rows by name. Example `WHERE` queries are commented out. |
| `update.py` | Prompts for an employee ID and salary, then updates that employee's salary. |
| `delete.py` | Prompts for an employee ID and deletes the matching record. |
| `delete_duplicate.py` | Replaces the `employee` table contents with distinct rows to remove exact duplicate records. |

## Setup and Running

Use Python 3. Install the external packages used by the examples:

```bash
python -m pip install mysql-connector-python reportlab
```

The MySQL examples also require a running local MySQL server. Review the connection settings in each script and use credentials appropriate for your machine. The examples currently contain the username `root` and password `root`; do not use those hard-coded credentials for a real or shared database.

For a fresh database, run the database examples in this order:

1. `data.py` creates the `python9` database.
2. `createtable.py` creates the `employee` table.
3. `insertrecord.py` inserts example records.
4. Run the select, update, or delete examples as needed.

Run scripts from this folder so their relative filenames (such as `data.txt`, `employee.csv`, and `first.pdf`) resolve correctly:

```bash
python demo.py
python readcsv.py
```

Each script runs its example directly when launched. Several scripts request keyboard input or modify files/database records. In particular, `writetext.py` replaces `data.txt`, `writecsv.py` appends CSV records, and the MySQL update/delete scripts change database data. Review the active statements before running them.

## Sample Text and Data Files

| File | Contents or role |
| --- | --- |
| `abc.txt` | Empty text file. |
| `abc1.txt` | Sample text used by `createtext.py`. |
| `data.txt` | Text-file handling example data; several scripts read, replace, or append to it. |

## Notes

- `26.2.1`, `9.0.0`, and `python` are zero-byte files with no extension. They are listed here for completeness, but their purpose is not evident from their current contents.
- The scripts are independent examples and do not share a command-line interface or automated test suite.
- File operations use paths relative to the current working directory. Start the scripts from this repository folder, or adjust the paths if running them elsewhere.