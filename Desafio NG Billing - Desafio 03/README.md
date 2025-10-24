# Desafio 3 - Bash (Monitoramento de Diretório)

Este projeto implementa um **serviço Linux** que monitora um diretório e move arquivos automaticamente para outro diretório assim que eles forem criados.

### Funcionalidade

- Monitorar diretório de origem usando `inotifywait`
- Mover arquivos detectados para diretório de destino
- Rodar como serviço systemd ativo no boot

### Configuração
> [!NOTE]
> Lembre-se de ajustar os caminhos conforme o seu ambiente.
> Altere em mover-arquivo.service e mover-arquivos.sh.


1. Instalar dependência:
```bash
sudo apt install inotify-tools
```

2. Ajustar diretórios no script `mover-arquivos.sh`:
```bash
SOURCE_DIR="/caminho/para/origem"
TARGET_DIR="/caminho/para/destino"
```
 
3. Colocar o script em executável
```bash
sudo chmod +x /caminho/para/executavel/mover-arquivos.sh
```

4. Copiar arquivo de serviço para systemd:
```bash
sudo cp mover-arquivo.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable mover-arquivo.service
sudo systemctl start mover-arquivo.service
sudo systemctl status mover-arquivo.service
```
#### Systemd + inotifywait: Serviço `mover-arquivo.service` em ação, movendo arquivos automaticamente de `01` para `02` ao detectar novas criações.

![01](https://github.com/liedserver/Desafio-NGBilling/blob/master/prints/desafio02.png?raw=true)

### Observações

- Logs podem ser vistos com:
```bash
journalctl -u mover-arquivo.service -f
```

- O serviço reinicia automaticamente se falhar (`Restart=always`).
