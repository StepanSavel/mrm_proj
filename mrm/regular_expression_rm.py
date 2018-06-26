"""
Removes files by expression, it use glob to find matches and create list of targets WIP!
"""
import os
import re
from multiprocessing import Process

from mrm_proj.mrm.output_tools import PerformanceCodes, FunctionsCodes

from mrm_proj.mrm.remove import remove


def regular_expression_rm(subtree, reg, trash_path, info_path):
    """
        Removes files by expression, it use glob to find matches and create list of targets WIP!
    """
    files_counter = 0
    dry = False
    for root, dirs, files in os.walk(subtree):
        for file in filter(lambda x: re.match(reg, x), files):
            files_counter += 1
            path = os.path.join(root, file)
            proc = Process(target=remove, args=(path, trash_path, info_path, dry))
            proc.start()
    if not files_counter:
        return reg, FunctionsCodes.REGULAR_EXPRESSION, PerformanceCodes.NO_FILE
    else:
        return reg, FunctionsCodes.REGULAR_EXPRESSION, PerformanceCodes.GOOD
