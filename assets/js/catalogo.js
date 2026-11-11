(()=>{
 'use strict';
 const categories=window.MASTERCOLOR_CATEGORIES||[];
 const products=window.MASTERCOLOR_PRODUCTS||[];
 const filters=document.getElementById('catalog-filters');
 const grid=document.getElementById('catalog-grid');
 const search=document.getElementById('catalog-search');
 const count=document.getElementById('catalog-count');
 if(!filters||!grid||!search)return;
 const params=new URLSearchParams(location.search);
 let selected=categories.some(c=>c.id===params.get('categoria'))?params.get('categoria'):'todos';
 const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const catalogCard=p=>`<article class="catalog-card"><a class="catalog-card-picture" href="produto.html?id=${encodeURIComponent(p.id)}"><img src="${esc(p.image)}" loading="lazy" alt="${esc(p.name)}"></a><div class="catalog-card-content"><span class="catalog-card-category">${esc(p.categoryName)}</span><h3>${esc(p.name)}</h3><p>${esc(p.short)}</p><a class="btn btn-blue btn-small" href="produto.html?id=${encodeURIComponent(p.id)}">Ver detalhes <img class="icon icon-white" src="assets/icones/arrow-right.svg" alt=""></a></div></article>`;
 const getSearch=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().trim();
 function render(){
  filters.innerHTML=`<button type="button" class="filter-chip ${selected==='todos'?'active':''}" data-category="todos">Todos os produtos</button>`+categories.map(c=>`<button type="button" class="filter-chip ${selected===c.id?'active':''}" data-category="${c.id}">${esc(c.name)}</button>`).join('');
  const q=getSearch(search.value);
  const results=products.filter(p=>(selected==='todos'||p.category===selected)&&getSearch(p.name+' '+p.short+' '+p.categoryName).includes(q));
  count.textContent=`${results.length} ${results.length===1?'produto encontrado':'produtos encontrados'}`;
  grid.innerHTML=results.length?results.map(catalogCard).join(''):'<div class="catalog-no-results">Não encontramos produtos com esses filtros. Tente outra busca ou categoria.</div>';
  filters.querySelectorAll('button').forEach(btn=>btn.addEventListener('click',()=>{selected=btn.dataset.category;const url=new URL(location.href);if(selected==='todos')url.searchParams.delete('categoria');else url.searchParams.set('categoria',selected);history.replaceState(null,'',url.pathname+url.search);render();}));
 }
 search.addEventListener('input',render);
 render();
})();
