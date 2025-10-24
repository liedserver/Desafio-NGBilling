#!/bin/bash

# MUDAR PARA O DIRETORIO DESEJADO
SOURCE_DIR="/caminho/para/origem" 
TARGET_DIR="/caminho/para/destino"

mkdir -p "$SOURCE_DIR"
mkdir -p "$TARGET_DIR"

inotifywait -m -e create --format "%f" "$SOURCE_DIR" | while read FILE
do
    echo "Arquivo detectado: $FILE"
    mv "$SOURCE_DIR/$FILE" "$TARGET_DIR/"
    echo "Arquivo $FILE movido para $TARGET_DIR"
done
