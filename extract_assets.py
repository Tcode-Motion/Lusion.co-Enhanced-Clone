import re
import os

def extract_assets():
    js_file = '_astro/hoisted.81170750.js'
    if not os.path.exists(js_file):
        print(f"File {js_file} not found")
        return

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    paths = set()
    
    # Direct matches for /assets/...
    # Using a simple non-raw string to avoid confusion
    paths.update(re.findall("/assets/[a-zA-Z0-9_./-]+", content))
    
    base_paths = {
        "TEAM_PATH": "assets/team/",
        "PROJECT_PATH": "assets/projects/",
        "MODEL_PATH": "assets/models/",
        "IMAGE_PATH": "assets/images/",
        "TEXTURE_PATH": "assets/textures/",
        "AUDIO_PATH": "assets/audios/",
        "SPRITE_PATH": "assets/sprites/"
    }
    
    # Search for something like: Settings.TEXTURE_PATH + "smaa-area.png"
    for key, val in base_paths.items():
        # Match Settings.TEXTURE_PATH + "filename.ext" or Settings.TEXTURE_PATH+"filename.ext"
        pattern = key + r'\s*\+\s*["\']([^"\']+)["\']'
        matches = re.findall(pattern, content)
        for m in matches:
            paths.add(val + m)

    # Cleanup paths
    clean_paths = set()
    for p in paths:
        p = p.lstrip('/')
        if '.' in os.path.basename(p): # Must have extension
            # Ensure it's not a JS variable or something
            if not p.endswith(('.js', '.css')):
                clean_paths.add(p)

    with open('detected_assets.txt', 'w', encoding='utf-8') as f:
        for p in sorted(clean_paths):
            f.write(p + '\n')
    
    print(f"Detected {len(clean_paths)} assets. Saved to detected_assets.txt")

if __name__ == "__main__":
    extract_assets()