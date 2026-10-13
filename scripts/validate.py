from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
for name in ('xiaoxiaoyouqu.conf', 'back-cn.conf'):
    text = (root / name).read_text()
    assert '[General]' in text and '[Rule]' in text, name
    rules = [s.strip() for s in text.split('[Rule]', 1)[1].splitlines() if s.strip() and not s.strip().startswith('#')]
    assert rules[-1] == 'FINAL,DIRECT', name
    assert sum(r.startswith('FINAL,') for r in rules) == 1, name
    assert all(r.split(',')[0] in {'DOMAIN', 'DOMAIN-SUFFIX', 'IP-CIDR', 'IP-CIDR6', 'GEOIP', 'FINAL'} for r in rules), name
    assert not re.search(r'(?i)(password|token|secret)\s*=\s*\S+', text), name
    assert len(rules) == len(set(rules)), name
    print('PASS', name, len(rules), 'rules')
