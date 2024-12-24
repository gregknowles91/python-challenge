# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Debugging: Print current working directory to check where the script is running
print("Current working directory:", os.getcwd())

# Check if the file exists before attempting to open it
if not os.path.exists(file_to_load):
    print(f"Error: The file '{file_to_load}' does not exist.")
else:
    # Define variables to track the financial data
    total_months = 0
    total_net = 0
    net_change_list = []
    previous_month_profit_loss = 0
    greatest_increase = ["", 0]  # [Month, Amount]
    greatest_decrease = ["", 0]  # [Month, Amount]

    try:
        # Open and read the CSV
        with open(file_to_load) as financial_data:
            reader = csv.reader(financial_data)

            # Skip the header row
            header = next(reader)

            # Process each row of data
            for row in reader:
                try:
                    # Increment the month counter
                    total_months += 1

                    # Track the total net amount
                    total_net += int(row[1])

                    # Calculate the net change in profits/losses
                    current_month_profit_loss = int(row[1])
                    if total_months > 1:  # For net change calculations, skip the first month
                        net_change = current_month_profit_loss - previous_month_profit_loss
                        net_change_list.append(net_change)

                        # Calculate the greatest increase in profits (month and amount)
                        if net_change > greatest_increase[1]:
                            greatest_increase = [row[0], net_change]

                        # Calculate the greatest decrease in losses (month and amount)
                        if net_change < greatest_decrease[1]:
                            greatest_decrease = [row[0], net_change]

                    # Update the previous month's profit/loss for next iteration
                    previous_month_profit_loss = current_month_profit_loss

                except ValueError as e:
                    print(f"Error: Invalid data in row {row}. Skipping this row. Error: {e}")

        # Calculate the average net change across the months
        if net_change_list:
            average_change = sum(net_change_list) / len(net_change_list)
        else:
            average_change = 0

        # Generate the output summary
        output = (
            f"Financial Analysis\n"
            f"----------------------------\n"
            f"Total Months: {total_months}\n"
            f"Total: ${total_net}\n"
            f"Average Change: ${average_change:.2f}\n"
            f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
            f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
        )

        # Print the output to the terminal
        print(output)

        # Write the results to a text file
        with open(file_to_output, "w") as txt_file:
            txt_file.write(output)

        print(f"Analysis saved to {file_to_output}")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please check the file path and try again.")
