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

1. Instale dependências:
```bash
pip install -r requirements.txt
```

2. Copie `.env.sample` para `.env` e preencha com suas credenciais reais

3. Execute o script:
```bash
python send_last_id.py
```
