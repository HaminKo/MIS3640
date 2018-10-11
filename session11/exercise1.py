def histogram(s):
    d = dict()
    for c in s:
        # d[c] = d.get(c , s.count(c))
        d[c] = d.get(c, 0) + 1
    return d

def print_hist(h):
    for c in h:
        print(c, h[c])
        
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

h = histogram('Massachusetts')
key = reverse_lookup(h, 2)
print(key)

key = reverse_lookup(h, 3)