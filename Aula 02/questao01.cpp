#include <iostream>
#include <string>

int main() {
    std::string nome;
    int idade;

    // Solicitar o nome e a idade do usuário
    std::cout << "Digite o seu nome: ";
    std::getline(std::cin, nome);  // Usamos getline para capturar o nome com espaços

    std::cout << "Digite a sua idade: ";
    std::cin >> idade;

    // Exibir a mensagem com nome e idade
    std::cout << "Olá, " << nome << ", Você tem " << idade << " anos!" << std::endl;

    return 0;
}
