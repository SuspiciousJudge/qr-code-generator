from fastapi import FastAPI
import qrcode
from io import BytesIO
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "QR Code Generator API is running!"}

@app.get("/generate/")
def generate_qr_code(data: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convert image to a stream
    img_io = BytesIO()
    img.save(img_io, format="PNG")
    img_io.seek(0)

    return StreamingResponse(img_io, media_type="image/png")
