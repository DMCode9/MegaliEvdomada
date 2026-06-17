import json
import os

def run():
    target_dir = '/Users/weril/Desktop/web apps/MegaliEvdomada/sequences'
    index_path = os.path.join(target_dir, 'index.json')
    
    with open(index_path, 'r', encoding='utf-8') as f:
        index_data = json.load(f)
        
    texts = {}
    for item in index_data:
        file_name = item['file']
        file_path = os.path.join(target_dir, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                texts[file_name] = f.read()
        else:
            texts[file_name] = ""
            
    glossary_path = os.path.join(target_dir, 'glossary.json')
    if os.path.exists(glossary_path):
        with open(glossary_path, 'r', encoding='utf-8') as f:
            glossary_data = json.load(f)
    else:
        glossary_data = {}
        
    bundle = {
        "index": index_data,
        "texts": texts,
        "glossary": glossary_data
    }
    
    bundle_js = f"window.SEQUENCE_BUNDLE = {json.dumps(bundle, ensure_ascii=False, indent=2)};"
    
    with open(os.path.join(target_dir, 'bundle.js'), 'w', encoding='utf-8') as f:
        f.write(bundle_js)
        
    print("bundle.js generated successfully.")

if __name__ == '__main__':
    run()
