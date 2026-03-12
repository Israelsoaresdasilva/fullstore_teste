import cv2
from ultralytics import YOLO

print("Iniciando FullStore AI...")

# 1. Carrega o modelo (YOLOv8 nano - leve e rápido)
model = YOLO('yolov8n.pt')

# 2. Abre a câmera (0 é a webcam padrão)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro: Câmera não encontrada!")
else:
    print("Câmera aberta. Pressione 'q' na janela de vídeo para sair.")
    while True:
        ret, frame = cap.read()
        if not ret: 
            print("Falha ao capturar frame.")
            break

        # 3. Faz a detecção de pessoas (classes=0)
        results = model(frame, classes=0, conf=0.5, verbose=False)
        
        # 4. Desenha os resultados no frame
        annotated_frame = results[0].plot()
        
        # 5. Mostra o resultado na janela
        cv2.imshow("FullStore AI - TESTE", annotated_frame)

        # Sai se apertar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Sistema encerrado.")
