
def is64Bit():
    import platform

    int64 = False
    for bit in platform.architecture():
        if '64' in bit:
            int64 = True

    return int64