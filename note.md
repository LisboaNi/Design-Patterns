# Componentes da Orientação a Objetos

**Encapsulamento**
- Convenção: `_nome_atributo` ou `__nome_atributo`
- Controla acesso aos atributos e métodos da classe

**Polimorfismo**
- Sobrescrita de métodos (ex: `__init__`)

**Herança**
- Classe Pai e Classe Filha

**Abstração**
- Classe ou função interna não visível ao usuário final

**Composição**
- Uma classe utiliza outra classe dentro dela

<br>

# Princípios SOLID

- **S – Single Responsibility Principle:** Uma classe deve ter apenas uma responsabilidade

- **O – Open/Closed Principle:** Classes devem ser abertas para extensão, mas fechadas para modificação

- **L – Liskov Substitution Principle:** Classes derivadas devem ser substituíveis por suas classes base sem alterar o comportamento

- **I – Interface Segregation Principle:** Interfaces específicas para cada cliente, evitando interfaces grandes e genéricas

- **D – Dependency Inversion Principle:** Classes devem depender de abstrações, não de implementações concretas

<br>

# Design Patterns (GoF)

### Taxonomia
- **Trecho de código:** Linguagem para determinado propósito
- **Design:** Solução para resolver um problema
- **Convenção:** Maneira de resolver um problema (_ex: `__` para privado_)
- **Padrão:** Solução eficiente e escalável

### Contexto
- **Participantes:** Classes envolvidas
- **Requisitos Não Funcionais:** Memória, desempenho, usabilidade
- **Negociações:** Decisões de implementação
- **Resultados:** Consequências do uso do padrão

### Classificação
- Padrões de Criação
- Padrões Estruturais
- Padrões Comportamentais

<br>

# Padrões de Criação

### Singleton
- Um único objeto e ponto de acesso global
- Exemplos: Log, conexão de BD, spoolers de impressão
- Vantagens: Controle de recurso compartilhado
- Desvantagens: Dependência de variável global

### Factory
- Criação de objetos sem expor lógica de construção
- Tipos:
  - **Simple Factory**
  - **Factory Method**
  - **Abstract Factory**
- Diferença: 
  - Factory Method usa herança para definir objeto
  - Abstract Factory usa composição para criar famílias de objetos

<br>

# Padrões Estruturais

### Facade
- Interface simplificada para um subsistema complexo

### Proxy
- Intermediário entre solicitante e provedor
- Tipos:
  - Virtual
  - Remoto
  - Proteção
  - Inteligente
- Diferença Proxy vs Facade:
  - Proxy controla acesso a um objeto
  - Facade simplifica interface de subsistema

<br>

# Padrões Comportamentais

### Observer
- Um objeto notifica dependentes sobre mudanças
- Modelos:
  - Pull: Observador busca os dados
  - Push: Observador recebe dados automaticamente

### Template Method
- Define passos de algoritmo, permitindo implementação em subclasses
- Hooks: Métodos com implementação default
- Princípio Hollywood: "Não nos ligue, nós ligaremos para você"

### State 
- Um objeto pode encapsular vários comportamentos de acordo com o seu estado interno

<br>

# Padrões Compostos

### Model-View-Controller (MVC)
- Combina padrões para separar responsabilidades
- **Model:** Dados e lógica
- **View:** Apresentação
- **Controller:** Ponte entre Model e View