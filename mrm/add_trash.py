import os


def add_trash(trash_fold):
    trash = os.path.join(trash_fold, "trash")
    info = os.path.join(trash_fold, "info")
    if not os.path.exists(trash_fold):
        os.mkdir(trash_fold)
        os.mkdir(trash)
        os.mkdir(info)
