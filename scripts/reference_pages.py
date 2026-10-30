#!/usr/bin/env python3
"""Extract selected visual references; never overwrite existing files."""
import argparse
import json
from pathlib import Path
import fitz


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pages', required=True, help='One-based pages, e.g. 1,3,14')
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / 'references' / 'reference.pdf'
    try:
        numbers = [int(item.strip()) for item in args.pages.split(',')]
    except ValueError:
        parser.error('--pages must contain comma-separated integers')
    with fitz.open(source) as doc:
        if not numbers or len(set(numbers)) != len(numbers) or any(n < 1 or n > len(doc) for n in numbers):
            parser.error(f'Pages must be unique and between 1 and {len(doc)}')
        results = []
        for number in numbers:
            page = doc[number - 1]
            images = page.get_image_info(xrefs=True)
            if len(images) == 1 and images[0]['xref'] and fitz.Rect(images[0]['bbox']).irect == page.rect.irect:
                embedded = doc.extract_image(images[0]['xref'])
                payload, extension = embedded['image'], embedded['ext']
            else:
                payload, extension = page.get_pixmap(matrix=fitz.Matrix(4/3, 4/3), alpha=False).tobytes('png'), 'png'
            target = args.output_dir / f'page-{number:02d}.{extension}'
            if target.exists():
                parser.error(f'Refusing to overwrite {target}')
            results.append((target, payload))
        args.output_dir.mkdir(parents=True, exist_ok=True)
        for target, payload in results:
            with target.open('xb') as handle:
                handle.write(payload)
        print(json.dumps({'source_pages': len(doc), 'files': [str(p.resolve()) for p, _ in results]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
