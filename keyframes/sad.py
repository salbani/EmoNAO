

def sad():
    # Choregraphe bezier export in Python.
    names = list()
    times = list()
    keys = list()

    timess = [0, 0.5, 0.8, 1.1, 1.4, 1.7, 2.0, 2.3, 2.6, 2.9, 3.4]

    names.append("HeadPitch")
    times.append(timess)
    keys.append([[0.0], [0.5], [0.5], [0.5], [0.5], [0.5], [0.5], [0.5], [0.5], [0.5], [0.0]])

    names.append("HeadYaw")
    times.append(timess)
    keys.append([[0.0], [0.0], [0.3], [0.0], [-0.3], [0.0], [0.3], [0.0], [-0.3], [0.0], [0.0]])

    names.append("LShoulderPitch")
    times.append([0, 0.5, 1.0])
    keys.append([[1.0], [1.0], [1.0]])

    names.append("LShoulderRoll")
    times.append([0, 0.5, 1.0])
    keys.append([[0.4], [0.4], [0.4]])

    names.append("LElbowYaw")
    times.append([0, 1, 2.6, 3.4])
    keys.append([[0.0], [0.8], [0.8], [0.0]])

    names.append("LElbowRoll")
    times.append([0, 1, 2.6, 3.4])
    keys.append([[-0.4], [-1.0], [-1.0], [-0.4]])

    names.append("RShoulderPitch")
    times.append([0, 0.5, 1.0])
    keys.append([[1.0], [1.0], [1.0]])

    names.append("RShoulderRoll")
    times.append([0, 0.5, 1.0])
    keys.append([[-0.4], [-0.4], [-0.4]])

    names.append("RElbowYaw")
    times.append([0, 1, 2.6, 3.4])
    keys.append([[0.0], [-0.8], [-0.8], [0.0]])

    names.append("RElbowRoll")
    times.append([0, 1, 2.6, 3.4])
    keys.append([[0.4], [1.0], [1.0], [0.4]])
    return names, times, keys
