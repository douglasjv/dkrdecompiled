#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

gmake -j4 CROSS=tools/binutils/mips64-elf-
