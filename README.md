# Desafios — Implementações

Este repositório contém soluções para os desafios na pasta `desafios`.

Cada seção abaixo descreve a implementação presente em cada arquivo.

**Participante:** Ana Lucia Oliveira de Paula.

---

## Desafio 1 — FizzBuzz
- Arquivo: [desafios/desafio1.py](desafios/desafio1.py)
- Descrição: Implementação do clássico FizzBuzz. A função `get_special_print(num)` retorna "Fizz" para múltiplos de 3, "Buzz" para múltiplos de 5, "FizzBuzz" para múltiplos de ambos e string vazia caso contrário. A função `fizz_buzz()` imprime os números de 1 a 100 substituindo conforme a regra.
- Execução: `python desafios/desafio1.py`
- Saída esperada (exemplo parcial):

```
1
2
Fizz
4
Buzz
...
FizzBuzz
```

---

## Desafio 2 — Verificador de Palíndromo
- Arquivo: [desafios/desafio2.py](desafios/desafio2.py)
- Descrição: Leitor interativo que pergunta por uma palavra (ou frase simples) e verifica se é palíndromo usando `is_palindrome(word)` (ignora maiúsculas/minúsculas). O programa roda em loop até o usuário digitar `quit`.
- Execução: `python desafios/desafio2.py`
- Exemplo de uso:

```
Enter a word to check if it's a palindrome (or 'quit' to exit): radar
True
```

---

## Desafio 3 — Identificação de Duplicados
- Arquivo: [desafios/desafio3.py](desafios/desafio3.py)
- Descrição: Lê uma lista de números a partir de uma string no formato `[1,2,3]`, converte para inteiros e retorna os valores duplicados. A função auxiliar `count_occurrences(lst, item)` conta aparições (com comportamento de saída precoce quando já passou de 1).
- Execução: `python desafios/desafio3.py`
- Entrada esperada: algo como `[1,2,3,2,4,1]`
- Saída esperada: `Duplicates found: [1, 2]`

---

## Desafio 4 — Validação de Parênteses
- Arquivo: [desafios/desafio4.py](desafios/desafio4.py)
- Descrição: Implementa validação de parênteses/colchetes/chaves aninhados com `validate_parentheses(s)`. Usa pilha para rastrear aberturas e verifica fechamentos com `validate_closing_parentheses(stack, char)`. Inclui um conjunto de testes simples que exercitam casos válidos e inválidos.
- Execução: `python desafios/desafio4.py`

---

## Desafio 5 — Agrupamento por Categoria (soma de valores)
- Arquivo: [desafios/desafio5.py](desafios/desafio5.py)
- Descrição: Recebe uma lista de dicionários com chaves `categoria` e `valor` e retorna um dicionário com a soma dos valores por categoria. Função principal: `data_clustering_by_category(input_list)`.
- Execução: `python desafios/desafio5.py`
- Exemplo de entrada (no próprio arquivo):

```
[{'categoria': 'Alimentação', 'valor': 10},
 {'categoria': 'Transporte', 'valor': 5},
 {'categoria': 'Alimentação', 'valor': 20},
 {'categoria': 'Lazer', 'valor': 50}]
```
- Saída esperada:

```
{'Alimentação': 30, 'Transporte': 5, 'Lazer': 50}
```

---

## Como executar
- Recomendado: Python 3.8+ instalado.
- Comando geral para rodar um desafio (exemplo `desafio2`):

```bash
python desafios/desafio2.py
```
