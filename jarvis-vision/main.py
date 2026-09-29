import time
import cv2
import yaml

from src.capture import ScreenCapture
from src.detector import Detector
from src.tracker import SimpleTracker
from src.target_selector import select_nearest, target_metrics
from src.overlay import draw_overlay

def main():
    with open("config.yaml", "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    cap = ScreenCapture(cfg["capture"]["monitor"])
    detector = Detector(
        cfg["detector"]["model"],
        cfg["detector"]["confidence"],
        cfg["detector"].get("classes"),
        cfg["detector"].get("device", "cpu")
    )
    tracker = SimpleTracker()
    window = cfg["display"]["window_name"]

    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window, cfg["display"]["width"], cfg["display"]["height"])

    last = time.perf_counter()
    smooth_fps = 0.0

    try:
        while True:
            start = time.perf_counter()
            frame = cap.grab()
            detections = detector.detect(frame)
            detections = tracker.update(detections)

            target = select_nearest(detections, frame.shape)
            metrics = target_metrics(target, frame.shape)

            now = time.perf_counter()
            instant_fps = 1.0 / max(now-last, 1e-6)
            last = now
            smooth_fps = instant_fps if smooth_fps == 0 else smooth_fps*0.9 + instant_fps*0.1
            latency = (time.perf_counter()-start)*1000

            frame = draw_overlay(
                frame, detections, target, metrics, smooth_fps, latency
            )
            cv2.imshow(window, frame)

            key = cv2.waitKey(1) & 0xFF
            if key in (27, ord("q")):
                break
    finally:
        cap.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
