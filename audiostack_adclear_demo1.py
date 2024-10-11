import requests

# Function to generate a script resource using Audiostack API
def generate_script(api_key_audiostack, product_description):
    audiostack_url = "https://v2.api.audio/content/script"
    headers = {
        "Authorization": f"Bearer {api_key_audiostack}",
        "Content-Type": "application/json"
    }
    data = {
        "productDescription": product_description,
        "voice": "en-US-Neural",
        "style": "casual"
    }
    response = requests.post(audiostack_url, headers=headers, json=data)
    return response.json()

# Function to generate an advert using the script resource
def generate_advert(api_key_audiostack, script_id):
    audiostack_url = f"https://v2.api.audio/content/generate/advert"
    headers = {
        "Authorization": f"Bearer {api_key_audiostack}",
        "Content-Type": "application/json"
    }
    data = {
        "scriptId": script_id
    }
    response = requests.post(audiostack_url, headers=headers, json=data)
    return response.json()

# Function to evaluate the generated advert using Adclear API
def evaluate_advert(api_key_adclear, advert_text):
    adclear_url = "https://app.adclear.ai/api/v1/evaluate/text"
    headers = {
        "Authorization": f"Bearer {api_key_adclear}",
        "Content-Type": "application/json"
    }
    data = {
        "text": advert_text,  # Now passing advert text (not URL)
        "evidenceProvided": False  # Set to True if the advert contains claims needing evidence
    }
    response = requests.post(adclear_url, headers=headers, json=data)
    return response.json()


# Main function to chain everything together
def run_demo(api_key_audiostack, api_key_adclear, product_description):
    # Step 1: Generate the script
    script_response = generate_script(api_key_audiostack, product_description)
    script_id = script_response.get("id")
    if not script_id:
        return "Error generating script."

    # Step 2: Generate the advert using the script
    advert_response = generate_advert(api_key_audiostack, script_id)
    advert_text = advert_response.get("advertText")
    if not advert_text:
        return "Error generating advert."

    # Step 3: Run the advert through Adclear's evaluation
    evaluation_response = evaluate_advert(api_key_adclear, advert_text)

    # Output the advert and evaluation
    return {
        "Generated Advert": advert_text,
        "Adclear Evaluation": evaluation_response
    }

# Replace these with your actual API keys
api_key_audiostack = "4bb2eddd-693b-4b24-9107-ee18bbaff5bf"
api_key_adclear = "your_adclear_api_key"

# Input section for the product description
product_description = input("Please provide a product description: ")

# Run the demo
result = run_demo(api_key_audiostack, api_key_adclear, product_description)
print(result)
