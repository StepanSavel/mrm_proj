"""
This module contains identification codes of functions and codes of performance, works with
this codes ,silent mode and logging
"""
import logging

from mrm_proj.mrm import Policy


class FunctionsCodes(object):
    """This class contains codes of functions"""
    REMOVE = 1
    RECOVER = 2
    CLEAR_TRASH = 3
    REGULAR_EXPRESSION = 4
    TRASH_POLICY = 5


class PerformanceCodes(object):
    """This class contains codes of performance"""
    GOOD = 0
    NO_FILE = 1
    UNKNOWN_ERROR = 2


def logging_and_silent(target, function_code, performance_code, silent):
    """This function processes codes of performance and functions"""
    if function_code == FunctionsCodes.REMOVE:
        if performance_code == PerformanceCodes.GOOD:
            if silent is not True:
                print("file or dir " + target + " removed")
            logging.info(target + " : removed")
            return performance_code
        elif performance_code == PerformanceCodes.NO_FILE:
            if silent is not True:
                print("file or dir " + target + " doesn't exist")
            logging.error('there is no file ' + target)
            return performance_code

    elif function_code == FunctionsCodes.RECOVER:
        if performance_code == PerformanceCodes.GOOD:
            if silent is not True:
                print("file or dir " + target + " recovered")
            logging.info(target + " : recovered")
            return performance_code
        elif performance_code == PerformanceCodes.NO_FILE:
            if silent is not True:
                print("file or dir " + target + " recovered")
            logging.error('there is no file ' + target + 'in trash')
            return performance_code

    elif function_code == FunctionsCodes.CLEAR_TRASH:
        if performance_code == PerformanceCodes.GOOD:
            if silent is not True:
                print("trash is clear")
            logging.info('trash is cleared')
            return performance_code
        elif performance_code == PerformanceCodes.NO_FILE:
            if silent is not True:
                print("No files in trash")
            logging.error('empty_trash : Error')
            return performance_code

    elif function_code == FunctionsCodes.REGULAR_EXPRESSION:
        if performance_code == PerformanceCodes.GOOD:
            if silent is not True:
                print("Files were deleted by regular expression: " + target)
            logging.info("Files were deleted by regular expression" + target)
            return performance_code
        elif performance_code == PerformanceCodes.NO_FILE:
            if silent is not True:
                print("No matching expression " + target + " files")
            logging.error("There are no files matching expression: " + target)
            return performance_code

    elif function_code == FunctionsCodes.TRASH_POLICY:
        if performance_code == PerformanceCodes.GOOD:
            if silent is not True:
                print("files was deleted by " + str(target) + " policy")
            if target == Policy.SIZE:
                logging.info('trash cleared by policy: size')
            elif target == Policy.DAY:
                logging.info('files deleted by policy: time')
            return performance_code
        elif performance_code == PerformanceCodes.UNKNOWN_ERROR:
            if silent is not True:
                print("unknown error in trash policy")
            logging.error('unknown error in trash policy')
            return performance_code
        elif performance_code == PerformanceCodes.NO_FILE:
            if silent is not True:
                print("no files deleted by trash policy")
            logging.info('no files deleted by trash policy')
            return performance_code
