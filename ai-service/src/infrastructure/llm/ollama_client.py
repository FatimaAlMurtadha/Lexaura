import requests

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