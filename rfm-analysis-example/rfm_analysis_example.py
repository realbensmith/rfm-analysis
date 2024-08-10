import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load your data from the Excel file 'AdventureWorksDW2022Sales.xlsx'
df = pd.read_excel('./RFM Analysis/AdventureWorksDW2022Sales.xlsx')

# Example columns in `df`:
# 'CustomerKey': A unique identifier for each customer (or entity)
# 'OrderDate': The date of each transaction or interaction
# 'OrderQuantity': The quantity of each transaction
# 'UnitPrice': The monetary value associated with each transaction
# 'SalesOrderNumber': A unique identifier for each order (used to calculate Frequency)

# Calculate the total amount spent by each customer
df["TotalAmount"] = df["UnitPrice"] * df["OrderQuantity"]

# Group by the unique customer identifier and calculate RFM metrics
group_df = df.groupby(["CustomerKey"], as_index=False).agg({
    "TotalAmount": "sum",  # Monetary Value (M)
    "OrderDate": "max",    # Recency (R)
    "SalesOrderNumber": lambda x: x.nunique()  # Frequency (F)
})

# Rename columns for clarity
group_df.rename(columns={"SalesOrderNumber": "TotalOrders"}, inplace=True)

# Convert TotalAmount to numeric in case of any non-numeric entries
group_df["TotalAmount"] = pd.to_numeric(group_df["TotalAmount"], errors="coerce")

# Calculate the number of unique orders if needed
unique_orders = group_df["TotalOrders"].nunique()
num_bins = 5
if unique_orders < 5:
    num_bins = unique_orders

# Calculate days since the last order (Recency)
group_df["DaysSinceLastOrder"] = (datetime.today() - group_df["OrderDate"]).dt.days

# Assign R, F, M scores based on quantiles
group_df["R_Score"] = pd.qcut(group_df["DaysSinceLastOrder"], 5, labels=range(5, 0, -1))
group_df["F_Score"] = pd.qcut(group_df["TotalOrders"].rank(method="first"), num_bins, labels=range(1, num_bins + 1))
group_df["M_Score"] = pd.qcut(group_df["TotalAmount"], 5, labels=range(1, 6))

# Create RFM segment and score
group_df["RFM_Segment"] = group_df["R_Score"].astype(str) + group_df["F_Score"].astype(str) + group_df["M_Score"].astype(str)
group_df['RFM_Score'] = group_df[['R_Score', 'F_Score', 'M_Score']].sum(axis=1)

# Function to categorize customers based on their RFM score
def segment_customers(df: pd.DataFrame) -> str:
    """
    Segments customers based on their RFM Score.

    Parameters:
    df (pd.DataFrame): A DataFrame row containing RFM_Score.

    Returns:
    str: The segment category for the customer.
    """
    if df["RFM_Score"] >= 9:
        return "Champions"
    elif df["RFM_Score"] >= 8:
        return "Loyal Customers"
    elif df["RFM_Score"] >= 7:
        return "Potential Loyalists"
    elif df["RFM_Score"] >= 6:
        return "New Customers"
    else:
        return "Others"

# Apply segmentation to each customer
group_df["Customer_Segment"] = group_df.apply(segment_customers, axis=1)

# Final DataFrame with CustomerKey, RFM Score, and Customer Segment
final_df = group_df.loc[:, ["CustomerKey", "RFM_Score", "Customer_Segment"]]

# Print output of the data (optional)
# Uncomment the line below if you want to see the final DataFrame
# print(final_df)

# Visualize the distribution of customer segments
plt.figure(figsize=(12, 8))
sns.countplot(data=final_df, x="Customer_Segment", order=final_df["Customer_Segment"].value_counts().index, color="#252734")
plt.title("Customer Segments Count")
plt.xlabel("Customer Segment")
plt.ylabel("Count")
plt.show()
