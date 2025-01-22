import os
import csv
import zipfile
import py7zr


def list_files_in_directory(directory):
    file_list = []

    print(f'Scanning directory: {directory}')

    # Walk through the directory
    for root, _, files in os.walk(directory):
        print(f"Processing directory: {root}")
        for file in files:
            print(f"Processing file: {file}")
            # Check if the file is a .zip or .7z file
            if file.endswith('.zip'):
                file_path = os.path.join(root, file)
                # Open and list files in the zip archive
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    for zf in zip_ref.namelist():
                        file_list.append((root, file, zf))
            elif file.endswith('.7z'):
                file_path = os.path.join(root, file)
                # Open and list files in the 7z archive
                with py7zr.SevenZipFile(file_path, 'r') as z7_ref:
                    for zf in z7_ref.getnames():
                        file_list.append((root, file, zf))
            else:
                # For regular files, just add to the list
                file_list.append((root, '', file))

    return file_list


def write_to_csv(file_list, output_csv):
    # Write the list of files to a CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        for entry in file_list:
            csv_writer.writerow(entry)


if __name__ == "__main__":
    directory_to_scan = 'C:\\workspace\\tmp\\d0'  # Replace with your directory path
    output_csv_file = 'output.csv'  # Specify the output CSV file

    # Get the list of files
    files = list_files_in_directory(directory_to_scan)
    # Write to CSV
    write_to_csv(files, output_csv_file)

    print(f"File list has been written to {output_csv_file}")
