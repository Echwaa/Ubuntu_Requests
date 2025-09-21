# PYTHON LIBRARIES ASSIGNMENT
# Ubuntu_Requests

import os
import requests
from urllib.parse import urlparse
import sys

def download_image(image_url):
    # Create directory 'Fetched_Images' if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    # Extract filename from URL or generate one
    parsed_url = urlparse(image_url)
    filename = os.path.basename(parsed_url.path)

    if not filename:
        filename = "downloaded_image"

    save_path = os.path.join("Fetched_Images", filename)

    try:
        # Use requests to fetch the image
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Save the image content in binary mode
        with open(save_path, "wb") as file:
            file.write(response.content)

        print(f"Image successfully downloaded and saved as {save_path}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Failed to establish a connection.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the image to download: ").strip()
    if url:
        download_image(url)
    else:
        print("No URL entered. Exiting program.")
        sys.exit(1)
