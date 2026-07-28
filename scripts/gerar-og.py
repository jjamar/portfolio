from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
import os

NM = "/sessions/vigilant-kind-heisenberg/mnt/Portfolio/node_modules/@fontsource"
TMP = "/sessions/vigilant-kind-heisenberg/mnt/outputs/fontes"; os.makedirs(TMP, exist_ok=True)

def woff2ttf(src, dst):
    f = TTFont(src); f.flavor = None; f.save(dst); return dst

FONTS = {
    "sora700": woff2ttf(f"{NM}/sora/files/sora-latin-700-normal.woff", f"{TMP}/sora700.ttf"),
    "sora600": woff2ttf(f"{NM}/sora/files/sora-latin-600-normal.woff", f"{TMP}/sora600.ttf"),
    "dm400":   woff2ttf(f"{NM}/dm-sans/files/dm-sans-latin-400-normal.woff", f"{TMP}/dm400.ttf"),
    "dm500":   woff2ttf(f"{NM}/dm-sans/files/dm-sans-latin-500-normal.woff", f"{TMP}/dm500.ttf"),
}

W, H = 1200, 630
CREME  = (245, 240, 232)
NAVY   = (13, 27, 42)
VERM   = (232, 76, 43)
LINHA  = (227, 220, 204)
MUTED  = (91, 102, 116)

img = Image.new("RGB", (W, H), CREME)
d = ImageDraw.Draw(img)

def F(nome, size): return ImageFont.truetype(FONTS[nome], size)
def largura(txt, fonte, track=0):
    return d.textlength(txt, font=fonte) + track * max(0, len(txt) - 1)
def escreve(x, y, txt, fonte, cor, track=0):
    if track == 0:
        d.text((x, y), txt, font=fonte, fill=cor); return x + d.textlength(txt, font=fonte)
    for ch in txt:
        d.text((x, y), ch, font=fonte, fill=cor)
        x += d.textlength(ch, font=fonte) + track
    return x

M = 76  # margem
util = W - 2 * M

# marca
escreve(M, 58, "JONATAN JAMAR", F("sora600", 20), NAVY, track=3.2)
# rotulo
escreve(M, 100, "SENIOR DIGITAL PRODUCT LEADER · PM BUILDER", F("sora600", 17), VERM, track=2.4)

# headline: ajusta corpo ate caber
linhas = ["Liderança de produto", "em escala de milhões.", "Capacidade de construção", "provada em produção."]
size = 62
while size > 34:
    f = F("sora700", size)
    if max(largura(l, f) for l in linhas) <= util: break
    size -= 1
f = F("sora700", size)
lh = int(size * 1.16)
y = 176
for i, l in enumerate(linhas):
    escreve(M, y, l, f, VERM if i >= 2 else NAVY)
    y += lh

# rodape
yl = H - 118
d.line([(M, yl), (W - M, yl)], fill=LINHA, width=1)

fm = F("sora600", 21)
fr = F("dm400", 19)
def seta(x, y, larg=20, cor=NAVY):
    """seta vetorial: a Sora latin nao traz o glifo U+2192"""
    d.line([(x, y), (x + larg, y)], fill=cor, width=2)
    d.line([(x + larg - 6, y - 5), (x + larg, y), (x + larg - 6, y + 5)], fill=cor, width=2, joint="curve")
    return x + larg

metricas = [("2M+", "usuários"), ("+36%", "MAU do App"), ("NPS", None), ("R$ 790 mil", "economia/ano")]
x = M
yb = yl + 30
for num, rot in metricas:
    if rot is None:
        xn = escreve(x, yb, "16", fm, NAVY)
        xn = seta(xn + 9, yb + 15) + 9
        xn = escreve(xn, yb, "47", fm, NAVY)
        escreve(xn + 9, yb + 3, "NPS B2B", fr, MUTED)
        x = xn + 9 + d.textlength("NPS B2B", font=fr) + 34
        continue
    xn = escreve(x, yb, num, fm, NAVY)
    escreve(xn + 9, yb + 3, rot, fr, MUTED)
    x = xn + 9 + d.textlength(rot, font=fr) + 34

fu = F("dm500", 20)
d.text((W - M - d.textlength("jonatanjamar.com.br", font=fu), yb + 2), "jonatanjamar.com.br", font=fu, fill=VERM)

img.save("/sessions/vigilant-kind-heisenberg/mnt/Portfolio/public/fotos/og.png", "PNG", optimize=True)
img.save("/sessions/vigilant-kind-heisenberg/mnt/outputs/og.png", "PNG", optimize=True)
print("corpo da headline:", size, "px")
print("tamanho:", round(os.path.getsize("/sessions/vigilant-kind-heisenberg/mnt/outputs/og.png")/1024, 1), "KB")
