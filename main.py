from typing import List, Optional
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Portfólio | Matheus Goveia")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Projeto(BaseModel):
    id: int
    titulo: str
    descricao: str
    tecnologias: List[str]
    link_github: str
    imagem_url: str

class Certificado(BaseModel):
    titulo: str
    instituicao: str
    url: str

class Habilidade(BaseModel):
    nome: str
    categoria: str
    icone: str  # Classe do FontAwesome

MEUS_PROJETOS: List[Projeto] = [
    Projeto(
        id=1,
        titulo="Sistema de Gestão para Pequenos Negócios",
        descricao="Projeto colaborativo em equipe centralizando vendas, clientes e operações, reduzindo processos manuais e automatizando a gestão.",
        tecnologias=["Python", "FastAPI", "SQL", "Análise de Requisitos"],
        link_github="https://github.com/mateuus-goveia",
        imagem_url="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500&q=80"
    ),
    Projeto(
        id=2,
        titulo="Sistema RPG em POO",
        descricao="Aplicação construída em Python aplicando conceitos avançados de Orientação a Objetos (herança, encapsulamento e polimorfismo).",
        tecnologias=["Python", "POO"],
        link_github="https://github.com/mateuus-goveia/sistema-rpg-poo",
        imagem_url="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=500&q=80"
    ),
    Projeto(
        id=3,
        titulo="Sabor Express OO",
        descricao="Sistema interativo de gerenciamento e modelagem de restaurantes em Python com foco em código limpo.",
        tecnologias=["Python", "POO"],
        link_github="https://github.com/mateuus-goveia/sabor-express-oo",
        imagem_url="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=500&q=80"
    ),
    Projeto(
        id=4,
        titulo="Portfólio Web & API FastAPI",
        descricao="Aplicação Web backend integrada com FastAPI e Jinja2 para expor projetos e documentação interativa via REST API.",
        tecnologias=["Python", "FastAPI", "Jinja2", "Pydantic"],
        link_github="https://github.com/mateuus-goveia/meu-portfolio-fastapi",
        imagem_url="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=500&q=80"
    )
]

MINHAS_HABILIDADES: List[Habilidade] = [
    Habilidade(nome="Python (POO, venv)", categoria="Linguagens", icone="fa-brands fa-python"),
    Habilidade(nome="FastAPI & REST APIs", categoria="Frameworks", icone="fa-solid fa-server"),
    Habilidade(nome="SQL (MySQL & PostgreSQL)", categoria="Bancos de Dados", icone="fa-solid fa-database"),
    Habilidade(nome="SQLAlchemy (ORM)", categoria="Bancos de Dados", icone="fa-solid fa-diagram-project"),
    Habilidade(nome="Git & GitHub", categoria="Ferramentas", icone="fa-brands fa-github"),
    Habilidade(nome="Linux Mint & WSL", categoria="Ambiente", icone="fa-brands fa-linux"),
    Habilidade(nome="Inglês (Fluency Academy)", categoria="Idiomas", icone="fa-solid fa-language")
]

CERTIFICADOS_ALURA: List[Certificado] = [
    Certificado(titulo="Python: Avance na Orientação a Objetos e Consuma API", instituicao="Alura", url="https://cursos.alura.com.br/certificate/b07b0809-be82-4fc7-8e2e-82667ce2bf90?lang=pt_BR"),
    Certificado(titulo="Redes e Protocolos: Fundamentos da Web", instituicao="Alura", url="https://cursos.alura.com.br/certificate/ba847461-8a1b-4927-92c2-45542f4c491f?lang=pt_BR"),
    Certificado(titulo="Git e GitHub: Compartilhando e Colaborando em Projetos", instituicao="Alura", url="https://cursos.alura.com.br/certificate/695fd2d0-cf6d-4389-9613-bb9726c25941?lang=pt_BR"),
    Certificado(titulo="Python: Crie a sua Primeira Aplicação", instituicao="Alura", url="https://cursos.alura.com.br/certificate/a38ece32-c4ce-42ca-813d-0a6e8de056c7?lang=pt_BR"),
    Certificado(titulo="Python: Aplicando a Orientação a Objetos", instituicao="Alura", url="https://cursos.alura.com.br/certificate/6340e6ae-3c2d-414e-b7d4-d795a42e52fb?lang=pt_BR"),
    Certificado(titulo="Aprofundando em Python", instituicao="Alura", url="https://cursos.alura.com.br/certificate/f954f5ff-3eae-4314-86c7-c8460e26209b?lang=pt_BR"),
    Certificado(titulo="Estrutura de Dados em Python", instituicao="Alura", url="https://cursos.alura.com.br/certificate/b72d41b3-4bfb-40c6-bb8e-fb8ba77c19f1?lang=pt_BR"),
    Certificado(titulo="Lógica de Programação com Python", instituicao="Alura", url="https://cursos.alura.com.br/certificate/6ea890f6-d563-4fab-b20d-aa8840596e9a?lang=pt_BR"),
    Certificado(titulo="HTTP: Entendendo a Web por Baixo dos Panos", instituicao="Alura", url="https://cursos.alura.com.br/certificate/52519f54-1793-41bb-934f-c94fc8ca8d5c?lang=pt_BR"),
    Certificado(titulo="Terminal Linux: Comandos e Shell Script", instituicao="Alura", url="https://cursos.alura.com.br/certificate/bd62d77e-b7b9-4d7a-90e4-608caebe86c0?lang=pt_BR"),
    Certificado(titulo="PostgreSQL: Primeiros Passos no Banco de Dados", instituicao="Alura", url="https://cursos.alura.com.br/certificate/82132c16-1318-4b3a-b425-54ff7f8dd2ee?lang=pt_BR"),
    Certificado(titulo="Consultas SQL no PostgreSQL", instituicao="Alura", url="https://cursos.alura.com.br/certificate/09409ad7-8a90-471f-837e-3119bd3449bd?lang=pt_BR"),
    Certificado(titulo="Linux Mint: Trabalhando no Terminal", instituicao="Alura", url="https://cursos.alura.com.br/certificate/7bfa5284-d507-4d5d-8cee-32c915063f4c?lang=pt_BR"),
    Certificado(titulo="Modelagem de Dados e Bancos Relacionais", instituicao="Alura", url="https://cursos.alura.com.br/certificate/4272eb5c-fe9a-4ee9-9a6b-9d9e6aaa50c9?lang=pt_BR"),
    Certificado(titulo="Arquitetura de Software e Boas Práticas", instituicao="Alura", url="https://cursos.alura.com.br/certificate/409402c2-f810-4102-9ab9-09ed5f8c7067?lang=pt_BR")
]

@app.get("/")
def home_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "desenvolvedor": "Matheus Goveia",
            "foco": "Backend Developer",
            "email": "mateuus.goveia@gmail.com",
            "localizacao": "Rio de Janeiro - RJ",
            "github_url": "https://github.com/mateuus-goveia",
            "linkedin_url": "https://www.linkedin.com/in/matheus-goveia",
            "curriculo_url": "/static/curriculo-matheus-goveia.pdf",
            "projetos": MEUS_PROJETOS,
            "habilidades": MINHAS_HABILIDADES,
            "certificados": CERTIFICADOS_ALURA
        }
    )