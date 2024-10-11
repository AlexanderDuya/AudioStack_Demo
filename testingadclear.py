import requests

url = "https://app.adclear.ai/api/v1/evaluate/text"

payload = {
    "text": "This is a test.",
    "evidenceProvided": True
}
headers = {
    "Authorization": "Bearer adclear_3ZMSQMKRUWNJTvhsrtDZ35jU",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)  # Check the response status
print("Response Text:", response.text)  # Check the response content
