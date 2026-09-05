import json
import base64
from openai import OpenAI

client = OpenAI()
generate_test_image = False

with open("storyboard.json", "r") as file:
    storyboard = json.load(file)

scenes = storyboard["scenes"]

image_prompts = []

character_profiles = {
    "user": "adult college student with dark wavy hair, brown eyes, wearing a dark navy shirt",
    "friend": "adult college student with shoulder-length dark hair, warm expression, casual neutral-colored clothing"
}

for scene in scenes:
    location_text = scene["location"]

    if location_text == "unspecified":
        location_text = "a simple neutral background with no distinctive location-specific details"

    if scene["time_of_day"] == "unspecified":
        lighting_text = "soft neutral natural lighting"
    else:
        lighting_text = f"{scene['time_of_day']} lighting"

    character_descriptions = []

    for character in scene["characters"]:
        if character in character_profiles:
            character_descriptions.append(
                f"{character}: {character_profiles[character]}"
            )
        else:
            character_descriptions.append(character)

    image_prompt = f"""
Create a cinematic realistic image showing: {scene["visual_description"]}

Characters: {"; ".join(character_descriptions)}
Setting: {location_text}
Lighting: {lighting_text}
Atmosphere: {scene["atmosphere"]}
Framing: {scene["shot_type"]}

Style: cinematic, slightly dreamy, emotionally expressive, soft lighting, memory-like, visually cohesive, and consistent character appearance across scenes.
"""

    image_prompts.append(image_prompt)

print("\nIMAGE PROMPTS:")

for image_prompt in image_prompts:
    print(image_prompt)

for index, image_prompt in enumerate(image_prompts[1:2], start=2):
    print(f"Scene {index} ready for generation")

    if generate_test_image:
        result = client.images.generate(
            model="gpt-image-2",
            prompt=image_prompt,
            size="1536x1024",
            quality="medium",
            n=1
        )

        image_base64 = result.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        filename = f"scene_{index}.png"

        with open(filename, "wb") as file:
            file.write(image_bytes)

first_image_prompt = image_prompts[0]

if generate_test_image:
    result = client.images.generate(
        model="gpt-image-2",
        prompt=first_image_prompt,
        size="1536x1024",
        quality="medium",
        n=1
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    with open("scene_1.png", "wb") as file:
        file.write(image_bytes)
        print(f"Saved {filename}")



