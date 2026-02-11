import os
import requests
import json

BASE_URL = "https://lusion.co"

def download_file(path):
    # Cleanup path
    path = path.replace('//', '/').lstrip('/')
    local_path = os.path.normpath(path)
    
    if os.path.exists(local_path):
        return True
    
    url = f"{BASE_URL}/{path}"
    print(f"[DOWNLOADING] {url} -> {local_path}")
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            with open(local_path, 'wb') as f:
                f.write(response.content)
            print(f"[SUCCESS] Saved to {local_path}")
            return True
        else:
            print(f"[FAILED] HTTP {response.status_code} for {url}")
            return False
    except Exception as e:
        print(f"[ERROR] downloading {url}: {e}")
        return False

def fix_team():
    team_json_path = "assets/team/team.json"
    if not os.path.exists(team_json_path):
        return
    
    try:
        with open(team_json_path, 'r', encoding='utf-8') as f:
            team_data = json.load(f)
            for member in team_data:
                member_id = member.get('id')
                if member_id:
                    download_file(f"assets/team/{member_id}.buf")
    except Exception as e:
        print(f"[ERROR] processing team.json: {e}")

if __name__ == "__main__":
    fix_team()
