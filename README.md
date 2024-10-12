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

Example Usage:

Please provide a product description: adclear.ai is a marketing compliance company

### Generated Advert

**Title**: *Clarity Through Compliance*

> Navigating complex marketing regulations often leaves businesses overwhelmed. But with Adclear.ai, clarity is just a step away. By offering expert compliance solutions, they transform chaos into seamless operations. Join countless brands who trust Adclear.ai to keep their campaigns compliant and stress-free. Ensure your marketing strategies meet legal standards effortlessly. Visit adclear dot ai and experience the ease of compliance today.

**Tags**: Marketing Compliance, Business Solution, Advertising Regulations

### Adclear Evaluation

This will need review to pass the relevant guidelines.

- **Rule 11.2:** Ensure that terms like "expert compliance solutions" are clear to consumers. Further explanation of the service's specifics may be needed to avoid ambiguity or confusion.
- **Rule 20.7:** Avoid potential exaggeration of the support level provided by stating "countless brands who trust Adclear.ai" without clearer context or specifics on support offered.
- The advert suggests that Adclear.ai can make compliance "effortless," which could require substantiation (**Rule 12.1**). Advertisers should demonstrate how their services achieve this and back claims where needed.
- Review for unintentional implications of guarantees or typical results (**Rule 20.8**). Ensure that claims about the "ease of compliance" do not imply guaranteed outcomes without evidence or substantiation.
- While the advertisement is creative and succinct, suggest including a brief overview of how Adclear.ai meets compliance needs to ensure consumer transparency.

**Recommendation:** The advertiser should provide evidence or further substantiation to support claims and consider using testimonials or case studies from recognized brands to fortify the message while ensuring the ad adheres to CAP and BCAP Codes.


Troubleshooting
If you encounter errors related to API requests, double-check your API keys and ensure you have internet connectivity.
Ensure that the input format for the product description matches the expected format.





