from email.message import EmailMessage
import ssl
import smtplib
import imghdr

# Definir las credenciales y destinatario.
email_emisor = "linaresvelascomichael@gmail.com"
email_password = "ghbkxzoobaxlojhn" # Contraseña generada despues de la verificación en dos pasos...
email_receptor = "linaresvelascomichael@gmail.com"

# Definir el asunto y el cuerpo del correo.
asunto = 'Mail enviado desde Python...'
cuerpo = """Te envío un correo desde mi script de Python..."""

# Definir cuántas veces deseas enviar el correo.
numero_envios = 3

# Iniciar un bucle para enviar el correo múltiples veces.
for _ in range(numero_envios):
    # Crear un objeto EmailMessage para componer el correo.
    em = EmailMessage()
    em['From'] = email_emisor
    em['To'] = email_receptor
    em['Subject'] = asunto
    em.set_content(cuerpo)

    # Adjuntar un archivo de imagen al correo.
    with open(r'C:\Users\Administrador\PycharmProjects\Curso_Selenium\Automatizar\Automatizar_gmail\paisaje.jpg', 'rb') as file:
        file_data = file.read()
        file_tipo = imghdr.what(file.name)
        file_nombre = file.name
    em.add_attachment(file_data, filename=file_nombre, subtype=file_tipo, maintype='image')

    # Configurar el contexto SSL seguro para la conexión SMTP.
    contexto = ssl.create_default_context()

    # Establecer una conexión SMTP segura con el servidor de Gmail.
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
        # Iniciar sesión en la cuenta de correo emisor
        smtp.login(email_emisor, email_password)

        # Enviar el correo electrónico.
        smtp.sendmail(email_emisor, email_receptor, em.as_string())

# Imprimir un mensaje de confirmación después de enviar el correo múltiples veces.
print(f"Mensaje enviado {numero_envios} veces.")





