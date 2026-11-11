from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw
from pathlib import Path
root=Path('/mnt/data/mastercolor-site/assets/imagens'); base=Path('/mnt/data')
ref=Image.open(base/'Homepage Vibrante da Tintas Mastercolor(1).png').convert('RGB')
src1=Image.open(base/'image(20261111-123521).png').convert('RGB')
src2=Image.open(base/'image(20261111-123530).png').convert('RGB')
src4=Image.open(base/'image(20261111-125538).png').convert('RGB')
src5=Image.open(base/'image(20261111-125548).png').convert('RGB')
src6=Image.open(base/'image(20261111-125558).png').convert('RGB')

def crop(im, rect, outfile, size=None, quality=90, brighten=1.0):
    c=im.crop(rect)
    if brighten != 1: c=ImageEnhance.Contrast(c).enhance(brighten)
    if size: c=c.resize(size, Image.Resampling.LANCZOS)
    c.save(root/outfile, 'WEBP', quality=quality, method=6)

crop(ref, (367,76,1024,351), 'hero/hero-sala.webp', (1314,550), 92)
crop(ref, (39,369,382,526), 'institucional/fabrica-ilustrativa.webp', (1029,471), 92)
cats=[('acrilicas',(47,596,206,675)),('oleo',(207,596,358,675)),('texturas',(366,596,515,675)),('esmaltes',(524,596,672,675)),('complementos',(683,596,832,675)),('solventes',(840,596,985,675))]
for nm,rect in cats:crop(ref,rect,f'categorias/{nm}.webp',(600,316),92)
prod=[('evolution',(83,781,226,891)),('premium',(234,781,375,891)),('standard',(382,781,519,891)),('fast-paint',(527,781,663,891)),('master-piso',(673,781,809,891)),('master-telha',(818,781,951,891))]
for nm,rect in prod: crop(ref,rect,f'produtos/{nm}.webp',(380,295),95)
# Additional products from real screenshots provided by user (screenshots of the public website)
crop(src1,(412,227,646,547),'produtos/evolution-original.webp',(380,520),90)
crop(src1,(188,670,405,862),'produtos/premium-original.webp',(420,372),92)
crop(src2,(841,691,1061,848),'produtos/standard-original.webp',(500,356),92)
crop(src4,(103,108,321,294),'produtos/oleo.webp',(450,385),92)
crop(src5,(746,45,995,436),'produtos/textura-lisa.webp',(385,602),92)
crop(src6,(103,148,424,386),'produtos/fast-paint-original.webp',(540,400),92)
# lifestyle environments
for nm,rect in [
 ('sala-neutra',(308,947,537,1084)),
 ('quarto-azul',(546,947,774,1084)),
 ('fachada-amarela',(782,947,998,1084))]:
 crop(ref,rect,f'ambientes/{nm}.webp',(916,548),93)
crop(ref,(0,1107,414,1242),'cores/master-mix-foto.webp',(1242,405),94)
crop(ref,(0,1312,221,1390),'institucional/rolo-tinta.webp',(884,312),93)
# Additional product card themed illustrated placeholders use product photos from same master images or via packaging mockup
# We only label assets as illustrative; see README for legal/accuracy caveat.
crop(ref,(0,1107,330,1242),'cores/leque-cores.webp',(990,405),93)
# Paint color palette visual for color page
p=Image.new('RGB',(1200,350),'white');d=ImageDraw.Draw(p)
colors=['#f5e8dd','#e4cdad','#b88f6e','#82919d','#183f65','#115078','#2d7573','#678d6b','#b0bb81','#f3b64f','#da844c','#ba625d','#894e61','#745f8c','#d6a9b5','#e6d9c3']
for i,co in enumerate(colors):
 x=i*75;d.rectangle((x,0,x+75,350),fill=co)
p.save(root/'cores/paleta.webp','WEBP',quality=94)
print('created',len(list(root.rglob('*.webp'))),'webp assets')
