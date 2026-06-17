with open('sequences/kiriaki-ton-vaion-esperas.md', 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    if "> Ὁ ἱερεύς" in lines[i] and "> Ὁ χορός" in lines[i+1] and "> Ὁ ἱερεύς" in lines[i+2]:
        print(f"Match around line {i+1}")
        for j in range(max(0, i-2), min(len(lines), i+6)):
            print(f"{j+1}: {lines[j].strip()}")
