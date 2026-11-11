(()=>{
 'use strict';
 const products=window.MASTERCOLOR_PRODUCTS||[];
 const id=new URLSearchParams(location.search).get('id');
 const product=products.find(p=>p.id===id);
 const main=document.getElementById('product-detail');
 const related=document.getElementById('related-products');
 const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 if(!main)return;
 if(!product){main.innerHTML='<div class="catalog-no-results"><h2>Produto não encontrado</h2><p>Verifique o endereço e explore nosso catálogo completo.</p><p><a class="btn btn-yellow" href="produtos.html">Voltar ao catálogo</a></p></div>';if(related)related.innerHTML='';return;}
 document.title=product.name+' | Tintas Mastercolor';
 const meta=document.querySelector('meta[name="description"]');if(meta)meta.setAttribute('content',product.short);
 const spec=Object.entries(product.specs).map(([k,v])=>`<div class="product-spec-row"><dt>${esc(k)}</dt><dd>${esc(v)}</dd></div>`).join('');
 main.innerHTML=`<div class="product-layout"><div class="product-visual"><img src="${esc(product.image)}" alt="${esc(product.name)}"></div><div><p class="eyebrow">${esc(product.categoryName)}</p><h1 class="product-title">${esc(product.name)}</h1><p class="product-description">${esc(product.description)}</p>${product.illustrative?'<p class="section-lead"><small>Imagem ilustrativa da categoria. Foto oficial do produto a confirmar.</small></p>':''}<div class="product-meta"><span>${esc(product.categoryName)}</span><span>Mastercolor</span></div><div class="product-specs"><dl style="margin:0">${spec}</dl></div><div class="product-cta"><a class="btn btn-yellow" href="${(window.MASTERCOLOR_WHATSAPP_URL||((message)=>`https://wa.me/${window.MASTERCOLOR_CONFIG.whatsapp}?text=${encodeURIComponent(message)}`))(`Olá, Mastercolor! Gostaria de informações sobre o produto ${product.name}.`)}" target="_blank" rel="noopener noreferrer"><img class="icon" src="assets/icones/whatsapp.svg" alt=""> Solicitar informações</a><a class="btn btn-outline-blue" href="produtos.html?categoria=${encodeURIComponent(product.category)}">Ver categoria</a></div></div></div>`;
 const choice=products.filter(p=>p.category===product.category&&p.id!==product.id).concat(products.filter(p=>p.category!==product.category)).slice(0,4);
 if(related)related.innerHTML=choice.map(p=>`<article class="catalog-card"><a class="catalog-card-picture" href="produto.html?id=${encodeURIComponent(p.id)}"><img src="${esc(p.image)}" loading="lazy" alt="${esc(p.name)}"></a><div class="catalog-card-content"><h3>${esc(p.name)}</h3><a class="btn btn-blue btn-small" href="produto.html?id=${encodeURIComponent(p.id)}">Ver detalhes</a></div></article>`).join('');
 const crumb=document.querySelector('.breadcrumb');if(crumb)crumb.innerHTML='<a href="index.html">Início</a> / <a href="produtos.html">Produtos</a> / '+esc(product.name);
 const requested=new URLSearchParams(location.search).get('produto');
})();
