# src/prompt_template.py

def create_prompt(context, current_call):
    instructions = """
    You are an AI assistant trained to categorize 911 calls into specific functions.
    Based on the following context and the new call, decide which function to invoke.
    """
    prompt = f"{instructions}\n\nContext:\n{context}\n\nNew Call:\n{current_call}\n\nFunction to invoke:"
    return prompt
