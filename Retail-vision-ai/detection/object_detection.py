class ObjectDetection:

    def __init__(self, detector):
        self.detector = detector

    def detect_objects(self, frame):

        results = self.detector.detect(frame)

        detections = []

        for result in results:
            boxes = result.boxes

            for box in boxes:

                x1, y1, x2, y2 = box.xyxy[0]

                conf = float(box.conf[0])
                cls = int(box.cls[0])

                detections.append({
                    "box": (int(x1), int(y1), int(x2), int(y2)),
                    "confidence": conf,
                    "class_id": cls
                })

        return detections