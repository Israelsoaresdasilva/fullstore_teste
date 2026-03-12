import cv2

class PeopleCounter:
    def __init__(self, line_y=0.5):
        self.line_y_ratio = line_y  # Posição da linha (0.5 = meio da tela)
        self.entries = 0
        self.exits = 0
        self.track_history = {} # Armazena a posição anterior de cada ID

    def update(self, tracks, frame_height):
        line_y = int(self.line_y_ratio * frame_height)
        
        for track in tracks:
            if not track.is_confirmed():
                continue
            
            track_id = track.track_id
            # Pega o centro da Bounding Box (pés da pessoa)
            bbox = track.to_tlbr()
            current_y = int(bbox[3]) # Coordenada Y do pé da pessoa

            if track_id in self.track_history:
                previous_y = self.track_history[track_id]

                # Lógica de cruzamento
                if previous_y < line_y and current_y >= line_y:
                    self.entries += 1
                    print(f"ID {track_id} ENTROU. Total: {self.entries}")
                elif previous_y > line_y and current_y <= line_y:
                    self.exits += 1
                    print(f"ID {track_id} SAIU. Total: {self.exits}")

            self.track_history[track_id] = current_y

    def draw_ui(self, frame):
        h, w, _ = frame.shape
        line_y = int(self.line_y_ratio * h)
        
        # Desenha a linha virtual
        cv2.line(frame, (0, line_y), (w, line_y), (0, 255, 255), 3)
        
        # Painel de contagem
        cv2.putText(frame, f"Entradas: {self.entries}", (20, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Saidas: {self.exits}", (20, 90), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)