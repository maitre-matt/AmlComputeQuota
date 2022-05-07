import argparse
import requests
from azure.identity import DefaultAzureCredential

parser = argparse.ArgumentParser(description="List available Azure ML Compute quotas across regions as CSV")
parser.add_argument("subscription_id", help="The Azure subscription to list quotas for")
args = parser.parse_args()

credential = DefaultAzureCredential()
access_token = credential.get_token("https://management.azure.com/.default").token
headers = {"Authorization": "Bearer " + access_token}

response = requests.get(f"https://management.azure.com/subscriptions/{args.subscription_id}/locations?api-version=2020-01-01", headers=headers)
response.raise_for_status()
regions = [value["name"] for value in response.json()["value"]]

print(f"region,available,current,limit,name")
for region in regions:
    try:
        response = requests.get(f"https://management.azure.com/subscriptions/{args.subscription_id}/providers/Microsoft.MachineLearningServices/locations/{region}/usages?api-version=2020-04-01", headers=headers)
        response.raise_for_status()
        for available_quota in [value for value in response.json()["value"] if value["limit"] > 0 and value["currentValue"] < value["limit"]]:
            print(f'{region},{available_quota["limit"] - available_quota["currentValue"]},{available_quota["currentValue"]},{available_quota["limit"]},{available_quota["name"]["value"]}')
    except Exception as e:
        pass

