# Sales-Team-Performance-Analysis-Using-LLM

# Overview
This project provides a backend system that analyzes sales data using a Large Language Model (LLM) to generate performance feedback for both individual sales representatives and the entire sales team. The system is built using Flask for API development, Pandas for data handling, and Hugging Face's Transformers for LLM integration.

# Features
- Individual Sales Performance: Analyze the performance of individual sales representatives.
- Team Performance Summary: Get insights into the overall performance of the sales team.
- Trends & Forecasting: Analyze historical data to identify trends and make performance forecasts.

Project Architecture
/sales_analysis_llm
    /api
        - __init__.py         # Initializes the API
        - endpoints.py        # Defines API routes (individual, team, trends)
    /services
        - __init__.py         # Initializes services
        - llm_analysis.py     # Handles LLM-based feedback generation
        - data_processing.py  # Handles data loading and processing from CSV
    /tests
        - test_endpoints.py   # Placeholder for testing the API endpoints
    app.py                    # Main application entry point (Flask app)
    sales_performance_data.csv # CSV file with sales data (not uploaded to GitHub)

# Technologies Used
Flask: Web framework for building the API.
Pandas: For data manipulation and processing.
Hugging Face Transformers: Used to integrate a pre-trained language model (GPT-Neo) for generating feedback.
PyTorch: Backend for the LLM model (needed by Hugging Face Transformers).

# Setup and Run Instructions
1. The "api" folder contains the endpoints.py file, the "services" folder contains llm_analysis.py & data_processing.py.

2. Clone the Repository
First, clone the repository to your local machine:
git clone 'https://github.com/saadayazzzz/Sales-Team-Performance-Analysis-Using-LLM.git'
cd sales_analysis_llm

3. Set Up Virtual Environment
Create a virtual environment and activate it:
python -m venv venv
.\venv\Scripts\activate

4. Place the CSV File
Make sure that the sales_performance_data.csv file (with columns like employee_id, lead_taken, revenue_confirmed, etc.) is placed in the root directory of the project.

5. Run the project
You should see the following output indicating that the server is running locally:
 * Running on http://127.0.0.1:5000/ 

# All URLS Used:
 * Running on http://127.0.0.1:500
 * http://127.0.0.1:5000/api/rep_performance?employee_id=123
 * http://127.0.0.1:5000/api/team_performance
 * http://127.0.0.1:5000/api/performance_trends

# How Feedback Generation Works

The feedback generation is powered by the GPT-Neo model from Hugging Face’s Transformers library. Here’s the process:
- The relevant sales performance data (individual or team) is extracted from the CSV file.
- This data is passed to the generate_feedback function, which uses the GPT-Neo model to generate a feedback summary based on the data.
- The feedback is returned as part of the API response, providing insights and actionable suggestions based on the performance data.



