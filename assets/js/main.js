(()=>{
  'use strict';
  document.querySelectorAll('.year').forEach(el => el.textContent=String(new Date().getFullYear()));
  const waNumber=String(window.MASTERCOLOR_CONFIG?.whatsapp||'').replace(/\D/g,'');
  const whatsappURL=message=>waNumber?`https://wa.me/${waNumber}?text=${encodeURIComponent(message)}`:null;
  window.MASTERCOLOR_WHATSAPP_URL=whatsappURL;
  // The WhatsApp number is controlled from assets/js/config.js.
  document.querySelectorAll('[data-whatsapp-message]').forEach(link=>{
    const url=whatsappURL(link.dataset.whatsappMessage);
    if(url){link.href=url;link.target='_blank';link.rel='noopener noreferrer';}
    else{link.href='contato.html';link.removeAttribute('target');}
  });
  const menu=document.getElementById('site-navigation');
  const toggle=document.getElementById('nav-toggle');
  if(toggle && menu){
    toggle.addEventListener('click',()=>{const isOpen=menu.classList.toggle('open');toggle.setAttribute('aria-expanded',String(isOpen));toggle.setAttribute('aria-label',isOpen?'Fechar menu':'Abrir menu');document.body.classList.toggle('menu-open',isOpen)});
    menu.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{menu.classList.remove('open');document.body.classList.remove('menu-open');toggle.setAttribute('aria-expanded','false')}));
    window.addEventListener('resize',()=>{if(window.innerWidth>680){menu.classList.remove('open');document.body.classList.remove('menu-open');toggle.setAttribute('aria-expanded','false')}});
  }
  const top=document.getElementById('back-top');
  if(top){const onScroll=()=>top.classList.toggle('show',window.scrollY>600);window.addEventListener('scroll',onScroll,{passive:true});onScroll();top.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));}
  const hero=document.querySelector('.hero');
  if(hero){
    const titles=[
      'Mastercolor.<br><span>Mais cor, qualidade<br>e vida</span> para seus<br> ambientes.',
      'Cores que<br><span>inspiram cada<br> novo espaço.</span>',
      'Sua casa.<br><span>Seu estilo.<br>Suas cores.</span>'
    ];
    const subs=[
      'Tintas e revestimentos desenvolvidos para transformar espaços com qualidade, tecnologia e acabamento.',
      'Descubra soluções em tintas e acabamentos para projetos com identidade e personalidade.',
      'Encontre produtos para valorizar ambientes internos, externos e superfícies especiais.'
    ];
    const dots=Array.from(hero.querySelectorAll('[data-slide]'));
    const title=document.getElementById('hero-title');
    const subtitle=document.getElementById('hero-subtitle');
    let active=0;
    let timer;
    const showSlide=index=>{
      active=(index+titles.length)%titles.length;
      hero.classList.remove('alt-1','alt-2');
      if(active)hero.classList.add('alt-'+active);
      if(title) title.innerHTML=titles[active];
      if(subtitle) subtitle.textContent=subs[active];
      dots.forEach((d,i)=>{const selected=i===active;d.classList.toggle('active',selected);d.setAttribute('aria-pressed',String(selected));});
    };
    const stop=()=>{if(timer)clearInterval(timer);timer=null;};
    const start=()=>{stop();if(!document.hidden && !window.matchMedia('(prefers-reduced-motion: reduce)').matches){timer=setInterval(()=>showSlide(active+1),5000);}};
    dots.forEach(dot=>dot.addEventListener('click',()=>{showSlide(Number(dot.dataset.slide));start();}));
    document.addEventListener('visibilitychange',start);
    hero.addEventListener('focusin',stop);
    hero.addEventListener('focusout',e=>{if(!hero.contains(e.relatedTarget))start();});
    start();
  }
  const featured=document.getElementById('featured-grid');
  if(featured){
    const prev=document.querySelector('.carousel-prev'),next=document.querySelector('.carousel-next');
    const scrollByCard=direction=>{const card=featured.querySelector('.featured-card');if(!card)return;const gap=12;featured.scrollBy({left:direction*(card.getBoundingClientRect().width+gap)*2,behavior:'smooth'});};
    if(prev)prev.addEventListener('click',()=>scrollByCard(-1));
    if(next)next.addEventListener('click',()=>scrollByCard(1));
    // Desktop: use a small offset animation on the row; on mobile use native scroll snapping.
    if(window.innerWidth>680){let page=0;function shift(dir){const cards=[...featured.children];if(cards.length<2)return;page=(page+dir+cards.length)%cards.length;featured.innerHTML='';cards.slice(page).concat(cards.slice(0,page)).forEach(c=>featured.appendChild(c));}if(prev)prev.addEventListener('click',()=>shift(-1));if(next)next.addEventListener('click',()=>shift(1));}
  }
  const lightbox=document.getElementById('lightbox');
  if(lightbox){
    const open=img=>{const target=lightbox.querySelector('img');target.src=img.src;target.alt=img.alt;lightbox.classList.add('open');document.body.style.overflow='hidden';lightbox.querySelector('button').focus()};
    const close=()=>{lightbox.classList.remove('open');document.body.style.overflow=''};
    document.querySelectorAll('.image-zoom img').forEach(img=>img.closest('button').addEventListener('click',()=>open(img)));
    lightbox.querySelector('button').addEventListener('click',close);
    lightbox.addEventListener('click',e=>{if(e.target===lightbox)close()});
    document.addEventListener('keydown',e=>{if(e.key==='Escape'&&lightbox.classList.contains('open'))close()});
  }
  const contact=document.getElementById('contact-form');
  if(contact){contact.addEventListener('submit',e=>{
    e.preventDefault();if(!contact.reportValidity())return;
    const val=name=>contact.elements.namedItem(name).value.trim();
    const body=`Olá, Mastercolor! Vim pelo site e gostaria de atendimento.\n\nNome: ${val('nome')}\nE-mail: ${val('email')}\nTelefone: ${val('telefone')||'Não informado'}\nAssunto: ${val('assunto')}\n\nMensagem: ${val('mensagem')}`;
    const url=whatsappURL(body);
    if(url)window.open(url,'_blank','noopener,noreferrer');
    else alert('Configure o número oficial do WhatsApp em assets/js/config.js para habilitar este envio.');
  });}

})();
