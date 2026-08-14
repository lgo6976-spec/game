from pathlib import Path

BASE = Path(__file__).resolve().parent
STATIC = BASE / 'static'
STATIC.mkdir(exist_ok=True)

INDEX_PARTS = sorted((BASE / 'source_parts' / 'index').glob('part_*.txt'))
SERVER_PARTS = sorted((BASE / 'source_parts' / 'server').glob('part_*.txt'))
if not INDEX_PARTS or not SERVER_PARTS:
    raise RuntimeError('server source parts not found')

(STATIC / 'index.html').write_text(
    ''.join(p.read_text(encoding='utf-8') for p in INDEX_PARTS),
    encoding='utf-8',
)
SOURCE = ''.join(p.read_text(encoding='utf-8') for p in SERVER_PARTS)
exec(compile(SOURCE, str(BASE / 'server_full.py'), 'exec'), globals(), globals())
