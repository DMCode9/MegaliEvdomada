with open('sequences/kiriaki-ton-vaion-esperas.md', 'r') as f:
    lines = f.read().split('\n')

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    new_lines.append(line)
    if line.strip() == '|||':
        if i + 1 < len(lines):
            new_lines.append(lines[i+1]) # The translation line
            i += 1
            # Next line should be empty if it's going to be a new original line, unless it's a heading or rubric
            if i + 1 < len(lines):
                next_line = lines[i+1].strip()
                if next_line != '' and not next_line.startswith('#') and not next_line.startswith('>'):
                    # Insert empty line!
                    new_lines.append('')
    i += 1

with open('sequences/kiriaki-ton-vaion-esperas_fixed.md', 'w') as f:
    f.write('\n'.join(new_lines))

print("Fixed!")
