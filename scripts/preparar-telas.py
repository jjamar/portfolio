from PIL import Image
import os

U = "/sessions/vigilant-kind-heisenberg/mnt/uploads"
D = "/sessions/vigilant-kind-heisenberg/mnt/Portfolio/public/fotos/feira-viva"
os.makedirs(D, exist_ok=True)

mapa = [
    ("Captura de tela 2026-07-27 215821.jpg", "01-descoberta"),
    ("Captura de tela 2026-07-27 215853.jpg", "02-feira"),
    ("Captura de tela 2026-07-27 215934.jpg", "03-reserva"),
    ("Captura de tela 2026-07-27 220003.jpg", "04-minhas-reservas"),
]

def ultima_linha_com_conteudo(im, tol=6):
    """acha a ultima linha que difere do fundo (canto inferior esquerdo)"""
    px = im.convert("RGB").load()
    w, h = im.size
    fundo = px[4, h - 4]
    for y in range(h - 1, 0, -1):
        for x in range(0, w, 3):
            r, g, b = px[x, y]
            if abs(r-fundo[0]) > tol or abs(g-fundo[1]) > tol or abs(b-fundo[2]) > tol:
                return y
    return h - 1

for origem, nome in mapa:
    im = Image.open(os.path.join(U, origem)).convert("RGB")
    w, h = im.size
    corte = min(h, ultima_linha_com_conteudo(im) + 48)
    im = im.crop((0, 0, w, corte))
    # normaliza largura para 1200
    if im.width != 1200:
        im = im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS)
    saida = os.path.join(D, nome + ".webp")
    im.save(saida, "WEBP", quality=88, method=6)
    print(f"{nome}.webp  {im.size[0]}x{im.size[1]}  {round(os.path.getsize(saida)/1024,1)} KB   (original {w}x{h})")
