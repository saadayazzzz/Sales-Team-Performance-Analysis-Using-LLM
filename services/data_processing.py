import pandas as pd

def load_sales_data(file_path):
    """Load the sales data from CSV file."""
    return pd.read_csv(file_path)

def get_rep_performance(data, employee_id):
    """Get performance of an individual sales rep by employee_id."""
    # Ensure 'employee_id' column exists
    if 'employee_id' not in data.columns:
        return {"error": "'employee_id' column not found in the data"}

    # Attempt to convert employee_id to the appropriate type (assuming integer)
    try:
        employee_id = int(employee_id)
    except ValueError:
        return {"error": "Invalid employee_id format. It should be an integer."}

    # Filter data for the specific sales representative
    rep_data = data[data['employee_id'] == employee_id]

    if rep_data.empty:
        return {"error": "Sales representative not found."}

    return rep_data.describe().to_dict()  # Summarize the representative's performance data
