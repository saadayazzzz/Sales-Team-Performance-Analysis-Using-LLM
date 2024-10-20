import pandas as pd

def load_sales_data(file_path):
   
    return pd.read_csv(file_path)

def get_rep_performance(data, employee_id):
    
    
    if 'employee_id' not in data.columns:
        return {"error": "'employee_id' column not found in the data"}

    try:
        employee_id = int(employee_id)
    except ValueError:
        return {"error": "Invalid employee_id format. It should be an integer."}


    rep_data = data[data['employee_id'] == employee_id]

    if rep_data.empty:
        return {"error": "Sales representative not found."}

    return rep_data.describe().to_dict() 
