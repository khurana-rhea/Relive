from openai import OpenAI
import json

client = OpenAI()
journal_entry = """Today I was really nervous before my exam. Afterward, my friend surprised me with coffee and I felt much better."""
print(journal_entry)
relive_schema = {
    "type": "object",
    "properties": {
        "events": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "event": {
                        "type": "string"
                    },
                    "characters": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "location": {
                        "type": "string"
                    },
                    "location_source": {
                        "type": "string",
                        "enum": [
                            "explicit",
                            "inferred",
                            "default",
                            "user_customized"
                        ]
                    },
                    "time_of_day": {
                        "type": "string",
                        "enum": [
                            "morning",
                            "afternoon",
                            "evening",
                            "night",
                            "unspecified"
                        ]
                    },
                    "time_source": {
                        "type": "string",
                        "enum": [
                            "explicit",
                            "inferred",
                            "default",
                            "user_customized"
                        ]
                    },
                    "emotions": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "minItems": 1,
                        "maxItems": 3
                    },
                    "importance": {
                        "type": "string",
                        "enum": ["low", "medium", "high"]
                    },
                    "explicit_visual_details": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "weather": {
                        "type": "string"
                    },
                    "weather_source": {
                        "type": "string",
                        "enum": [
                            "explicit",
                            "inferred",
                            "default",
                            "user_customized"
                        ]
                    },
                    "atmosphere": {
                        "type": "string"
                    },
                    "character_expressions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "character": {
                                    "type": "string"
                                },
                                "expression": {
                                    "type": "string"
                                },
                                "source": {
                                    "type": "string",
                                    "enum": [
                                        "explicit",
                                        "inferred",
                                        "default",
                                        "user_customized"
                                    ]
                                }
                            },
                            "required": [
                                "character",
                                "expression",
                                "source"
                            ],
                            "additionalProperties": False
                        }
                    }
                },
                "required": [
                    "event",
                    "characters",
                    "location",
                    "location_source",
                    "time_of_day",
                    "time_source",
                    "emotions",
                    "importance",
                    "explicit_visual_details",
                    "weather",
                    "weather_source",
                    "atmosphere",
                    "character_expressions"
                ],
                "additionalProperties": False
            }
        },
        "emotional_arc": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": [
        "events",
        "emotional_arc"
    ],
    "additionalProperties":False
}

relive_instructions = """
You are the story-understanding engine for Relive.

Analyze the user's journal entry while preserving the meaning of their memory.

Identify events in chronological order.

For each event:
- Identify the characters involved.
- Always refer to the person writing the journal as "user" in the character
- Preserve explicit details from the journal.
- Infer location, time, weather, and expressions only when the context reasonably supports it.
- Do not invent vague placeholder locations such as "exam location" or "near the exam location". If a specific place or place type cannot be reasonably inferred, use "unspecified" with source "default".
- Do not invent vague plaeholder locations such as "exam location" or "near the exam location". If a specific place or place type cannot be reasonably inferred, use "unspecified" with source "default".
- Choose 1 to 3 nuanced emotions.
- Rate importance as low, medium, or high based on emotional significance, narrative impact, user emphasis, and whether the moment is important to the story.
- Describe the atmosphere of the scene.
- Do not invent major events or facts that the user did not provide.

Use the source fields accurately:
- explicit = directly stated by the user
- inferred = reasonably derived from context
- default = there is not enough information, so a neutral fallback is used
- user_customized = intentionally choosen or changed by the user

Finally, describe the overall emotional arc of the journal entry in chronological order. 
"""

relive_input = [
    {
        "role": "system",
        "content": relive_instructions
    },
    {
        "role":"user",
        "content": journal_entry
    }
]

response = client.responses.create(
    model = "gpt-5.6-terra",
    input=relive_input,
    text={
        "format":{
            "type": "json_schema",
            "name": "relive_analysis",
            "schema": relive_schema,
            "strict": True
        }
    }
)
analysis = json.loads(response.output_text)
print("\nANALYSIS:")
print(json.dumps(analysis, indent=2, ensure_ascii=False))

with open("analysis.json", "w") as file:
    json.dump(analysis, file, indent=2, ensure_ascii=False)

events = analysis["events"]


selected_events = []

