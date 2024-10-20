from transformers import pipeline, Pipeline
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


try:
    llm: Pipeline = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
    logger.info("LLM model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading LLM model: {e}")
    llm = None


def generate_feedback(performance_data):
   
    if not llm:
        return "LLM model is not available."

    text_input = f"Analyze the following sales data and provide feedback: {str(performance_data)[:500]}"

    try:
        generated_responses = llm(text_input, max_new_tokens=500)
        logger.info("LLM feedback generated successfully.")
    except Exception as e:
        logger.error(f"Error during text generation: {e}")
        return f"An error occurred during text generation: {str(e)}"

    if not generated_responses or 'generated_text' not in generated_responses[0]:
        return "No feedback could be generated."

    feedback = generated_responses[0]['generated_text']

    return feedback
