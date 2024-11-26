import os


class SQLFileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.result_folder = "Results"
        os.makedirs(self.result_folder, exist_ok=True)
        self.result_path = os.path.join(self.result_folder, os.path.basename(file_path))

    def trim_trailing_spaces(self, lines):
        """Removes trailing spaces at the end of each line."""
        return [line.rstrip() + '\n' for line in lines]

    def normalize_empty_lines(self, lines):
        """
        Ensures no more than one consecutive empty line exists at the beginning,
        between lines, or at the end of the file.
        """
        result = []
        empty_line_flag = False  # Tracks whether the last line added was empty

        for line in lines:
            if line.strip() == "":
                if not empty_line_flag:
                    result.append(line)  # Keep a single empty line
                    empty_line_flag = True
            else:
                result.append(line)  # Add non-empty lines
                empty_line_flag = False  # Reset the flag for non-empty lines

        # Ensure the file ends with at most one empty line
        while result and result[-1].strip() == "":
            result.pop()
        result.append("\n")  # Add one empty line at the end if there's content
        return result

    def process_file(self, trim_spaces=False, delete_empty_lines=False):
        """Processes the file based on selected options."""
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        if delete_empty_lines:
            lines = self.normalize_empty_lines(lines)
        if trim_spaces:
            lines = self.trim_trailing_spaces(lines)

        self._save_to_result(lines)
        print(f"Processing completed and saved to {self.result_path}")

    def _save_to_result(self, lines):
        """Helper method to save processed lines to the result file."""
        with open(self.result_path, 'w') as file:
            file.writelines(lines)


def main():
    print("SQL File Processor")
    file_path = input("Enter the path of the SQL file to process: ").strip()
    if not os.path.isfile(file_path):
        print("File not found. Please enter a valid file path.")
        return

    processor = SQLFileProcessor(file_path)

    while True:
        print("\nChoose an option:")
        print("1. Trim trailing spaces at the end of lines")
        print("2. Normalize empty lines (start, middle, and end)")
        print("3. Do both (1 and 2)")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '1':
            processor.process_file(trim_spaces=True)
        elif choice == '2':
            processor.process_file(delete_empty_lines=True)
        elif choice == '3':
            processor.process_file(trim_spaces=True, delete_empty_lines=True)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
