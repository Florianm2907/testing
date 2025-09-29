import os
import subprocess

# Set your source and output folder here
source_folder = "F:/Filme"
output_folder = "F:/Filmeneu"

# Supported input extensions
video_exts = {'.avi', '.mp4', '.mov', '.flv', '.wmv', '.m2ts'}

def convert_video(input_path, output_path):
    cmd = [
        "ffmpeg", "-y",
        "-hwaccel", "auto",
        "-i", input_path,
        "-map", "0",
        "-c:v", "av1_nvenc",  # << hardware encoder
        "-preset", "p7",
        "-cq", "26",                # Options: default, slow, p1–p7 (depends on encoder)
        # "-b:v", "8M",          # Target bitrate, adjust as needed
        # "-maxrate", "50M",
        # "-bufsize", "10M",
        "-c:a", "aac",
        "-c:s", "copy",
        output_path
    ]
    try:
        subprocess.check_output(cmd)
    except subprocess.CalledProcessError as e:
        print(e)


def process_folder():
    for root, _, files in os.walk(source_folder):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in video_exts:
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, source_folder)
                output_dir = os.path.join(output_folder, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                output_filename = os.path.splitext(file)[0] + ".mkv"
                output_path = os.path.join(output_dir, output_filename)

                print(f"Converting: {input_path} -> {output_path}")
                convert_video(input_path, output_path)
process_folder()