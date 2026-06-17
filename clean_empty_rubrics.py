with open('sequences/kiriaki-ton-vaion-esperas.md', 'r') as f:
    lines = f.read().split('\n')

new_lines = []
for i, line in enumerate(lines):
    # If it's a rubric line "> Ὁ ἱερεύς" or "> Ὁ χορός", check if the next line is also a rubric or a heading
    # Wait, the user specifically mentioned lines 510-520 which is a block of them.
    # We can just remove lines that are exactly "> Ὁ ἱερεύς" or "> Ὁ χορός"
    # IF the next line is ALSO one of those, or is empty, or is a heading.
    # Actually, let's only keep "> Ὁ ἱερεύς" if the next line is NOT "> Ὁ χορός" or "> Ὁ ἱερεύς" etc.
    if line.strip() in ['> Ὁ ἱερεύς', '> Ὁ χορός', '> Ὁ ἱερεύς ποιεῖ τήν Ἀπόλυσιν.']:
        # check next non-empty line
        j = i + 1
        has_text = False
        while j < len(lines):
            nxt = lines[j].strip()
            if nxt == '':
                j += 1
                continue
            if nxt.startswith('> ') or nxt.startswith('## '):
                # Next thing is another rubric or heading, so current one has no text
                has_text = False
                break
            else:
                has_text = True
                break
        
        if not has_text:
            print(f"Removing empty rubric at line {i+1}: {line}")
            continue

    new_lines.append(line)

with open('sequences/kiriaki-ton-vaion-esperas.md', 'w') as f:
    f.write('\n'.join(new_lines))
