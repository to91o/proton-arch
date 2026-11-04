# Proton VPN on Arch Linux

Install and run the **actual Proton VPN GTK app**, with its upstream UI, assets,
login flow and VPN backend. This project integrates the community-maintained
package in Arch's official `extra` repository. It is not a new VPN implementation
and is not affiliated with Proton AG. UI availability follows the packaged
upstream version; newer upstream releases may reach Arch later.

## Install

Requires an up-to-date x86_64 Arch Linux desktop, internet access, systemd,
NetworkManager and a working desktop Secret Service. Run from this directory:

```sh
./proton-arch install
```

The command uses pacman's signed packages and performs a full system upgrade.
Review pacman's transaction before accepting. It installs the upstream app and
its transitive daemon/backend dependencies, plus NetworkManager and GNOME Keyring.
An existing compatible Secret Service can be used instead of GNOME Keyring.
Do not run multiple competing keyring providers.

If NetworkManager does not already manage your connection, migrate your network
configuration first. On a machine configured for NetworkManager, enable it with
`sudo systemctl enable --now NetworkManager`. This can affect connectivity;
the installer deliberately leaves service configuration to you.
The daemon package enables `proton.VPN.service`; if it is inactive after install,
inspect `systemctl status proton.VPN.service` and start it with
`sudo systemctl enable --now proton.VPN.service`.

Log into a graphical desktop as your regular user, with the login keyring
unlocked, then run:

```sh
./proton-arch doctor
./proton-arch launch
```

You can also launch Proton VPN from the desktop application menu. Do not run the
GUI with sudo. Log in using your Proton account in the upstream app; do not put
credentials into this repository or shell commands. Features depend on your plan
and the upstream Linux app. No web UI replica or simulated VPN is included.

## Verify a real connection

1. Before connecting, record your public IPv4/IPv6 addresses and DNS resolvers.
2. Sign in and connect using the app; confirm the connected state and a VPN
   interface/connection in `nmcli connection show --active`.
3. Confirm public traffic exits through the chosen VPN server. Check both IPv4
   and IPv6 and use an independent DNS leak check.
4. Test disconnect/reconnect, reboot, and your selected kill-switch behavior.
   Test loss of tunnel connectivity before relying on leak protection.

`doctor` validates desktop prerequisites, not encryption, routing, DNS leak
protection, account access, or every upstream feature. Never infer a working VPN
from a running process alone.

## Development and validation

```sh
bash -n proton-arch
python3 -m unittest discover -s tests -v
```

Package metadata: https://archlinux.org/packages/extra/any/proton-vpn-gtk-app/

Upstream source and licensing: https://github.com/ProtonVPN/proton-vpn-gtk-app
(GPL-3.0-or-later). This repository does not redistribute upstream source or
artwork. Obtain the corresponding sources through the Arch packaging links.

The cloud development host is Debian, without a desktop VPN session or TUN
device. Live account login, tunnel routing and leak tests must run on a suitable
Arch desktop. See `VALIDATION.md` for the checks actually performed.
