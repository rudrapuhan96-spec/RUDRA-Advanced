# RUDRA Advanced | Windows Maintenance & Diagnostics

**Version 0.3.0** · **Python · Tkinter · Windows**

RUDRA Advanced is a Windows desktop utility designed to centralize common system tools, provide system diagnostics, and simplify routine maintenance through a clean graphical interface.

The project focuses on usability, controlled actions, diagnostic visibility, and safer interaction with Windows utilities.

## Overview

RUDRA Advanced provides a centralized interface for accessing supported Windows tools, viewing system information, running predefined diagnostics, and performing temporary-file cleanup.

## Key Features

### System Dashboard
- Dashboard interface with Overview, Quick Actions, Diagnostics, and Activity & Logs.
- Centralized navigation to supported Windows utilities.
- Activity visibility for supported operations.

### Windows Quick Actions
Shortcuts to commonly used system tools and settings, including:

- Windows Settings and Network Settings
- Device Manager and Task Manager
- Notepad and File Explorer
- Windows Update settings
- Display, Sound, and Bluetooth settings
- Installed Apps, Calculator, and Snipping Tool
- Command Prompt and PowerShell

These actions launch the corresponding tools or settings pages; they do not necessarily execute the underlying maintenance operation.

### System Diagnostics
- System health information
- Network diagnostics
- Fixed-disk capacity reports
- Top memory-consuming process reports
- Predefined command-bar actions, such as `network check`, `system status`, and `disk report`

### Temporary File Cleanup
- Cleanup of user temporary files, Windows temporary files, and Prefetch files.
- Skips files and folders that cannot be accessed or are in use.
- Cleanup results depend on system permissions and file availability.

### Reliability and Command Controls
- Background workers and a UI event queue for supported diagnostic tasks.
- PowerShell command timeouts and bounded output.
- Cancellation checkpoints in supported operations.
- Predefined command phrases instead of unrestricted shell execution through the command box.

## Screenshots

### Main Interface

![RUDRA Advanced - Main Interface](pictures/RUDRA%20%E2%80%94%20Advanced%20Windows%20AI%20Operator.png)

### Additional Interface View

![RUDRA Advanced - Additional View](pictures/RUDRA%20%E2%80%94%20Advanced%20Windows%20AI%20Operator1.png)

## Demo

[**View the RUDRA Advanced demo video**](videos/RUDRA%20%E2%80%94%20Advanced%20Windows%20AI%20Operator.mp4)

## Technology Stack

- **Language:** Python 3.11+
- **GUI:** Tkinter
- **Platform:** Windows 10 / Windows 11
- **System integration:** Windows utilities and PowerShell for supported diagnostic operations
- **Version control:** Git and GitHub

## Installation and Usage

### Prerequisites

- Windows 10 or Windows 11
- Python 3.11 or later, with Tkinter available

### Run from Source

1. Clone or download this repository.
2. Open a terminal in the project root directory.
3. Launch the application:

```bat
python rudra\app.py
```

If your terminal is already inside the `rudra` directory:

```bat
python app.py
```

## Testing

The project includes a manual test plan in [`tests/TEST_PLAN.md`](tests/TEST_PLAN.md).

Run the application in your own Windows environment and verify the relevant actions before relying on them. Results may vary according to Windows version, permissions, and system configuration.

## Security and Limitations

RUDRA Advanced is a prototype and does not replace Windows security controls.

- Voice recognition, wake-word activation, and LLM-based planning are not yet implemented.
- Automated repair workflows with rollback and post-change verification are not yet implemented.
- Driver modification and administrator-level maintenance workflows are not included.
- Windows Update integration currently provides access to its settings page; automated scanning, downloading, and installation are not implemented.
- Opening a utility does not guarantee that the requested task completed successfully.

Use appropriate backups and review maintenance actions before proceeding. Do not disable User Account Control (UAC) or store administrator credentials in the application.

## Roadmap

- Add push-to-talk speech input with offline and online speech adapters.
- Introduce a restricted intent planner that can select only registered tools.
- Develop repair workflows with previews, explicit approval, backups or rollback where possible, and post-action verification.
- Add optional AI model providers through a settings interface.
- Expand automated testing and prepare a signed installer.

## Project Information

- **Project:** RUDRA Advanced
- **Release:** v0.3.0
- **Status:** Prototype under active development

RUDRA Advanced is being developed as a foundation for a more capable, transparent, and safety-conscious Windows maintenance assistant.