# Assistente Amplia

O projeto é dividido em três partes:

- Sistema
- Burocracias de planejamento
- Burocracias de desenvolvimento

## Sistema

É a parte grossa, a parte principal do código que vamos desenvolver, o próprio "Assistente Amplia". Ele deve conter:

TODO: inserir requisitos do sistema

## Burocracias de planejamento

São os documentos de projeto relativos ao seu design e planejamento de estrutura e desenvolvimento. Aqui se encontram:

- Diagrama de Casos de Uso
- Diagrama de Classe
- Diagrama de Pacote
- Diagrama de Componentes (opcional)
- Diagrama de Sequência (opcional)
- Relatório em PDF com a cobertura do código

## Burocracias de implementação

Incluí basicamente os testes e requisitos não funcionais do sistema. Ou seja, são coisas que devemos ter em mente antes de começar a implementação do sistema, já que irão reger a forma como o código é desenvolvido.

- Evidências de TDD
    - Cada integrante deve ter duas unidades desenvolvidas com TDD
    - Cria-se um teste
    - Cria-se um código ruim que passa no teste
    - Faz-se refactor deixando o código bom
    - **! VALE NOTA:**
        - Commitar o código ruim antes de fazer o refactor
        - Utilizar comentários para marcar o estado do código:
            - red == código que não passa no teste
            - green == código que passa no teste
- Evidência de revisão de código
    - Implementar partes do sistema por branches
    - Abrir pull request
    - Alguém que não desenvolveu a branch aceitar/negar a pull request
- Boas práticas (que serão avaliadas)
    - Comentários
    - Documentação (DocString. PEP 257)
    - Código limpo e modularizado (PEP 8)
    - Exceções User-Defined Data Type
- Extra
    - Utilizar ferramenta de verificação de qualidade


