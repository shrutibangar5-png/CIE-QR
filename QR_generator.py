import qrcode

def generator_qr(qr_data, output_path):

    qr = qrcode.QRCode(
        version=5,
        box_size=10,
        border=4
    )

    qr.add_data(qr_data)

    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    img.save(output_path)

    print(f"QR saved: {output_path}")