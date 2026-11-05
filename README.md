# Portfólio | Matheus Goveia

Site pessoal feito com FastAPI e Jinja2. A mesma base de dados alimenta a página e uma API REST com documentação interativa.

## Rodar localmente

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Abra http://127.0.0.1:8000 (site) e http://127.0.0.1:8000/docs (API).

## Como atualizar o conteúdo

Edite apenas o `data.py`: projetos, habilidades, experiências e certificados ficam lá. A página e a API se atualizam juntas.

- Novo projeto: adicione um `Projeto(...)` em `PROJETOS`. Marque `destaque=True` para ele virar o projeto em destaque, com imagem em `static/img/`.
- Novo certificado: adicione uma linha `_alura(...)` em `CERTIFICADOS`. Com `destaque=True` ele aparece na lista principal.
- Currículo: substitua `static/curriculo-matheus-goveia.pdf`.

## Endpoints

| Rota | O que devolve |
|------|---------------|
| `/` | Página do portfólio |
| `/api/perfil` | Dados do perfil |
| `/api/projetos` e `/api/projetos/{id}` | Projetos |
| `/api/habilidades` | Habilidades por categoria |
| `/api/experiencias` | Formação e experiência |
| `/api/certificados` | Certificados |
| `/health` | Verificação leve de disponibilidade |
| `/docs` | Documentação interativa (Swagger) |

## Estrutura

```
main.py        rotas e API
data.py        modelos Pydantic e todo o conteúdo
icons.py       ícones SVG inline
templates/     index.html
static/        style.css, imagens, ícones e currículo em PDF
```

Ícones: Font Awesome Free (CC BY 4.0).
