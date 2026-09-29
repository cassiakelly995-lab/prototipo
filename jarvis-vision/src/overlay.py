import cv2

def draw_overlay(frame, detections, target, metrics, fps, latency_ms):
    h, w = frame.shape[:2]
    cx, cy = w // 2, h // 2

    # Crosshair
    cv2.line(frame, (cx-12, cy), (cx+12, cy), (255,255,255), 1)
    cv2.line(frame, (cx, cy-12), (cx, cy+12), (255,255,255), 1)

    for det in detections:
        x1,y1,x2,y2 = det["box"]
        selected = det is target
        thickness = 3 if selected else 1
        cv2.rectangle(frame, (x1,y1), (x2,y2), (255,255,255), thickness)
        ax, ay = det["aim_point"]
        cv2.circle(frame, (ax,ay), 4, (255,255,255), -1)
        label = f'ID {det.get("track_id","?")}  {det["confidence"]:.0%}'
        cv2.putText(frame, label, (x1,max(20,y1-8)),
                    cv2.FONT_HERSHEY_SIMPLEX, .55, (255,255,255), 1, cv2.LINE_AA)

    cv2.rectangle(frame, (15,15), (345,145), (0,0,0), -1)
    cv2.putText(frame, "JARVIS VISION | CV DEMO", (28,42),
                cv2.FONT_HERSHEY_SIMPLEX, .62, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(frame, f"FPS: {fps:5.1f}   LATENCY: {latency_ms:5.1f} ms",
                (28,70), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 1)
    cv2.putText(frame, f"DETECTIONS: {len(detections)}",
                (28,95), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 1)

    if metrics:
        cv2.putText(frame,
            f'dX: {metrics["dx"]:+d}px  dY: {metrics["dy"]:+d}px  D: {metrics["distance"]:.0f}px',
            (28,120), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 1)
    return frame
