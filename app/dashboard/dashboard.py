import sqlite3
import tkinter as tk
from tkinter import messagebox
import subprocess

DB_PATH = "data/rdrs.db"


def get_statistics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM file_events")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM file_events WHERE status='Normal'")
    normal = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM file_events WHERE status='Suspicious'")
    suspicious = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM file_events WHERE status='Error'")
    errors = cursor.fetchone()[0]

    conn.close()

    return total, normal, suspicious, errors


def refresh():
    total, normal, suspicious, errors = get_statistics()

    total_label.config(text=f"Total Events : {total}")
    normal_label.config(text=f"Normal Events : {normal}")
    suspicious_label.config(text=f"Suspicious Events : {suspicious}")
    error_label.config(text=f"Error Events : {errors}")


def generate_report():
    messagebox.showinfo(
        "Report",
        "Run:\n\npython app/reports/generate_report.py\n\nfrom the terminal to generate the latest report."
    )


# ---------------- GUI ----------------

root = tk.Tk()
root.title("RDRS Dashboard")
root.geometry("500x350")
root.resizable(False, False)

title = tk.Label(
    root,
    text="RDRS Dashboard",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

total_label = tk.Label(root, font=("Arial", 12))
total_label.pack(pady=5)

normal_label = tk.Label(root, font=("Arial", 12))
normal_label.pack(pady=5)

suspicious_label = tk.Label(root, font=("Arial", 12))
suspicious_label.pack(pady=5)

error_label = tk.Label(root, font=("Arial", 12))
error_label.pack(pady=5)

tk.Button(
    root,
    text="Refresh",
    width=20,
    command=refresh
).pack(pady=10)

tk.Button(
    root,
    text="Generate Report",
    width=20,
    command=generate_report
).pack(pady=5)

tk.Button(
    root,
    text="Exit",
    width=20,
    command=root.destroy
).pack(pady=15)

refresh()

root.mainloop()