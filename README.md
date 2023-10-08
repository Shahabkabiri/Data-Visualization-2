# Log File Analysis and Visualization

This Python script is designed to process log files related to a machine learning or deep learning project. It extracts data from these log files, combines them into a single Excel file, and creates visualizations of loss values across epochs.

## Prerequisites

- Python
- pandas
- matplotlib
- keras (for loading model history)

## Usage

1. Clone this repository.
2. Modify the following variables at the beginning of the script to specify your file paths:
   - `folder_path`: Path to the folder containing log files.
   - `output_file`: Name of the Excel file to save the combined data.
   - `combined_image_path`: Path to save the combined chart image.
   - `text_file_path`: Path to the text file containing additional data.
3. Run the script.

## Description

This script does the following:
- Iterates through log files in the specified folder.
- Extracts loss and validation loss data from the log files.
- Reads additional data from a text file.
- Combines all the data into a single Excel file (`output_file`) with different sheets.
- Creates a set of loss vs. epoch charts for each sheet.
- Annotates the charts with additional data from the text file.

## Example Folder Structure

For the script to work, you should organize your log files and text file as follows:

Project Root/
│
├── LSTMLogFiles/
│ ├── 1-history
│ ├── 2-history
│ ├── ...
│ ├── Results.txt
│ └── combined_charts.png
│
├── YourScript.py
├── README.md
│
└── ...



## License

This project is licensed under the [MIT License](LICENSE).