for event in events:
    if event["importance"] in ["high", "medium"]:
        selected_events.append(event)

if len(selected_events) < 2:
    for event in events:
        if event not in selected_events:
            selected_events.append(event)

        if len(selected_events) == 2:
            break
    
selected_events = selected_events[:4]



selected_events_json = json.dumps(selected_events)

storyboard_schema = {
    "type": "object",
    "properties":{
        "scenes": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "scene_number": {
                        "type": "integer"
                    },
                    "event": {
                        "type": "string"
                    },
                    "visual_description": {
                        "type": "string"
                    },
                    "characters": {
                        "type": "array",
                        "items":{
                            "type": "string"
                        }
                    },
                    "location":{
                        "type": "string"
                    },
                    "time_of_day":{
                        "type": "string",
                        "enum":[
                            "morning",
                            "afternoon",
                            "evening",
                            "night",
                            "unspecified"
                        ]
                        },
                        "atmosphere":{
                            "type":"string"
                        },
                        "shot_type":{
                            "type": "string"
                        },
                        "camera_motion":{
                            "type":"string"
                        },
                        "duration_seconds":{
                            "type":"integer"
                        }
                    },
                    "required":[
                        "scene_number",
                        "event",
                        "visual_description",
                        "characters",
                        "location",
                        "time_of_day",
                        "atmosphere",
                        "shot_type",
                        "camera_motion",
                        "duration_seconds"
                    ],
                    "additionalProperties": False
                }
            }
        },
        "required": [
            "scenes"
        ],
        "additionalProperties": False
    }

storyboard_instructions = """
You are the storyboard planner for Relive

Convert the selected memory events into a short cinematic storyboard.

For each selected event:
- Create one storyboard scene.
- Preserve the meaning of the original event/
- Do not invent major facts that were not present in the analysis.
- Make the visual_description describe what should actually be visible on screen.
- Use the characters, location, time of day, and atmosphere from the event.
- Choose a shot_type that fits the emotional purpose of the scene.
- Choose a simple cinematic camera_motion.
- Keep each scene between 4 and 8 seconds.
- Keep scenes in chronological order.
"""

storyboard_input = [
    {
        "role":"system",
        "content": storyboard_instructions
    },
    {
        "role": "user",
        "content": selected_events_json
    }
]

storyboard_response = client.responses.create(
    model = "gpt-5.6-terra",
    input = storyboard_input,
    text={
        "format":{
            "type":"json_schema",
            "name": "relive_storyboard",
            "schema": storyboard_schema,
            "strict": True
        }
    }
)

storyboard = json.loads(storyboard_response.output_text)

scenes = storyboard["scenes"]
visual_prompts = []
image_prompts = []

for scene in scenes:
    prompt = f"""
Create a cinematic scene showing: {scene["visual_description"]}

Characters: {", ".join(scene["characters"])}
Location: {scene["location"]}
Time of day: {scene["time_of_day"]}
Atmosphere: {scene["atmosphere"]}
Shot type: {scene["shot_type"]}
Camera motion: {scene["camera_motion"]}
"""

    visual_prompts.append(prompt)

    location_text = scene["location"]

    if location_text == "unspecified":
        location_text = "a simple neutral background with no distinctive location-specific details"

    if scene["time_of_day"] == "unspecified":
        lighting_text = "soft neutral natural lighting"
    else:
        lighting_text = f"{scene['time_of_day']} lighting"

    image_prompt = f"""
Create a cinematic realistic image showing: {scene["visual_description"]}

Characters: {", ".join(scene["characters"])}
Setting: {location_text}
Lighting: {lighting_text}
Atmosphere: {scene["atmosphere"]}
Framing: {scene["shot_type"]}

Style: cinematic, realistic, emotionally expressive, natural-looking, visually cohesive, and consistent character appearance across scenes.
"""

    image_prompts.append(image_prompt)

print("\nIMAGE PROMPTS:")

for image_prompt in image_prompts:
    print(image_prompt)
    
print("\nVISUAL PROMPTS:")

for prompt in visual_prompts:
    print(prompt)

print("\nSTORYBOARD:")
print(json.dumps(storyboard, indent=2, ensure_ascii=False))

with open("storyboard.json", "w") as file:
    json.dump(storyboard, file, indent=2, ensure_ascii=False)

