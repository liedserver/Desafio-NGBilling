# Desafio 2 - Python (Oracle + E-mail)

Este projeto implementa um script Python que lê o **último ID de uma sequência** de uma tabela Oracle e envia esse valor por e-mail.

### Funcionalidade

1. Conecta ao banco Oracle usando `cx_Oracle`
2. Recupera o último ID da sequência
3. Envia o ID por e-mail usando `smtplib`

### Segurança

- Senhas **não estão no código**, mas em arquivo `.env`
- Conexão TLS para e-mail
- Arquivo `.env` deve ser listado em `.gitignore`

### Como usar
0. Instalar Oracle Instant Client e outros pré-requisitos para cx_Oracle
```bash
wget https://download.oracle.com/otn_software/linux/instantclient/2326000/instantclient-basic-linux.x64-23.26.0.0.0.zip

export LD_LIBRARY_PATH=/local/onde/foi/baixado/instantclient_23_26:$LD_LIBRARY_PATH

sudo ln -s /usr/lib/x86_64-linux-gnu/libaio.so.1t64 /usr/lib/x86_64-linux-gnu/libaio.so.1
```
1. Instalar suporte a virtualenv
```bash
sudo apt install python3-venv
```
2. Criar e ativar ambiente virtual
```bash
python3 -m venv venv
source ./venv/bin/activate
```
3. Instale dependências:
```bash
pip install -r requirements.txt
```
#### Caso queira garantir que todas as libs do script estejam instaladas (se não estiverem no requirements.txt):
```bash
pip install aiosmtplib aiosmtpd python-dotenv cx_Oracle
```

4. Copie `.env.sample` para `.env` e preencha com suas credenciais reais
```bash
cp .env.sample .env
```

5. Rodar servidor SMTP fake para testes python -m aiosmtpd -n -l localhost:1025
```bash
python -m aiosmtpd -n -l localhost:1025
```
> [!NOTE]
> Este terminal ficará “pendurado” esperando conexões. Todos os e-mails enviados aparecerão no console

6. Execute o script:
```bash
python app.py
```

7. Teste
![03](https://github.com/liedserver/Desafio-NGBilling/blob/master/prints/desafio03.png?raw=true)