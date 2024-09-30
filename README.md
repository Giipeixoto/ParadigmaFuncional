# Projeto Paradigma Funcional

Este projeto é um exemplo de aplicação simples que utiliza o paradigma funcional em C++. O objetivo é demonstrar conceitos e práticas de programação funcional, incluindo funções de ordem superior, imutabilidade e composição de funções.

## Descrição

O projeto implementa um jogo de adivinhação em que o usuário deve adivinhar um número aleatório gerado pelo programa. O código é estruturado para seguir princípios de programação funcional, evitando efeitos colaterais e promovendo a reutilização de funções.

## Funcionalidades

- 🎲 Geração de um número aleatório.
- 💡 Solicitação de tentativas do usuário.
- ✅ Verificação das tentativas com feedback ao usuário.
- 🔄 Continuação do jogo até que o número correto seja adivinhado.

## Estrutura do Projeto

O projeto contém os seguintes arquivos:

- `main.cpp`: O arquivo principal com a lógica do jogo, implementada segundo o paradigma funcional.
- `jogo.py`: Um script Python para facilitar a execução do jogo compilado.

## Como Executar

### Compilação e Execução em C++

1. **Pré-requisitos**: Certifique-se de que o compilador `g++` está instalado e corretamente configurado no seu sistema.
2. **Navegue até o diretório** onde o arquivo `main.cpp` está localizado.
3. **Compile o código** usando o seguinte comando:

    ```bash
    g++ main.cpp -o jogo
    ```

4. **Execute o programa gerado**:

    ```bash
    ./jogo
    ```

### Execução Usando Python

Para facilitar a execução, você também pode usar o script Python fornecido:

1. **Compile o jogo** conforme as instruções acima.
2. **Execute o jogo** usando o script Python:

    ```bash
    python jogo.py
    ```

## Exemplo de Uso

Ao executar o programa, você será solicitado a adivinhar um número. O jogo continuará até que você forneça a resposta correta. O programa dará feedback se o número fornecido é maior ou menor do que o número aleatório.

### Demonstração

```plaintext
Adivinhe o número entre 1 e 100:
Seu palpite: 50
O número é maior.
Seu palpite: 75
O número é menor.
Seu palpite: 62
Parabéns! Você adivinhou o número!
