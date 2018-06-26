"""
This module recovers target from trash path to its place
"""
import os
from mrm.output_tools import FunctionsCodes, PerformanceCodes


def recover(target, trash_path, info_path, dry):
    """
    This function recovers target from trash path to its place
    """

    try:
        trash = os.path.join(trash_path, target)
        info = os.path.join(info_path, target)

        with open(info, "r") as file:
            recover_path = file.read()

        if dry is True:
            print(trash + " would be recovered")
        else:
            os.rename(trash, recover_path)
            os.remove(info)

        return target, FunctionsCodes.RECOVER, PerformanceCodes.GOOD
    except OSError:
        return target, FunctionsCodes.RECOVER, PerformanceCodes.NO_FILE
