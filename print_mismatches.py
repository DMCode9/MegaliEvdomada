import re

with open('sequences/kiriaki-ton-vaion-esperas.md', 'r') as f:
    content = f.read()

blocks = content.split('|||')

for i in [115, 71, 16]:
    if i < len(blocks) - 1:
        orig = blocks[i].strip().split('\n')[-2:]
        trans = blocks[i+1].strip().split('\n')[:2]
        print(f"--- Block {i} ---")
        print("Original (last lines):", '\n'.join(orig))
        print("Translation (first lines):", '\n'.join(trans))

