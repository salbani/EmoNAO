

def handsUp():
    # Choregraphe bezier export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("LShoulderPitch")
    times.append([0, 0.5, 1.0])
    keys.append([[1.0], [0.0], [-1.0]])

    names.append("LShoulderRoll")
    times.append([0, 0.5, 1.0])
    keys.append([[0.4], [0.35], [0.3]])

    names.append("LElbowYaw")
    times.append([0, 0.5, 1.0])
    keys.append([[0.0], [-0.4], [-0.8]])

    names.append("LElbowRoll")
    times.append([0, 0.5, 1.0])
    keys.append([[-0.4], [-7.0], [-1.0]])

    names.append("RShoulderPitch")
    times.append([0, 0.5, 1.0])
    keys.append([[1.0], [0.0], [-1.0]])

    names.append("RShoulderRoll")
    times.append([0, 0.5, 1.0])
    keys.append([[-0.4], [-0.35], [-0.3]])

    names.append("RElbowYaw")
    times.append([0, 0.5, 1.0])
    keys.append([[0.0], [0.4], [0.8]])

    names.append("RElbowRoll")
    times.append([0, 0.5, 1.0])
    keys.append([[0.4], [7.0], [1.0]])

    return names, times, keys
