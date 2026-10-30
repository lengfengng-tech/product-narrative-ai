#!/usr/bin/env python3
"""Assemble explicitly ordered image pages without stretching or overwriting by default."""
import argparse
import json
import os
from pathlib import Path
import tempfile
import fitz


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--overwrite', action='store_true')
    parser.add_argument('pages', nargs='+', type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.suffix.lower() != '.pdf':
        parser.error('Output must have a .pdf extension')
    if output in [p.resolve() for p in args.pages]:
        parser.error('Output cannot replace a source image')
    if output.exists() and not args.overwrite:
        parser.error(f'Refusing to overwrite {output}; use --overwrite explicitly')
    sources = []
    ratio = None
    for path in args.pages:
        if not path.is_file() or path.suffix.lower() not in {'.png', '.jpg', '.jpeg'}:
            parser.error(f'Expected a PNG/JPEG file: {path}')
        payload = path.read_bytes()
        try:
            pixmap = fitz.Pixmap(payload)
            current = pixmap.width / pixmap.height
            del pixmap
        except Exception as exc:
            parser.error(f'Invalid image {path}: {exc}')
        if ratio is None:
            ratio = current
        if abs(current / ratio - 1) > 0.001:
            parser.error(f'Page aspect ratios differ: {path}; export all pages at one ratio')
        sources.append(payload)
    width, height = 1152.0, 1152.0 / ratio
    output.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.product-solution-', suffix='.pdf', dir=output.parent)
    os.close(fd)
    temporary = Path(name)
    try:
        with fitz.open() as doc:
            for payload in sources:
                page = doc.new_page(width=width, height=height)
                page.insert_image(page.rect, stream=payload, keep_proportion=True)
            doc.save(temporary)
        with fitz.open(temporary) as check:
            if len(check) != len(sources) or any(abs(p.rect.width-width) > .01 or abs(p.rect.height-height) > .01 or len(p.get_images()) != 1 for p in check):
                raise RuntimeError('Generated PDF failed page verification')
        if args.overwrite:
            os.replace(temporary, output)
        else:
            os.link(temporary, output)  # exclusive destination creation, even across concurrent calls
            temporary.unlink()
    finally:
        temporary.unlink(missing_ok=True)
    print(json.dumps({'output': str(output), 'pages': len(sources), 'page_size_pt': [width, height]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
