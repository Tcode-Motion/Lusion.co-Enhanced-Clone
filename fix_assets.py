import os
from bs4 import BeautifulSoup
import re

# 1x1 pixel white JPEG
ONE_PIXEL_JPG = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xdb\x00C\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x11\x08\x00\x01\x00\x01\x03\x01\x22\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x15\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xff\xc4\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xc4\x00\x14\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xc4\x00\x14\x11\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00\x3f\x00\xbf\x80\x01\xff\xd9'

# 1x1 pixel transparent WebP
ONE_PIXEL_WEBP = b'RIFF\x1a\x00\x00\x00WEBPVP8L\x0d\x00\x00\x00\x2f\x00\x00\x00\x10\x07\x10\x11\x11\x88\x88\xfe\x07\x00'

def create_placeholder(path, content=ONE_PIXEL_JPG):
    if os.path.exists(path):
        return
    
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f:
            f.write(content)
        print(f"[CREATED] {path}")
    except Exception as e:
        print(f"[ERROR] generating {path}: {e}")

def fix_assets(root_dir):
    print(f"Scanning {root_dir} for missing assets in data attributes...")
    
    missing_assets = set()

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if not file.lower().endswith(".html"):
                continue
                
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue

            # Look for specific attributes used for lazy loading / 3D textures
            # data-filename is the main one seen in user logs
            for attr in ['data-filename', 'data-src', 'data-image', 'poster']:
                for tag in soup.find_all(attrs={attr: True}):
                    link = tag[attr]
                    
                    if link.startswith(('http', '//', '#', 'data:')):
                         continue
                    
                    # Resolve path
                    # Assuming absolute paths from root like /assets/...
                    full_path = ""
                    if link.startswith('/'):
                        full_path = os.path.join(root_dir, link.lstrip('/'))
                    else:
                        # Relative to file
                        full_path = os.path.join(os.path.dirname(file_path), link)
                    
                    full_path = os.path.normpath(full_path)
                    
                    if not os.path.exists(full_path):
                        # Try to guess missing file
                        # If no extension, add .jpg and .webp
                        if not os.path.splitext(full_path)[1]:
                             missing_assets.add((full_path + ".jpg", ONE_PIXEL_JPG))
                             missing_assets.add((full_path + ".webp", ONE_PIXEL_WEBP))
                        else:
                             # Has extension, just create it
                             content = ONE_PIXEL_JPG
                             if full_path.endswith('.webp'):
                                 content = ONE_PIXEL_WEBP
                             missing_assets.add((full_path, content))

    print(f"Found {len(missing_assets)} missing asset targets.")
    
    for path, content in missing_assets:
        create_placeholder(path, content)

if __name__ == "__main__":
    root = r"c:/Users/tanmoy/Documents/website clone/lusion.co"
    fix_assets(root)
