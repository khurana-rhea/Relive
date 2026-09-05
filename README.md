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

## Future Improvements

Planned improvements for Relive include:

- 'User Profiles & Saved Memories': allow users to save, revisit, and organize past Relive memories
- 'My People / Saved Characters': save recurring people such as friends, family members, and pets for more consistent appearences across memories.
- 'Persistent User Avatar': maintain a consistent visual representation of the user across generated scenes
- 'Manifestation/Imagine Mode': allow users to visualize future goals, dreams, and imagined experiences in addition to past journal entries 
- 'Enhanced Audio Experience' - automatically select music based on emotion of the journal entry and allow users to customize the soundtrack
- 'AI Voice Narration' - optionally turn parts of the journal entry into voice-over narration
- 'Improved Character Consistency' - maintain stronger visual consistency for people across multiple generated scenes
- 'Scene Regenaration & Editing; - allow users to regenerate or modify individual scenes without recreating the entire memory
- 'Longer Multi-Scene Memories' - generate richer cinematic stories from longer journal entries
- 'Memory Timeline' - orgnaize generated memories chronologically so users can look back through their life visually
- 'Photo-Based Personalization': allow users to upload their own photo for more accurate self-representation in generated memories
- 'Saved People Library' - let users save recurring people such as friends, family members, and pets for more personalization and consistent memory generation
- 'Location-Aware Memories': optionally user user location data to make generated scenes more contexually accurate
- 'Conext-Aware Memory Generation': incorporate real-world details such as location, time, and weather to create more realistic memory montages
- 'Full Web Application' - build and deploy an interactive frontend for writing, generating, viewing, and managing memories

## Status

Relive is currently in active development.

The MVP successfully converts a written journal entry into a cinematic memory video using AI-generated analysis, storyboarding, images, motion, transitions, and background audio.

Future development will focus on personalization, user-facing customization, stronger character consistency, location-aware memory generation, and a full interactive web application. 