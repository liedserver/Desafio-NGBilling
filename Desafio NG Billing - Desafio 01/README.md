# Desafio 01 - Docker (Python + Flask)

Este projeto implementa uma aplicação **Python (Flask)** que lê o conteúdo de um diretório (mapeado do host local) e retorna a lista de arquivos via uma requisição HTTP `GET`.

### Funcionalidade

- Endpoint disponível:
  ```
  GET /arquivos
  ```

Exemplo de resposta:
```json
{
  "arquivos": ["teste.txt", "foto.png", "log.txt"]
}
```
### Como executar

> [!NOTE]
> Certifique-se de ter o Docker instalado antes de executar os comandos.

#### 1. Criar diretório local
```bash
mkdir ~/arquivos_teste
touch ~/arquivos_teste/arquivo1.txt ~/arquivos_teste/arquivo2.log
```

#### 2. Construir imagem Docker
```bash
docker build -t desafio1-python .
```

#### 3. Executar container
```bash
sudo docker run -d -p 8080:8080 -v ~/arquivos_teste:/arquivos --name desafio1 desafio1-python
```

#### 4. Ver o container em execução
```bash
sudo docker ps
```

#### 5. Testar
```bash
curl http://localhost:8080/arquivos
```
### Monitoramento e estabilidade

| Tipo | O que Monitorar | Por quê |
|------|------------------|---------|
| **Disponibilidade** | Endpoint `/arquivos` responde (HTTP 200) | Detectar falhas |
| **Uso de CPU e Memória** | Métricas do container | Evitar sobrecarga |
| **Espaço em disco** | Diretório mapeado | Evitar erros de leitura/escrita |
| **Logs** | Logs do Flask e Docker | Diagnóstico de falhas |
| **Latência** | Tempo de resposta | Detecção de lentidão |

Exemplo opcional de HEALTHCHECK:
```dockerfile
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
 CMD curl -f http://localhost:8080/arquivos || exit 1
```