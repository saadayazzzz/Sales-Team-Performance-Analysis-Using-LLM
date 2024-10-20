from transformers import pipeline, Pipeline
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load a pre-trained model for text generation (using a smaller model for efficiency)
try:
    llm: Pipeline = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
    logger.info("LLM model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading LLM model: {e}")
    llm = None


def generate_feedback(performance_data):
    """
    Generate feedback using the LLM (GPT-Neo) based on performance data.

    :param performance_data: The sales performance data (dict) to analyze
    :return: A generated text feedback based on the performance data
    """
    if not llm:
        return "LLM model is not available."

    # Prepare the text input for the LLM, limiting the length to prevent exceeding token limits
    text_input = f"Analyze the following sales data and provide feedback: {str(performance_data)[:500]}"

    try:
        # Generate feedback using the LLM, setting max_new_tokens to control the output length
        generated_responses = llm(text_input, max_new_tokens=500)
        logger.info("LLM feedback generated successfully.")
    except Exception as e:
        logger.error(f"Error during text generation: {e}")
        return f"An error occurred during text generation: {str(e)}"

    # Check if the model generated any output
    if not generated_responses or 'generated_text' not in generated_responses[0]:
        return "No feedback could be generated."

    # Return the generated feedback
    feedback = generated_responses[0]['generated_text']

    return feedback
