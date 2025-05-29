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
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
pip install -r requirements.txt

Uso Básico
bash
python src/main.py [ENDEREÇO|ARQUIVO] [OPÇÕES]
Exemplos:

Endereço decimal:
bash
python src/main.py 19986


Endereço hexadecimal:
bash
python src/main.py 0x4E12
Arquivo de endereços:

bash
python src/main.py data/addresses_16b.txt
Opções:
--page_size: Tamanho da página em bytes (256, 1024 ou 4096)

--tlb_size: Tamanho da TLB (padrão: 16)

--verbose: Mostrar detalhes adicionais

Exemplo de Saída
Endereço Virtual: 19986 (0x4E12)
- Número da Página: 4
- Deslocamento: 3602
- TLB: miss
- Page Table: hit
- Ação: Carregado da memória principal
- Valor lido: 50
Estrutura do Código
data/
  addresses_16b.txt    # Endereços de exemplo 16-bit
  addresses_32b.txt    # Endereços de exemplo 32-bit
  data_memory.txt      # Memória física simulada
  backing_store.txt    # Armazenamento secundário
src/
  address_parser.py    # Interpretador de endereços
  memory_manager.py    # Núcleo do gerenciador
  page_table.py        # Tabela de páginas
  tlb.py               # TLB com política LRU
  main.py              # Interface de linha de comando
tests/
  test_*.py            # Testes unitários
Funcionalidades Implementadas
✔ Tradução de endereços virtuais (16-32 bits)
✔ Suporte a hexadecimal (0x...) e decimal
✔ Paginação hierárquica (2 níveis para 32 bits)
✔ TLB com política LRU (16 entradas)
✔ Simulação de page faults
✔ Bits de controle (valid, dirty, accessed)
✔ Tratamento de erros para endereços inválidos