// The World in One Image — Saturday 21 November 2026.
// make.fun competition news-image-20261121, harness program/v1.
// This entry's image is the entry.png beside this file: a one-page
// newspaper front page drawn by tools/render.py (Python PIL + DejaVu).
// The program only copies that image to the output directory, so both
// grader runs write exactly the same bytes. No network, no randomness.
// The input image is read from MAKEFUN_INPUT_DIR when that directory
// holds an entry.png (the grader's input directory), otherwise from
// this file's own directory; the output goes to MAKEFUN_OUTPUT_DIR,
// defaulting to /output.
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const inputDir = process.env.MAKEFUN_INPUT_DIR;
const src = inputDir && existsSync(join(inputDir, 'entry.png'))
  ? join(inputDir, 'entry.png')
  : join(here, 'entry.png');
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(src, join(outDir, 'entry.png'));
