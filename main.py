import requests
import time
file_path = 'userid.txt'


# Hardcoded list of UIDs (replace with your actual list)
uids = [
    '100006338568' # Example: Replace with your UIDs
    # Add more UIDs here...
]
with open(file_path, 'r') as file:
    uids = [line.strip() for line in file]
# print(uids)
# Prompt user for the gift code
gift_code = input("Enter the gift code: ").strip()

if not gift_code:
    print("Please enter a gift code.")
    exit()

if not uids:
    print("No UIDs provided in the hardcoded list.")
    exit()

url = 'https://www.amatsukimahjong.com/sys/reqRedeem.php'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

for uid in uids:
    data = f'uid={uid}&giftCode={gift_code}'
    
    try:
        response = requests.post(url, headers=headers, data=data)
        print(f"Request for UID {uid}: {response.text}")
    except Exception as e:
        print(f"Error for UID {uid}: {str(e)}")
    
    time.sleep(2)  # Wait 2 seconds before the next request

print("All requests completed.")