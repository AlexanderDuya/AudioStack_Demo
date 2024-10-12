import requests
import json
import audiostack

# Set your Audiostack API key
audiostack.api_key = "XXX-XXX-XXX-XXX"  # Use your actual API key here

# Function to generate a script resource using Audiostack API
def generate_script(product_description):
    url = "https://v2.api.audio/content/script"
    payload = {
        "projectName": "untitled",  # Set your project name as needed
        "moduleName": "untitled",    # Set your module name as needed
        "scriptName": "untitled",    # Set your script name as needed
        "scriptText": f'<as:section name="intro" soundsegment="intro">{product_description}</as:section>'
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": audiostack.api_key  # Use the Audiostack API key
    }
    
    print("Generating script with payload:", payload)  # Debugging statement
    
    response = requests.post(url, json=payload, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        script_response = response.json()
        script_id = script_response['data'].get('scriptId')  # Access scriptId safely
        if script_id:
            print("Script created successfully.")
            return script_id  # Return the script ID for further processing
        else:
            print("Script ID not found in response.")
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
    
    print("Generating advert with data:", data)  # Debugging statement
    
    response = requests.post(audiostack_url, headers=headers, json=data)

    # Check if the response is successful
    if response.status_code in [200, 201]:  # Accept both 200 and 201 as success
        print("Advert generated successfully.")
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
        "evidenceProvided": True  # Set to True if the advert contains claims needing evidence
    }
    
    print("Evaluating advert with text:", advert_text)  # Debugging statement

    response = requests.post(adclear_url, headers=headers, json=data)

    # Debugging: Check response status and content
    if response.status_code != 200:
        print(f"Error evaluating advert (Adclear API): {response.status_code}, {response.text}")
        return {"error": f"Error from Adclear: {response.text}"}

    print("Advert evaluated successfully.")
    return response.json()

# Function to format and display the output
def display_output(advert_data, evaluation_data):
    # Extract advert details
    ad_name = advert_data.get('data', {}).get('adName', 'N/A')
    ad_text = advert_data.get('data', {}).get('adText', 'N/A')
    ad_tags = advert_data.get('data', {}).get('tags', [])
    
    # Extract evaluation result
    evaluation_result = evaluation_data.get('result', 'No evaluation result available.')
    
    # Format and display the output
    print("\n" + "-" * 80)
    print(f"### Generated Advert\n")
    print(f"**Title**: *{ad_name}*\n")
    print(f"> {ad_text}\n")
    print(f"**Tags**: {', '.join(ad_tags)}")
    print("-" * 80)
    print(f"### Adclear Evaluation\n")
    print(f"{evaluation_result}")
    print("-" * 80)

# Main function to chain everything together
def run_demo(api_key_adclear, product_description):
    # Step 1: Generate the script
    script_id = generate_script(product_description)
    if not script_id:
        print("Failed to generate script. Check Audiostack API key and request format.")
        return

    # Step 2: Generate the advert using the script
    product_name = "Sample Product"  # Replace with actual product name
    mood = "Exciting"  # Replace with actual mood
    tone = "Friendly"  # Replace with actual tone

    advert_response = generate_advert(script_id, product_name, product_description, mood, tone)
    
    # Check if the advert was generated successfully
    if 'error' in advert_response or advert_response.get('message') != 'advert created':
        print("Failed to generate advert. Check Audiostack API response.")
        return

    advert_text = advert_response.get("data", {}).get("adText")  # Accessing adText safely
    if not advert_text:
        print("Failed to retrieve advert text. Check Audiostack API response.")
        return

    # Step 3: Run the advert through Adclear's evaluation
    evaluation_response = evaluate_advert(api_key_adclear, advert_text)

    # Output the advert and evaluation
    if "error" in evaluation_response:
        print("Evaluation failed. Check Adclear API key and request format.")
        print({
            "Generated Advert": advert_text,
            "Adclear Evaluation": evaluation_response
        })
        return

    # Step 4: Display the formatted output
    display_output(advert_response, evaluation_response)

# Replace this with your actual Adclear API key
api_key_adclear = "XXX-XXX-XXX-XXX"  # Update with the correct API key

# Input section for the product description
product_description = input("Please provide a product description: ")

# Run the demo
run_demo(api_key_adclear, product_description)
