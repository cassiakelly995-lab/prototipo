from ultralytics import YOLO

class Detector:
    def __init__(self, model_path, confidence=0.35, classes=None, device="cpu"):
        self.model = YOLO(model_path)
        self.confidence = float(confidence)
        self.classes = classes
        self.device = device

    def detect(self, frame):
        result = self.model.predict(
            source=frame,
            conf=self.confidence,
            classes=self.classes,
            device=self.device,
            verbose=False
        )[0]

        detections = []
        if result.boxes is None:
            return detections

        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            detections.append({
                "box": (x1, y1, x2, y2),
                "confidence": conf,
                "class_id": cls_id,
                "center": ((x1+x2)//2, (y1+y2)//2),
                # Visual estimate only. For a custom game model this can
                # be replaced by a dedicated head/keypoint prediction.
                "aim_point": ((x1+x2)//2, y1 + int((y2-y1)*0.20))
            })
        return detections
