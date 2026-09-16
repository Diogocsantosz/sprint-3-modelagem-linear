import nbformat as nbf
import re
from pathlib import Path

codigo = Path("challenge_sprint3.py").read_text(encoding="utf-8")

nb = nbf.v4.new_notebook()

md_intro = """# Challenge Sprint 3 - Probabilidade e Regressao Linear

## Integrantes
| Nome completo | RM |
|---|---|
| [COLOCAR NOME COMPLETO] | [RM xxxxxx] |
| [COLOCAR NOME COMPLETO] | [RM xxxxxx] |
| [COLOCAR NOME COMPLETO] | [RM xxxxxx] |

---

Base: **California Housing** (20.640 registros, salva em `california_housing.csv` pelo script `gerar_dados.py`).

- Variavel de probabilidade: **MedHouseVal** (valor mediano dos imoveis, em 100 mil US$)
- Variaveis da regressao: **MedInc** (renda mediana do bairro) -> **MedHouseVal**
"""
nb.cells.append(nbf.v4.new_markdown_cell(md_intro))

# separa o script nos blocos marcados por # ===...===
partes = re.split(r"# ={30,}\s*\n", codigo)

for i, bloco in enumerate(partes):
    if not bloco.strip():
        continue
    # tenta achar um titulo de secao nos comentarios iniciais do bloco
    linhas = bloco.splitlines()
    titulo = None
    for l in linhas[:6]:
        if l.startswith("# Q1") or l.startswith("# Q2") or l.startswith("# Q3"):
            titulo = l[2:].strip()
            break

    if titulo:
        nb.cells.append(nbf.v4.new_markdown_cell("## " + titulo))

    nb.cells.append(nbf.v4.new_code_cell(bloco.strip()))

nbf.write(nb, "challenge_sprint3.ipynb")
print("notebook criado com", len(nb.cells), "celulas")
