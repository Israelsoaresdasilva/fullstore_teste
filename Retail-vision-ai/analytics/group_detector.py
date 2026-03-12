import numpy as np

def detect_groups(tracks):

    groups = []

    for t1 in tracks:
        for t2 in tracks:

            if t1 == t2:
                continue

            dist = np.linalg.norm(
                np.array(t1.center) - np.array(t2.center)
            )

            if dist < 100:
                groups.append((t1.id, t2.id))

    return groups