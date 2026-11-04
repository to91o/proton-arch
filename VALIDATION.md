# Validation performed

Date: 2026-11-04.

## Passed

- `bash -n proton-arch`.
- `python3 -m unittest discover -s tests -v`: four tests passed on Debian.
- Official `archlinux:base` container image, digest
  `sha256:ece6c971fec3c532fd508bce299a446deaf469feecbfe7c353e995bc1a5e7bba`.
- Full `pacman -Syu --noconfirm --needed proton-vpn-gtk-app networkmanager
  gnome-keyring xorg-server-xvfb` transaction with package signature verification
  enabled. The session proxy CA was added to the disposable container's system
  trust store; no TLS or signature checks were disabled.
- Installed `proton-vpn-gtk-app 4.18.8-1`, `proton-vpn-daemon 0.13.8-1`,
  `networkmanager 1.58.1-3`, `gnome-keyring 1:51.1-1`.
- Imported the packaged Proton `App` class, GTK 4 and NetworkManager GI bindings.
- Created a GTK window under Xvfb. Software-rendering/session-bus warnings were
  emitted; the window creation completed successfully.

## Not validated

The installer shell wrapper itself was not executed on a booted Arch desktop;
its pacman transaction was tested directly in the container with `--noconfirm`.
The container does not boot systemd, so service activation hooks could not start
the Proton daemon. A running NetworkManager, an unlocked user Secret Service,
the complete Proton application window, account login, VPN connections, DNS/IPv6
leak protection, kill switch, suspend/reconnect and reboot behavior have not been
validated. The host has no `/dev/net/tun`.

This is installation and integration tooling for the existing upstream Arch
package, not a separately implemented port or a claim of full VPN certification.
Follow the real-connection checks in README.md on an Arch desktop before relying
on the VPN.
