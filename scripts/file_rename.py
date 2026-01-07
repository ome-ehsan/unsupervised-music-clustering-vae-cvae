import os
def rename_files():

    folder_path = r"E:\cse425_project\fma\converted"

    if not os.path.exists(folder_path):
        print(f"Error: The directory {folder_path} does not exist.")
        return

    # Counter to track changes
    count = 0


    for filename in os.listdir(folder_path):
        # processing wavs
        if filename.endswith(".wav"):
        
            name_body, extension = os.path.splitext(filename)
            parts = name_body.split('_')
            if len(parts) >= 2:
            
                second_portion = parts[1]
                new_name_body = second_portion.lstrip('0')
                if new_name_body == "":
                    new_name_body = "0"
                
                # "102" + ".wav" -> "102.wav"
                new_filename = new_name_body + extension
                
                # full paths
                old_file_path = os.path.join(folder_path, filename)
                new_file_path = os.path.join(folder_path, new_filename)
                
                # Renaming
                try:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                    count += 1
                except FileExistsError:
                    print(f"Skipped: {new_filename} already exists.")
                except Exception as e:
                    print(f"Error renaming {filename}: {e}")

    print("------------------------------------------------")
    print(f"Process complete. {count} files renamed.")

if __name__ == "__main__":
    rename_files()
