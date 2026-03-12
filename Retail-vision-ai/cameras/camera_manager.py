from .camera_stream import CameraStream

class CameraManager:
    def __init__(self):
        self.cameras = {}

    def add_camera(self, camera_id, source):
        cam = CameraStream(source=source, name=camera_id)
        self.cameras[camera_id] = cam.start()
        print(f"[INFO] Câmera {camera_id} inicializada.")

    def get_all_frames(self):
        # Retorna um dicionário {id_da_camera: frame_atual}
        return {id: cam.get_frame() for id, cam in self.cameras.items() if cam.status}

    def stop_all(self):
        for cam in self.cameras.values():
            cam.stop()