import re

with open('sequences/kiriaki-ton-vaion-esperas.md', 'r') as f:
    content = f.read()

pairs = content.split('|||')
print(f"Total pairs: {len(pairs)-1}")
# We have original before ||| and translation after |||
# The format is typically: 
# Original text
# |||
# Translated text
# (Next Original Text)
# |||

blocks = content.split('|||')
orig_words = 0
trans_words = 0

for i in range(len(blocks)-1):
    # original is the end of blocks[i] (after the last translation, or beginning if i=0)
    # Actually, it's easier to split by lines
    lines = blocks[i].split('\n')
    orig_text = '\n'.join([l for l in lines if l.strip() and not l.startswith('>') and not l.startswith('#')])
    
    lines2 = blocks[i+1].split('\n')
    # The translation is until the next > or # or empty line...
    # Let's just find the first paragraph in blocks[i+1]
    trans_text = ''
    for l in lines2:
        if l.strip() == '': continue
        if l.startswith('>') or l.startswith('#'): break
        trans_text += l + '\n'
        
    ow = len(orig_text.split())
    tw = len(trans_text.split())
    if abs(ow - tw) > 20:
        print(f"Mismatch in block {i}: Original words: {ow}, Trans words: {tw}")

