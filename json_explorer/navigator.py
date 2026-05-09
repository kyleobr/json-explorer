def get_by_path(data, path):
    parts = path.replace('[', '.[').split('.')
    cur = data
    for p in parts:
        if p == '$': continue
        if p.startswith('[') and p.endswith(']'):
            cur = cur[int(p[1:-1])]
        else:
            cur = cur[p]
    return cur
