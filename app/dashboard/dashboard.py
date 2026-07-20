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

    cursor.execute("SELECT AVG(entropy) FROM file_events")
    avg_entropy = cursor.fetchone()[0]
    if avg_entropy is None:
        avg_entropy = 0

    cursor.execute("SELECT MAX(entropy) FROM file_events")
    max_entropy = cursor.fetchone()[0]
    if max_entropy is None:
        max_entropy = 0

    cursor.execute("""
        SELECT filename, status, timestamp
        FROM file_events
        ORDER BY id DESC
        LIMIT 1
    """)

    latest = cursor.fetchone()

    conn.close()

    return (
        total,
        normal,
        suspicious,
        errors,
        avg_entropy,
        max_entropy,
        latest
    )


def refresh():

    (
        total,
        normal,
        suspicious,
        errors,
        avg_entropy,
        max_entropy,
        latest
    ) = get_statistics()

    total_label.config(text=f"Total Events : {total}")
    normal_label.config(text=f"Normal Events : {normal}")
    suspicious_label.config(text=f"Suspicious Events : {suspicious}")
    error_label.config(text=f"Error Events : {errors}")

    avg_label.config(text=f"Average Entropy : {avg_entropy:.2f}")
    max_label.config(text=f"Highest Entropy : {max_entropy:.2f}")

    if latest:
        latest_file.config(text=f"Latest File : {latest[0]}")
        latest_status.config(text=f"Latest Status : {latest[1]}")
        latest_time.config(text=f"Last Updated : {latest[2]}")

    root.after(5000, refresh)


def generate_report():
    subprocess.run(
        ["python", "app/reports/generate_report.py"]
    )

    messagebox.showinfo(
        "Success",
        "Security Report Generated Successfully!"
    )


# ---------------- GUI ----------------

root = tk.Tk()

root.title("Ransomware Detection & Response System")

root.geometry("650x520")

root.resizable(False, False)

title = tk.Label(
    root,
    text="🛡 Ransomware Detection & Response System",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Real-Time Security Dashboard",
    font=("Arial", 11)
)

subtitle.pack()

tk.Label(
    root,
    text="----------------------------------------------------------"
).pack()

total_label = tk.Label(root, font=("Arial", 13))
total_label.pack(pady=5)

normal_label = tk.Label(root, font=("Arial", 13))
normal_label.pack()

suspicious_label = tk.Label(root, font=("Arial", 13))
suspicious_label.pack()

error_label = tk.Label(root, font=("Arial", 13))
error_label.pack()

avg_label = tk.Label(root, font=("Arial", 13))
avg_label.pack(pady=10)

max_label = tk.Label(root, font=("Arial", 13))
max_label.pack()

tk.Label(
    root,
    text="Latest Event",
    font=("Arial", 14, "bold")
).pack(pady=10)

latest_file = tk.Label(root, font=("Arial", 12))
latest_file.pack()

latest_status = tk.Label(root, font=("Arial", 12))
latest_status.pack()

latest_time = tk.Label(root, font=("Arial", 12))
latest_time.pack()

tk.Button(
    root,
    text="Refresh Dashboard",
    width=25,
    command=refresh
).pack(pady=15)

tk.Button(
    root,
    text="Generate Security Report",
    width=25,
    command=generate_report
).pack()

tk.Button(
    root,
    text="Exit",
    width=25,
    command=root.destroy
).pack(pady=15)

refresh()

root.mainloop()