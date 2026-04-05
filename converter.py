import subprocess

class VideoConverter:
    def __init__(self):
        pass

    def convert_video(self, input_path, output_path):
        command = [
            "ffmpeg",
            "-y",
            "-i", input_path,
            "-c:v", "libx264",
            "-preset", "faster",
            "-threads", "2",
            "-profile:v", "baseline",
            "-level", "3.0",
            "-pix_fmt", "yuv420p",
            "-vf", "scale='min(1280,iw)':-2",
            "-c:a", "aac",
            "-ac", "2",
            "-b:a", "128k",
            "-movflags", "+faststart",
            output_path
        ]

        process = subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        process.wait()
        return process.returncode == 0