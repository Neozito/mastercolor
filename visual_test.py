from playwright.sync_api import sync_playwright
from pathlib import Path
from urllib.parse import urljoin
import http.server, socketserver, threading
p=Path('/mnt/data/mastercolor-site')
class Handler(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**kw):super().__init__(*a,directory=str(p),**kw)
 def log_message(self,*a):pass
srv=socketserver.TCPServer(('127.0.0.1',8765),Handler)
t=threading.Thread(target=srv.serve_forever,daemon=True);t.start()
with sync_playwright() as w:
 browser=w.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for width,height in [(1024,850),(1440,900),(390,844)]:
  context=browser.new_context(viewport={'width':width,'height':height},device_scale_factor=1)
  page=context.new_page(); errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
  page.goto('http://127.0.0.1:8765/index.html',wait_until='load',timeout=30000)
  page.screenshot(path=f'/mnt/data/mastercolor-home-{width}.png',full_page=True)
  print(width,'title=',page.title(),'height=',page.locator('body').evaluate('(e)=>e.scrollHeight'),'overflow=',page.evaluate('document.documentElement.scrollWidth > window.innerWidth'),'images=',page.locator('img').count(),'broken=',page.locator('img').evaluate_all('(es)=>es.filter(e=>!e.complete || e.naturalWidth === 0).map(e=>e.src)'),'errors=',errors)
  context.close()
 context=browser.new_context(viewport={'width':1024,'height':850})
 for url in ['produtos.html','produtos.html?categoria=acrilicas','produto.html?id=acrilica-premium','produto.html?id=nope','contato.html','cores.html','sobre.html','master-mix.html','404.html']:
  page=context.new_page();errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
  r=page.goto('http://127.0.0.1:8765/'+url,wait_until='load',timeout=30000)
  print(url, r.status, 'title=',page.title(),'broken=',page.locator('img').evaluate_all('(es)=>es.filter(e=>!e.complete || e.naturalWidth === 0).map(e=>e.src)'),'errors=',errs)
  if url=='produtos.html':
   print('catalog count',page.locator('.catalog-card').count())
   page.locator('#catalog-search').fill('premium');print('search premium',page.locator('.catalog-card').count())
  page.close()
 browser.close()
srv.shutdown()
