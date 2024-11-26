# SQL File Processor

The **SQL File Processor** is a Python application designed to clean and format SQL files. It provides functionality to:

1. Trim trailing spaces from the end of each line.
2. Normalize empty lines by:
   - Removing excess empty lines at the beginning of the file.
   - Ensuring no more than one consecutive empty line within the file.
   - Reducing multiple empty lines at the end of the file to a maximum of one.

Processed files are saved in a `Results` folder, preserving the original file.

---

## Features

- **Trim Trailing Spaces**: Removes unwanted spaces at the end of SQL lines.
- **Normalize Empty Lines**:
  - Removes redundant empty lines at the start of the file.
  - Keeps a single empty line where multiple consecutive empty lines exist.
  - Ensures the file ends with at most one empty line.
- **Safe Processing**: The original file remains unaltered; results are saved in a separate folder.

---

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.7 or higher installed.
3. **Create and activate a virtual environment** (optional but recommended):

   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
    On macOS/Linux
    ```bash
    python3 -m venv venv
   source venv/bin/activate
   ```

---

## Usage

1. Place the SQL file you want to process in the same directory as the script (or provide its full path when prompted).
2. Run the script:

   ```bash
   python main.py
   ```
