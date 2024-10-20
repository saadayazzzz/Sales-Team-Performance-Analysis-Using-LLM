from flask import Blueprint, request, jsonify
from services.data_processing import load_sales_data, get_rep_performance
from services.llm_analysis import generate_feedback

api_blueprint = Blueprint("api", __name__)

# Load the sales data from CSV (ensure the path is correct)
data = load_sales_data("sales_performance_data.csv")


# Endpoint for individual rep performance
@api_blueprint.route("/rep_performance", methods=["GET"])
def rep_performance():
    employee_id = request.args.get('employee_id')  # Changed from 'rep_id' to 'employee_id'
    if not employee_id:
        return jsonify({"error": "Missing employee_id parameter"}), 400

    # Get sales data for the specific representative
    performance_data = get_rep_performance(data, employee_id)
    if 'error' in performance_data:
        return jsonify({"error": performance_data['error']}), 404

    # Generate feedback using LLM
    feedback = generate_feedback(performance_data)

    return jsonify({"performance": performance_data, "feedback": feedback})


# Endpoint for team performance
@api_blueprint.route("/team_performance", methods=["GET"])
def team_performance():
    team_performance_data = data.describe().to_dict()  # Simple team summary
    feedback = generate_feedback(team_performance_data)
    return jsonify({"team_performance": team_performance_data, "feedback": feedback})


# Endpoint for trends and forecasting (simplified)
@api_blueprint.route("/performance_trends", methods=["GET"])
def performance_trends():
    # You can further improve by adding time_period filters
    trends_data = data.tail(10).to_dict()  # Simplified to last 10 records
    feedback = generate_feedback(trends_data)
    return jsonify({"trends": trends_data, "feedback": feedback})
