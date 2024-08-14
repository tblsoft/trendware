from openai import OpenAI
import requests
import json
import os


def generate_image(prompt):
    openai = OpenAI(api_key=api_key)
    model = "dall-e-3"
    response = openai.images.generate(prompt=prompt, model=model)
    image_url = response.data[0].url
    return image_url

def download_image(image_url, filename='image.png'):
    # Send a GET request to the image URL
    response = requests.get(image_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Write the content to a file
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded and saved as {filename}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")


base_path = os.getcwd()
api_key = '****'

with open(base_path + "/products.json", 'r', encoding='utf-8') as file:
    products = json.load(file)

for product in products:
    id = product["id"]
    image_file_name = f"{base_path}/shop/data/img/{id}.png"
    if os.path.exists(image_file_name):
        continue

    prompt = """
    Ich habe einen Online Shop und verkaufe Mode Sachen. Erstelle mir ein Bild für das Produkt:
    
    """ + product["title"]
    print(prompt)
    image_url = generate_image(prompt)
    download_image(image_url, image_file_name)
