import json

COLORS = {'key': '\033[36m', 'str': '\033[32m', 'num': '\033[33m', 'reset': '\033[0m'}

def render_tree(data, indent=0):
    prefix = "  " * indent
    lines = []
    if isinstance(data, dict):
        for k, v in data.items():
            ks = f'{COLORS["key"]}{k}{COLORS["reset"]}'
            if isinstance(v, (dict, list)):
                lines.append(f'{prefix}{ks}:')
                lines.extend(render_tree(v, indent+1))
            else:
                lines.append(f'{prefix}{ks}: {v}')
    elif isinstance(data, list):
        for i, v in enumerate(data):
            if isinstance(v, (dict, list)):
                lines.append(f'{prefix}[{i}]:')
                lines.extend(render_tree(v, indent+1))
            else:
                lines.append(f'{prefix}[{i}]: {v}')
    return lines
