from typing import List

from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from data import (
    CERTIFICADOS,
    EXPERIENCIAS,
    HABILIDADES,
    PERFIL,
    PROJETOS,
    Certificado,
    Experiencia,
    GrupoHabilidades,
    Perfil,
    Projeto,
)
from icons import icon

app = FastAPI(
    title="Portfólio | Matheus Goveia",
    description="Site pessoal e API REST com os mesmos dados da página: projetos, habilidades, certificados e experiências.",
    version="2.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
templates.env.globals["icon"] = icon


@app.get("/", include_in_schema=False)
def home_page(request: Request):
    destaque = next((p for p in PROJETOS if p.destaque), None)
    outros = [p for p in PROJETOS if not p.destaque]
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "perfil": PERFIL,
            "destaque": destaque,
            "outros_projetos": outros,
            "habilidades": HABILIDADES,
            "experiencias": EXPERIENCIAS,
            "certificados_destaque": [c for c in CERTIFICADOS if c.destaque],
            "certificados_outros": [c for c in CERTIFICADOS if not c.destaque],
            "total_certificados": len(CERTIFICADOS),
        },
    )


@app.get("/health", tags=["Sistema"])
def health():
    """Resposta leve, boa para um monitor de uptime manter o site acordado."""
    return {"status": "ok"}


@app.get("/api/perfil", response_model=Perfil, tags=["API"])
def api_perfil():
    return PERFIL


@app.get("/api/projetos", response_model=List[Projeto], tags=["API"])
def api_projetos():
    return PROJETOS


@app.get("/api/projetos/{projeto_id}", response_model=Projeto, tags=["API"])
def api_projeto(projeto_id: int):
    for projeto in PROJETOS:
        if projeto.id == projeto_id:
            return projeto
    raise HTTPException(status_code=404, detail="Projeto não encontrado")


@app.get("/api/habilidades", response_model=List[GrupoHabilidades], tags=["API"])
def api_habilidades():
    return HABILIDADES


@app.get("/api/experiencias", response_model=List[Experiencia], tags=["API"])
def api_experiencias():
    return EXPERIENCIAS


@app.get("/api/certificados", response_model=List[Certificado], tags=["API"])
def api_certificados():
    return CERTIFICADOS
