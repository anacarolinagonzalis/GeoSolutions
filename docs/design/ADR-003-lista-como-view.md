# ADR 003 — A listagem é uma view, não o admin

Problema:    o admin do Django já mostra os dados de Clientes e Projetos.
             Por que escrever uma view e um template para mostrar a mesma
             coisa?

Decisão:     a listagem do sistema (páginas /clientes/ e /projetos/) é uma
             view própria, porque o admin é só para a equipe interna
             (porta de serviço). O usuário final do GeoSolutions nunca
             entra no admin.

Alternativa descartada: deixar o usuário ver os dados de clientes e
             projetos pelo admin do Django.
             O admin dá poder demais (editar, excluir tudo) e não tem a
             cara do nosso sistema.

Consequência: temos páginas próprias (listar_clientes e listar_projetos),
             que vamos evoluir para receber formulário de cadastro na
             próxima aula.

Commit:   