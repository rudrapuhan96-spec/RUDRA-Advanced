from __future__ import annotations

import os
import tempfile
from pathlib import Path


def clean_temp_files(progress, cancel):
    """Remove temporary files; skip locked or inaccessible items."""
    locations = [
        ("User Temp", Path(tempfile.gettempdir())),
        ("Windows Temp", Path(os.environ.get("WINDIR", r"C:\Windows")) / "Temp"),
        ("Prefetch", Path(os.environ.get("WINDIR", r"C:\Windows")) / "Prefetch"),
    ]

    deleted_files = 0
    deleted_dirs = 0
    skipped = 0
    freed_bytes = 0
    details = []

    for label, folder in locations:
        cancel.checkpoint()
        progress(f"Cleaning {label}: {folder}")

        if not folder.is_dir():
            details.append(f"{label}: folder unavailable; skipped.")
            continue

        for item in folder.iterdir():
            cancel.checkpoint()
            try:
                if item.is_symlink():
                    skipped += 1
                    continue

                if item.is_file():
                    size = item.stat().st_size
                    item.unlink()
                    deleted_files += 1
                    freed_bytes += size

                elif item.is_dir():
                    size_before = 0
                    for root, dirs, files in os.walk(item, followlinks=False):
                        dirs[:] = [
                            d for d in dirs
                            if not (Path(root) / d).is_symlink()
                        ]
                        for name in files:
                            child = Path(root) / name
                            try:
                                if not child.is_symlink():
                                    size_before += child.stat().st_size
                            except OSError:
                                pass

                    import shutil
                    shutil.rmtree(item)
                    deleted_dirs += 1
                    freed_bytes += size_before

            except (OSError, PermissionError):
                skipped += 1

        details.append(f"{label}: processed.")

    return (
        "TEMP CLEANUP FINISHED\n"
        f"Files deleted: {deleted_files}\n"
        f"Folders deleted: {deleted_dirs}\n"
        f"Items skipped (locked/access denied): {skipped}\n"
        f"Estimated space freed: {freed_bytes / (1024 ** 2):.2f} MB\n\n"
        + "\n".join(details)
    )
