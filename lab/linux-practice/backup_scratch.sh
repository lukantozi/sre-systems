#!/bin/bash
set -e

SRC="scratch"
DEST="backups/scratch-$(date +%Y%m%d-%H%M%S)"

mkdir -p "$DEST"
cp -r "$SRC"/* "$DEST"/

echo "Backup from $SRC to $DEST done"
