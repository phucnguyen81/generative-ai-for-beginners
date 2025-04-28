"""Generate an image using OpenAI API"""
import json
import os

import dotenv
import requests
from openai import AzureOpenAI
from PIL import Image

from pup import config

# Search for .env file and load it
dotenv.load_dotenv()

prompt = """You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult

Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
"""

client = AzureOpenAI(
    api_key=config.AZURE_OPENAI_API_KEY,
    api_version=config.AZURE_OPENAI_IMAGE_API_VERSION,
    azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
)

# Create an image by using the image generation API
result = client.images.generate(
    model=config.AZURE_OPENAI_IMAGE_DEPLOYMENT,
    prompt=prompt,    # Enter your prompt text here
    size='1024x1024',
    n=1
)

generation_response = json.loads(result.model_dump_json())

# Set the directory for the stored image
image_dir = config.CHAPTER_09_DIR / "images"
if not image_dir.exists():
    image_dir.mkdir()

# Initialize the image path (note the filetype should be png)
image_path = image_dir / 'ch9-sol-generated-image.png'

# Retrieve the generated image
# extract image URL from response
image_url = generation_response["data"][0]["url"]
generated_image = requests.get(
    image_url, timeout=config.REQUEST_TIMEOUT).content  # download the image
with open(image_path, "wb") as image_file:
    image_file.write(generated_image)

# Display the image in the default image viewer
image = Image.open(image_path)
image.show()


# ---creating variation below---

# response = openai.Image.create_variation(
#   image=open(image_path, "rb"),
#   n=1,
#   size="1024x1024"
# )

# image_path = os.path.join(image_dir, 'generated_variation.png')

# image_url = response['data'][0]['url']

# generated_image = requests.get(image_url).content  # download the image
# with open(image_path, "wb") as image_file:
#     image_file.write(generated_image)

# # Display the image in the default image viewer
# image = Image.open(image_path)
# image.show()
