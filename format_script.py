import re

with open('sequences/kiriaki-ton-vaion-esperas.md', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    text = line.strip()
    if not text:
        new_lines.append("\n")
        continue

    # Titles
    title_keywords = [
        "Ακολουθία του Νυμφίου", "Κυριακή των Βαΐων εσπέρας",
        "Το Τρισάγιον", "Τροπάρια", "Καταβασία", "Εὐχὴ τοῦ ἁγίου Ἐφραίμ"
    ]
    is_title = any(text.startswith(k) for k in title_keywords) or \
               text.startswith("Ψαλμός") or \
               text.startswith("Ἦχος") or \
               text.startswith("ᾨδὴ")
    
    # Speaker / Directions
    direction_keywords = [
        "Ὁ ἱερεύς", "Ὁ χορός", "Ο ἱερεύς", "Ο χορός", "Καὶ πάλιν", 
        "Ἐκ τοῦ κατὰ Ματθαῖον", "Ἀρχόμεθα τοῦ Ἑξαψάλμου"
    ]
    is_direction = any(text.startswith(k) for k in direction_keywords)

    if is_direction:
        new_lines.append(f"> {text}\n")
    elif is_title:
        new_lines.append(f"## {text}\n")
    else:
        new_lines.append(line)

with open('sequences/kiriaki-ton-vaion-esperas.md', 'w') as f:
    f.writelines(new_lines)
print("Done")
