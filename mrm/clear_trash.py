"""
this module will clear trash. It removes all trash files and all info files
"""
import os
import shutil
from mrm_proj.mrm.output_tools import FunctionsCodes, PerformanceCodes


def empty_trash(trash_path, info_path, dry):
    """this function will clear trash. It removes all trash files and all info files"""
    try:
        if dry is True:
            print("trash would by cleared")
        else:
            for file in os.listdir(trash_path):
                trash = os.path.join(trash_path, file)
                if os.path.isdir(trash):
                    shutil.rmtree(trash)
                else:
                    os.remove(trash)

            for info in os.listdir(info_path):
                os.remove(os.path.join(info_path, info))

            return trash_path, FunctionsCodes.CLEAR_TRASH, PerformanceCodes.GOOD

    except OSError:
        return trash_path, FunctionsCodes.CLEAR_TRASH, PerformanceCodes.NO_FILE
