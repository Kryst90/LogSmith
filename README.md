# LogSmith
A Python script that copies machine log files from a specified source location to a destination folder, then parses the logs and generates a structured CSV file with extracted data.

## How It Works
This script:
1. Asks the user for the folder path containing PDF files.
2. Uses the folder name as a date reference for the report.
3. Reads all `.pdf` files in the folder and splits their filenames into parts based on `_`.
4. Saves the extracted data into a CSV file with a clear header and date-based name.

## Example
Suppose the folder contains these files:
123_Product1_OK_456_SOCKET1_2023-09-29_14-35.pdf
124_Product2_FAIL_789_SOCKET2_2023-09-29_15-20.pdf

The script will generate:

With contents like:
| Product | Machine | Status | ID  | SOCKET  | Date       | Time   |
|--------|---------|--------|-----|--------|-----------|--------|
| 123    | Product1| OK     | 456 | SOCKET1| 2023-09-29| 14-35 |
| 124    | Product2| FAIL   | 789 | SOCKET2| 2023-09-29| 15-20 |

## Requirements
- Python 3.8+
- No additional external libraries required (uses built-in `os`, `csv`, and `re`)

## Usage
Run the script in your terminal:

python "Flashing records.py"

When prompted, enter the full path to the folder containing the PDF files.
A CSV report will be created in the same folder.

## Output

CSV file is saved in the same folder as the input PDFs

File is named: Flashing raport from <FOLDER_NAME>.csv

## License

MIT License – free to use, modify.
