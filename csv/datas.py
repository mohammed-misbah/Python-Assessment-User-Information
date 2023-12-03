import csv

data = [
    {"Name": "Alice", "Age": 25},
    {"Name": "Bob", "Age": 30},
    {"Name": "Charlie", "Age": 22},
    {"Name": "David", "Age": 28},
    {"Name": "Eve", "Age": 35},
]

file_name = "people_data.csv"

# Write data to CSV file
with open(file_name, mode='w', newline='') as csv_file:
    fieldnames = ["Name", "Age"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    writer.writerows(data)

print(f"CSV file '{file_name}' has been created.")
