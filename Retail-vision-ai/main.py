import cv2
from detection.yolo_detector import YoloDetector
from tracking.deep_sort_tracker import DeepSortTracker # Verifique se este nome bate com seu arquivo
from analytics.people_counter import PeopleCounter

def rodar_loja():
    cap = cv2.VideoCapture(0)
    detector = YoloDetector()
    tracker = DeepSortTracker()
    counter = PeopleCounter(line_y=0.6) # Linha a 60% da altura da tela

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break

        # 1. Detecção
        detections = detector.detect_objects(frame)
        
        # 2. Tracking (Passa as detecções para o DeepSORT)
        tracks = tracker.update(detections, frame)

        # 3. Contagem
        counter.update(tracks, frame.shape[0])
        
        # 4. Visualização
        for track in tracks:
            if track.is_confirmed():
                bbox = track.to_tlbr()
                cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (255,0,0), 2)
                cv2.putText(frame, f"ID: {track.track_id}", (int(bbox[0]), int(bbox[1]-10)), 0, 0.6, (255,255,255), 2)

        counter.draw_ui(frame)
        cv2.imshow("FullStore AI - Analytics", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    rodar_loja()