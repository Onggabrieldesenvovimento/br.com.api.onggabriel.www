# Devops
```mermaid
%% Diagrama de Caso de Uso para o site da ONG Gabriel
%% Este diagrama considera as funcionalidades apresentadas na imagem

usecaseDiagram
  actor Usuário as "Usuário"
  actor Administrador as "Administrador do Site"
  
  Usuário --> (Visualizar Informações sobre a ONG)
  Usuário --> (Consultar Agenda de Eventos)
  Usuário --> (Doar para a ONG)
  Usuário --> (Cadastrar-se como Voluntário)
  Usuário --> (Entrar em Contato com a ONG)
  Usuário --> (Acessar Recursos de Ajuda)

  Administrador --> (Gerenciar Agenda de Eventos)
  Administrador --> (Gerenciar Inscrições de Voluntários)
  Administrador --> (Gerenciar Doações)
  Administrador --> (Publicar Informações sobre a ONG)
```