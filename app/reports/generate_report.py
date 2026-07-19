import sqlite3
import os

DB_PATH = "data/rdrs.db"


def generate_report():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM file_events")
    total_events = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM file_events WHERE status='Normal'")
    normal_events = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM file_events WHERE status='Suspicious'")
    suspicious_events = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM file_events WHERE status='Error'")
    error_events = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(entropy) FROM file_events")
    avg_entropy = cursor.fetchone()[0] or 0

    cursor.execute("SELECT MAX(entropy) FROM file_events")
    max_entropy = cursor.fetchone()[0] or 0

    cursor.execute("""
        SELECT filename, event_type, status, timestamp
        FROM file_events
        ORDER BY id DESC
        LIMIT 1
    """)

    latest = cursor.fetchone()

    conn.close()

    report = f"""
==================================================
              RDRS SECURITY REPORT
==================================================

Total Events      : {total_events}
Normal Events     : {normal_events}
Suspicious Events : {suspicious_events}
Error Events      : {error_events}

Average Entropy   : {avg_entropy:.2f}
Highest Entropy   : {max_entropy:.2f}

Latest Event
--------------------------------------------------
File      : {latest[0] if latest else 'N/A'}
Event     : {latest[1] if latest else 'N/A'}
Status    : {latest[2] if latest else 'N/A'}
Time      : {latest[3] if latest else 'N/A'}

==================================================
"""

    print(report)

    os.makedirs("reports", exist_ok=True)

    with open("reports/security_report.txt", "w") as file:
        file.write(report)

    print("✅ Report saved to reports/security_report.txt")


if __name__ == "__main__":
    generate_report()