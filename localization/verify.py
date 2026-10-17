from pathlib import Path
import hashlib
import json
import re


def fenced_blocks(text):
    blocks = []
    active = None
    current = []
    for line in text.splitlines(keepends=True):
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            token = match.group(1)
            if active is None:
                active = (token[0], len(token))
                current = [line]
                continue
            if token[0] == active[0] and len(token) >= active[1]:
                current.append(line)
                blocks.append(''.join(current))
                active = None
                continue
        if active is not None:
            current.append(line)
    return blocks


def subsequence(expected, actual):
    iterator = iter(actual)
    return all(any(block == candidate for candidate in iterator) for block in expected)


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'localization/source-manifest.json').read_text())
    problems = []
    for item in manifest['upstream_files']:
        path = (root / item['path']).resolve()
        if root not in path.parents or not path.is_file():
            problems.append({'path': item['path'], 'problem': 'missing or unsafe source path'})
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != item['sha256']:
            problems.append({'path': item['path'], 'problem': 'source hash changed'})
    for item in manifest['documents']:
        path = (root / item['translation']).resolve()
        if root not in path.parents or not path.is_file():
            problems.append({'path': item['translation'], 'problem': 'missing or unsafe translation path'})
            continue
        text = path.read_text()
        if hashlib.sha256(path.read_bytes()).hexdigest() != item['translation_sha256']:
            problems.append({'path': item['translation'], 'problem': 'translation hash changed'})
        original = (root / item['source']).read_text()
        if not subsequence(fenced_blocks(original), fenced_blocks(text)):
            problems.append({'path': item['translation'], 'problem': 'original fenced block missing or changed'})
        if re.search(r'ZXQ(?:KEEP|UNIT)\d+QXZ', text):
            problems.append({'path': item['translation'], 'problem': 'unresolved translation token'})
    result = {'upstream_commit': manifest['upstream_commit'],
              'source_files_checked': len(manifest['upstream_files']),
              'documents_checked': len(manifest['documents']), 'problems': problems}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(1 if problems else 0)


if __name__ == '__main__':
    main()
