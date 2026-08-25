# ADR 001 — Proteção do campo data_vencimento

## Contexto
No sistema de gestão ambiental da Moriah Geotecnologia, cada projeto/processo
possui prazos importantes junto a órgãos ambientais (ex: renovação de licença,
entrega de laudo). O campo `data_vencimento` aceitava, hoje, qualquer data,
inclusive uma data anterior à data de início do processo (`data_inicio`) ou
uma data já vencida no momento do cadastro. Isso é um problema porque o
sistema depende desse campo para gerar alertas de vencimento — um dado
inconsistente compromete todo o controle de prazos, que é uma das
funcionalidades centrais do projeto.

## Decisão
Vamos validar o campo `data_vencimento` usando uma `@property` com setter na
classe do processo/projeto ambiental, garantindo que:
- a data de vencimento não pode ser anterior à data de início do processo;
- a data de vencimento não pode ser uma data já passada no momento do cadastro.

Caso alguma dessas regras seja violada, o setter levanta um `ValueError`,
impedindo que o dado inválido seja salvo no banco.

## Alternativa descartada
Consideramos validar essa regra apenas no formulário da tela de cadastro
(front-end). Descartamos essa opção porque não protegeria o dado quando o
processo for criado por outros caminhos, como no Django Admin, em scripts de
importação de planilhas antigas, ou em testes automatizados — cenários comuns
neste projeto, já que uma das motivações é migrar dados que hoje estão
dispersos em planilhas e e-mails.

## Consequência
O objeto responsável pelo processo ambiental passa a se proteger sozinho,
garantindo prazos coerentes independente de onde o registro seja criado. Em
troca, o código da classe fica um pouco maior, pois a lógica de validação
passa a viver dentro do setter em vez de apenas na interface.

## Commit
[preencher depois de fazer o commit da proteção no código]
