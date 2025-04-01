### 📄 `README.md`

# Desktop Productivity Tracker

## Overview

The **Desktop Productivity Tracker** is a lightweight Python project that automatically tracks your activity across desktop applications and websites. It runs in the background, detects when you switch between apps or tabs, and logs each session — helping you understand how you spend your time.

This tool was built to give users control over their daily digital behavior and improve time management. Whether you're switching between work apps or spending a little too long on YouTube, this script helps you visualize your habits and regain focus.

## Motivation

I built this project because I was struggling with time management. I would often jump between apps, get distracted, or spend too much time on websites without realizing it. I wanted to monitor how I spend time on my computer and be more aware of my digital behavior.

To find a solution, I searched for tutorials on YouTube and discovered the concept of activity tracking using Python. I combined what I learned from those tutorials with help from **ChatGPT**, who guided me step-by-step through the logic and implementation. As a result, I created this productivity tracker — and it’s already helping me stay more accountable and manage my time better.

## Features

- **Tracks Active Windows**: Detects the exact application or website you're using.
- **Website Detection**: If you're browsing in Chrome, Firefox, or Edge, it extracts the website/tab title.
- **Automatic Time Logging**: Starts and stops timers based on your window focus.
- **JSON Logging**: All activities are saved in a structured JSON file.
- **Works in the Background**: Minimal setup, no GUI needed — just run and focus.

## Installation

### Prerequisites

Before running this script, make sure you have Python installed (preferably Python 3.x). Then install the required dependency:

```bash
pip install pywin32
```

### File Structure

This project includes:

- `tracker.py`: Monitors activity and window changes.
- `logger.py`: Logs data to a JSON file and calculates idle time.
- `activity_log.json`: Output file with your tracked session data.

## How to Use

1. Clone this repo or copy the files into a local folder.
2. Open a terminal and navigate to the folder.
3. Run the tracker script:

```bash
python tracker.py
```

The script will start running in the background. As you switch between apps and websites, it will log each session's:
- Start & End Time
- Duration
- App/Website Name
- Activity Type & Category

You can stop it anytime by pressing `Ctrl + C` in the terminal.

## Example Log Entry

```json
{
  "activity_name": "YouTube",
  "window_title": "YouTube - Google Chrome",
  "start_time": "2025-04-01 15:20:12",
  "end_time": "2025-04-01 15:25:30",
  "seconds": 318,
  "day": "2025-04-01",
  "category": "Browser",
  "app_type": "website",
  "idle_time": 120
}
```

## How It Works

1. The script starts and immediately records your active window.
2. If you switch to a new app or browser tab, it logs the previous one.
3. All sessions are saved into `activity_log.json` for analysis.

## Acknowledgements

- **YouTube Tutorials**: Helped me understand how to track desktop activity using Python.
- **ChatGPT**: Guided me in building the logic, solving bugs, and improving the final code.
- **Open-source Libraries**: `pywin32` and Python's standard library made this possible.

## License

This project is open-source and available under the [MIT License](LICENSE).
