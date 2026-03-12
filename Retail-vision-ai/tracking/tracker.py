class Tracker:

    def __init__(self):
        self.object_id = 0
        self.objects = {}

    def update(self, detections):

        tracked_objects = []

        for detection in detections:

            self.object_id += 1

            tracked_objects.append({
                "id": self.object_id,
                "box": detection["box"]
            })

        return tracked_objects