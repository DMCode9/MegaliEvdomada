import json

with open('sequences/glossary.json', 'r', encoding='utf-8') as f:
    glossary = json.load(f)

glossary["ἀνομίαν"] = "αμαρτία / παρανομία"
glossary["ἀνομίαις"] = "αμαρτίες / παρανομίες"
glossary["ἀνόμημά"] = "αμάρτημα / παράβαση"
glossary["ἀνόμους"] = "παράνομους / αμαρτωλούς"

with open('sequences/glossary.json', 'w', encoding='utf-8') as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)
