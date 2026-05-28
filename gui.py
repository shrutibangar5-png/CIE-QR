import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
import os

from excel_reader import read_excel
from QR_generator import generator_qr
from pdf_generator import create_pdf


def process_file():

    # Open File Picker
    file_path = filedialog.askopenfilename(
        filetypes=[("Excel Files", "*.xlsx")]
    )

    if not file_path:
        return

    # Auto Create Output Folder
    if not os.path.exists("output"):
        os.makedirs("output")

    # Read Excel
    data = read_excel(file_path)

    # Combine all entries into ONE QR
    all_data = ""

    for index, row in data.iterrows():

        row_text = (
            f"Part:{row['Part Number']}, "
            f"Batch:{row['Batch']}, "
            f"Serial:{row['Serial Number']}\n"
        )

        all_data += row_text

    # Create unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    qr_path = f"output/final_qr_{timestamp}.png"

    # Generate ONE QR
    generator_qr(all_data, qr_path)

    # Generate PDF
    create_pdf(data, qr_path)

    # Success Popup
    messagebox.showinfo(
        "Success",
        "QR Labels PDF Generated Successfully!"
    )


# =========================
# GUI WINDOW
# =========================

root = tk.Tk()

root.title("CIE QR Generator")

root.geometry("600x400")

root.configure(bg="#f4f4f4")


# =========================
# TITLE
# =========================

title = tk.Label(
    root,
    text="CIE QR Automation",
    font=("Arial", 20, "bold"),
    bg="#f4f4f4",
    fg="#222222"
)

title.pack(pady=40)


# =========================
# DESCRIPTION
# =========================

description = tk.Label(
    root,
    text="Upload Excel file to generate QR labels PDF",
    font=("Arial", 12),
    bg="#f4f4f4",
    fg="#555555"
)

description.pack(pady=10)


# =========================
# UPLOAD BUTTON
# =========================

upload_btn = tk.Button(
    root,
    text="Upload Excel File",
    font=("Arial", 14, "bold"),
    bg="#0078D7",
    fg="white",
    padx=20,
    pady=10,
    command=process_file
)

upload_btn.pack(pady=40)


# =========================
# FOOTER
# =========================

footer = tk.Label(
    root,
    text="Developed for CIE",
    font=("Arial", 10),
    bg="#f4f4f4",
    fg="#888888"
)

footer.pack(side="bottom", pady=20)


# =========================
# START GUI
# =========================

root.mainloop()