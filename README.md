# 🧠 Algoritmos de Ordenação em Python

Este projeto foi criado com o objetivo de **praticar, comparar e entender** como funcionam os principais algoritmos de ordenação. Todos os códigos estão escritos em **Python** e comentados em **português**, com explicações das **vantagens e desvantagens** de cada abordagem.

---

## ✨ O que está incluso?

Aqui você encontra a implementação dos seguintes algoritmos:

- 📌 Selection Sort (Ordenação por Seleção)
- 💭 Bubble Sort (Ordenação por Bolha)
- 🧱 Insertion Sort (Ordenação por Inserção)
- 🧬 Merge Sort (Ordenação por Intercalação)
- ⚡ Quick Sort (Ordenação Rápida)
- 🏗️ Heap Sort
- 🧮 Counting Sort
- 📊 Radix Sort
- 🪣 Bucket Sort

Cada algoritmo tem seus prós e contras explicados diretamente no código, para facilitar a compreensão.

---

## 🚀 Como usar

Você pode rodar os algoritmos diretamente em um terminal Python ou importar os métodos para seu próprio código.

### Exemplo:

```python
from ordenacao import quick_sort

lista = [42, 23, 7, 15, 99]
ordenada = quick_sort(lista)
print(ordenada)

| Algoritmo      | Melhor Caso | Médio Caso | Pior Caso  | Estável |
| -------------- | ----------- | ---------- | ---------- | ------- |
| Selection Sort | O(n²)       | O(n²)      | O(n²)      | ❌       |
| Bubble Sort    | O(n)        | O(n²)      | O(n²)      | ✅       |
| Insertion Sort | O(n)        | O(n²)      | O(n²)      | ✅       |
| Merge Sort     | O(n log n)  | O(n log n) | O(n log n) | ✅       |
| Quick Sort     | O(n log n)  | O(n log n) | O(n²)      | ❌       |
| Heap Sort      | O(n log n)  | O(n log n) | O(n log n) | ❌       |
| Counting Sort  | O(n + k)    | O(n + k)   | O(n + k)   | ✅       |
| Radix Sort     | O(nk)       | O(nk)      | O(nk)      | ✅       |
| Bucket Sort    | O(n + k)    | O(n + k)   | O(n²)      | ✅       |


🔧 Requisitos
Python 3.x instalado.

Nenhuma biblioteca externa é necessária.

📦 Organização do código
Todo o código está em um único arquivo .py para facilitar testes e experimentações. Sinta-se à vontade para separar por módulos se quiser algo mais estruturado.

🤝 Contribuindo
Esse projeto foi feito com fins educacionais, mas qualquer sugestão ou melhoria é super bem-vinda! 😄

📄 Licença
Código livre para uso pessoal, educacional ou acadêmico.

✍️ Autor
Feito com dedicação para ajudar na jornada de quem está aprendendo algoritmos e estruturas de dados.
