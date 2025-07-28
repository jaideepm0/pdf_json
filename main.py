import json
from pathlib import Path
from collections import defaultdict

import pymupdf4llm
from pymupdf import Document


def get_md(file_path: Path) -> defaultdict[list]:
    doc = Document(str(file_path))
    required = defaultdict(list)
    for page in range(doc.page_count):
        md_content = pymupdf4llm.to_markdown(doc, pages=[page]).split('\n')
        required[page] = md_content
    return required


def process_md(values: defaultdict[list], output_path: Path):
    final = {}
    final['outline'] = []

    for page, content in values.items():
        for value in content:
            temp = {}

            if value.startswith('########'):
                temp['level'] = 'H6'
                temp['text'] = ' '.join(value.split()[1:])
                temp['page'] = page
                final['outline'].append(temp)

            elif value.startswith('#######'):
                temp['level'] = 'H5'
                temp['text'] = ' '.join(value.split()[1:])
                temp['page'] = page
                final['outline'].append(temp)

            elif value.startswith('######'):
                temp['level'] = 'H4'
                temp['text'] = ' '.join(value.split()[1:])
                temp['page'] = page
                final['outline'].append(temp)

            elif value.startswith('#####'):
                temp['level'] = 'H3'
                temp['text'] = ' '.join(value.split()[1:])
                temp['page'] = page
                final['outline'].append(temp)

            elif value.startswith('####'):
                temp['level'] = 'H2'
                temp['text'] = ' '.join(value.split()[1:])
                temp['page'] = page
                final['outline'].append(temp)

            elif value.startswith('###'):
                temp['level'] = 'H1'
                temp['text'] = ' '.join(value.split()[1:])
                temp['page'] = page
                final['outline'].append(temp)

            elif value.startswith('#'):
                final['title'] = ' '.join(value.split()[1:])

    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(final, file, indent=2)


def main():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_path in input_dir.glob("*.pdf"):
        values = get_md(pdf_path)
        output_path = output_dir / f"{pdf_path.stem}.json"
        process_md(values, output_path)


if __name__ == "__main__":
    main()
