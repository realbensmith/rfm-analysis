import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Sample Data - Replace with your own data
rfm_data = []  # Replace with your actual data
rfm_data_columns = []  # Replace with your actual column names
df = pd.DataFrame(rfm_data, columns=rfm_data_columns)

# Example columns in `df`:
# 'EntityID': A unique identifier for each entity (e.g., CustomerID, ProductID)
# 'OrderDate': The date of each transaction or interaction
# 'OrderQuantity': The quantity of each transaction
# 'UnitPrice': The monetary value associated with each transaction

# Calculate the total amount spent by each entity
df["TotalAmount"] = df["UnitPrice"] * df["OrderQuantity"]

# Group by the unique entity identifier and calculate RFM metrics
group_df = df.groupby(["EntityID"], as_index=False).agg({
    "TotalAmount": "sum",  # Monetary Value (M)
    "OrderDate": "max",    # Recency (R)
    "OrderQuantity": "sum" # Frequency (F)
})

# Convert TotalAmount to numeric in case of any non-numeric entries
group_df["TotalAmount"] = pd.to_numeric(group_df["TotalAmount"], errors="coerce")

# Calculate the number of unique orders if needed
unique_orders = group_df["OrderQuantity"].nunique()
num_bins = 5
if unique_orders < 5:
    num_bins = unique_orders

# Calculate days since the last order (Recency)
group_df["DaysSinceLastOrder"] = (datetime.today() - group_df["OrderDate"]).dt.days

# Assign R, F, M scores based on quantiles
group_df["R_Score"] = pd.qcut(group_df["DaysSinceLastOrder"], 5, labels=range(5, 0, -1))
group_df["F_Score"] = pd.qcut(group_df["OrderQuantity"].rank(method="first"), num_bins, labels=range(1, num_bins + 1))
group_df["M_Score"] = pd.qcut(group_df["TotalAmount"], 5, labels=range(1, 6))

# Create RFM segment and score
group_df["RFM_Segment"] = group_df["R_Score"].astype(str) + group_df["F_Score"].astype(str) + group_df["M_Score"].astype(str)
group_df['RFM_Score'] = group_df[['R_Score', 'F_Score', 'M_Score']].sum(axis=1)

# Function to categorize entities based on their RFM score
def segment_entities(df: pd.DataFrame) -> str:
    """
    Segments entities based on their RFM Score.

    Parameters:
    df (pd.DataFrame): A DataFrame row containing RFM_Score.

    Returns:
    str: The segment category for the entity.
    """
    if df["RFM_Score"] >= 9:
        return "Champions"
    elif df["RFM_Score"] >= 8:
        return "Loyal Entities"
    elif df["RFM_Score"] >= 7:
        return "Potential Loyalists"
    elif df["RFM_Score"] >= 6:
        return "New Entities"
    else:
        return "Others"

# Apply segmentation to each entity
group_df["Entity_Segment"] = group_df.apply(segment_entities, axis=1)

# Final DataFrame with EntityID, RFM Score, and Entity Segment
final_df = group_df.loc[:, ["EntityID", "RFM_Score", "Entity_Segment"]]
print(final_df)

# Visualize the distribution of entity segments
plt.figure(figsize=(12, 8))
sns.countplot(data=final_df, x="Entity_Segment", order=final_df["Entity_Segment"].value_counts().index, color="#252734")
plt.title("Entity Segments Count")
plt.xlabel("Entity Segment")
plt.ylabel("Count")
plt.show()
