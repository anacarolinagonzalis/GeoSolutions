# ADR 001 - Uso do Django como framework backend

## Status
Aceito

## Contexto
Precisávamos escolher um framework backend para o sistema de 
"caderno digital de clientes". A equipe tem familiaridade limitada 
com backend e o prazo do Marco 1 é curto.

## Decisão
Usar Django (Python) com SQLite no ambiente de desenvolvimento.

## Justificativa
- Django tem ORM embutido, reduzindo a necessidade de escrever SQL manual.
- Curva de aprendizado documentada e com muito material em português.
- SQLite não exige configuração de servidor de banco, facilitando o setup inicial.
- Alternativas consideradas: Flask (mais leve, mas exigiria montar mais 
  estrutura manualmente) e Node/Express (equipe tem menos experiência).

## Consequências
- Positivo: desenvolvimento mais rápido no início.
- Negativo: será necessário migrar para PostgreSQL/MySQL antes de produção,
  pois SQLite não é recomendado para múltiplos usuários simultâneos.
