Operação Modular
--
### Descrição do Trabalho


O trabalho consiste na implementação de uma aplicação baseada no modelo cliente-servidor para realizar cálculos de operações modulares. A aplicação permite que o cliente envie três valores inteiros (x, y e n) ao servidor. Este, por sua vez, processa os valores recebidos e realiza o cálculo da operação modular 
(𝑥 × 𝑦 ) mod 𝑛
(x×y)modn. Após realizar o cálculo, o servidor devolve o resultado ao cliente.

Este projeto tem como objetivo explorar e aplicar conceitos fundamentais de programação em rede (protocolo TCP/IP), bem como demonstrar o uso prático de operações matemáticas básicas dentro de um ambiente distribuído.

### Arquitectura do trabalho

IMAGEM DO PROJECTO

### Descrição da Arquitectura

### Cliente:
  Interage com o utilizador para recolher os dados de entrada (x, y e n).
Envia os dados para o servidor usando sockets.
Recebe o resultado do servidor e exibe-o ao utilizador.

### Servidor:
  Recebe os dados enviados pelo cliente.
Calcula o resultado da operação modular (x×y) mod  n.
Envia o resultado de volta ao cliente.

## Descrição da Implementação

### Implementação do Servidor
- Criar um socket que aguarde conexões de clientes.
- Quando um cliente se conecta, o servidor:
  1. Recebe os valores `x`, `y` e `n`.
  2. Calcula o resultado da operação \((x \times y) \mod n\).
  3. Envia o resultado de volta ao cliente.
- O servidor permanece disponível para atender novos pedidos enquanto está ativo.

### Implementação do Cliente
- Criar um socket para se conectar ao servidor.
- Recolher os dados (`x`, `y` e `n`) do utilizador.
- Enviar os dados para o servidor.
- Receber o resultado da operação do servidor.
- Exibir o resultado ao utilizador.

---

## Descrição do Trabalho
O trabalho consiste em implementar uma aplicação cliente-servidor que realiza a operação modular com multiplicação. O cliente envia três números inteiros (\(x, y, n\)) ao servidor, e este calcula o resultado da expressão \((x \times y) \mod n\). O servidor devolve o resultado ao cliente, que o apresenta ao utilizador. Este trabalho explora conceitos de programação de rede e matemática modular.

---

## Arquitectura do Trabalho

### Diagrama de Blocos
O fluxo de dados entre cliente e servidor é representado no seguinte diagrama de blocos:

1. O **Cliente** recolhe os números \(x\), \(y\) e \(n\) do utilizador e envia-os para o **Servidor**.
2. O **Servidor** processa os valores recebidos, calcula a operação \((x \times y) \mod n\) e envia o resultado de volta ao **Cliente**.
3. O **Cliente** apresenta o resultado ao utilizador.

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
2. Recolher os dados (\(x\), \(y\) e \(n\) do utilizador).
3. Enviar os dados para o servidor.
4. Receber o resultado da operação do servidor.
5. Exibir o resultado ao utilizador.

Código Implementado
---
### SERVIDOR



