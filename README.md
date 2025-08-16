# Componentes

- **Encapsulamento:** Convenção _nome_atributo ou __nome_atributo, utiliza underline antes do nome do atributo.
- **Polimorfismo:** Sobrescrita de métodos com init
- **Herança:** Classe Pai e Classe Filha
- **Abstração:** Uma Classe / Função interna que não é visível para o usuário final
- **Composição:** Uma classe que utiliza outra classe dentro dela

<br>

# SOLID

- **Principio de aberto / fechado:** Determina que as clesses ou métodos devem ser abertos para extensão, mas fechados para modificação.
- **Principio da inversão de controle:** Determina que as classes devem depender de abstrações e não de implementações concretas. Os modulos devem ser independentes entre si.
- **Principio da segregação de interfaces:** Determina que as interfaces devem ser específicas para cada cliente, evitando a criação de interfaces grandes e genéricas.
- **Principio da responsabilidade:** Determina que uma classe deve ter apenas uma responsabilidade, ou seja, deve ser responsável por apenas uma parte do comportamento do sistema.
- **Principio da substituição de Liskov:** Determina que as classes derivadas devem ser substituíveis por suas classes base sem alterar o comportamento do programa.

<br>

# Design Patterns 

GoF (Gang of Four) - Os padrões de projeto foram inicialmente introduzidos como soluções para determinados problemas da orientação a objetos.

### Taxonomia 

Nem todo código ou design pode ser classificado como padrão.

- **Trecho de código:** Linguagem que serve a determinado propósito (Ex. Conexão com BD)
- **Design:** Solução para resolver um problema em particular
- **Convenção:** Maneira de resolver algum tipo de problema (__ para privado)
- **Padrão:** Solução eficiente e escalável

### Contexto

- **Participantes:** São classes usadas nos padrões, desempenham diferentes papéis para atingir vários objetivos.
- **Requisitos Não Funcionais:** Como otimização de memória, usabilidade e desempenho. Fatores exercem impacto na solução.
- **Negociações:** São decisões que você toma quando usar um padrão de projeto em sua aplicação.
- **Resultados:** Compreender as consequências do uso dos padrões de projeto.

### Classificação dos Padrões de Projeto

- Padrões de Criação
- Padrões Estruturais 
- Padrões Comportamentais 

<br>

# Singleton

- Padrão de Criação

Proporciona uma forma de ter um, e somente um, objeto de determinado tipo, além de um ponto de acesso global.

### Utiliza

Em resumo:

- Garantir que um objeto de determinada classe seja instanciado;
- Oferecer um ponto de acesso para o objeto que seja global;
- Controlar o acesso concorrente a recursos compartilhados.

<br>

Ex.: Logging (Log), Operações de BD e Spoolers de impressão

**Objetivo:** Evitar requesições conflitantes para o mesmo recurso.

### Desvantagens

- Variáveis globais podem ser alteradas por engano;
- Variáveis referênica podem ser criadas para o mesmo objeto;
- Classe que são dependente da variavel global de modo que exercer um impacto inesperado.

# Factory

- Padrão de Criação

### Utiliza

Em resumo:

É uma fábrica de objetos, refere-se um classe responsável por criar objetos de outros tipos. O cliente chama esse método com determinados parâmetros e retornar paar ele.

### Tipos

- **Simple Factory:** Permite que as interfaces criem objetos sem expor a lógica de sua criação;
- **Factory Method:** Permite que as interfaces criem objetos, mas adia a decisão para que as subclasses determinem a classe para a criação do objeto;
- **Abstract Factory:** Interface para criar objteros relacionados sem especificar/expor suas classes.

### Factory Method

- Flexibilidade;
- Baixo aclopamento;

### Factoty Method / Abstract Factory

Expõe um metodo ao cliente para ciar objetos **vs** Contém um ou mais metodos de fabrica para criar uma familia de objetos relacionado.
<br>
Usa herança e subclasses para definir o objeto a ser criado **vs** Usa composição para deletar  aresponsabilidade de criar objetos de outra classe.
<br>
Usado para criar um produto **vs** Usado para criar famílias de produtos relacionados.

