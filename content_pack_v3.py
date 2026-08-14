from pathlib import Path

BASE = Path(__file__).resolve().parent
PARTS = sorted((BASE / 'source_parts' / 'content').glob('part_*.txt'))
if not PARTS:
    raise RuntimeError('content source parts not found')
SOURCE = ''.join(p.read_text(encoding='utf-8') for p in PARTS)
exec(compile(SOURCE, str(BASE / 'content_pack_v3_full.py'), 'exec'), globals(), globals())
