# RFM Customer Segmentation Analysis

This repository contains a Python script that performs RFM (Recency, Frequency, Monetary) analysis on customer data extracted from a sales database. The script calculates RFM scores, segments customers, and visualizes the distribution of customer segments.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Overview

RFM analysis is a marketing technique used to quantitatively rank and group customers based on their purchasing behavior. The script calculates RFM scores for each customer by evaluating:
- **Recency (R):** How recently a customer made a purchase.
- **Frequency (F):** How often a customer makes a purchase.
- **Monetary (M):** How much money a customer spends on purchases.

Based on the RFM scores, customers are segmented into groups such as "Champions," "Loyal Customers," "Potential Loyalists," "New Customers," and "Others." These segments can be used to tailor marketing strategies.

## Installation

To run the script, you'll need to have Python installed along with the following libraries:
- `pandas`
- `sqlalchemy`
- `matplotlib`
- `seaborn`

### Steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/realbensmith/RFM_Analysis.git
    ```

2. Navigate to the project directory:
    ```bash
    cd RFM_Analysis
    ```

3. Install the required dependencies:
    ```bash
    pip install pandas sqlalchemy matplotlib seaborn
    ```

4. Set up your database connection by defining the `url_object` in the script.

## Usage

### Running the Script

1. **Configure Database Connection:** 
   - Update the `url_object` variable to reflect your database credentials.

2. **Execute the Script:**
   - Run the Python script using the command:
     ```bash
     python rfm_analysis.py
     ```

### What the Script Does:

1. Connects to the specified sales database.
2. Retrieves customer sales data including `CustomerKey`, `OrderDate`, `SalesOrderNumber`, `OrderQuantity`, and `UnitPrice`.
3. Calculates the total amount spent by each customer.
4. Aggregates the data to calculate:
   - The most recent purchase date.
   - The total number of unique orders.
   - The total monetary value of purchases.
5. Assigns RFM scores based on the calculated metrics.
6. Segments customers based on their RFM scores.
7. Outputs the customer segments along with a visualization of the segment distribution.

## Customization

The script can be customized to fit specific business needs:

- **Adjust the RFM Scoring:**
  - You can modify the logic within the script to change how the RFM scores are assigned, e.g., by adjusting the number of bins in the `qcut` function or changing the segmentation thresholds.

- **Visualization Customization:**
  - The script uses Seaborn for visualization. You can customize the plot by adjusting parameters like color, plot type, labels, and titles.

- **Data Source:**
  - The script is configured to work with a sales database. You can modify the SQL query to retrieve data from a different table or source as required.

## Output

### DataFrame Output

The script outputs a DataFrame containing the following columns:
- `CustomerKey`: The unique identifier for each customer.
- `RFM_Score`: The combined score from the RFM analysis.
- `Customer_Segment`: The segment assigned to each customer based on their RFM score.

### Visualization

The script also produces a bar chart that shows the count of customers in each segment. This visualization helps to quickly identify the distribution of customers across different segments.

![Customer Segments Count](https://yourimageurl.com/customer_segments.png)

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

