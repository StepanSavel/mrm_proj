"""
This module removes files by policy if you confirm
"""
import os
import time

from mrm_proj.mrm.clear_trash import empty_trash
from mrm_proj.mrm.output_tools import PerformanceCodes, FunctionsCodes
from mrm_proj.mrm.read_config import Policy


def trash_policy(trash_path, info_path, policy, day, size):
    """
    This function removes files by policy if you confirm
    """
    try:
        if policy is Policy.DAY:
            SEC_IN_DAY = 86400
            days_in_sec = day * SEC_IN_DAY
            current_time = time.time()
            files_list = os.listdir(trash_path)

            if files_list:
                for file in files_list:
                    file_path = os.path.join(trash_path, file)
                    remove_time = os.path.getmtime(file_path)

                    if current_time - remove_time > days_in_sec:
                        print ("i'll delete this: " + file_path + "by time policy")
                        confirm = True
                        if confirm is True:
                            os.remove(file_path)
                            return policy, FunctionsCodes.TRASH_POLICY, PerformanceCodes.GOOD
                        else:
                            return policy, FunctionsCodes.TRASH_POLICY, PerformanceCodes.NO_FILE

                    return policy, FunctionsCodes.TRASH_POLICY, PerformanceCodes.NO_FILE
            else:
                return policy, FunctionsCodes.TRASH_POLICY, PerformanceCodes.NO_FILE
        elif policy is Policy.SIZE:
            if get_size(trash_path) + get_size(info_path) >= size:
                print ("i'll clear the trash")
                empty_trash(trash_path, info_path, dry=False)
            return policy, FunctionsCodes.TRASH_POLICY, PerformanceCodes.GOOD
    except OSError:
        return policy, FunctionsCodes.TRASH_POLICY, PerformanceCodes.UNKNOWN_ERROR


def get_size(path):
    size = 0
    for dir_path, dirs, files in os.walk(path):
        for f in files:
            file_path = os.path.join(dir_path, f)
            size += os.path.getsize(file_path)
    return size
