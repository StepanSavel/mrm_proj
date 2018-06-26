"""
cosmetic tool, is shows deleting progress
"""


def progress(size, new_size):
    """
    cosmetic tool, is shows deleting progress
    """
    prg = float(new_size) / float(size) * 100.0
    bar_lenghth = int(25 * new_size // size)
    bar = "*" * bar_lenghth

    print(bar + "-" + str(prg) + "% was removed")
