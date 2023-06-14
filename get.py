import requests
import pandas as pd
from requests.auth import HTTPBasicAuth
import json
from langdetect import detect
import os

# Get your username and password from environment variables
username = os.getenv('DOME9_USERNAME')
password = os.getenv('DOME9_PASSWORD')

# Check if environment variables are set
if username is None or password is None:
    print("Please set the environment variables DOME9_USERNAME and DOME9_PASSWORD.")
    exit(1)

# URL of the API you want to call
url = 'https://api.dome9.com/v2/Compliance/Ruleset'

# Make the API call
response = requests.get(url, headers={'accept': 'application/json'}, auth=HTTPBasicAuth(username, password))

# Function to detect if a text is in English or not
def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

# Function to process rules
def process_rules(data, rule_prefix):
    rule_names = set()
    rule_logic_hashes = set()
    rules = []
    for item in data:
        for rule in item["rules"]:
            if rule["ruleId"] and rule["ruleId"].startswith(rule_prefix) and rule["logicHash"] not in rule_logic_hashes and rule["name"] not in rule_names:
                if not is_english(rule['name']) or not is_english(rule['description']) or not is_english(rule['remediation']):
                    continue
                original_name = rule["name"]
                i = 1
                while rule["name"] in rule_names:
                    rule["name"] = original_name + " " + str(i)
                    i += 1
                rules.append(rule)
                rule_names.add(rule["name"])
                rule_logic_hashes.add(rule["logicHash"])
    return rules

# Check if the request was successful
if response.status_code == 200:
    # Load the response content as JSON
    data = response.json()

    # Process AWS rules
    aws_rules = process_rules(data, "D9.AWS")
    with open('rules_aws.json', 'w') as aws_file:
        json.dump(aws_rules, aws_file)
    print(f'{len(aws_rules)} unique AWS rules written to rules_aws.json')

    # Process AZU rules
    AZU_rules = process_rules(data, "D9.AZU")
    with open('rules_AZU.json', 'w') as AZU_file:
        json.dump(AZU_rules, AZU_file)
    print(f'{len(AZU_rules)} unique AZU rules written to rules_AZU.json')

    # Process GCP rules
    gcp_rules = process_rules(data, "D9.GCP")
    with open('rules_gcp.json', 'w') as gcp_file:
        json.dump(gcp_rules, gcp_file)
    print(f'{len(gcp_rules)} unique GCP rules written to rules_gcp.json')

    # Convert the JSON data to a DataFrame
    df = pd.json_normalize(data)

    # Given API output schema
    schema = {
        "$schema": "http://json-schema.org/schema#",
        # ... rest of your schema here ...
    }

    # Write the schema to a file
    with open('rules_schema.json', 'w') as schema_file:
        json.dump(schema, schema_file, indent=4)
else:
    print('Failed to get data:', response.status_code)

