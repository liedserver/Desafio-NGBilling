import os
import asyncio
from email.mime.text import MIMEText
from dotenv import load_dotenv
import cx_Oracle
from aiosmtplib import SMTP

load_dotenv()

# Config Oracle
user = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")
dsn = os.getenv("ORACLE_DSN")

SQL = "SELECT SEQ_ID.NEXTVAL AS ULTIMO_ID FROM DUAL"

def get_last_id():
    try:
        connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)
        cursor = connection.cursor()
        cursor.execute(SQL)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result[0] if result else None
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao acessar Oracle: {e}")
        return None

async def send_email_async(last_id):
    email_host = os.getenv("EMAIL_HOST", "localhost")
    email_port = int(os.getenv("EMAIL_PORT", 1025))
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_to = os.getenv("EMAIL_TO", "teste@local").split(",")

    msg = MIMEText(f"O último ID da sequência é: {last_id}")
    msg['Subject'] = "Último ID da sequência"
    msg['From'] = email_user
    msg['To'] = ", ".join(email_to)

    try:
        if email_host in ("localhost", "127.0.0.1") and email_port == 1025:
            #smtp-fake
            smtp = SMTP(hostname=email_host, port=email_port)
            await smtp.connect()
        else:
            # SMTP real
            if email_port == 465:
                smtp = SMTP(hostname=email_host, port=email_port, use_tls=True)
                await smtp.connect()
                await smtp.login(email_user, email_password)
            else:
                smtp = SMTP(hostname=email_host, port=email_port, start_tls=True)
                await smtp.connect()
                await smtp.login(email_user, email_password)

        await smtp.send_message(msg)
        await smtp.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    last_id = get_last_id()
    if last_id is not None:
        asyncio.run(send_email_async(last_id))
    else:
        print("Não foi possível obter o último ID.")
