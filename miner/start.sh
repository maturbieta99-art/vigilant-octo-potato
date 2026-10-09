#!/bin/sh
# Starts XMRig with config.json. Run with sudo on Linux for ~20% more speed (huge pages).
cd "$(dirname "$0")" || exit 1
if grep -q YOUR_MONERO_ADDRESS config.json; then
    echo "Open config.json and replace YOUR_MONERO_ADDRESS (both places) with your Monero wallet address."
    exit 1
fi
if [ ! -x ./xmrig ]; then
    echo "xmrig not found. Put this file and config.json in the same folder as the xmrig program."
    exit 1
fi
exec ./xmrig --config=config.json
