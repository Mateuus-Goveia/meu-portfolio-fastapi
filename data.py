"""Modelos (Pydantic) e conteúdo do portfólio.

Para atualizar o site, edite só este arquivo: projetos, certificados,
habilidades e experiências ficam aqui e alimentam tanto a página quanto a API.
"""
from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class Perfil(BaseModel):
    nome: str
    status: str
    headline: str
    resumo: str
    email: str
    localizacao: str
    github_url: str
    linkedin_url: str
    curriculo_url: str


class Projeto(BaseModel):
    id: int
    titulo: str
    descricao: str
    tecnologias: List[str]
    link_github: str
    link_extra: Optional[str] = None
    rotulo_extra: Optional[str] = None
    destaque: bool = False
    imagem: Optional[str] = None
    pontos: List[str] = Field(default_factory=list)
    icone: str = "code"
    aviso: Optional[str] = None


class GrupoHabilidades(BaseModel):
    categoria: str
    icone: str
    itens: List[str]


class Certificado(BaseModel):
    titulo: str
    instituicao: str
    url: str
    destaque: bool = False


class Experiencia(BaseModel):
    tipo: Literal["formacao", "trabalho"]
    titulo: str
    organizacao: str
    periodo: str
    descricao: List[str] = Field(default_factory=list)


PERFIL = Perfil(
    nome="Matheus Goveia",
    status="Disponível para estágio",
    headline="Construo ferramentas que resolvem problemas reais.",
    resumo=(
        "Estudante de Análise e Desenvolvimento de Sistemas, com Python, APIs e bancos de dados. "
        "Estou em busca do meu primeiro estágio em desenvolvimento de sistemas."
    ),
    email="mateuus.goveia@gmail.com",
    localizacao="Rio de Janeiro - RJ",
    github_url="https://github.com/Mateuus-Goveia",
    linkedin_url="https://www.linkedin.com/in/matheus-goveia",
    curriculo_url="/static/curriculo-matheus-goveia.pdf",
)

PROJETOS: List[Projeto] = [
    Projeto(
        id=1,
        titulo="Buff Tracker",
        descricao=(
            "App desktop para Windows que avisa quando um buff está prestes a acabar. "
            "Nasceu de um problema meu: eu sempre esquecia de renovar os buffs durante o jogo."
        ),
        tecnologias=["Python", "PySide6 (Qt)", "pytest", "GitHub Actions", "PyInstaller"],
        link_github="https://github.com/Mateuus-Goveia/buff-tracker",
        link_extra="https://github.com/Mateuus-Goveia/buff-tracker/releases",
        rotulo_extra="Baixar a versão beta",
        destaque=True,
        imagem="/static/img/buff-tracker-app.webp",
        pontos=[
            "Timers configuráveis, com overlay translúcido sempre no topo e alerta sonoro",
            "Interface em português e inglês, 22 sons de lembrete, atalhos por teclado ou controle",
            "Versão portátil para Windows, que não exige Python instalado",
            "Testes automatizados, integração contínua, changelog e licença MIT",
        ],
        icone="gamepad",
        aviso="Projeto independente, sem vínculo com a Nexon. Desenvolvido com apoio de IA (Claude e Codex): eu defini os requisitos, revisei, testei e corrigi o código.",
    ),
    Projeto(
        id=2,
        titulo="Este portfólio",
        descricao=(
            "Site em FastAPI e Jinja2 que apresenta meus projetos, e que também "
            "oferece os mesmos dados por uma API REST com documentação interativa."
        ),
        tecnologias=["Python", "FastAPI", "Jinja2", "Pydantic"],
        link_github="https://github.com/Mateuus-Goveia/meu-portfolio-fastapi",
        link_extra="/docs",
        rotulo_extra="Ver a API",
        icone="server",
    ),
    Projeto(
        id=3,
        titulo="Sistema RPG em POO",
        descricao=(
            "Aplicação em Python que usa herança, encapsulamento e polimorfismo "
            "para modelar personagens e combates."
        ),
        tecnologias=["Python", "POO"],
        link_github="https://github.com/Mateuus-Goveia/sistema-rpg-poo",
        icone="dice-d20",
    ),
    Projeto(
        id=4,
        titulo="Sabor Express OO",
        descricao=(
            "Sistema interativo de gerenciamento e modelagem de restaurantes em Python, "
            "com foco em código limpo."
        ),
        tecnologias=["Python", "POO"],
        link_github="https://github.com/Mateuus-Goveia/sabor-express-oo",
        icone="utensils",
    ),
]

