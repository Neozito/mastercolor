from pathlib import Path
p=Path('/mnt/data/mastercolor-site/assets/icones')
icons={
 'location':'<path d="M20 10c0 5-8 12-8 12S4 15 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
 'phone':'<path d="M22 16.9v3a2 2 0 0 1-2.2 2A19.7 19.7 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7l.6 2.8a2 2 0 0 1-.6 1.9L7.5 10a16 16 0 0 0 6.5 6.5l1.6-1.6a2 2 0 0 1 1.9-.6l2.8.6A2 2 0 0 1 22 16.9Z"/>',
 'mail':'<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m3 6 9 7 9-7"/>',
 'paint-roller':'<rect x="2" y="3" width="17" height="7" rx="1.5"/><path d="M19 6h2v6h-9v3M12 15v6M9 21h6"/>',
 'paintbrush':'<path d="m15 4 5 5-9 9-5-5 9-9ZM5 14l5 5M3 22c0-3 1-6 4-6 2 0 3 2 2 4-1 2-3 2-6 2Z"/>',
 'texture':'<path d="M3 3h18v18H3zM6 8l5-5M3 13 13 3M3 19 19 3M7 21 21 7M13 21l8-8M19 21l2-2"/>',
 'bucket':'<path d="M5 7h14l-1.5 14h-11L5 7ZM4 7h16M9 7V5a3 3 0 0 1 6 0v2"/>',
 'home':'<path d="m3 10 9-7 9 7v11h-7v-7h-4v7H3V10Z"/>',
 'flask':'<path d="M9 3h6m-5 0v7L4 20a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1l-6-10V3M7 16h10"/>',
 'arrow-right':'<path d="M5 12h14m-6-6 6 6-6 6"/>',
 'arrow-left':'<path d="M19 12H5m6-6-6 6 6 6"/>',
 'chevron-down':'<path d="m6 9 6 6 6-6"/>',
 'chevron-left':'<path d="m15 18-6-6 6-6"/>',
 'chevron-right':'<path d="m9 18 6-6-6-6"/>',
 'chat':'<path d="M21 11.5a8.4 8.4 0 0 1-.9 3.8A9 9 0 0 1 12 20a8.5 8.5 0 0 1-3.8-.9L3 21l1.9-5.2A8.5 8.5 0 0 1 4 12a9 9 0 0 1 4.7-8.1A8.4 8.4 0 0 1 12.5 3h.5a8.9 8.9 0 0 1 8 8v.5Z"/><path d="M8.5 11.7h.1m3.4 0h.1m3.4 0h.1"/>',
 'layers':'<path d="m12 2 10 5-10 5L2 7l10-5Zm-10 10 10 5 10-5M2 17l10 5 10-5"/>',
 'palette':'<path d="M12 3a9 9 0 0 0 0 18h1.2c1.7 0 2.5-1.8 1.6-3-.8-1.2-.3-2.5 1.4-2.5H18A4 4 0 0 0 22 12a9.5 9.5 0 0 0-10-9Z"/><circle cx="6.5" cy="11" r="1"/><circle cx="10" cy="7" r="1"/><circle cx="15" cy="7" r="1"/><circle cx="18" cy="11" r="1"/>',
 'award':'<circle cx="12" cy="8" r="6"/><path d="m8 13-1 9 5-3 5 3-1-9"/>',
 'calendar':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 2v6m10-6v6M3 11h18"/>',
 'tag':'<path d="m20 12-8 8-10-10V2h8l10 10ZM7 7h.01"/>',
 'search':'<circle cx="11" cy="11" r="7"/><path d="m16 16 5 5"/>',
 'menu':'<path d="M4 7h16M4 12h16M4 17h16"/>',
 'close':'<path d="M5 5 19 19M19 5 5 19"/>',
 'check':'<path d="m4 12 5 5L20 6"/>',
 'shield':'<path d="m12 2 9 4v7c0 5-4 8-9 9-5-1-9-4-9-9V6l9-4Z"/><path d="m8 12 3 3 5-6"/>',
 'facebook':'<path d="M15 21v-8h3l.5-4H15V7c0-1.2.4-2 2-2h2V1.5C18.5 1.2 17.5 1 16 1c-3.5 0-5 2-5 5v3H8v4h3v8h4Z"/>',
 'instagram':'<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>',
 'external':'<path d="M14 3h7v7m0-7-10 10M20 14v6H4V4h6"/>',
 'filter':'<path d="M4 7h16M7 12h10m-7 5h4"/>',
 'info':'<circle cx="12" cy="12" r="10"/><path d="M12 11v6m0-10h.01"/>',
 'drop':'<path d="M12 2S5 11 5 15a7 7 0 0 0 14 0c0-4-7-13-7-13Z"/>',
 'sparkles':'<path d="m12 3 2.5 6.5L21 12l-6.5 2.5L12 21l-2.5-6.5L3 12l6.5-2.5L12 3Z"/>',
}
for name, paths in icons.items():
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{paths}</svg>'
 (p/(name+'.svg')).write_text(svg, encoding='utf-8')

# Single-asset vector brand mark. This is a layout approximation; replace with official vector provided by brand before publication.
logo_dir=Path('/mnt/data/mastercolor-site/assets/imagens/logo')
for white in [False,True]:
 ink='#ffffff' if white else '#0b2056'
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="252" height="92" viewBox="0 0 252 92" role="img" aria-label="Mastercolor">
 <g font-family="Arial,Helvetica,sans-serif" fill="{ink}" font-style="italic" font-weight="900">
 <text x="3" y="51" font-size="56" letter-spacing="-3.2">Master</text>
 <text x="116" y="80" font-size="34" letter-spacing="-2">color</text>
 </g>
 <g transform="translate(4 62)">
 <rect width="18" height="14" fill="#ed2638"/><rect x="19" width="18" height="14" fill="#f3a422"/><rect x="38" width="18" height="14" fill="#f3d122"/><rect x="57" width="18" height="14" fill="#43b84a"/><rect x="76" width="18" height="14" fill="#00a0cb"/><rect x="95" width="18" height="14" fill="#1678c6"/>
 </g></svg>'''
 (logo_dir/('mastercolor-branco.svg' if white else 'mastercolor.svg')).write_text(svg,encoding='utf-8')
logo_dir.joinpath('master-mix.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 150"><g transform="translate(130 74)"><path d="M0 0 L-115 -9 A115 115 0 0 1 -100 -58Z" fill="#ee2c39"/><path d="M0 0 L-100 -58 A115 115 0 0 1 -65 -95Z" fill="#ff8f19"/><path d="M0 0 L-65 -95 A115 115 0 0 1 -18 -114Z" fill="#f7cf22"/><path d="M0 0 L-18 -114 A115 115 0 0 1 35 -109Z" fill="#48ae63"/><path d="M0 0 L35 -109 A115 115 0 0 1 82 -80Z" fill="#0e9abc"/><path d="M0 0 L82 -80 A115 115 0 0 1 113 -22Z" fill="#2369b6"/></g><text x="29" y="112" font-family="Arial" font-style="italic" font-weight="900" fill="#081d5a" font-size="38">Master Mix</text><text x="58" y="133" font-family="Arial" font-size="10" fill="#081d5a" letter-spacing="2">SISTEMA TINTOMÉTRICO</text></svg>''',encoding='utf-8')
print('icons',len(icons))
