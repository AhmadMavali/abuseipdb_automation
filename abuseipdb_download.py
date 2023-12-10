import requests

api_key = 'ABUSEIPDB_KEY'  #you should create an API key on the abuseipdb.com site and put the key here
output_file = '/opt/abuseipdb.txt' #Where the list of download IPs are placed with its name.

url = 'https://api.abuseipdb.com/api/v2/blacklist'

params = {
    'confidenceMinimum': 1, #Scoring level of download IPs
    'limit': 100000,  #Count of IPs you want to download
}

headers = {
    'Key': api_key,
    'Accept': 'application/json'
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    ips = [entry['ipAddress'] for entry in data['data']]
    with open(output_file, 'w') as file:
        file.write('\n'.join(ips))
    print(f"Malicious IPs saved to {output_file}")
else:
    print("Error occurred while making the API request.")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
