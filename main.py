
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from imageProcess import process_image

# Define the directory to monitor and the directory to save processed images
watched_folder = "/Users/munirdinjadikar/Documents/python_projects/AutoImageProcess/inputImage"
output_folder = "/Users/munirdinjadikar/Documents/python_projects/AutoImageProcess/outputImage"

class ImageProcessingHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith((".png", ".jpg", ".jpeg")):
            process_image(event.src_path, output_folder)

def main():
    event_handler = ImageProcessingHandler()
    observer = Observer()
    observer.schedule(event_handler, path=watched_folder, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    main()