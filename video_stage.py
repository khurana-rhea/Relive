from moviepy import ImageClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips, vfx
import json

with open("storyboard.json", "r") as file:
    storyboard = json.load(file)

scenes = storyboard["scenes"]

scene_1_duration = scenes[0]["duration_seconds"]

base_clip_1 = ImageClip("scene_1.png").with_duration(scene_1_duration)

zoomed_clip_1 = base_clip_1.resized(
    lambda t: 1 + 0.08 * (t/scene_1_duration)   
).with_position("center")

clip_1 = CompositeVideoClip(
    [zoomed_clip_1],
    size=base_clip_1.size
).with_duration(scene_1_duration)

scene_2_duration = scenes[1]["duration_seconds"]
base_clip_2 = ImageClip("scene_2.png").with_duration(scene_2_duration)

moving_clip_2 = base_clip_2.resized(1.06).with_position(
    lambda t:(
        -40 * (t/ scene_2_duration),
        "center"
    )
)

clip_2 = CompositeVideoClip(
    [moving_clip_2],
    size = base_clip_2.size
).with_duration(scene_2_duration)

clip_2 = clip_2.with_effects([vfx.CrossFadeIn(0.6)])

final_video = concatenate_videoclips(
    [clip_1, clip_2],
    method = "compose"
    )

music = AudioFileClip("dreamy_ambient.mp3")
music = music.subclipped(0, final_video.duration)
music = music.with_volume_scaled(0.25)

final_video = final_video.with_audio(music)

final_video.write_videofile(
    "relive_memory.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac"
)
     

