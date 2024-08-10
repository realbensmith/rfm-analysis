# RFM Entity Segmentation Analysis

This repository contains a Python script that performs RFM (Recency, Frequency, Monetary) analysis on any dataset with an identifiable entity. The script calculates RFM scores, segments the entities, and visualizes the distribution of these segments.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Overview

RFM analysis is a versatile technique used to quantitatively rank and group entities based on their behavior. Although traditionally applied to customers, this script can be adapted to analyze any entity with data on:
- **Recency (R):** How recently an event or transaction occurred.
- **Frequency (F):** How often the event or transaction occurs.
- **Monetary (M):** The monetary value associated with the event or transaction.

By evaluating these metrics, entities are segmented into groups such as "High Value," "Moderate Engagement," "New Entrants," and others. This segmentation can help inform strategies, whether you're analyzing customers, suppliers, employees, or any other type of entity.

## Installation

To run the script, you'll need to have Python installed along with the following libraries:
- `pandas`
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
    pip install pandas matplotlib seaborn
    ```

## Usage

### Preparing Your Dataset

1. **Identify Your Entity:** 
   - Ensure your dataset includes a unique identifier for each entity you want to analyze (e.g., `EntityID`, `CustomerID`, `SupplierID`).

2. **Key Columns Required:**
   - **Entity Identifier:** A unique key for each entity (e.g., `CustomerID`).
   - **Transaction/Interaction Date:** The date of each transaction or interaction.
   - **Transaction/Interaction Value:** The monetary value associated with each transaction or interaction.
   - **Transaction/Interaction Count (Optional):** If you wish to count unique transactions.

### Running the Script

1. **Load Your Data:**
   - Modify the script to load your dataset, ensuring it includes the key columns mentioned above.

2. **Execute the Script:**
   - Run the Python script using the command:
     ```bash
     python rfm_analysis.py
     ```

### What the Script Does:

1. Loads the dataset and processes it to calculate:
   - The total value of transactions or interactions for each entity.
   - The most recent date of a transaction or interaction.
   - The total number of unique transactions or interactions.
2. Assigns RFM scores based on the calculated metrics.
3. Segments entities based on their RFM scores.
4. Outputs the entity segments along with a visualization of the segment distribution.

## Customization

The script can be customized to fit specific use cases:

- **Adjust the RFM Scoring:**
  - Modify the logic within the script to change how the RFM scores are assigned, e.g., by adjusting the number of bins in the `qcut` function or changing the segmentation thresholds.

- **Entity Types:**
  - Although the script is demonstrated with a customer dataset, it can be applied to any entity type with relevant data. Adjust the columns and logic as necessary for your specific use case.

- **Visualization Customization:**
  - The script uses Seaborn for visualization. You can customize the plot by adjusting parameters like color, plot type, labels, and titles.

## Output

### DataFrame Output

The script outputs a DataFrame containing the following columns:
- `EntityID`: The unique identifier for each entity.
- `RFM_Score`: The combined score from the RFM analysis.
- `Entity_Segment`: The segment assigned to each entity based on their RFM score.

### Visualization

The script also produces a bar chart that shows the count of entities in each segment. This visualization helps to quickly identify the distribution of entities across different segments.

![Entity Segments Count](https://yourimageurl.com/entity_segments.png)

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
