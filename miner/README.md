# Monero CPU miner

Mines Monero (XMR) on your own computer's processor using [XMRig](https://github.com/xmrig/xmrig), the standard open-source miner, and the [SupportXMR](https://supportxmr.com) pool. The pool pays straight to your wallet. You don't need an account or ID, and it's free to start.

**You need a Windows, Mac or Linux computer.** Phones can't mine anything worthwhile, and phone "mining" apps are mostly fake.

## What it really earns

Very little. Roughly, before electricity:

| Computer | Speed (H/s) | Per month |
|---|---|---|
| Typical laptop | 1,000 – 4,000 | under $1 – $5 |
| Mid-range desktop (e.g. Ryzen 5 5600X) | ~8,000 | about $5 – $11 |
| High-end desktop (e.g. Ryzen 9 7950X) | ~20,000 | about $13 – $27 |

The table assumes about 0.00015 XMR per day for every 1,000 H/s, with XMR at $150–$300. Both numbers change all the time.

Mining runs your processor at full power. At typical home electricity prices that costs about as much as you earn, so whoever pays the power bill pays for it. It also makes the computer hot and loud. Laptops especially should sit on a hard, flat surface.

## Setup (about 15 minutes)

1. **Get a free Monero wallet.** [Cake Wallet](https://cakewallet.com) works on a phone, or get the official wallet from [getmonero.org](https://www.getmonero.org/downloads/). Write the seed words down on paper; they're the only way to recover the wallet. Copy your receiving address, a long string starting with `4` or `8`.
2. **Download XMRig** from the official page only: <https://github.com/xmrig/xmrig/releases>. Choose the file for your system:
   - Windows: `xmrig-…-windows-x64.zip`
   - Mac (Apple chip): `xmrig-…-macos-arm64.tar.gz`
   - Mac (Intel): `xmrig-…-macos-x64.tar.gz`
   - Linux: `xmrig-…-linux-static-x64.tar.gz`

   Unzip it.
3. **Copy `config.json` and the start file** (`start.bat` for Windows, `start.sh` for Mac/Linux) into the XMRig folder, next to the `xmrig` program. Replace its `config.json` if it has one.
4. **Open `config.json`** in Notepad or TextEdit and replace `YOUR_MONERO_ADDRESS` with your wallet address. It appears twice.
5. **Start it.** On Windows, double-click `start.bat`. Run it as administrator once for about 20% more speed. On Mac or Linux, run `./start.sh` in Terminal (Linux: `sudo ./start.sh` for the extra speed).

Within a minute you should see `speed 10s/60s/15m` lines; that's your H/s. To stop, close the window or press `Ctrl+C`.

### "Windows says it's a virus"
Criminals hide XMRig on other people's computers, so antivirus flags it even when it's the real thing. Only allow it if you downloaded it from the GitHub link above. To check it's genuine, compare the file's SHA256 with the one listed on the release page. On Windows, run `certutil -hashfile <file>.zip SHA256`. Then go to Windows Security → Protection history → Allow on device.

## Getting paid

- Check your balance at [supportxmr.com](https://supportxmr.com) by pasting in your wallet address.
- The pool sends XMR to your wallet once you pass its minimum payout. Third-party lists say 0.003 XMR, about 1–3 weeks on a laptop. Check the current number on the site.
- Cake Wallet can swap XMR into other coins. Turning crypto into cash needs an exchange account, and those usually require ID.

## Settings

- `"max-threads-hint": 75` uses about 75% of your processor so the computer stays usable. Set it to `100` for maximum speed, or lower it if the computer gets too hot.
- `"pass": "my-pc"` is this computer's name on the pool dashboard. Give each computer a different name.
- `"donate-level": 1` gives 1% of mining time to XMRig's developers. That's the minimum the official version allows.
