# Virtual Memory Translator

## Descrição do Projeto
Implementação de um sistema de gerenciamento de memória virtual que traduz endereços virtuais (16-32 bits) para endereços físicos, com suporte a:
- Paginação com tamanhos de página de 256B a 4KB
- Tabela de páginas hierárquica para endereços 32 bits
- TLB (Translation Lookaside Buffer) com política LRU
- Simulação de page faults e carregamento por demanda

## Como Executar

### Pré-requisitos
- Python 3.6+
- Git (para clonar o repositório)

### Instalação

## 🚀 Instalação

Clone o repositório e instale as dependências:

```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
pip install -r requirements.txt
```

---

## ▶️ Uso Básico

Execute o programa passando um endereço ou um arquivo com endereços, seguido das opções desejadas:

```bash
python src/main.py [ENDEREÇO|ARQUIVO] [OPÇÕES]
```

---

## 📌 Exemplos

### 🔢 Endereço decimal:

```bash
python src/main.py 19986
```

### 🔠 Endereço hexadecimal:

```bash
python src/main.py 0x4E12
```

### 📄 Arquivo de endereços:

```bash
python src/main.py data/addresses_16b.txt
```

---

## ⚙️ Opções

| Opção         | Descrição                                         |
|----------------|---------------------------------------------------|
| `--page_size`  | Tamanho da página em bytes (256, 1024 ou 4096)    |
| `--tlb_size`   | Tamanho da TLB (padrão: 16)                       |
| `--verbose`    | Mostrar detalhes adicionais                       |

---

## 🖥️ Exemplo de Saída

```text
Endereço Virtual: 19986 (0x4E12)
- Número da Página: 4
- Deslocamento: 3602
- TLB: miss
- Page Table: hit
- Ação: Carregado da memória principal
- Valor lido: 50
```

---

## 📁 Estrutura do Código

```
data/
  addresses_16b.txt       # Endereços de exemplo 16-bit
  addresses_32b.txt       # Endereços de exemplo 32-bit
  data_memory.txt         # Memória física simulada
  data.py

src/
  address_parser.py       # Interpretador de endereços
  memory_manager.py       # Núcleo do gerenciador
  page_table.py           # Tabela de páginas
  tlb.py                  # TLB com política LRU
  main.py                 # Interface de linha de comando
```

---

## ✅ Funcionalidades Implementadas

- ✔️ Tradução de endereços virtuais (16-32 bits)
- ✔️ Suporte a endereços em hexadecimal (`0x...`) e decimal
- ✔️ Paginação hierárquica (2 níveis para endereços 32 bits)
- ✔️ TLB com política **LRU** (16 entradas)
- ✔️ Simulação de **page faults** e carregamento sob demanda
- ✔️ Bits de controle (**valid**, **dirty**, **accessed**)
- ✔️ Tratamento de erros para endereços inválidos
