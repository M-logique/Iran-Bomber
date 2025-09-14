#!/usr/bin/env bash
#
# ARCHITECT'S NOTE: Final version with a robust version parser
# that correctly handles the multi-line ASCII art output.

set -eu

# --- Configuration ---
DEBUG=${DEBUG:-0}
REPO="M-logique/iran-bomber"
BIN_NAME="iran-bomber"

# --- Utility Functions ---
log() { if [ "$DEBUG" -eq 1 ]; then printf "\033[93m[DEBUG] %s\033[0m\n" "$@" >&2; fi; }
info() { printf "\033[36m[INFO]\033[0m %s\n" "$@"; }
success() { printf "\033[92m[SUCCESS]\033[0m %s\n" "$@"; }
error_exit() { printf "\033[91m[ERROR]\033[0m %s\n" "$@" >&2; exit 1; }

# --- Main Logic ---

# Step 1: Detect OS and Architecture
log "Detecting OS and architecture..."
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)
case "$ARCH" in
  x86_64 | amd64) ARCH="amd64" ;;
  i386 | i686) ARCH="386" ;;
  armv7l) ARCH="arm" ;;
  aarch64 | arm64) ARCH="arm64" ;;
  *) error_exit "Unsupported architecture: $ARCH" ;;
esac
log "Detected OS=$OS, ARCH=$ARCH"

# Step 2: Determine Installation Directory
if [ -n "${PREFIX-}" ] && [ -d "/data/data/com.termux" ]; then
    DEST="$PREFIX/bin"
else
    DEST="$HOME/.local/bin"
fi
mkdir -p "$DEST"
BINARY_PATH="$DEST/$BIN_NAME"
log "Binary path is set to $BINARY_PATH"

# Step 3: Check for existing binary and compare version if it exists
if [ -f "$BINARY_PATH" ]; then
    log "Binary found at $BINARY_PATH. Checking version..."
    
    API_URL="https://api.github.com/repos/$REPO/releases/latest"
    TAG_RAW=$(curl -sSL "$API_URL" | grep '"tag_name":' | cut -d '"' -f 4 || true)
    
    if [ -n "$TAG_RAW" ]; then
        log "Latest release tag from GitHub: $TAG_RAW"

        # Try to get version from the installed binary using --version
        CURRENT_VERSION_RAW=$("$BINARY_PATH" -v 2>/dev/null || true)
        log "Raw --version output: <<EOF\n$CURRENT_VERSION_RAW\nEOF"

        # 1) Preferred pattern: "iran-bomber Version: v1.2.3" (case-insensitive)
        CURRENT_TAG=$(printf "%s\n" "$CURRENT_VERSION_RAW" | grep -oP '(?i)iran-bomber\s+version:\s*\Kv[0-9]+(?:\.[0-9A-Za-z_.-]*)*' || true)

        # 2) Fallback: "Version: v1.2.3" or "version: v1.2.3"
        if [ -z "$CURRENT_TAG" ]; then
            CURRENT_TAG=$(printf "%s\n" "$CURRENT_VERSION_RAW" | grep -oP '(?i)version:\s*\Kv[0-9]+(?:\.[0-9A-Za-z_.-]*)*' || true)
        fi

        # 3) Another fallback: bare vX.Y.Z anywhere
        if [ -z "$CURRENT_TAG" ]; then
            CURRENT_TAG=$(printf "%s\n" "$CURRENT_VERSION_RAW" | grep -oP 'v[0-9]+(?:\.[0-9A-Za-z_.-]*)*' || true)
        fi

        # Make sure we have something; otherwise mark as none
        if [ -z "$CURRENT_TAG" ]; then
            CURRENT_TAG="none"
        fi

        log "Parsed current installed tag: $CURRENT_TAG"
        
        if [ "$CURRENT_TAG" = "$TAG_RAW" ]; then
            info "Running the latest version of $BIN_NAME ($TAG_RAW)..."
            echo "-----------------------------------------"
            exec "$BINARY_PATH" "$@"
        fi

        info "Update found. Current: ${CURRENT_TAG#v}, Latest: ${TAG_RAW#v}"
    else
      log "Could not fetch latest tag. Running local version."
      info "Could not check for updates. Running installed version..."
      echo "-----------------------------------------"
      exec "$BINARY_PATH" "$@"
    fi
fi

# --- The rest of the script only runs if an install or update is needed ---

info "Setting up $BIN_NAME..."

# Step 4: Fetch Latest Release Tag (if not already fetched)
if [ -z "${TAG_RAW-}" ]; then
    log "Fetching latest release tag..."
    API_URL="https://api.github.com/repos/$REPO/releases/latest"
    TAG_RAW=$(curl -sSL "$API_URL" | grep '"tag_name":' | cut -d '"' -f 4 || true)
    if [ -z "$TAG_RAW" ]; then
        error_exit "Could not fetch the latest release tag. Cannot install/update."
    fi
fi
TAG=${TAG_RAW#v}
log "Latest release tag: $TAG_RAW (version: $TAG)"

# Step 5: Download and Install
if [ -f "$BINARY_PATH" ]; then
  info "Updating $BIN_NAME to version $TAG..."
else
  info "Installing $BIN_NAME version $TAG..."
fi

EXT=""
if [ "$OS" = "windows" ]; then EXT=".exe"; fi

# NOTE: adjust FILE_NAME rule if your artifacts omit/add "v" in their filename.
# Example filename formats:
# - with v: iran-bomber-linux-amd64-v1.2.3
# - without v: iran-bomber-linux-amd64-1.2.3
# If your real artifact names do NOT contain the leading 'v', use ${TAG} instead of ${TAG_RAW} below.
# FILE_NAME="${BIN_NAME}-${OS}-${ARCH}-${TAG_RAW}${EXT}"
FILE_NAME="${BIN_NAME}-${OS}-${ARCH}-${TAG}${EXT}"   # safer default (no leading v in filename)
URL="https://github.com/$REPO/releases/download/$TAG_RAW/$FILE_NAME"
log "Download URL: $URL"

info "Downloading binary..."

TMP_DOWNLOAD_PATH="${BINARY_PATH}.tmp"
if ! curl -SL --progress-bar "$URL" -o "$TMP_DOWNLOAD_PATH"; then
    rm -f "$TMP_DOWNLOAD_PATH"
    error_exit "Download failed. Check the URL and your network."
fi
log "Download complete."

chmod +x "$TMP_DOWNLOAD_PATH"
log "Set executable permission."

mv "$TMP_DOWNLOAD_PATH" "$BINARY_PATH"
log "Installation complete."

success "$BIN_NAME has been successfully installed/updated to version $TAG at '$BINARY_PATH'"

# --- Final Step ---
info "Make sure '$DEST' is in your system's PATH."
echo ""
info "Running the newly installed application..."
echo "-----------------------------------------"
exec "$BINARY_PATH" "$@"
