"""
This module moves target(path) to the trash and creates info file
"""
import os


from mrm.output_tools import FunctionsCodes, PerformanceCodes


def remove(path, trash_path, info_path, dry):
    """
    This function moves target(path) to the trash and creates info file
    """
    target_path = os.path.abspath(str(path))

    if dry is True:
        print(path + " would be moved to trash ")
    else:
        try:
            trash = os.path.join(trash_path, os.path.basename(target_path))
            info = os.path.join(info_path, os.path.basename(target_path))
            if os.path.exists(trash):
                name_index = 1

                while os.path.exists("{}_nfm_{}".format(trash, name_index)):
                    name_index += 1

                trash += "_nfm_{}".format(name_index)
                info += "_nfm_{}".format(name_index)

            os.rename(target_path, target_path)
            os.rename(target_path, trash)

            with open(info, 'w') as file:
                file.write(target_path)

            return path, FunctionsCodes.REMOVE, PerformanceCodes.GOOD
        except OSError:
            return path, FunctionsCodes.REMOVE, PerformanceCodes.NO_FILE
