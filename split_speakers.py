import re

with open('sequences/kiriaki-ton-vaion-esperas.md', 'r') as f:
    lines = f.readlines()

new_lines = []
pattern = re.compile(r'^(>\s*(?:Ὁ ἱερεύς|Ὁ χορός|Ο ἱερεύς|Ο χορός))[,·:]\s+(.+)$')

for line in lines:
    match = pattern.match(line.strip())
    if match:
        speaker = match.group(1)
        text = match.group(2)
        new_lines.append(f"{speaker}\n")
        new_lines.append(f"{text}\n")
    else:
        new_lines.append(line)

with open('sequences/kiriaki-ton-vaion-esperas.md', 'w') as f:
    f.writelines(new_lines)
print("Done")
