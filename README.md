# Operação Modular

## Descrição do Trabalho
Este trabalho consiste na implementação de uma aplicação baseada no modelo **cliente-servidor** para realizar cálculos de operações modulares. O cliente envia três valores inteiros (\(x\), \(y\) e \(n\)) ao servidor. O servidor processa os valores recebidos e calcula a operação modular \((x \times y) \mod n\). Após realizar o cálculo, o servidor devolve o resultado ao cliente.

### Objetivos
- Explorar conceitos fundamentais de programação em rede utilizando o protocolo **TCP/IP**.
- Demonstrar a aplicação prática de operações matemáticas básicas em um ambiente distribuído.
- Implementar uma arquitetura eficiente para comunicação cliente-servidor.

---

## Arquitetura do Trabalho

### Representação Gráfica
**[Inserir imagem do diagrama de blocos aqui]**

### Diagrama de Blocos
1. **Cliente** recolhe os números \(x\), \(y\) e \(n\) do utilizador e envia-os para o **Servidor**.
2. **Servidor** processa os valores recebidos, calcula a operação \((x \times y) \mod n\) e envia o resultado de volta ao **Cliente**.
3. **Cliente** apresenta o resultado ao utilizador.

---

## Descrição da Arquitetura

### Cliente
- Interage com o utilizador para recolher os dados de entrada (\(x\), \(y\) e \(n\)).
- Envia os dados para o servidor utilizando sockets.
- Recebe o resultado do servidor e exibe-o ao utilizador.

### Servidor
- Recebe os dados enviados pelo cliente.
- Calcula o resultado da operação modular \((x \times y) \mod n\).
- Envia o resultado de volta ao cliente.

---

## Descrição da Implementação

### Implementação do Servidor
1. Criar um socket que aguarde conexões de clientes.
2. Quando um cliente se conecta, o servidor:
   - Recebe os valores \(x\), \(y\) e \(n\).
   - Calcula o resultado da operação \((x \times y) \mod n\).
   - Envia o resultado de volta ao cliente.
3. O servidor permanece disponível para atender novos pedidos enquanto está ativo.

### Implementação do Cliente
1. Criar um socket para se conectar ao servidor.
2. Recolher os dados (\(x\), \(y\) e \(n\)) do utilizador.
3. Enviar os dados para o servidor.
4. Receber o resultado da operação do servidor.
5. Exibir o resultado ao utilizador.

---

## Código Implementado

### Servidor
