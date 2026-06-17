import os
import re
import json

def run():
    target_dir = '/Users/weril/Desktop/web apps/MegaliEvdomada/sequences'
    
    # 1. Strip [word]{translation} from all markdown files
    files = [f for f in os.listdir(target_dir) if f.endswith('.md')]
    for f in files:
        filepath = os.path.join(target_dir, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Regex to match [word]{translation} and replace with word
        # Note: some nested brackets might exist if script ran twice, but we'll try a generic replace:
        new_content = re.sub(r'\[([^\]]+)\]\{[^}]+\}', r'\1', content)
        
        # Run it twice in case there were double nestings like [[word]{trans}]{trans}
        new_content = re.sub(r'\[([^\]]+)\]\{[^}]+\}', r'\1', new_content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Cleaned {f}")
            
    # 2. Extract glossary from add_glossary.py
    import sys
    sys.path.append('/Users/weril/Desktop/web apps/MegaliEvdomada')
    from add_glossary import glossary
    
    # 3. Write glossary.json
    glossary_path = os.path.join(target_dir, 'glossary.json')
    with open(glossary_path, 'w', encoding='utf-8') as gf:
        json.dump(glossary, gf, ensure_ascii=False, indent=2)
    print("Created glossary.json")
    
if __name__ == '__main__':
    run()
