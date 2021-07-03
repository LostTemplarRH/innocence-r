from .skit import skit_extract_text, SkitLine, SkitChoices
import csv

def split_speakers(speakers):
    split = []
    for i in range(0, 16):
        if (speakers & (1 << i)) != 0:
            split.append(i)
    return split
    #return ','.join(split)

def extract_skits(l7cdir, outputdir):
    skits = {}
    for file in l7cdir.glob('_Data/Field/Skit/Data/*.dat'):
        with file.open('rb') as f:
            binary = f.read()
            path = file.relative_to(l7cdir / '_Data/Field/Skit/Data')
            skits['/'.join(path.parts)] = skit_extract_text(binary)

    with open(outputdir / 'Skit.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['File', 'Field', 'Index', 'Speakers', 'Japanese'])
        for path, text in skits.items():
            for i, speaker in enumerate(text[0]):
                writer.writerow([path, 'speaker', i, '', speaker])
            for i, line in enumerate(text[1]):
                if isinstance(line, SkitLine):
                    if line.speakerName:
                        writer.writerow([path, 'line_speaker', i, '', line.speakerName])
                    speakers = split_speakers(line.speakers)
                    speakers = '\n'.join(f'{i} [{text[0][i]}]' for i in speakers)
                    writer.writerow([path, 'line', i, speakers, line.text])
                elif isinstance(line, SkitChoices):
                    for j, choice in enumerate(line.choices):
                        writer.writerow([path, 'choice', i, j, choice])

