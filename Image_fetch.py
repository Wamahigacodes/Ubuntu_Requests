import requests
import os
import hashlib
from urllib.parse import urlparse
from pathlib import Path

def calculate_file_hash(filepath):
    """Calculate MD5 hash of a file to check for duplicates"""
    hash_md5 = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except IOError:
        return None

def is_safe_file_type(content_type, url):
    """Check if the content type is a safe image type"""
    safe_image_types = [
        'image/jpeg', 
        'image/png', 
        'image/gif', 
        'image/bmp', 
        'image/webp',
        'image/svg+xml'
    ]
    
    if content_type not in safe_image_types:
        # Also check file extension as a secondary precaution
        parsed_url = urlparse(url)
        path = parsed_url.path.lower()
        safe_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg']
        if not any(path.endswith(ext) for ext in safe_extensions):
            return False
    return True

def get_filename_from_url(url, response):
    """Extract filename from URL or generate one based on content"""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    # If no filename in URL, generate one based on content type
    if not filename or '.' not in filename:
        content_type = response.headers.get('content-type', '').split(';')[0]
        extension = '.jpg'  # default
        
        if 'jpeg' in content_type or 'jpg' in content_type:
            extension = '.jpg'
        elif 'png' in content_type:
            extension = '.png'
        elif 'gif' in content_type:
            extension = '.gif'
        elif 'webp' in content_type:
            extension = '.webp'
        elif 'svg' in content_type:
            extension = '.svg'
            
        # Create filename from domain and content hash
        domain = parsed_url.netloc.replace('www.', '').split('.')[0]
        content_hash = hashlib.md5(response.content).hexdigest()[:8]
        filename = f"{domain}_{content_hash}{extension}"
    
    return filename

def download_image(url, download_dir="Fetched_Images"):
    """Download an image from a URL with safety checks"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(download_dir, exist_ok=True)
        
        # Set a respectful user-agent header
        headers = {
            'User-Agent': 'UbuntuImageFetcher/1.0 (Community Image Collector)'
        }
        
        # Fetch the image with timeout
        print(f"Connecting to {urlparse(url).netloc}...")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Check important HTTP headers
        content_type = response.headers.get('content-type', '').split(';')[0]
        content_length = response.headers.get('content-length')
        
        print(f"Content-Type: {content_type}")
        if content_length:
            print(f"Content-Length: {content_length} bytes")
        
        # Security precaution: Check if this is a safe image file type
        if not is_safe_file_type(content_type, url):
            print(f"⚠️  Warning: Unsupported file type ({content_type}). Download cancelled.")
            return False
        
        # Extract filename from URL or generate one
        filename = get_filename_from_url(url, response)
        filepath = os.path.join(download_dir, filename)
        
        # Check for duplicates by content hash
        new_content_hash = hashlib.md5(response.content).hexdigest()
        for existing_file in os.listdir(download_dir):
            existing_path = os.path.join(download_dir, existing_file)
            if calculate_file_hash(existing_path) == new_content_hash:
                print(f"✓ Image already exists as: {existing_file}")
                print("No duplicate created. Community resources preserved.")
                return True
        
        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        return True
        
    except requests.exceptions.Timeout:
        print("✗ Connection timed out. Please try again later.")
    except requests.exceptions.ConnectionError:
        print("✗ Connection error. Please check your internet connection.")
    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"✗ An error occurred: {e}")
    except IOError as e:
        print(f"✗ Error saving file: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")
    
    return False

def main():
    print("=" * 60)
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web")
    print("=" * 60)
    
    # Get URL(s) from user
    url_input = input("Please enter image URL(s), separated by commas if multiple: ").strip()
    
    if not url_input:
        print("No URLs provided. Exiting gracefully.")
        return
    
    urls = [url.strip() for url in url_input.split(',')]
    successful_downloads = 0
    
    for url in urls:
        if not url:
            continue
            
        print(f"\n--- Processing: {url} ---")
        if download_image(url):
            successful_downloads += 1
    
    print("\n" + "=" * 60)
    print(f"Download summary: {successful_downloads} of {len(urls)} images fetched successfully")
    
    if successful_downloads > 0:
        print("Connection strengthened. Community enriched.")
    else:
        print("No images were downloaded, but community respect was maintained.")
    print("=" * 60)

if __name__ == "__main__":
    main()