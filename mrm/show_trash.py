"""
shows last N elements in trash
"""
import os


def show_trash(trash_path, number_of_elem, dry):
    """
    shows last N elements in trash
    """
    if dry is True:
        print("will show last " + number_of_elem + "elements")
    else:
        trash_content = os.listdir(trash_path)[-number_of_elem:]

        return trash_content
