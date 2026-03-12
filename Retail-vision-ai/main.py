import cv2
from ultralytics import YOLO

# 1. Carrega o modelo da YOLO
model = YOLO('yolov8n.pt') 

# 2. Inicia a câmera
cap = cv2.VideoCapture(0)

print("Pressione 'q' para fechar a janela.")

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # 3. Detecta apenas PESSOAS (class 0)
        results = model(frame, classes=[0], conf=0.5)

        # 4. Desenha as caixas na tela
        annotated_frame = results[0].plot()

        cv2.imshow("FullStore - Detector de Clientes", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()