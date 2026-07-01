import requests

# I can control the LLMs configurations here: Max Tokens, Top-K , Top-P and Temperature
# Such as:
# payload = {
# "model": "llama3b",
# "prompt": prompt,
# "stream": False,
# "options": {
#     "temperature": 0.2,
#     "top_k": 40,
#     "top_p": 0.9,
#     "num_predict": 512
#  }
#}

# This function sends a prompt to the Ollama API and returns the generated answer.
def generate_answer(prompt: str) -> str:
    url = "http://localhost:11434/api/generate" # Ollama API endpoint
    payload = {
        "model": "llama3-13b", # as an example
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload) # Send request to Ollama
    response.raise_for_status() # Check for HTTP errors
    data = response.json() # Parse JSON response
    return data.get("response", "").strip() # Extract and return the generated answer