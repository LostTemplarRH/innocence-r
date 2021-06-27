from .script import Script, DecompilationException
import csv

def extract_dat(file):
    dat = file.open('rb')
    binary = dat.read()
    try:
        script = Script.decompile(binary)
    except DecompilationException as e:
        print(f'error while decompiling {file}: {e}')
        #with open(f'{file.path.replace("/", "_")}.scr', 'w', encoding='utf-8') as f:
            #e.script.dump(f)
        return
    except Exception as e:
        print(f'error while decompiling {file}: {e}')
        #with open(f'{file.path.replace("/", "_")}', 'wb') as f:
            #f.write(binary)
        return
    return script.collect_texts()

def extract_dats(l7cdir):
    locations = {}
    files = l7cdir.glob('_Data/Script/*/*/*/*.dat')
    for file in files:            
        texts = extract_dat(file)
        if texts:
            path = file.relative_to(l7cdir / '_Data/Script/')
            locations['/'.join(path.parts)] = texts
    return locations

def write_to_csv(script, outputdir):
    with open(outputdir / 'Script.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, ['path', 'id', 'text'])
        for location, texts in script.items():
            for id, text in texts.items():
                writer.writerow({
                    'path': location,
                    'id': id,
                    'text': text,
                })

def extract_script(l7cdir, outputdir):
    script = extract_dats(l7cdir)
    write_to_csv(script, outputdir)
