# 📦 Sistema de Controle de Equipamentos

## O Sistema de Controle de Equipamentos tem como objetivo centralizar e otimizar a gestão interna das máquinas e equipamentos do Departanento de Suporte. Ele permitirá o rastreamento da localização física e do status de cada item, garantindo maior controle e precisão nos inventários.

### 🚀 Funcionalidades

🔐 Autenticação
- Login e cadastro utilizando o sistema de autenticação padrão do Django.
- Tela de perfil exibindo:
    - Nome de usuário
    - Nome completo
    - Email
    - Endereço (via API ViaCEP)
    - Data de registro


🛠️ Gerenciamento de Equipamentos
-Listagem completa de equipamentos
-Cadastro de novos equipamentos
-Edição de equipamentos existentes
-Exclusão lógica (soft delete)
-Página de “Excluídos” com:
    - Restaurar equipamento
    - Excluir definitivamente


📁 Modelos do Sistema
Opção de "Adicionar Equipamento"
- nome
- tipo
- Número de patrimonio
- status
- setor
- usuario atual
- observação


📍 Telas Implementadas

 - Login

 - Cadastro

 - Perfil do usuário

 - Listagem de equipamentos

 - Cadastro de equipamento

 - Edição de equipamento

 - Lista de excluídos
    - Onde é possível restaurar e excluir definivamente o equipamento


🧰 Tecnologias Utilizadas

- Python 

- Django 

- SQLite

- Bootstrap 

- JavaScript (para integração com ViaCEP)

- HTML/CSS


🧪 Funcionalidades Extras

- Integração com API ViaCEP
  
- Gráfico que mostra o status dos equipamentos(Em uso, Manutenção e Disponível)
  
- Verificação automática de endereço via CEP

- Checkbox para indicar se o usuário possui equipamento em casa


👩‍💻 Desenvolvido por
Bianca Alverne Dos Santos — estudante de Análise e Desenvolvimento de Sistemas
