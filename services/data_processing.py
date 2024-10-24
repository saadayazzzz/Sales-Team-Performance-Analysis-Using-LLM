import pandas as pd

def load_sales_data(file_path):
    """Load the sales data from CSV file."""
    return pd.read_csv(file_path)

def generate_feedback(stats):
    """
    Generate feedback based on performance statistics.
    """
    feedback = ""

    if 'lead_taken' in stats:
        lead_taken_mean = stats['lead_taken']['mean']
        if lead_taken_mean > 15:
            feedback += "The employee has taken a significant number of leads, indicating proactive effort.\n"
        elif 10 <= lead_taken_mean <= 15:
            feedback += "The employee's lead-taking is average, there is room for improvement.\n"
        else:
            feedback += "The employee's lead-taking is below expectations, encourage more activity.\n"

    if 'applications' in stats:
        applications_mean = stats['applications']['mean']
        if applications_mean > 5:
            feedback += "Excellent application submission rate. Keep up the high performance.\n"
        elif 3 <= applications_mean <= 5:
            feedback += "The employee's application rate is decent but can improve.\n"
        else:
            feedback += "Application submissions are lower than expected. Focus on improving this area.\n"

    if 'tours_booked' in stats:
        tours_booked_mean = stats['tours_booked']['mean']
        if tours_booked_mean > 10:
            feedback += "Great job on booking tours, you're exceeding expectations.\n"
        elif 5 <= tours_booked_mean <= 10:
            feedback += "Tours booked are satisfactory, but there's room for optimization.\n"
        else:
            feedback += "Tours booked are below expectations. Consider improving your follow-up strategies.\n"

    return feedback

def get_rep_performance(data, employee_id):
    """Get performance of an individual sales rep by employee_id."""

    if 'employee_id' not in data.columns:
        return {"error": "'employee_id' column not found in the data"}

    try:
        employee_id = int(employee_id)
    except ValueError:
        return {"error": "Invalid employee_id format. It should be an integer."}


    rep_data = data[data['employee_id'] == employee_id]

    if rep_data.empty:
        return {"error": "Sales representative not found."}

    stats = rep_data.describe().to_dict()

 
    feedback = generate_feedback(stats)

    
    return {"performance": stats, "feedback": feedback}

