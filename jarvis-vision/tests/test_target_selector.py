from src.target_selector import select_nearest, target_metrics

def test_nearest():
    shape = (720, 1280, 3)
    detections = [
        {"aim_point": (100,100)},
        {"aim_point": (650,370)}
    ]
    target = select_nearest(detections, shape)
    assert target["aim_point"] == (650,370)
    m = target_metrics(target, shape)
    assert m["dx"] == 10
    assert m["dy"] == 10
