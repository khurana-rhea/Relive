# Relive

Relive is an AI-powered journalling application that transforms written memories into visuals. It is designed to capture individual's experience and for them to relive their memorable moments in a short cinematic video montage. 

## How It Works

Relive turns a journal entry into a cinematic memory through a multi-stage AI pipeline:

1. User writes a journal entry.
2. An LLM analyzes the entry and extracts events, characters, emotions, locations, and other visual details.
3. Relive selects the most important moments from the entry.
4. A storyboard is generated for the selected scenes.
5. Image prompts are created and used to generate cinematic scene images.
6. MoviePy adds camera motion, transitions, timing, and background music.
7. The final memory is exported as an MP4 video. 

## Tech Stack

- Python: backend piperline and orchestration
- OpenAI API: journal analysis, structured scene planning, and image generation
- JSON: structured intermediate data for analysis and storyboards.
- MoviePy: video assembly, camera motion, transitions, and audio
- FFmpeg: video and audio encoding

## Project Structure

- 'main.py' - analyzes journal entries, selects important events, and generates structured storyboards
- 'visual_stage.py' - converts storyboard scenes into image prompts and generates scene images
- 'video_stage.py' - turns the generated images into a cinematic video with motion, transitions, and music
- 'analysis.json' - stores the structured journal analysis
- 'storyboard.json' - stores the generated scene plan
- 'scene_1.png', 'scene_2.png' - generated visual scenes
- 'relive_memory.mp4' - final generated memory video

## Current MVP

The current Relive prototype can:

- Accept a written journal entry
- Analyze the entry using an LLM
- Extract events, characters, emotions, locations, and visual details
- Select the most important moments
- Generate a structured storyboard
- Generate cinematic scene images
- Add camera motion and transitions
- Add background music
- Export the final memory as an MP4 video

## Future Development

Relive is still evolving. Future work will focus on:

- stronger personalization
- improved character and scene consistency
- more user customization
- richer audio and visual generation
- more context-aware memories
- a polished interactive experience

## Status

Relive is currently in active development.

The MVP successfully converts a written journal entry into a cinematic memory video using AI-generated analysis, storyboarding, images, motion, transitions, and background audio.

Future development will focus on personalization, user-facing customization, stronger character consistency, location-aware memory generation, and a full interactive web application. 

