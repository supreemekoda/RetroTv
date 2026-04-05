import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

from Build.converter import VideoConverter
from Build.config import Config

class BatchProcessor:
    def __init__(self):
        self.config = Config()
        self.converter = VideoConverter()

    def batch_convert(self, folder_path):
        output_folder = os.path.join(folder_path, "converted_for_tv")
        os.makedirs(output_folder, exist_ok=True)

        files = [
            f for f in os.listdir(folder_path)
            if f.lower().endswith(self.config.VIDEO_EXTENSIONS)
        ]

        if not files:
            print("No video files found.")
            return

        print(f"Found {len(files)} video(s). Converting with {self.config.MAX_WORKERS} workers...\n")

        jobs = {
            os.path.join(folder_path, f): os.path.join(
                output_folder,
                os.path.splitext(f)[0] + "_tv.mp4"
            )
            for f in files
        }

        failed = []

        with ThreadPoolExecutor(max_workers=self.config.MAX_WORKERS) as executor:
            futures = {
                executor.submit(self.converter.convert_video, inp, out): inp
                for inp, out in jobs.items()
            }

            with tqdm(total=len(futures), desc="Converting", unit="file") as bar:
                for future in as_completed(futures):
                    src = futures[future]
                    success = future.result()
                    if not success:
                        failed.append(os.path.basename(src))
                    bar.update(1)

        print("\n✅ Done! Converted files saved in:", output_folder)

        if failed:
            print(f"⚠️ {len(failed)} file(s) failed:")
            for f in failed:
                print(f" - {f}")