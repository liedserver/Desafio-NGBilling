# 🐳 Desafio 1 - Docker  

### 📋 Descrição  

Aplicação **Python + Flask** que lê um diretório mapeado do host local (como volume Docker) e retorna a lista de arquivos disponíveis através de uma requisição **HTTP GET**.  

A aplicação também possui um endpoint de **verificação de saúde (/health)** para monitoramento da disponibilidade.  

---

### 🧱 Estrutura  

```
desafio1/
├── app.py
├── requirements.txt
└── Dockerfile
```

---
### 🐍 Código principal (`app.py`)  

```python
from flask import Flask, jsonify
import os

app = Flask(__name__)
DIRECTORY = "/data"

@app.route("/files", methods=["GET"])
def list_files():
    try:
        files = os.listdir(DIRECTORY)
        return jsonify({"files": files})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

---
### 📦 Dependências (requirements.txt)
```
flask==3.0.3
```

---
### 🐳 Dockerfile
```Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN mkdir -p /data

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl -f http://localhost:8080/health || exit 1

CMD ["python", "app.py"]
```

---
### 🚀 Como executar

#### Gerar a imagem Docker:
```bash
docker build -t desafio1-python .
```

#### Criar um diretório local de teste:
```bash
mkdir ~/arquivos_teste
touch ~/arquivos_teste/arquivo1.txt ~/arquivos_teste/arquivo2.log
```

#### Executar o container com volume mapeado:
```bash
docker run -d \
  -p 8080:8080 \
  -v ~/arquivos_teste:/data \
  --name desafio1 \
  desafio1-python
```

#### Testar os endpoints:

##### Lista de arquivos:
```bash
curl http://localhost:8080/files
```

##### Retorno esperado:
```json
{"files": ["arquivo1.txt", "arquivo2.log"]}
```

##### Healthcheck:
```bash
curl http://localhost:8080/health
```

##### Retorno esperado:
```json
{"status": "ok"}
```

---

### 🧠 Monitoramento e Estabilidade

Para garantir que a aplicação permaneça estável e disponível, é importante monitorar:

#### 🔹 Recursos do Container
- **CPU** — picos de uso podem indicar sobrecarga.  
- **Memória (RAM)** — crescimento anormal pode sinalizar vazamentos.  
- **Uso de disco (/data)** — acompanhar o volume mapeado no host.  

#### 🔹 Saúde da Aplicação
- **Status HTTP** — endpoints `/files` e `/health` devem responder `200`.  
- **Tempo de resposta** — monitorar latência e falhas.  
- **Logs do Flask** — erros de leitura, permissões, exceções, etc.  

#### 🔹 Infraestrutura Docker
- **Restart Count** — reinicializações frequentes indicam falhas.  
- **Logs do container** — `docker logs desafio1` para verificar erros no runtime.  
- **Healthcheck Docker** — reinicia automaticamente em caso de falha no `/health`.  

#### 🔹 Boas práticas adicionais
Usar política de reinício automático:
```bash
docker run --restart=always ...
```

Integrar com **Prometheus + Grafana** para métricas e alertas.  
Acompanhar logs via **Loki** ou **ELK Stack**.
