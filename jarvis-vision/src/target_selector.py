import math

def select_nearest(detections, frame_shape):
    if not detections:
        return None

    h, w = frame_shape[:2]
    cx, cy = w // 2, h // 2

    def distance(det):
        tx, ty = det["aim_point"]
        return math.hypot(tx-cx, ty-cy)

    return min(detections, key=distance)

def target_metrics(target, frame_shape):
    if target is None:
        return None
    h, w = frame_shape[:2]
    cx, cy = w // 2, h // 2
    tx, ty = target["aim_point"]
    dx, dy = tx-cx, ty-cy
    return {
        "dx": dx,
        "dy": dy,
        "distance": (dx*dx + dy*dy) ** 0.5
    }
