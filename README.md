# Projetos

Aplicação Django para organizar anotações por tópicos. Usuários podem criar
tópicos e adicionar ou editar entradas em cada tópico.

## Requisitos

- Python
- Django 6.1.2
- django-bootstrap3 26.3

## Como executar

No PowerShell, na pasta do projeto:

```powershell
.\django_env\Scripts\Activate.ps1
python manage.py migrate
python manage.py runserver
```

Abra <http://127.0.0.1:8000/>.

## Login padrão local

- **Usuário:** `admin`
- **Senha:** `123`

A conta está cadastrada como superusuário no banco SQLite local (`db.sqlite3`).
Use essa senha fraca apenas para desenvolvimento local; não a utilize em
servidores ou ambientes compartilhados.

- Login da aplicação: <http://127.0.0.1:8000/users/login>
- Administração do Django: <http://127.0.0.1:8000/admin/>
