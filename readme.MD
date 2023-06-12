# Test-Driven Development (TDD)

## Introdução ao Test-Driven Development (TDD)

O Test-Driven Development (Desenvolvimento Orientado a Testes) é uma prática de desenvolvimento de software que envolve a escrita de testes automatizados **ANTES** da implementação do código. Com o TDD, o ciclo de desenvolvimento segue uma abordagem de "teste, código, refatoração", em que os testes são escritos primeiro, depois o código é desenvolvido para passar nesses testes e, em seguida, o código e os testes são refinados para melhorar a qualidade do software.

## Benefícios do Test-Driven Development

O TDD traz vários benefícios para o processo de desenvolvimento de software:

1. **Código mais confiável**: Como os testes são escritos antes da implementação, eles ajudam a garantir que o código esteja funcionando corretamente e cumpra os requisitos especificados.

2. **Design orientado a testes**: O TDD incentiva a criação de código modular e de fácil testabilidade. Ao escrever os testes primeiro, é necessário pensar na interface e nos casos de teste antes da implementação.

3. **Detecção precoce de bugs**: Os testes automatizados permitem detectar problemas e erros mais cedo no processo de desenvolvimento, facilitando sua correção antes que se tornem mais complexos e caros de resolver.

4. **Refatoração segura**: O TDD encoraja a refatoração contínua do código. Os testes fornecem uma rede de segurança, permitindo que você faça alterações no código com confiança, sabendo que os testes garantirão que a funcionalidade continue funcionando corretamente.

5. **Documentação viva**: Os testes servem como documentação executável do software, descrevendo como o código deve se comportar em diferentes situações. Isso facilita a compreensão e a manutenção do código ao longo do tempo.

## O ciclo TDD

O TDD segue um ciclo iterativo e incremental, composto por três etapas: teste, código e refatoração. Aqui está uma descrição detalhada de cada etapa:

1. **Teste**: Na etapa de teste, escrevemos um teste automatizado que descreve o comportamento esperado do código. O teste deve falhar inicialmente, pois o código correspondente ainda não foi implementado.

2. **Código**: Nesta etapa, implementamos o código mínimo necessário para fazer o teste passar. O objetivo é escrever o código mais simples possível para atender aos requisitos do teste.

3. **Refatoração**: Após o teste ter passado, podemos refatorar o código, melhorando sua qualidade sem alterar seu comportamento externo. Durante a refatoração, é importante garantir que todos os testes ainda passem, validando que as alterações não introduziram erros no código.

Esse ciclo é repetido várias vezes, adicionando novos testes e funcionalidades incrementalmente, ao mesmo tempo em que garantimos a integridade do código existente.

## Princípios do Test-Driven Development

O TDD é baseado em alguns princípios essenciais que orientam a sua prática:

1. **Teste primeiro**: O teste é escrito antes do código. Isso ajuda a direcionar a implementação e garante que o código seja testável desde o início.

2. **Testes automatizados**: Os testes devem ser automatizados, permitindo que sejam executados repetidamente sem intervenção manual. Isso garante a consistência e a agilidade na execução dos testes.

3. **Testes de unidade**: O foco principal do TDD são os testes de unidade, que verificam o comportamento de componentes individuais do código. Isolar as unidades de código é essencial para facilitar a identificação e correção de problemas.

4. **Refatoração contínua**: A refatoração é uma parte essencial do TDD. Ao melhorar a estrutura e a qualidade do código, garantimos sua manutenibilidade e evitamos a acumulação de dívidas técnicas.

## Conclusão

O Test-Driven Development é uma abordagem de desenvolvimento de software que enfatiza a criação de testes automatizados antes da implementação do código. Ao seguir esse ciclo de teste, código e refatoração, o TDD ajuda a melhorar a qualidade do código, a detectar problemas precocemente e a garantir a confiabilidade do software. Adotar o TDD como parte do processo de desenvolvimento pode resultar em um código mais confiável, modular e de fácil manutenção.

# Estrutura de um Teste Unitário

Um teste unitário é uma forma de validar o comportamento de uma unidade de código, como uma função, um método ou uma classe isolada, de maneira independente. Esses testes são escritos para garantir que cada unidade de código funcione corretamente e produza os resultados esperados.

## Componentes de um Teste Unitário

Um teste unitário geralmente é composto por três partes principais:

1. **Preparação (Setup)**: Nesta etapa, você configura o ambiente necessário para o teste. Isso pode incluir a criação de objetos, a definição de variáveis de teste, a configuração de parâmetros de entrada e qualquer outra ação necessária para preparar o cenário de teste.

