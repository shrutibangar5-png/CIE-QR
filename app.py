from excel_reader import read_excel
from QR_generator import generator_qr
from pdf_generator import create_pdf

# Read Excel File
data = read_excel("sample_data.xlsx")

print(data)

# Combine all rows into one QR text
all_data = ""

for index, row in data.iterrows():

    row_text = (
        f"Part:{row['Part Number']}, "
        f"Batch:{row['Batch']}, "
        f"Serial:{row['Serial Number']}\n"
    )

    all_data += row_text

# Generate Single QR
qr_path = "output/final_qr.png"

generator_qr(all_data, qr_path)

# Generate PDF
create_pdf(data, qr_path)