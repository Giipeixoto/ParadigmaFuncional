#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <limits>
#include <functional>

int gerarNumeroAleatorio(int intervalo) {
    return std::rand() % intervalo + 1;
}

std::string avaliarTentativa(int tentativa, int numeroAleatorio) {
    if (tentativa < numeroAleatorio) {
        return "O numero e maior!";
    } else if (tentativa > numeroAleatorio) {
        return "O numero e menor!";
    } else {
        return "Parabens! Voce acertou o numero!";
    }
}

std::string fornecerDicas(int tentativa, int numeroAleatorio) {
    int diferenca = std::abs(tentativa - numeroAleatorio);
    if (diferenca <= 10) {
        return "Voce esta muito perto!";
    } else if (diferenca <= 20) {
        return "Voce esta perto!";
    } else {
        return "Voce esta longe!";
    }
}


void jogar(int intervalo, int tentativasRestantes) {
    std::srand(std::time(0));
    int numeroAleatorio = gerarNumeroAleatorio(intervalo);
    int tentativa;
    bool acertou = false;

    std::cout << "Tente adivinhar o numero entre 1 e " << intervalo << "." << std::endl;

    while (tentativasRestantes > 0 && !acertou) {
        std::cout << "Digite sua tentativa (tentativas restantes: " << tentativasRestantes << "): ";
        std::cin >> tentativa;

        if (std::cin.fail() || tentativa < 1 || tentativa > intervalo) {
            std::cout << "Entrada invalida. Por favor, insira um numero entre 1 e " << intervalo << "." << std::endl;
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        std::string resultado = avaliarTentativa(tentativa, numeroAleatorio);
        std::cout << resultado << std::endl;

        if (resultado == "Parabens! Voce acertou o numero!") {
            acertou = true;
        } else {
            std::cout << fornecerDicas(tentativa, numeroAleatorio) << std::endl;
        }

        tentativasRestantes--;
    }

    if (!acertou) {
        std::cout << "Voce perdeu. O numero era " << numeroAleatorio << "." << std::endl;
    }
}


void mostrarRegras() {
    std::cout << "Regras do Jogo de Adivinhacao:" << std::endl;
    std::cout << "1. O computador escolhe um numero entre 1 e 100." << std::endl;
    std::cout << "2. Voce tem um numero limitado de tentativas para adivinhar o numero." << std::endl;
    std::cout << "3. Após cada tentativa, o jogo dira se o numero e maior ou menor." << std::endl;
    std::cout << "4. Tente acertar o numero antes que suas tentativas se esgotem!" << std::endl;
}

int main() {
    int escolha;

    do {
        std::cout << "Menu:" << std::endl;
        std::cout << "1. Jogar" << std::endl;
        std::cout << "2. Regras" << std::endl;
        std::cout << "3. Sair" << std::endl;
        std::cout << "Escolha uma opcao: ";
        std::cin >> escolha;

        if (std::cin.fail()) {
            std::cout << "Entrada invalida. Tente novamente." << std::endl;
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            escolha = 0;
        }

        switch (escolha) {
            case 1:
                {
                    int intervalo = 100;
                    int tentativasRestantes = 10;
                    int dificuldade;

                    std::cout << "Escolha o nivel de dificuldade (1 - Facil, 2 - Medio, 3 - Dificil): ";
                    std::cin >> dificuldade;

                    if (std::cin.fail() || dificuldade < 1 || dificuldade > 3) {
                        std::cout << "Entrada invalida. Considerando nivel de dificuldade Facil." << std::endl;
                        dificuldade = 1;
                    }

                    if (dificuldade == 2) {
                        intervalo = 500;
                        tentativasRestantes = 7;
                    } else if (dificuldade == 3) {
                        intervalo = 1000;
                        tentativasRestantes = 5;
                    }

                    jogar(intervalo, tentativasRestantes);
                }
                break;
            case 2:
                mostrarRegras();
                break;
            case 3:
                std::cout << "Saindo do jogo. Ate mais!" << std::endl;
                break;
            default:
                std::cout << "Opcao invalida. Tente novamente." << std::endl;
        }

    } while (escolha != 3);

    return 0;

}
