# Audiostack and Adclear Advert Generation Demo

This project integrates the **Audiostack** and **Adclear** APIs to generate and evaluate marketing adverts based on a provided product description. 

## Overview

The demo includes the following steps:
1. **Generate a script** using the Audiostack API based on the product description.
2. **Generate an advert** using the script created in step 1.
3. **Evaluate the advert** using the Adclear API to ensure compliance with advertising regulations.
4. **Display the generated advert and evaluation results.**

## Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)

## Configuration

### Setting Up API Keys

1. **Audiostack API Key**: Replace the placeholder API key in the code with your actual Audiostack API key.
   ```python
   audiostack.api_key = "YOUR_AUDIOSTACK_API_KEY"
   api_key_adclear = "YOUR_ADCLEAR_API_KEY"

### ad_length variable can be changed

advert_response = generate_advert(script_id, product_name, product_description, mood, tone, ad_length=YOUR_DESIRED_LENGTH)

### How to Run
python audiostack_adclear_demo.py


Output
The program will display:

The generated advert with its title, text, and tags.
The evaluation results from Adclear, including any compliance issues or suggestions for improvement.

**Example Usage:**

Please provide a product description: Brown Nugget

Title: Brown Nugget: The Culinary Star

In the mysterious world of culinary delights, the Brown Nugget emerges as a singular star. This tantalizing treat promises unparalleled satisfaction with every bite, captivating food enthusiasts everywhere. Its rich flavors and delightful texture create an unforgettable experience that leaves taste buds yearning for more. Discover this extraordinary delicacy and elevate your dining adventures to new heights! Grab yours today.

**Tags**
Culinary Delights
Food Enthusiasts
Gourmet Treats
Dining Adventures

**Adclear Evaluation**
Overall Assessment: This will need review to pass the relevant guidelines.

Suggested Changes:
-The advertiser should provide substantiation for claims about the "unparalleled satisfaction" and "extraordinary delicacy" of the Brown Nugget. These claims could be interpreted as health or nutrition claims, which require evidence under **Rule 15.1**.
-Ensure that any claims made do not imply a health benefit without substantiation to comply with **Rule 15.1** and avoid making unsubstantiated health or nutrition claims.

**Recommendation:** The advertiser should provide evidence or further substantiation to support claims and consider using testimonials or case studies from recognized brands to fortify the message while ensuring the ad adheres to CAP and BCAP Codes.

Troubleshooting
If you encounter errors related to API requests, double-check your API keys and ensure you have internet connectivity.
Ensure that the input format for the product description matches the expected format.





