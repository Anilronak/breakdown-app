import csv
from datetime import datetime
import os

FILE_NAME = "breakdown_log.csv"

# Create file with headers if it does not exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Date",
            "Machine Name",
            "Problem",
            "Action Taken",
            "Attended By (Engineer Name)"
        ])

def add_breakdown_entry():
    date = input("Enter Date (YYYY-MM-DD) or press Enter for today: ")
    if date.strip() == "":
        date = datetime.today().strftime("%Y-%m-%d")

    machine_name = input("Enter Machine Name: ")
    problem = input("Enter Problem Description: ")
    action_taken = input("Enter Action Taken: ")
    engineer_name = input("Enter Engineer Name: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            date,
            machine_name,
            problem,
            action_taken,
            engineer_name
        ])

    print("\n✅ Breakdown entry saved successfully!\n")

while True:
    print("=== Breakdown Filling Application ===")
    print("1. Add New Breakdown Entry")
    print("2. Exit")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        add_breakdown_entry()
    elif choice == "2":
        print("👋 Exiting application.")
        break
    else:
        print("❌ Invalid choice. Please try again.\n")
