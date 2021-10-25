

def questionable():
    # Choregraphe bezier export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("LShoulderPitch")
    times.append([0, 0.2, 0.4, 0.6, 0.8, 1])
    keys.append([[0.6], [0.5], [0.6], [0.5], [0.6], [0.5]])

    names.append("LShoulderRoll")
    times.append([0, 1])
    keys.append([[0.3], [0.3]])

    names.append("LElbowYaw")
    times.append([0, 1])
    keys.append([[0.5], [0.5]])

    names.append("LElbowRoll")
    times.append([0, 1])
    keys.append([[-1], [-1]])

    return names, times, keys

