from ultralytics import YOLO

class YoloDetector:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)

    def detect_objects(self, frame):
        # conf=0.5 para evitar falsos positivos, classes=0 para detectar apenas PESSOAS
        results = self.model(frame, classes=0, conf=0.5, verbose=False)
        detections = []
        
        for r in results[0].boxes:
            x1, y1, x2, y2 = r.xyxy[0].tolist()
            conf = float(r.conf[0])
            cls = int(r.cls[0])
            detections.append({
                "box": [int(x1), int(y1), int(x2), int(y2)],
                "confidence": conf,
                "class_id": cls
            })
        return detections