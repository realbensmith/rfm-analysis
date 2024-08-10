# RFM Analysis Script

This repository contains a Python script that performs RFM (Recency, Frequency, Monetary) analysis on customer data from a sales database.

## Overview

The script connects to a database, retrieves customer sales data, and calculates RFM scores for each customer. It then segments customers into different categories based on their RFM scores and visualizes the distribution of customer segments.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/RFM_Analysis.git
    ```
2. Install the required dependencies:
    ```bash
    pip install pandas sqlalchemy matplotlib seaborn
    ```

## Usage

1. Modify the connection string in the script to point to your database.
2. Run the script:
    ```bash
    python rfm_analysis.py
    ```
3. The script will output a DataFrame containing customer keys, RFM scores, and customer segments, along with a plot showing the distribution of customer segments.

## Customization

You can customize the customer segments or the visualization by modifying the respective sections in the script.
