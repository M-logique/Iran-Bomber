#!/usr/bin/env bash
set -e

DEBUG=1  # 1=on, 0=off
log() { if [ $DEBUG -eq 1 ]; then echo "[DEBUG]" "$@"; fi }

REPO="M-logique/iran-bomber"
BIN_NAME="iran-bomber"

# Detect OS and ARCH
log "Detecting OS and architecture..."
OS=$(uname | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

case $ARCH in
  x86_64) ARCH="amd64" ;;
  i386|i686) ARCH="386" ;;
  armv7*) ARCH="arm" ;;
  aarch64) ARCH="arm64" ;;
  *) echo "Unsupported architecture: $ARCH"; exit 1 ;;
esac
log "Detected OS=$OS, ARCH=$ARCH"

# Termux detection
if [ -n "$PREFIX" ] && [ -d "/data/data/com.termux" ]; then
    OS="linux"
    TERMUX=1
else
    TERMUX=0
fi
log "TERMUX=$TERMUX"

# Destination directory
if [ $TERMUX -eq 1 ]; then
    DEST="$HOME/.termux/bin"
else
    DEST="$HOME/.local/bin"
fi
mkdir -p "$DEST"
BINARY_PATH="$DEST/$BIN_NAME"
log "Binary path will be $BINARY_PATH"

# Fetch latest release tag
log "Fetching latest release tag from GitHub..."
TAG_RAW=$(curl -s https://api.github.com/repos/$REPO/releases/latest | jq -r '.tag_name')
TAG=${TAG_RAW#v}  # remove 'v' if present
log "Latest release tag: $TAG_RAW, File tag: $TAG"

EXT=""
if [ "$OS" = "windows" ]; then EXT=".exe"; fi
FILE_NAME="${BIN_NAME}-${OS}-${ARCH}-${TAG}${EXT}"
URL="https://github.com/$REPO/releases/download/$TAG_RAW/$FILE_NAME"
log "Download URL: $URL"

# Check if binary exists and version
UPDATE=1
if [ -f "$BINARY_PATH" ]; then
    CURRENT_VERSION=$("$BINARY_PATH" --version 2>/dev/null || echo "none")
    if [ "$CURRENT_VERSION" = "$TAG" ]; then
        echo "$BIN_NAME is already up-to-date ($CURRENT_VERSION)"
        UPDATE=0
    else
        echo "Updating $BIN_NAME from $CURRENT_VERSION to $TAG..."
    fi
else
    echo "Installing $BIN_NAME version $TAG..."
fi

# Download and install if needed
if [ $UPDATE -eq 1 ]; then
    log "Downloading binary..."
    curl -L "$URL" -o "$BINARY_PATH"
    log "Setting executable permission..."
    chmod +x "$BINARY_PATH"
    echo "$BIN_NAME has been installed/updated to $TAG at $BINARY_PATH"
fi

echo "Make sure $DEST is in your PATH"
