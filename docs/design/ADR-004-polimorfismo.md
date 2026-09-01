# ADR 004 — Onde polimorfismo caberia no nosso projeto

## Contexto
No nosso sistema de gestão de projetos de escritório de arquitetura/urbanismo,
temos a classe base `Projeto` e duas especializações: `ProjetoUrbano` e
`ProjetoRural`. Cada tipo de projeto calcula o prazo de entrega de forma
diferente (regras urbanas x regras rurais), além de terem cliente e título
em comum.

Hoje, cada subclasse sobrescreve o método `calcular_prazo()`, mas em várias
partes do sistema (admin, views, relatórios) ainda existe a tentação de usar
`if isinstance(projeto, ProjetoUrbano): ... elif isinstance(projeto, ProjetoRural): ...`
para decidir o que fazer com cada tipo, ao invés de simplesmente chamar o
método do objeto.

## Decisão
Vale aplicar polimorfismo de forma consistente: cada subclasse (`ProjetoUrbano`,
`ProjetoRural`) implementa seu próprio `calcular_prazo()`, e qualquer código
que precise desse valor apenas chama `projeto.calcular_prazo()`, sem saber
(nem precisar saber) qual subtipo está sendo tratado.

Isso evita blocos de `if/elif` espalhados pelo projeto (admin, views, relatórios)
sempre que precisarmos tratar tipos diferentes de projeto.

## Alternativa considerada
Manter `if isinstance(...)` nos lugares que precisam dessa lógica (ex.: na view
de listagem de projetos, ou num relatório de prazos). Funciona hoje porque só
existem dois tipos, mas cada novo tipo de projeto (ex.: `ProjetoIndustrial`)
exigiria caçar todos os `if/elif` no código e adicionar mais um bloco,
arriscando esquecer algum lugar e quebrar o comportamento.

## Consequência
Se seguirmos usando o método `calcular_prazo()` de forma polimórfica em todo
o projeto (admin, views, relatórios, API), adicionar um novo tipo de projeto
no futuro (ex.: `ProjetoIndustrial`) exigirá apenas criar a nova subclasse e
implementar seu `calcular_prazo()` — sem precisar tocar em nenhum código
que já existe e já funciona.

## Status
Proposto — já implementado parcialmente nos models (`calcular_prazo`), mas
ainda não aplicado de forma consistente em todo o projeto (admin, views).
