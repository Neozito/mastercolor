# Tintas Mastercolor — Website HTML estático

Website responsivo inspirado no layout de home aprovado, com catálogo de 13 linhas/produtos, detalhes técnicos, páginas institucionais, cores, Master Mix e contato.

## Como acessar

Abra `index.html` diretamente no navegador ou publique a pasta completa em um servidor estático (Cloudflare Pages, GitHub Pages, cPanel, etc.). A versão local funciona sem PHP e sem banco de dados. Para testar por um servidor local, execute `python -m http.server 8000` na pasta do site e acesse `http://localhost:8000/`.

## Páginas

- `index.html`: home fiel à estrutura de referência
- `sobre.html`: história e posicionamento
- `produtos.html`: catálogo com busca/filtros
- `produto.html?id=acrilica-premium`: ficha técnica dinâmica (13 produtos)
- `cores.html`: paleta de inspiração, não catálogo oficial
- `master-mix.html`: sistema tintométrico
- `contato.html`: dados e formulário que abre o cliente de e-mail
- `politica-privacidade.html`: política provisória para versão demonstrativa
- `404.html`: página de erro

## Imagens locais

Todas as imagens utilizadas estão em `assets/imagens`. São recortes otimizados das referências visuais fornecidas durante a conversa (incluindo a prévia aprovada) e de capturas de tela de páginas de produtos, **não fotos oficiais em alta resolução obtidas diretamente do fabricante**. Algumas embalagens da seção em destaque são representações visuais da arte-conceito. A imagem de fábrica também é ilustrativa: **não apresentá-la ao público como foto real da unidade**. Substituir pelos arquivos oficiais de foto/logotipo autorizados antes de publicação comercial. Logomarcas em SVG são aproximações reproduzidas da referência, não arquivos vetoriais oficiais. Nenhum produto sem foto verificada é apresentado como embalagem oficial: nesses casos aparece imagem de categoria e aviso na ficha.

## Dados e ajustes

- Produtos e especificações: `assets/js/produtos-data.js`
- E-mail, telefone e configuração do futuro WhatsApp: `assets/js/config.js`
- Estilos: `assets/css/style.css` e `responsive.css`
- Menu, hero, carrossel, galeria e formulário: `assets/js/main.js`
- Busca e filtros: `assets/js/catalogo.js`
- Fichas individuais: `assets/js/produto.js`

Informações técnicas foram transcritas das páginas públicas consultadas no site `tintasmastercolor.com.br` e prints fornecidos em novembro de 2026. **Reconfirmar atualizações técnicas, linhas em produção e rotulagem antes de publicar.**

O formulário usa `mailto:` e **não envia dados por conta própria**; não existe backend. Necessário instalar serviço de formulário ou endpoint apropriado para envio automatizado. O link de WhatsApp não foi publicado porque não há número oficial confirmado. Ícones sociais levam ao contato até que sejam fornecidos links oficiais, evitando inventar perfis.

O `sitemap.xml` e `robots.txt` consideram o domínio oficial como destino de publicação. **Ajuste o domínio se for publicar em ambiente diferente.** A página de política de privacidade é apenas inicial e precisa ser revisada conforme integrações futuras.

## Estrutura

- `assets/imagens/hero/` — arte do hero
- `assets/imagens/institucional/` — fábrica ilustrativa, rolo de pintura
- `assets/imagens/categorias/` — seis imagens de categorias
- `assets/imagens/produtos/` — fotos e imagens ilustrativas
- `assets/imagens/ambientes/` — três ambientes
- `assets/imagens/cores/` — Master Mix e paleta
- `assets/imagens/logo/` — logotipos vetoriais de demonstração
- `assets/icones/` — ícones SVG locais

Crédito de desenvolvimento: Agência Neo Arte.


## Atualizações de novembro de 2026

- Hero com três slides e troca automática a cada 5 segundos. Clique nos indicadores para escolher manualmente. A reprodução pausa quando a aba não está visível, durante navegação por teclado; usuários que preferem menos animação não recebem rotação automática.
- WhatsApp flutuante com ícone próprio em todas as páginas. Botões comerciais do cabeçalho, hero, banner, Master Mix e detalhes dos produtos abrem a conversa, com mensagem contextual.
- Formulário da página de contato envia os dados *para a tela de composição do WhatsApp*; o visitante precisa confirmar o envio no aplicativo. Nenhuma mensagem é enviada automaticamente.
- Mapa do Google Maps incorporado na página `contato.html`. O mapa requer conexão com a internet e pode depender da política de incorporação do Google.
- Logomarca Master Mix redesenhada para esta prévia em `assets/imagens/logo/master-mix-recriado.png`, baseada na arte de referência. Solicite o arquivo vetorial oficial da marca antes de publicar.
- Faixa azul inferior reorganizada com mais respiro entre texto, descrição e botões.

### IMPORTANTE: validar o número de WhatsApp antes de publicar

Foi usado provisoriamente o número **(45) 99973-3739**, encontrado em cadastro público da MASTERCOLOR LTDA ligado ao domínio `tintasmastercolor.com.br`. Ele **não foi confirmado no site institucional da E.L. Franco & Cia Ltda.** Confirme com o cliente se é o número comercial correto.

Para trocar em todo o projeto basta editar `window.MASTERCOLOR_CONFIG.whatsapp` em `assets/js/config.js` para os dígitos do número, por exemplo `5545XXXXXXXXX`. Não altere os links HTML individualmente: `main.js` atualiza-os ao carregar.

O endereço do mapa usa Rua Júlia Lemes de Carvalho, 52, conforme a página de contato do site institucional. Verifique a localização e o endereço atualizados antes de publicar.

**Não execute os scripts de geração legados (`build_site.py`, `build_assets.py`, `make_icons.py`) após fazer ajustes: eles pertencem à geração inicial e podem sobrescrever parte das alterações.**


### Ícones sociais no rodapé
- Facebook, Instagram e WhatsApp aparecem juntos na coluna Contato do rodapé.
- O botão verde de WhatsApp continua flutuante à direita.
- Os perfis oficiais de Facebook e Instagram não foram confirmados; os ícones são visuais, sem links ativos, até que os endereços oficiais sejam informados.
