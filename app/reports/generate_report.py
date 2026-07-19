def generate_report():
    try:
        subprocess.run(
            ["python", "app/reports/generate_report.py"],
            check=True
        )

        messagebox.showinfo(
            "Success",
            "Security report generated successfully!\n\nCheck:\nreports/security_report.txt"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )