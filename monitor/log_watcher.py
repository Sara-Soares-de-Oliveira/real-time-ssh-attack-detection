from __future__ import annotations
import time
import os 


def tail_lines(file_path: str): 
 try:
    with open(file_path, "r") as file:
        file.seek(0, os.SEEK_END)
        
  
        while True: 
            line = file.readline()
            if line: 
                yield line
            else: 
                time.sleep(0.5)
 except(FileNotFoundError, PermissionError, OSError) as e:
     print(f"Error: {e}")
        
