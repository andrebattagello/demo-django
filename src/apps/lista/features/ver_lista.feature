# language: pt-br

Funcionalidade: Ver lista completa de items
    Como um usuário anônimo
    Para que eu possa saber o que devo fazer e o que já fiz
    Eu gostaria de visualizar a lista completa de items

    Cenário: Lista vazia
        Dado que exista uma lista
            E a lista está vazia
        Quando eu ver a lista
        Então eu devo ser apresentado com "Lista Vazia"