# RUDRA Advanced Windows Operator — v0.3.0

RUDRA is a lightweight Windows desktop prototype for approved quick actions and read-only diagnostics.

## Requirements
- Windows 10/11
- Python 3.11+ (Tkinter included with the standard Windows Python installer)

## Run
Open CMD in the extracted `RUDRA_Advanced_v03` folder and run:

```bat
python rudra\app.py
```

If CMD is already inside the `rudra` folder, use `python app.py`.

## Included
- Dashboard-style UI with Overview, Quick Actions, Diagnostics, Activity & Logs
- Fast allow-listed launch actions: Settings, Network Settings, Device Manager, Task Manager, Notepad, File Explorer, Windows Update, Display/Sound/Bluetooth settings, Installed Apps, Calculator, Snipping Tool, CMD and PowerShell
- Read-only system health, network, fixed-disk capacity, and top-memory-process reports
- Background workers and a UI event queue so diagnostics don't freeze the interface
- Basic command bar for predefined phrases, e.g. `network check`, `system status`, `disk report`, `open task manager`
- Timeouts on PowerShell commands, bounded output, and cancellation checkpoints
- No arbitrary shell execution from the command box

## Important limitations
- Voice recognition, wake word, LLM/AI planning, automatic repair, driver changes, and administrator operations are **not included yet**.
- A recognized action is not proof that the launched app fully opened or that a repair worked. Verify outcomes.
- Diagnostics can briefly use CPU/RAM. On a 8 GB machine, avoid running many tools concurrently; this build allows one diagnostic task at a time.
- This is a prototype, not a replacement for Windows security controls. Do not disable UAC or store administrator passwords.

## Next architecture steps
1. Add offline/online speech adapter with push-to-talk first.
2. Add intent planner that can only select registered tools, not emit arbitrary shell commands.
3. Add repair workflow with preview, approval, backup/rollback where possible, and post-change verification.
4. Add optional model providers behind a settings page; never require cloud AI for basic launch actions.
5. Add unit tests and signed installer after stable behavior is confirmed.
