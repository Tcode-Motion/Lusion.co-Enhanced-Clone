import os
import requests

ASSETS_TO_DOWNLOAD = [
    "assets/textures/smaa-search.png",
    "assets/textures/smaa-area.png",
    "assets/textures/LDR_RGB1_0.png",
    "assets/audios/generic.ogg",
    "assets/audios/cinematic_0.ogg",
    "assets/audios/cinematic_2.ogg",
    "assets/audios/cinematic_3.ogg",
    "assets/audios/generic_end.ogg",
    "assets/textures/reel/desktop.mp4",
    "assets/textures/reel/mobile.mp4",
    "assets/models/home/cross.buf",
    "assets/models/home/cross_ld.buf",
]

BASE_URL = "https://lusion.co"

def download_file(path):
    local_path = os.path.normpath(path)
    if os.path.exists(local_path):
        print(f"[EXISTS] {local_path}")
        return True
    
    url = f"{BASE_URL}/{path}"
    print(f"[DOWNLOADING] {url} -> {local_path}")
    
    try:
        response = requests.get(url, timeout=10)
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

def fix_projects():
    projects_dir = "assets/projects"
    if not os.path.exists(projects_dir):
        print(f"[ERROR] {projects_dir} not found")
        return
    
    for project_id in os.listdir(projects_dir):
        project_path = os.path.join(projects_dir, project_id)
        if os.path.isdir(project_path):
            download_file(f"assets/projects/{project_id}/home.webp")
            download_file(f"assets/projects/{project_id}/home_depth.webp")

if __name__ == "__main__":
    for asset in ASSETS_TO_DOWNLOAD:
        download_file(asset)
    
    fix_projects()
