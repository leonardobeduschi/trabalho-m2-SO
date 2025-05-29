# Virtual Memory Simulator

Simula a tradução de endereços virtuais para físicos com suporte a:

- TLB com política LRU
- Page Table com bits de validade, acesso e dirty
- Simulação de page fault com carregamento da backing store (data_memory.txt)

## 🚀 Como rodar

1. Clone o repositório.
2. Acesse a pasta do projeto.
3. (Opcional) Gere o arquivo de memória:
   ```bash
   python data/data.py
