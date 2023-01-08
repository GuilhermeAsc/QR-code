#By asC-_ :)

import qrcode
from PIL import Image

# Cria o QR Code
qr_code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adiciona o texto a ser codificado
qr_code.add_data('https://www.youtube.com/@MARSHMALLOWATACA')

# Gera o QR Code
qr_code.make(fit=True)

# Cria uma imagem a partir do QR Code
img = qr_code.make_image(fill_color="black", back_color="white")

print('QR CODE GERADO!!')
# Salva a imagem em um arquivo
img.save('qr_code.png')