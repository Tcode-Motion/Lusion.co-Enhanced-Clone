import re
import os

def extract_assets():
    js_file = '_astro/hoisted.81170750.js'
    if not os.path.exists(js_file):
        print(f"File {js_file} not found")
        return

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find patterns like settings.TEXTURE_PATH + "something.png"
    # settings.TEXTURE_PATH is "/assets/textures/"
    # We also look for direct /assets/ strings
    
    paths = set()
    
    # Direct matches
    paths.update(re.findall(r'/assets/[^"']+', content))
    
    # Base paths
    # CDN_PATH = "";
    # TEAM_PATH = "/assets/team/";
    # PROJECT_PATH = "/assets/projects/";
    # MODEL_PATH = "/assets/models/";
    # IMAGE_PATH = "/assets/images/";
    # TEXTURE_PATH = "/assets/textures/";
    # AUDIO_PATH = "/assets/audios/";
    # SPRITE_PATH = "/assets/sprites/";
    
    base_paths = {
        "TEAM_PATH": "assets/team/",
        "PROJECT_PATH": "assets/projects/",
        "MODEL_PATH": "assets/models/",
        "IMAGE_PATH": "assets/images/",
        "TEXTURE_PATH": "assets/textures/",
        "AUDIO_PATH": "assets/audios/",
        "SPRITE_PATH": "assets/sprites/"
    }
    
    # Search for something like: settings.TEXTURE_PATH+"smaa-area.png"
    for key, val in base_paths.items():
        pattern = key + r'["']?\s*\+\s*["']([^"']+)'
        matches = re.findall(pattern, content)
        for m in matches:
            paths.add(val + m)

    # Some paths might have variables, e.g. settings.TEAM_PATH+e+".buf"
    # We can't resolve 'e' easily, but we can see common suffixes
    
    # Cleanup paths
    clean_paths = set()
    for p in paths:
        p = p.lstrip('/')
        # Remove any JS code remnants if regex was too greedy
        p = p.split('?')[0].split('#')[0]
        if '.' in os.path.basename(p): # Must have extension
            clean_paths.add(p)

    with open('detected_assets.txt', 'w', encoding='utf-8') as f:
        for p in sorted(clean_paths):
            f.write(p + '
')
    
    print(f"Detected {len(clean_paths)} assets. Saved to detected_assets.txt")

if __name__ == "__main__":
    extract_assets()
