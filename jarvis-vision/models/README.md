# Models

By default, `config.yaml` uses `yolov8n.pt`, which Ultralytics downloads
automatically on first execution. That generic COCO model detects the `person`
class and is useful for validating the pipeline.

For a domain-specific authorized CV demonstration, place your own trained
Ultralytics-compatible `.pt` model here and change:

```yaml
detector:
  model: "models/your_model.pt"
```

Model weights are intentionally excluded from Git with `.gitignore`.