HABILIDADES: List[GrupoHabilidades] = [
    GrupoHabilidades(
        categoria="Fundamentos",
        icone="lightbulb",
        itens=["Lógica de programação", "POO", "Algoritmos", "Estruturas de dados", "Big O"],
    ),
    GrupoHabilidades(
        categoria="Python e APIs",
        icone="python",
        itens=["Python", "FastAPI", "APIs REST", "Pydantic", "pytest"],
    ),
    GrupoHabilidades(
        categoria="Banco de dados",
        icone="database",
        itens=["SQL", "PostgreSQL", "MySQL", "SQLAlchemy", "Modelagem de dados"],
    ),
    GrupoHabilidades(
        categoria="Ferramentas",
        icone="screwdriver-wrench",
        itens=["Git e GitHub", "GitHub Actions", "Linux (Mint e WSL)", "Shell script", "PySide6 (Qt)"],
    ),
]

EXPERIENCIAS: List[Experiencia] = [
    Experiencia(
        tipo="formacao",
        titulo="Análise e Desenvolvimento de Sistemas",
        organizacao="Uniasselvi",
        periodo="Jan/2026 – Jul/2028 (previsto)",
    ),
    Experiencia(
        tipo="formacao",
        titulo="Inglês",
        organizacao="Fluency",
        periodo="Set/2026 – Set/2027 (previsto)",
        descricao=["Leitura de documentação técnica: avançado. Conversação: básico."],
    ),
    Experiencia(
        tipo="trabalho",
        titulo="Assistente administrativo",
        organizacao="Giglio Revendedora Autorizada de Gás",
        periodo="Jul/2023 – Nov/2023",
        descricao=[
            "Liderei, junto a um colega, a padronização dos dados financeiros de 62 empresas, "
            "criando um novo modelo de controle, análise e consolidação de informações.",
            "A solução foi adotada como padrão pelo escritório e serviu de base para indicadores e relatórios gerenciais.",
            "Treinei a equipe no uso do novo processo.",
        ],
    ),
]


def _alura(titulo: str, codigo: str, destaque: bool = False) -> Certificado:
    return Certificado(
        titulo=titulo,
        instituicao="Alura",
        url=f"https://cursos.alura.com.br/certificate/{codigo}?lang=pt_BR",
        destaque=destaque,
    )


CERTIFICADOS: List[Certificado] = [
    _alura("Python: Avance na Orientação a Objetos e Consuma API", "b07b0809-be82-4fc7-8e2e-82667ce2bf90", True),
    _alura("Redes e Protocolos: Fundamentos da Web", "ba847461-8a1b-4927-92c2-45542f4c491f", True),
    _alura("Git e GitHub: Compartilhando e Colaborando em Projetos", "695fd2d0-cf6d-4389-9613-bb9726c25941", True),
    _alura("Estrutura de Dados em Python", "b72d41b3-4bfb-40c6-bb8e-fb8ba77c19f1", True),
    _alura("Consultas SQL no PostgreSQL", "09409ad7-8a90-471f-837e-3119bd3449bd", True),
    _alura("Arquitetura de Software e Boas Práticas", "409402c2-f810-4102-9ab9-09ed5f8c7067", True),
    _alura("Python: Crie a sua Primeira Aplicação", "a38ece32-c4ce-42ca-813d-0a6e8de056c7"),
    _alura("Python: Aplicando a Orientação a Objetos", "6340e6ae-3c2d-414e-b7d4-d795a42e52fb"),
    _alura("Aprofundando em Python", "f954f5ff-3eae-4314-86c7-c8460e26209b"),
    _alura("Lógica de Programação com Python", "6ea890f6-d563-4fab-b20d-aa8840596e9a"),
    _alura("HTTP: Entendendo a Web por Baixo dos Panos", "52519f54-1793-41bb-934f-c94fc8ca8d5c"),
    _alura("Terminal Linux: Comandos e Shell Script", "bd62d77e-b7b9-4d7a-90e4-608caebe86c0"),
    _alura("PostgreSQL: Primeiros Passos no Banco de Dados", "82132c16-1318-4b3a-b425-54ff7f8dd2ee"),
    _alura("Linux Mint: Trabalhando no Terminal", "7bfa5284-d507-4d5d-8cee-32c915063f4c"),
    _alura("Modelagem de Dados e Bancos Relacionais", "4272eb5c-fe9a-4ee9-9a6b-9d9e6aaa50c9"),
]
