from pathlib import Path

BASE = Path(__file__).resolve().parent
STATIC = BASE / 'static'
STATIC.mkdir(exist_ok=True)

INDEX_PARTS = sorted((BASE / 'source_parts' / 'index').glob('part_*.txt'))
SERVER_PARTS = sorted((BASE / 'source_parts' / 'server').glob('part_*.txt'))
if not INDEX_PARTS or not SERVER_PARTS:
    raise RuntimeError('server source parts not found')

# index hotfix fragments are injected before </body> so the generated HTML stays valid.
fix_parts=[p for p in INDEX_PARTS if 'fix' in p.stem]
base_parts=[p for p in INDEX_PARTS if p not in fix_parts]
html=''.join(p.read_text(encoding='utf-8') for p in base_parts)
fix='\n'.join(p.read_text(encoding='utf-8') for p in fix_parts)
if fix:
    html=html.replace('</body>',fix+'\n</body>',1)
(STATIC / 'index.html').write_text(html,encoding='utf-8')

SOURCE = ''.join(p.read_text(encoding='utf-8') for p in SERVER_PARTS)
# Execute the assembled runtime with a non-main name so the original embedded
# main guard does not start the server before later hotfix definitions load.
runtime={'__name__':'bamnolja_runtime','__file__':str(BASE/'server_full.py'),'__package__':None}
exec(compile(SOURCE, str(BASE / 'server_full.py'), 'exec'), runtime, runtime)
# Expose runtime objects for import-based checks/tests.
for k,v in runtime.items():
    if k not in {'__name__','__builtins__'}:
        globals()[k]=v

if __name__=='__main__':
    runtime['main']()
