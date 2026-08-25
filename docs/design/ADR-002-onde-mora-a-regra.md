# ADR 002 — Onde mora a regra do campo telefone

## Problema

O campo `telefone` do model `Cliente` era um `CharField` simples, sem 
nenhuma restrição de formato. Isso permitia cadastrar valores como 
"abc", "telefone inválido" ou strings vazias com espaços — dados que 
não existem no mundo real.

Isso é um problema para o negócio porque o sistema GeoSolutions usa o 
telefone do cliente para contato direto sobre vencimentos de documentos 
e prazos de projetos. Um telefone inválido salvo no banco significa que, 
na hora em que a equipe precisar avisar o cliente sobre um prazo 
crítico, o contato simplesmente não existe ou não funciona — gerando 
risco de perda de prazo e falha de comunicação com o cliente.

## Decisão

Validar no **model**, usando `RegexValidator`, exigindo que o campo 
`telefone` contenha apenas dígitos, com 10 ou 11 caracteres 
(DDD + número). A regra foi colocada como `validator` do próprio campo 
em `models.py`, e não em uma validação feita na view ou no formulário.

## Alternativa descartada

Validar apenas no formulário da tela (admin ou ModelForm customizado).

Essa alternativa foi descartada porque ela só protege quem passa pelo 
formulário. Ela não protege quem grava o dado por outros caminhos, como:
- o shell do Django (`python manage.py shell`);
- um script de importação em massa de clientes;
- uma futura API que expõe o cadastro de clientes.

Em todos esses casos, o dado passaria direto para o banco sem checagem, 
porque o `save()` do model não valida nada por padrão — só quem chama 
`full_clean()` (como os formulários) dispara a validação.

## Consequência

Como a regra está no model, e não só na tela, quem gravar pelos fundos 
também é recusado — não importa se é pelo shell, por script ou por 
uma futura API. A validação passa a ser uma característica do dado, 
não da interface que o insere.

Como efeito colateral positivo, o admin do Django passou a recusar 
automaticamente valores inválidos, exibindo a mensagem de erro embaixo 
do campo, sem que precisássemos escrever nenhuma tela ou lógica extra 
de validação no admin.

## Commit

## Commit

`a3b1951c2245634e730e14cef104ada394a34c35`

