# 🚀 Desafio NG Billing - Analista de Produção

Este repositório reúne três desafios técnicos focados em automação, monitoramento e desenvolvimento de serviços, demonstrando habilidades práticas em um ambiente de Infraestrutura e DevOps. Cada desafio está contido em seu próprio diretório com sua respectiva solução e documentação.

## 📂 Estrutura do Repositório 
```
DESAFIO-NGBILLING/ 
├── 📁 Desafio NG Billing - Desafio 01 
│ ├── 📄 app.py 
│ ├── 🐳 Dockerfile 
│ ├── 📄 README.md 
│ └── 📄 requirements.txt 
├── 📁 Desafio NG Billing - Desafio 02 
│ ├── 📄 .env.sample 
│ ├── 🐍 app.py 
│ ├── 📄 README.md 
│ └── 📄 requirements.txt 
├── 📁 Desafio NG Billing - Desafio 03 
│ ├── 📄 mover-arquivo.service 
│ ├── 📜 mover-arquivos.sh 
│ └── 📄 README.md 
└── 📄 README.md
```
---

## 1: API em Python com Docker para Listagem de Arquivos

Neste desafio, foi desenvolvida uma aplicação **Python** utilizando o framework **Flask** para criar uma API que lista arquivos de um diretório específico. A aplicação é totalmente containerizada com Docker, garantindo portabilidade e um ambiente de execução consistente.

* **Tecnologias:** `Python`, `Flask`, `Docker`.
* **Funcionalidade:**
    * Expõe um endpoint `GET /arquivos` que retorna uma lista de nomes de arquivos em formato JSON.
    * O diretório `/arquivos` dentro do container é mapeado a partir do host local, permitindo a leitura de arquivos externos.
* **Monitoramento:** O `README.md` do desafio detalha estratégias de monitoramento para disponibilidade, uso de recursos (CPU, memória), espaço em disco e logs.

---

## 2: Script Python para Consulta em Banco Oracle e Envio de E-mail

Este projeto consiste em um script **Python** que automatiza a tarefa de consultar o próximo valor de uma `SEQUENCE` em um banco de dados **Oracle** e notificar este valor por e-mail.

* **Tecnologias:** `Python`, `cx_Oracle`, `smtplib`.
* **Funcionalidade:**
    * Conecta-se a um banco de dados Oracle para executar a query `SELECT SEQ_ID.NEXTVAL AS ULTIMO_ID FROM DUAL`.
    * Envia o resultado obtido para um destinatário de e-mail pré-configurado.
* **Segurança:** As credenciais sensíveis (banco de dados e e-mail) são gerenciadas de forma segura através de um arquivo `.env`, que não deve ser versionado.

---

## 3: Serviço Linux em Bash para Monitoramento e Movimentação de Arquivos

O terceiro desafio implementa um serviço **Linux**, gerenciado pelo `systemd`, que monitora um diretório e move arquivos recém-criados para outro local automaticamente.

* **Tecnologias:** `Bash`, `inotify-tools`, `systemd`.
* **Funcionalidade:**
    * Utiliza o comando `inotifywait` para detectar o evento de criação de novos arquivos em um diretório de origem.
    * Move o arquivo detectado para um diretório de destino.
    * O script é configurado para rodar como um serviço (`.service`) que inicia com o sistema e reinicia automaticamente em caso de falha (`Restart=always`).

---

## ✍️ Autor

**Liedson Saraiva** Infraestrutura e DevOps Engineer 💻