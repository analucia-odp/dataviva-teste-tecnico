# 🚀 Desafio Técnico - Bolsa de Pesquisa (DataViva)

Bem-vindo(a) ao desafio técnico para a vaga de Bolsa de Pesquisa em Engenharia de Software no DataViva!

Este teste tem como objetivo avaliar sua **lógica de programação** e familiaridade com **estruturas de dados**. Não buscamos código perfeito, mas sim entender como você pensa e resolve problemas.

## 📋 Instruções Gerais

1.  **Linguagem:** Você pode resolver os desafios utilizando **Python** ou **JavaScript/TypeScript**. Escolha a que você se sentir mais confortável.
2.  **Organização:** Separe cada desafio em um arquivo ou função diferente. Ex: `desafio1.js`, `desafio2.py`, etc.
3.  **Comentários:** Comente seu código explicando sua linha de raciocínio, especialmente se tomar alguma decisão de design.

---

## 🧩 Os Desafios

### 1. O Clássico FizzBuzz
Escreva um programa que imprima os números de 1 a 100.
* Para múltiplos de **3**, imprima `Fizz` em vez do número.
* Para múltiplos de **5**, imprima `Buzz` em vez do número.
* Para números múltiplos de **3 e 5** ao mesmo tempo, imprima `FizzBuzz`.

### 2. Verificador de Palíndromo
Crie uma função que receba uma palavra (string) e retorne `true` se ela for um palíndromo e `false` caso contrário.
* *Definição:* Palíndromo é uma palavra que pode ser lida da mesma forma de trás para frente.
* **Exemplos:** `"arara"` (true), `"ovo"` (true), `"casa"` (false).

### 3. Encontrar Duplicados
Dada uma lista de números inteiros, escreva uma função que identifique e retorne o número que aparece repetido.
* **Entrada:** `[1, 2, 3, 4, 2, 5]`
* **Saída Esperada:** `2`

### 4. Validação de Parênteses
Dada uma string contendo apenas os caracteres `(`, `)`, `{`, `}`, `[` e `]`, determine se a string é válida.
Uma string é válida se:
1.  Os parênteses abertos são fechados pelo mesmo tipo de parênteses.
2.  Os parênteses abertos são fechados na ordem correta.
* **Exemplos:**
    * `{[()]}` ✅ Válido
    * `{[(])}` ❌ Inválido (ordem errada)
    * `{{[[(]]}}` ❌ Inválido (falta fechar)

### 5. Manipulação de Dados (Bônus)

Este desafio simula um cenário comum no DataViva: agrupar dados para visualização.
Dado um array de objetos representando transações:

```json
[
  { "categoria": "Alimentação", "valor": 10 },
  { "categoria": "Transporte", "valor": 5 },
  { "categoria": "Alimentação", "valor": 20 },
  { "categoria": "Lazer", "valor": 50 }
]
```
Escreva uma função que retorne um objeto (ou dicionário) somando os valores por categoria.

* **Saída Esperada:** 

```json
{
  "Alimentação": 30,
  "Transporte": 5,
  "Lazer": 50
}
```

Excelente iniciativa, Samuel. Criar um repositório centraliza tudo e já serve como um filtro natural para quem sabe usar o básico de Git.

Preparei abaixo um modelo completo de README.md para você usar. Ele está formatado para ser profissional, acolhedor para estudantes e claro nos objetivos.

Você pode copiar o código abaixo, criar um arquivo README.md no seu repositório e commitar.

📄 Modelo de README.md para o Desafio
Markdown

# 🚀 Desafio Técnico - Bolsa de Pesquisa (DataViva)

Bem-vindo(a) ao desafio técnico para a vaga de Bolsa de Pesquisa em Engenharia de Software no DataViva!

Este teste tem como objetivo avaliar sua **lógica de programação** e familiaridade com **estruturas de dados**. Não buscamos código perfeito, mas sim entender como você pensa e resolve problemas.

## 📋 Instruções Gerais

1.  **Linguagem:** Você pode resolver os desafios utilizando **Python** ou **JavaScript/TypeScript**. Escolha a que você se sentir mais confortável.
2.  **Organização:** Separe cada desafio em um arquivo ou função diferente. Ex: `desafio1.js`, `desafio2.py`, etc.
3.  **Comentários:** Comente seu código explicando sua linha de raciocínio, especialmente se tomar alguma decisão de design.

---

## 🧩 Os Desafios

### 1. O Clássico FizzBuzz
Escreva um programa que imprima os números de 1 a 100.
* Para múltiplos de **3**, imprima `Fizz` em vez do número.
* Para múltiplos de **5**, imprima `Buzz` em vez do número.
* Para números múltiplos de **3 e 5** ao mesmo tempo, imprima `FizzBuzz`.

### 2. Verificador de Palíndromo
Crie uma função que receba uma palavra (string) e retorne `true` se ela for um palíndromo e `false` caso contrário.
* *Definição:* Palíndromo é uma palavra que pode ser lida da mesma forma de trás para frente.
* **Exemplos:** `"arara"` (true), `"ovo"` (true), `"casa"` (false).
* *Diferencial:* Ignorar letras maiúsculas/minúsculas.

### 3. Encontrar Duplicados
Dada uma lista de números inteiros, escreva uma função que identifique e retorne o número que aparece repetido.
* **Entrada:** `[1, 2, 3, 4, 2, 5]`
* **Saída Esperada:** `2`
* *Diferencial:* Tente resolver pensando em performance (evitar loops aninhados).

### 4. Validação de Parênteses
Dada uma string contendo apenas os caracteres `(`, `)`, `{`, `}`, `[` e `]`, determine se a string é válida.
Uma string é válida se:
1.  Os parênteses abertos são fechados pelo mesmo tipo de parênteses.
2.  Os parênteses abertos são fechados na ordem correta.
* **Exemplos:**
    * `{[()]}` ✅ Válido
    * `{[(])}` ❌ Inválido (ordem errada)
    * `{{[[(]]}}` ❌ Inválido (falta fechar)

### 5. Manipulação de Dados (Bônus)
Este desafio simula um cenário comum no DataViva: agrupar dados para visualização.
Dado um array de objetos representando transações:
```json
[
  { "categoria": "Alimentação", "valor": 10 },
  { "categoria": "Transporte", "valor": 5 },
  { "categoria": "Alimentação", "valor": 20 },
  { "categoria": "Lazer", "valor": 50 }
]
```
Escreva uma função que retorne um objeto (ou dicionário) somando os valores por categoria.

* **Saída Esperada:**

```json
{
  "Alimentação": 30,
  "Transporte": 5,'
  "Lazer": 50
}
```

## 📤 Como entregar
Crie um repositório no seu GitHub (pode ser público).

Faça o upload dos seus códigos.

Envie o link do repositório para o e-mail da vaga (dataviva.info@gmail.com) com o assunto: Desafio Técnico - [Seu Nome].

## 🚀 Boa sorte! 

