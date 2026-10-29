# RUDRA v0.3.0 test plan

1. Run `python rudra\app.py` on Windows 10/11 with Python 3.11+.
2. Confirm all four tabs render and the window remains responsive.
3. Click System health, Network, Disk space, and Top processes one at a time.
4. While a diagnostic runs, switch tabs and confirm the UI still responds.
5. Test command phrases: `system status`, `network check`, `disk report`, `open task manager`, `settings kholo`.
6. Enter an unknown phrase and confirm it is rejected without launching a shell command.
7. Verify no task is allowed to run concurrently.
8. Confirm no system settings are changed by diagnostics.
