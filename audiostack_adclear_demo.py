import requests
import json
import audiostack

# Set your Audiostack API key
audiostack.api_key = "4bb2eddd-693b-4b24-9107-ee18bbaff5bf"  # Use your actual API key here

# Function to generate a script resource using Audiostack API
def generate_script(product_description):
    url = "https://v2.api.audio/content/script"
    payload = {
        "projectName": "untitled",  # Set your project name as needed
        "moduleName": "untitled",    # Set your module name as needed
        "scriptName": "untitled",    # Set your script name as needed
        "scriptText": f"<as:section name=\"intro\" soundsegment=\"intro\">{product_description}</as:section>"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": audiostack.api_key  # Use the Audiostack API key
    }
    
    response = requests.post(url, json=payload, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        script_response = response.json()
        script_id = script_response['data'].get('scriptId')  # Access scriptId safely
        if script_id:
            print("Script created successfully:", script_response)
            return script_id  # Return the script ID for further processing
        else:
            print("Script ID not found in response:", script_response)
            return None
    else:
        print(f"Error generating script (Audiostack API): {response.status_code}, {response.text}")
        return None

# Function to generate an advert using the script resource
def generate_advert(script_id, product_name, product_description, mood, tone, ad_length=30):
    audiostack_url = "https://v2.api.audio/content/generate/advert"
    headers = {
        "x-api-key": audiostack.api_key,  # Use the Audiostack API key
        "Content-Type": "application/json"
    }
    data = {
        "scriptId": script_id,
        "productName": product_name,
        "productDescription": product_description,
        "mood": mood,
        "tone": tone,
        "thirdPerson": True,  # Assuming this is needed
        "adLength": ad_length  # Set ad length to a valid value (default is 30)
    }
    
    response = requests.post(audiostack_url, headers=headers, json=data)

    # Check if the response is successful
    if response.status_code in [200, 201]:  # Accept both 200 and 201 as success
        return response.json()  # Return the entire JSON response for further processing
    else:
        print(f"Error generating advert (Audiostack API): {response.status_code}, {response.text}")
        return {"error": f"Error from Audiostack: {response.text}"}

# Function to evaluate the generated advert using Adclear API
def evaluate_advert(api_key_adclear, advert_text):
    adclear_url = "https://app.adclear.ai/api/v1/evaluate/text"
    headers = {
        "Authorization": f"Bearer {api_key_adclear}",
        "Content-Type": "application/json"
    }
    data = {
        "text": advert_text,
        "evidenceProvided": False  # Set to True if the advert contains claims needing evidence
    }
    
    response = requests.post(adclear_url, headers=headers, json=data)

    # Debugging: Check response status and content
    if response.status_code != 200:
        print(f"Error evaluating advert (Adclear API): {response.status_code}, {response.text}")
        return {"error": f"Error from Adclear: {response.text}"}

    return response.json()

# Main function to chain everything together
def run_demo(api_key_adclear, product_description):
    # Step 1: Generate the script
    script_id = generate_script(product_description)
    if not script_id:
        print("Failed to generate script. Check Audiostack API key and request format.")
        return "Error generating script."

    # Step 2: Generate the advert using the script
    product_name = "Sample Product"  # Replace with actual product name
    mood = "Exciting"  # Replace with actual mood
    tone = "Friendly"  # Replace with actual tone

    advert_response = generate_advert(script_id, product_name, product_description, mood, tone)
    
    # Debugging: Log advert response
    print("Advert Response:", advert_response)
    
    # Check if the advert was generated successfully
    if 'error' in advert_response or advert_response.get('message') != 'advert created':
        print("Failed to generate advert. Check Audiostack API response.")
        return "Error generating advert."

    advert_text = advert_response.get("data", {}).get("adText")  # Accessing adText safely
    if not advert_text:
        print("Failed to retrieve advert text. Check Audiostack API response.")
        return "Error retrieving advert text."

    # Step 3: Run the advert through Adclear's evaluation
    evaluation_response = evaluate_advert(api_key_adclear, advert_text)

    # Output the advert and evaluation
    if "error" in evaluation_response:
        print("Evaluation failed. Check Adclear API key and request format.")
        return {
            "Generated Advert": advert_text,
            "Adclear Evaluation": evaluation_response
        }

    return {
        "Generated Advert": advert_text,
        "Adclear Evaluation": evaluation_response
    }

# Replace this with your actual Adclear API key
api_key_adclear = "your_adclear_api_key"  # Update with the correct API key

# Input section for the product description
product_description = input("Please provide a product description: ")

# Run the demo
result = run_demo(api_key_adclear, product_description)
print(result)
