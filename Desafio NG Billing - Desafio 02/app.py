import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import cx_Oracle

load_dotenv()

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

def send_email(last_id):
    email_host = os.getenv("EMAIL_HOST")
    email_port = int(os.getenv("EMAIL_PORT", 587))
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_to = os.getenv("EMAIL_TO")

    msg = EmailMessage()
    msg['Subject'] = "Último ID da sequência"
    msg['From'] = email_user
    msg['To'] = email_to
    msg.set_content(f"O último ID da sequência é: {last_id}")

    try:
        with smtplib.SMTP(email_host, email_port) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.send_message(msg)
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    last_id = get_last_id()
    if last_id is not None:
        send_email(last_id)
    else:
        print("Não foi possível obter o último ID.")