2. **Execução**: Aqui é onde você executa a unidade de código que está sendo testada. Você chama a função, método ou classe e passa os argumentos apropriados.

3. **Verificação (Assert)**: Na fase de verificação, você verifica se o resultado da execução corresponde ao resultado esperado. Isso é feito usando declarações de assert, que comparam o valor obtido com o valor esperado. Se a asserção falhar, o teste é considerado um erro.

## Exemplo de Estrutura de um Teste Unitário

Aqui está um exemplo básico de como um teste unitário pode ser estruturado:

```python
import pytest

# Importe a unidade de código a ser testada
from minha_funcao import minha_funcao

# Defina uma função de teste usando o prefixo "test_"
def test_minha_funcao():
    # Preparação (Setup)
    # Configuração do ambiente de teste, criação de objetos, definição de variáveis, etc.

    # Execução
    resultado = minha_funcao(argumentos)

    # Verificação (Assert)
    assert resultado == resultado_esperado
```

Nesse exemplo, importamos a unidade de código que queremos testar, definimos uma função de teste com o prefixo "test_", preparamos o ambiente de teste, executamos a função a ser testada e verificamos se o resultado obtido corresponde ao resultado esperado usando a declaração assert.

## Frameworks de Teste

Existem várias estruturas e frameworks de teste disponíveis para diferentes linguagens de programação que facilitam a criação e execução de testes unitários. Alguns exemplos populares incluem o **pytest**, **unittest** (para Python), **JUnit** (para Java) e **Mocha** (para JavaScript). Essas estruturas fornecem recursos adicionais, como a organização de testes em suítes, a geração de relatórios de teste e a configuração de testes em massa.

## Conclusão

Os testes unitários desempenham um papel fundamental no desenvolvimento de software, garantindo a funcionalidade correta de cada unidade de código. Ao seguir a estrutura adequada de um teste unitário, você pode criar testes eficazes e confiáveis, ajudando a identificar problemas e a manter a qualidade do seu código. Utilizar frameworks de teste apropriados pode facilitar ainda mais o processo de escrita e execução de testes unitários.

# Requisitos Funcionais - Calculadora

1. A calculadora deve ser capaz de realizar a operação de adição entre dois números.
2. A calculadora deve ser capaz de realizar a operação de subtração entre dois números.
3. A calculadora deve ser capaz de realizar a operação de multiplicação entre dois números.
4. A calculadora deve ser capaz de realizar a operação de divisão entre dois números.
5. A calculadora deve tratar adequadamente erros e exceções, como divisão por zero ou entrada inválida.

## Observações:
- Todos os métodos de operação (add, subtract, multiply, divide) devem receber dois argumentos numéricos.
- O método de divisão (divide) deve lançar uma exceção do tipo CalculatorError se o segundo argumento for zero.
- O método de divisão (divide) deve retornar o resultado da divisão entre os dois números.
- A verificação de entrada é realizada pelo método privado _check_inputs, que lança uma exceção do tipo CalculatorError se algum dos argumentos não for um número válido.

###  Exemplo de calculadora com pessimas praticas
```
class Calculator:
    def add(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise Exception("Invalid input. Both inputs must be integers.")
        return a + b
    
    def subtract(self, a, b):
        if type(a) != int or type(b) != int:
            raise Exception("Invalid input. Both inputs must be integers.")
        return a - b
    
    def multiply(self, a, b):
        if not (type(a) == int and type(b) == int):
            raise Exception("Invalid input. Both inputs must be integers.")
        return a * b
    
    def divide(self, a, b):
        if type(a) is not int or type(b) is not int:
            raise Exception("Invalid input. Both inputs must be integers.")
        if b == 0:
            raise Exception("Cannot divide by zero.")
        return a / b
```

## Sobre Mim

![Lucas Balieiro](https://github.com/lucasbalieiro.png)


- Nome: Lucas Balieiro
- Formação: Ciência da Computação
- Idade: 26 anos
- Estado atual dos cabelos: Já fui menos calvo, mas ainda estou aqui!
- Experiência: 4 anos como Desenvolvedor Web
    - 1 ano no INDT (~~Sherlock-Holmes 4.0~~ e SMTExpert)
## Contato

Se você deseja entrar em contato comigo para fazer perguntas, fornecer feedback ou colaborar em projetos, você pode me encontrar nos seguintes canais:

- Github: [https://github.com/lucasbalieiro]
- LinkedIn: [https://www.linkedin.com/in/lucasbalieiro/]
