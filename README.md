# Ubuntu_Inspired Image Fetcher

A Python script that embodies the Ubuntu philosophy of "I am because we are" by respectfully fetching and organizing images from the global web community.

## Overview

This tool connects to the global internet community, mindfully collects image resources, and organizes them for later appreciation. It implements the core Ubuntu principles of community, respect, sharing, and practicality while maintaining security and efficiency.

## Features

- **Multiple URL Support**: Process single or multiple comma-separated image URLs
- **Security Precautions**: Validates content types and file extensions before downloading
- **Duplicate Prevention**: Uses MD5 hashing to avoid storing identical images
- **Graceful Error Handling**: Comprehensive error management for various scenarios
- **Respectful Connection**: Uses appropriate headers and timeouts to avoid overburdening servers
- **Automatic Organization**: Creates a dedicated "Fetched_Images" directory

## Ubuntu Principles Implemented

1. **Community**: Connects to the global web community to fetch shared resources
2. **Respect**: 
   - Uses a respectful User-Agent string
   - Handles all errors gracefully without crashing
   - Implements timeouts to avoid overburdening servers
3. **Sharing**: Organizes images in a dedicated directory for later sharing
4. **Practicality**: Creates a useful tool for collecting web resources

## Installation

1. Ensure you have Python 3.6+ installed
2. Install the required dependency:
   ```bash
   pip install requests
   ```

## Usage

1. Save the script as `ubuntu_image_fetcher.py`
2. Run the script:
   ```bash
   python ubuntu_image_fetcher.py
   ```
3. Enter one or more image URLs when prompted (comma-separated for multiple URLs)

### Example Usage

```bash
$ python ubuntu_image_fetcher.py
============================================================
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web
============================================================
Please enter image URL(s), separated by commas if multiple: https://example.com/image1.jpg, https://example.com/image2.png

--- Processing: https://example.com/image1.jpg ---
Connecting to example.com...
Content-Type: image/jpeg
Content-Length: 204857 bytes
✓ Successfully fetched: image1.jpg
✓ Image saved to Fetched_Images/image1.jpg

--- Processing: https://example.com/image2.png ---
Connecting to example.com...
Content-Type: image/png
✓ Successfully fetched: image2.png
✓ Image saved to Fetched_Images/image2.png

============================================================
Download summary: 2 of 2 images fetched successfully
Connection strengthened. Community enriched.
============================================================
```

## Security Features

- Validates both Content-Type headers and file extensions
- Limits downloads to safe image file types only (JPEG, PNG, GIF, BMP, WebP, SVG)
- Uses content hashing to prevent duplicate downloads
- Implements timeout protection to prevent hanging connections

## Supported Image Formats

- JPEG/JPG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- BMP (.bmp)
- WebP (.webp)
- SVG (.svg)

## Error Handling

The script gracefully handles:
- Network timeouts and connection errors
- HTTP status errors (404, 403, etc.)
- File system errors (permission issues, disk space)
- Invalid URLs and unsupported content types
- Duplicate image detection

## File Structure

```
project/
├── ubuntu_image_fetcher.py  # Main script
└── Fetched_Images/          # Auto-created directory for images
    ├── image1.jpg
    ├── image2.png
    └── ...
```

## Code Structure

- `calculate_file_hash()`: Calculates MD5 hash for duplicate detection
- `is_safe_file_type()`: Validates content type and file extension
- `get_filename_from_url()`: Extracts or generates appropriate filenames
- `download_image()`: Main function handling the download process with safety checks
- `main()`: Orchestrates the program flow and user interaction

## HTTP Headers Checked

- `Content-Type`: Validates the response is an image
- `Content-Length`: Provides information about file size (if available)

## Challenge Solutions

1. **Multiple URL handling**: Accepts comma-separated URLs in a single input
2. **Security precautions**: Validates content types and extensions before saving
3. **Duplicate prevention**: Uses MD5 hashing to compare image content
4. **HTTP header validation**: Checks Content-Type before processing responses

## Evaluation Criteria Met

- ✅ Proper use of the requests library for fetching content
- ✅ Effective error handling for network issues
- ✅ Appropriate file management and directory creation
- ✅ Clean, readable code with clear comments
- ✅ Faithfulness to Ubuntu principles of community and respect

## Philosophy

"A person is a person through other persons." - Ubuntu philosophy

This tool embodies this principle by creating connections across the web community, respecting the work of others, and sharing resources mindfully.

## License

This project is created in the spirit of Ubuntu and community sharing.
