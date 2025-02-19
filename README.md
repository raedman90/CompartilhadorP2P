# Compartilhador de Arquivos P2P

## 📌 Sobre o Projeto

Este projeto implementa um **compartilhador de arquivos P2P** utilizando **sockets** em Python, baseado no modelo **Napster**. O sistema permite que múltiplos clientes se conectem a um **servidor central** para registrar e buscar arquivos, além de possibilitar **transferência direta** entre clientes.

## 🚀 Funcionalidades

✅ **Servidor Central**:

- Gerencia conexões de clientes
- Armazena a lista de arquivos compartilhados por cada cliente
- Processa buscas e retorna os IPs dos clientes que possuem o arquivo

✅ **Cliente**:

- Conecta-se ao servidor e registra seus arquivos
- Permite buscar arquivos compartilhados na rede
- Faz download diretamente de outro cliente
- Pode adicionar e remover arquivos dinamicamente

## 🎯 Como Executar o Projeto

### 1️⃣ Clonar o Repositório

```sh
git clone https://github.com/seu-usuario/CompartilhadorP2P.git
cd CompartilhadorP2P
```

### 2️⃣ Instalar Dependências

```sh
pip install -r requirements.txt
```

### 3️⃣ Executar o Servidor

```sh
python main.py
```

Digite `servidor` quando solicitado.

### 4️⃣ Executar um Cliente

```sh
python main.py
```

Digite `cliente` e informe o IP do servidor (exemplo: `127.0.0.1`).

## 📜 Comandos do Cliente

- **Registrar novo arquivo:** `CREATEFILE nome_do_arquivo tamanho_em_bytes`
- **Buscar arquivos na rede:** `SEARCH nome_do_arquivo`
- **Baixar arquivo:** `DOWNLOAD ip_do_cliente nome_do_arquivo`
- **Deletar arquivo:** `DELETEFILE nome_do_arquivo`
- **Sair da rede:** `LEAVE`

## 📡 Testes

✅ **Conectar cliente ao servidor** ✅ **Registrar arquivos automaticamente** ✅ **Buscar arquivos disponíveis** ✅ **Baixar arquivos entre clientes** ✅ **Remover arquivos e verificar se são deletados do servidor** ✅ **Testar saída do cliente e remoção de arquivos do servidor**

## 📌 Tecnologias Utilizadas

- **Python 3**
- **Sockets** para comunicação entre cliente e servidor
- **Threading** para manipulação de múltiplas conexões

## 📄 Licença

Este projeto é open-source e está licenciado sob a **MIT License**.

