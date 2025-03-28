import os
import shutil


def rename_part_to_file_name(source_dir, file_name):
    file_path = os.path.join(source_dir, file_name)

    for file in os.listdir(source_dir):
        if file.startswith("part-") and file.endswith(".csv"):
            shutil.move(os.path.join(source_dir, file), file_path)
        else:
            os.remove(os.path.join(source_dir, file))
