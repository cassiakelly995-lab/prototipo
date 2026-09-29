class SimpleTracker:
    # Lightweight visual identity assignment based on nearest centers.
    # It does not interact with the game process.
    def __init__(self, max_distance=100):
        self.max_distance = max_distance
        self.previous = {}
        self.next_id = 1

    def update(self, detections):
        import math
        new = {}
        used = set()

        for det in detections:
            cx, cy = det["center"]
            best_id, best_d = None, float("inf")
            for tid, (px, py) in self.previous.items():
                if tid in used:
                    continue
                d = math.hypot(cx-px, cy-py)
                if d < best_d and d <= self.max_distance:
                    best_id, best_d = tid, d

            if best_id is None:
                best_id = self.next_id
                self.next_id += 1

            det["track_id"] = best_id
            new[best_id] = (cx, cy)
            used.add(best_id)

        self.previous = new
        return detections
