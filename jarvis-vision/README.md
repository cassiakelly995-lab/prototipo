# JARVIS Vision

Real-time computer-vision demonstration for Windows.

JARVIS Vision captures the selected monitor, performs visual object detection
and lightweight tracking, selects the detection nearest the screen crosshair,
and displays CV metrics such as confidence, FPS, latency and pixel offset.

**CV demonstration only:** this project does not move the mouse, fire, inject
code into another process, read game memory, or bypass anti-cheat software.

## Features

- Real-time monitor capture with MSS
- Ultralytics YOLO inference
- Person detection with the default generic model
- Lightweight tracking IDs
- Visual target selection nearest the screen center
- Aim-point and dX/dY/distance visualization
- FPS and inference-pipeline latency
- Continuous execution until Q or Esc is pressed

## Windows installation

Install Python 3.11 or newer. Then open PowerShell in the project directory:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

The first run can download the default Ultralytics model automatically.

Press **Q** or **Esc** to exit.

## Configuration

Edit `config.yaml`.

For NVIDIA acceleration, install a CUDA-compatible PyTorch build and change
`device` from `cpu` to the appropriate CUDA device supported by your setup.

## Important model note

The default YOLO model is a general-purpose person detector. It is included so
the full CV pipeline can be tested immediately, but it is not a specialized
Free Fire character detector.

A reliable domain-specific detector requires an appropriately licensed and
authorized dataset and a model trained for that visual domain. See
`models/README.md`.

## Architecture

```text
Monitor pixels
    |
ScreenCapture
    |
YOLO detector
    |
SimpleTracker
    |
Target selector
    |
Metrics
    |
OpenCV visualization
```

## GitHub

Create an empty repository, then from this folder:

```powershell
git init
git add .
git commit -m "Initial JARVIS Vision CV demo"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

## License

MIT. See `LICENSE`.
