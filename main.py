import requests
import time
file_path = 'userid.txt'


# Hardcoded list of UIDs (replace with your actual list)
with open(file_path, 'r') as file:
    uids = [line.strip() for line in file]

# Prompt user for the gift code
while True:
    gift_code = input("Enter the gift code: ").strip()
    if (gift_code == "q" or gift_code == "Q"):
        break

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
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(url, headers=headers, data=data)
                print(f"Request for UID {uid}: {response.text}")
                
                # Retry if response contains -1
                if "-1" in response.text and attempt < max_retries - 1:
                    print(f"Failed response (-1) for UID {uid}, retrying... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(5)
                    continue
                break
            except Exception as e:
                print(f"Error for UID {uid}: {str(e)}")
                if attempt < max_retries - 1:
                    print(f"Retrying... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(5)
                else:
                    break
        
        time.sleep(5)  # Wait 5 seconds before the next request
    print(f"All requests for {gift_code} completed.")