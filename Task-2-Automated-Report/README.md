# Task 2 - Automated PDF Report Generation

## Project Title

Sales Data Analysis and Automated PDF Report

## Objective

The objective of this project is to read sales data from a CSV file, analyze the data using Python and Pandas, and generate a formatted PDF report using ReportLab.

## Technologies Used

- Python
- Pandas
- ReportLab

## Project Features

- Reads sales data from a CSV file
- Processes sales data using Pandas
- Calculates total revenue
- Calculates total quantity sold
- Calculates average sale
- Identifies the best-selling product
- Identifies the best-performing region
- Performs product-wise sales analysis
- Performs region-wise sales analysis
- Generates a formatted PDF report
- Includes detailed sales data in the report

## Project Structure

```text
Task-2-Automated-Report/
│
├── report_generator.py
├── requirements.txt
├── README.md
│
├── data/
│   └── sales_data.csv
│
└── reports/
    └── sales_report.pdf
```

## How to Run

### Step 1 - Install Required Libraries

Open the terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### Step 2 - Run the Program

```bash
python report_generator.py
```

## Input

The program reads sales data from:

```text
data/sales_data.csv
```

The CSV file contains information such as:

- Date
- Product
- Category
- Region
- Quantity
- Unit Price

## Output

After successful execution, the program generates:

```text
reports/sales_report.pdf
```

The PDF report contains:

- Sales summary
- Total revenue
- Total quantity sold
- Average sale
- Best-selling product
- Best-performing region
- Product-wise sales
- Region-wise sales
- Detailed sales records
- Conclusion

## Working Process

```text
Sales CSV File
      ↓
Read Data using Pandas
      ↓
Analyze Sales Data
      ↓
Calculate Statistics
      ↓
Generate PDF using ReportLab
      ↓
Save sales_report.pdf
```

## Conclusion

This project demonstrates how Python can be used to read and analyze data from a CSV file and automatically generate a professional PDF report. Pandas is used for data analysis and ReportLab is used for PDF generation.

## Internship Task

Task 2 - Automated PDF Report Generation