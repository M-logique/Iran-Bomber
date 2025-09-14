#!/usr/bin/env bash
#
# ARCHITECT'S NOTE: Final version with smart launcher logic.
# If the binary is up-to-date, it runs it immediately. Otherwise, it updates first.

# Set strict error handling.
# -e: Exit immediately if a command fails.
# -u: Treat unset variables as an error (safer).
set -eu

# --- Configuration ---
DEBUG=${DEBUG:-0} # Set to 1 to enable debug logs, e.g., `DEBUG=1 ./install.sh`
REPO="M-logique/iran-bomber"
BIN_NAME="iran-bomber"

# --- Utility Functions ---
log() {
  if [ "$DEBUG" -eq 1 ]; then
    printf "\033[93m[DEBUG] %s\033[0m\n" "$@" >&2
  fi
}

info() {
  printf "\033[36m[INFO]\033[0m %s\n" "$@"
}

success() {
  printf "\033[92m[SUCCESS]\033[0m %s\n" "$@"
}

error_exit() {
  printf "\033[91m[ERROR]\033[0m %s\n" "$@" >&2
  exit 1
}

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

#==============================================================================
# ARCHITECT'S NOTE: This is the key logic change.
# We now check the version first. If it's up-to-date, we execute and exit.
# The rest of the script only runs if an installation or update is needed.
#==============================================================================

# Step 3: Check for existing binary and compare version if it exists
if [ -f "$BINARY_PATH" ]; then
    log "Binary found at $BINARY_PATH. Checking version..."
    
    # Fetch the latest tag from GitHub API
    API_URL="https://api.github.com/repos/$REPO/releases/latest"
    TAG_RAW=$(curl -sSL "$API_URL" | grep '"tag_name":' | cut -d '"' -f 4 || true)
    
    if [ -n "$TAG_RAW" ]; then
        TAG=${TAG_RAW#v} # remove leading 'v'
        log "Latest release tag: $TAG"

        # Run the installed binary to get its current version output
        CURRENT_VERSION_OUTPUT=$("$BINARY_PATH" 2>/dev/null | head -n 1 || echo "none")
        log "Current binary version output: '$CURRENT_VERSION_OUTPUT'"
        
        # Check if the latest tag is present in the output
        if echo "$CURRENT_VERSION_OUTPUT" | grep -q "$TAG"; then
            info "Running the latest version of $BIN_NAME ($TAG)..."
            echo "-----------------------------------------"
            # Execute the existing, up-to-date binary and exit the script
            exec "$BINARY_PATH" "$@"
            # 'exec' replaces the current script process with the binary's process.
            # The script will not continue after this line.
        fi
        
        # If versions do not match, fall through to the update logic below.
        CURRENT_VERSION_STRING=$(echo "$CURRENT_VERSION_OUTPUT" | cut -d ' ' -f 3 || echo "unknown")
        info "Update found. Current version: $CURRENT_VERSION_STRING, Latest: $TAG"
    else
      log "Could not fetch latest tag. Proceeding to run local version."
      info "Could not check for updates. Running installed version..."
      echo "-----------------------------------------"
      exec "$BINARY_PATH" "$@"
    fi
fi

# --- The rest of the script only runs if the binary needs to be installed or updated ---

info "Setting up $BIN_NAME..."

# Step 4: Fetch Latest Release Tag (if not already fetched)
if [ -z "${TAG_RAW-}" ]; then
    log "Fetching latest release tag..."
    API_URL="https://api.github.com/repos/$REPO/releases/latest"
    TAG_RAW=$(curl -sSL "$API_URL" | grep '"tag_name":' | cut -d '"' -f 4 || true)
    if [ -z "$TAG_RAW" ]; then
        error_exit "Could not fetch the latest release tag. Cannot install/update."
    fi
    TAG=${TAG_RAW#v}
    log "Latest release tag: $TAG_RAW (version: $TAG)"
fi

# Step 5: Download and Install
if [ -f "$BINARY_PATH" ]; then
  info "Updating $BIN_NAME to version $TAG..."
else
  info "Installing $BIN_NAME version $TAG..."
fi

EXT=""
if [ "$OS" = "windows" ]; then EXT=".exe"; fi

FILE_NAME="${BIN_NAME}-${OS}-${ARCH}-${TAG}${EXT}"
URL="https://github.com/$REPO/releases/download/$TAG_RAW/$FILE_NAME"
log "Download URL: $URL"

info "Downloading binary..."

TMP_DOWNLOAD_PATH="${BINARY_PATH}.tmp"
if ! curl -SL --progress-bar "$URL" -o "$TMP_DOWNLOAD_PATH"; then
    rm -f "$TMP_DOWNLOAD_PATH" # Clean up failed download
    error_exit "Download failed. Please check the URL and your network."
fi
log "Download complete."

chmod +x "$TMP_DOWNLOAD_PATH"
log "Set executable permission."

mv "$TMP_DOWNLOAD_PATH" "$BINARY_PATH"
log "Installation complete."

success "$BIN_NAME has been successfully installed/updated to version $TAG at '$BINARY_PATH'"

# --- Final Step: User Instructions & Execution ---
info "Make sure '$DEST' is in your system's PATH environment variable."
echo "" 

info "Running the newly installed application..."
echo "-----------------------------------------"
# Execute the newly installed binary, passing along any arguments this script might have received.
exec "$BINARY_PATH" "$@"