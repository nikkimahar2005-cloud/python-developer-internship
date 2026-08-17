import os
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


# File paths
DATA_FILE = os.path.join("data", "sales_data.csv")
REPORT_FOLDER = "reports"
REPORT_FILE = os.path.join(REPORT_FOLDER, "sales_report.pdf")


def read_sales_data():
    """Read sales data from the CSV file."""
    return pd.read_csv(DATA_FILE)


def analyze_sales_data(df):
    """Calculate important sales statistics."""

    # Calculate total sales for each row
    df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

    total_revenue = df["Total_Sales"].sum()
    total_quantity = df["Quantity"].sum()
    average_sale = df["Total_Sales"].mean()

    best_product = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    best_region = (
        df.groupby("Region")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    return (
        total_revenue,
        total_quantity,
        average_sale,
        best_product,
        best_region,
    )


def create_pdf(df, statistics):
    """Generate a formatted PDF report."""

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    (
        total_revenue,
        total_quantity,
        average_sale,
        best_product,
        best_region,
    ) = statistics

    document = SimpleDocTemplate(
        REPORT_FILE,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=20,
        spaceAfter=20,
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10,
    )

    normal_style = ParagraphStyle(
        "NormalStyle",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
    )

    story = []

    # Title
    story.append(
        Paragraph("Sales Analysis Report", title_style)
    )

    story.append(
        Paragraph(
            "Automated report generated using Python, Pandas and ReportLab.",
            normal_style,
        )
    )

    story.append(Spacer(1, 15))

    # Summary section
    story.append(
        Paragraph("1. Sales Summary", heading_style)
    )

    summary_data = [
        ["Metric", "Value"],
        ["Total Revenue", f"₹{total_revenue:,.2f}"],
        ["Total Quantity Sold", f"{total_quantity:,}"],
        ["Average Sale", f"₹{average_sale:,.2f}"],
        ["Best-Selling Product", best_product],
        ["Best Region", best_region],
    ]

    summary_table = Table(
        summary_data,
        colWidths=[220, 220],
    )

    summary_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("PADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story.append(summary_table)
    story.append(Spacer(1, 20))

    # Product analysis
    story.append(
        Paragraph("2. Product-wise Sales", heading_style)
    )

    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    product_data = [["Product", "Total Sales"]]

    for product, sales in product_sales.items():
        product_data.append(
            [product, f"₹{sales:,.2f}"]
        )

    product_table = Table(
        product_data,
        colWidths=[220, 220],
    )

    product_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("PADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story.append(product_table)
    story.append(Spacer(1, 20))

    # Region analysis
    story.append(
        Paragraph("3. Region-wise Sales", heading_style)
    )

    region_sales = (
        df.groupby("Region")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    region_data = [["Region", "Total Sales"]]

    for region, sales in region_sales.items():
        region_data.append(
            [region, f"₹{sales:,.2f}"]
        )

    region_table = Table(
        region_data,
        colWidths=[220, 220],
    )

    region_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("PADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story.append(region_table)
    story.append(Spacer(1, 20))

    # Detailed sales data
    story.append(
        Paragraph("4. Detailed Sales Data", heading_style)
    )

    detail_data = [
        [
            "Date",
            "Product",
            "Region",
            "Qty",
            "Unit Price",
            "Total",
        ]
    ]

    for _, row in df.iterrows():
        detail_data.append(
            [
                str(row["Date"]),
                str(row["Product"]),
                str(row["Region"]),
                str(row["Quantity"]),
                f"₹{row['Unit_Price']:,.0f}",
                f"₹{row['Total_Sales']:,.0f}",
            ]
        )

    detail_table = Table(
        detail_data,
        repeatRows=1,
        colWidths=[65, 75, 55, 35, 70, 70],
    )

    detail_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("PADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )

    story.append(detail_table)
    story.append(Spacer(1, 20))

    # Conclusion
    story.append(
        Paragraph("5. Conclusion", heading_style)
    )

    conclusion = (
        f"The total revenue generated was ₹{total_revenue:,.2f}. "
        f"A total of {total_quantity:,} units were sold. "
        f"The best-selling product based on revenue was {best_product}, "
        f"while {best_region} was the highest-performing region."
    )

    story.append(
        Paragraph(conclusion, normal_style)
    )

    # Build PDF
    document.build(story)


def main():
    """Main function."""

    print("Reading sales data...")

    df = read_sales_data()

    print("Analyzing sales data...")

    statistics = analyze_sales_data(df)

    print("Generating PDF report...")

    create_pdf(df, statistics)

    print("Report generated successfully!")
    print(f"PDF location: {REPORT_FILE}")


if __name__ == "__main__":
    main()