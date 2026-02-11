import os
from bs4 import BeautifulSoup
import re

def check_css_links(file_path, base_dir):
    print(f"Scanning CSS {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading CSS {file_path}: {e}")
        return

    urls = re.findall(r'url\((.*?)\)', content)
    for url in urls:
        # Clean quotes
        url = url.strip('\'"')
        if url.startswith(('http', '//', 'data:')):
            continue
        
        # CSS paths are relative to the CSS file usually, but sometimes relative to root.
        css_dir = os.path.dirname(file_path)
        full_path = os.path.join(css_dir, url)
        
        if url.startswith('/'):
            full_path = os.path.join(base_dir, url.lstrip('/'))
        
        # Normalize
        full_path = os.path.normpath(full_path)
        
        if not os.path.exists(full_path):
            print(f"[MISSING IN CSS] {url} -> {full_path}")

def check_links(file_path, root_dir):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"Scanning {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    base_dir = os.path.dirname(file_path)
    links = []
    
    # Check data-filename, data-src, data-image, poster
    for attr in ['data-filename', 'data-src', 'data-image', 'poster']:
        for tag in soup.find_all(attrs={attr: True}):
            link = tag[attr]
            links.append(link)

    css_files = []

    errors = 0
    for link in links:
        # Skip external links, anchors, and data URIs
        if link.startswith(('http', '//', '#', 'mailto:', 'tel:', 'data:')):
            continue
            
        # Clean query strings/fragments
        clean_link = link.split('?')[0].split('#')[0]
        if not clean_link:
            continue
            
        full_path = os.path.join(base_dir, clean_link)
        if clean_link.startswith('/'):
             full_path = os.path.join(root_dir, clean_link.lstrip('/'))

        # Check for file existence. 
        # For data-filename, it might lack extension. Try common image extensions.
        if not os.path.exists(full_path):
            found_with_ext = False
            for ext in ['.jpg', '.jpeg', '.png', '.webp', '.mp4', '.svg']:
                if os.path.exists(full_path + ext):
                    found_with_ext = True
                    break
            
            if not found_with_ext:
                print(f"[MISSING] {link} -> {full_path}")
                errors += 1
        
        if clean_link.endswith('.css'):
            css_files.append(full_path)

    for css_file in css_files:
        if os.path.exists(css_file):
             check_css_links(css_file, root_dir)

if __name__ == "__main__":
    root_directory = r"c:/Users/tanmoy/Documents/website clone/lusion.co"
    print(f"Scanning directory: {root_directory}")
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.lower().endswith(".html"):
                full_path = os.path.join(root, file)
                check_links(full_path, root_directory)
