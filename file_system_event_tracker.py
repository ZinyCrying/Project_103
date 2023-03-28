import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "D:/projects/Project_102"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")

    def on_deleted(self, event):
        print(f"Oops! {event.src_path} has been deleted")

    def on_moved(self, event):
        print(f"Hey, {event.src_path} has been moved")

    def on_modified(self, event):
        print(f"hey, {event.src_path} has been modified")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive = True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running... ")
except:
    if(KeyboardInterrupt):
        print("Stopped")
        observer.stop()