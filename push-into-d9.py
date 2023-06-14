import requests
import json
from datetime import datetime
import sys
import os
import base64

# Retrieve DOME9_USERNAME and DOME9_PASSWORD from system variables
username = os.getenv('DOME9_USERNAME')
password = os.getenv('DOME9_PASSWORD')

# Check if username and password are set
if not username or not password:
    print("DOME9_USERNAME and/or DOME9_PASSWORD are not set.")
    username = input("Enter your DOME9 username: ")
    password = input("Enter your DOME9 password: ")
    if not username or not password:
        print("Username and/or password cannot be empty. Exiting...")
        sys.exit(1)

# Check if AWS rules file exists
aws_rules_file = "rules_aws.json"
if not os.path.isfile(aws_rules_file):
    print(f"Error: {aws_rules_file} not found in the current directory.")
    sys.exit(1)

# Check if Azure rules file exists
azu_rules_file = "rules_AZU.json"
if not os.path.isfile(azu_rules_file):
    print(f"Error: {azu_rules_file} not found in the current directory.")
    sys.exit(1)

# Check if GCP rules file exists
gcp_rules_file = "rules_gcp.json"
if not os.path.isfile(gcp_rules_file):
    print(f"Error: {gcp_rules_file} not found in the current directory.")
    sys.exit(1)

# Load the AWS rules from the file
with open(aws_rules_file, 'r') as aws_file:
    aws_rules = json.load(aws_file)

# Load the Azure rules from the file
with open(azu_rules_file, 'r') as azu_file:
    azu_rules = json.load(azu_file)

# Load the GCP rules from the file
with open(gcp_rules_file, 'r') as gcp_file:
    gcp_rules = json.load(gcp_file)

url = "https://api.dome9.com/v2/Compliance/Ruleset"

actions = sys.argv[1:]  # Get command-line arguments excluding the script name

valid_actions = ["aws", "azure", "gcp"]

if not actions:
    print("No action specified. Please provide an action (aws, azure, gcp).")
    sys.exit(1)

for action in actions:
    if action not in valid_actions:
        print(f"Invalid action: {action}")
        print("Valid actions are: aws, azure, gcp")
        continue

    if action == "aws":
        # Create AWS payload
        aws_payload = {
            "minFeatureTier": "Trial",
            "cloudVendor": "aws",
            "language": "en",
            "name": "AWS Custom Ruleset",
            "description": f"AWS Custom Ruleset {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "rules": aws_rules
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode()}"
        }

        # Send AWS request
        aws_response = requests.post(url, json=aws_payload, headers=headers)
        print("AWS response:", aws_response.text)

    elif action == "azure":
        # Create Azure payload
        azu_payload = {
            "minFeatureTier": "Trial",
            "cloudVendor": "azure",
            "language": "en",
            "name": "Azure Custom Ruleset",
            "description": f"Azure Custom Ruleset {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "rules": azu_rules
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode()}"
        }

        # Send Azure request
        azu_response = requests.post(url, json=azu_payload, headers=headers)
        print("Azure response:", azu_response.text)

    elif action == "gcp":
        # Create GCP payload
        gcp_payload = {
            "minFeatureTier": "Trial",
            "cloudVendor": "google",
            "language": "en",
            "name": "GCP Custom Ruleset",
            "description": f"GCP Custom Ruleset {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "rules": gcp_rules
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode()}"
        }

        # Send GCP request
        gcp_response = requests.post(url, json=gcp_payload, headers=headers)
        print("GCP response:", gcp_response.text)

