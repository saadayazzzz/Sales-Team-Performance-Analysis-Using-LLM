from flask import Blueprint, request, jsonify
from services.data_processing import load_sales_data, get_rep_performance
from services.llm_analysis import generate_feedback

api_blueprint = Blueprint("api", __name__)

data = load_sales_data("sales_performance_data.csv")


@api_blueprint.route("/rep_performance", methods=["GET"])
def rep_performance():
    employee_id = request.args.get('employee_id')  
    if not employee_id:
        return jsonify({"error": "Missing employee_id parameter"}), 400

    performance_data = get_rep_performance(data, employee_id)
    if 'error' in performance_data:
        return jsonify({"error": performance_data['error']}), 404

    feedback = generate_feedback(performance_data)

    return jsonify({"performance": performance_data, "feedback": feedback})


@api_blueprint.route("/team_performance", methods=["GET"])
def team_performance():
    team_performance_data = data.describe().to_dict()  
    feedback = generate_feedback(team_performance_data)
    return jsonify({"team_performance": team_performance_data, "feedback": feedback})

@api_blueprint.route("/performance_trends", methods=["GET"])
def performance_trends():

    trends_data = data.tail(10).to_dict()
    feedback = generate_feedback(trends_data)
    return jsonify({"trends": trends_data, "feedback": feedback})
