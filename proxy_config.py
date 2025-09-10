#!/usr/bin/env python3
import os
import subprocess

# -------------------- Configuration --------------------
ANCHOR_FILE = "/etc/pf.anchors/proxy_redirect"
PF_CONF = "/etc/pf.conf"
ANCHOR_NAME = "proxy_redirect"

# Separate lines for HTTP and HTTPS to avoid PF syntax issues
ANCHOR_CONTENT = """\
# Redirect HTTP and HTTPS to mitmproxy
rdr pass on lo0 inet proto tcp from any to any port 80 -> 127.0.0.1 port 8080
rdr pass on lo0 inet proto tcp from any to any port 443 -> 127.0.0.1 port 8080
"""

# -------------------- Functions --------------------
def write_anchor_file():
    """Write PF anchor file with redirection rules."""
    with open(ANCHOR_FILE, "w") as f:
        f.write(ANCHOR_CONTENT)
    print(f"[+] Written anchor file to {ANCHOR_FILE}")


def check_and_update_pf_conf():
    """Ensure pf.conf loads the anchor file."""
    with open(PF_CONF, "r") as f:
        pf_conf = f.read()

    anchor_line = f'anchor "{ANCHOR_NAME}"'
    load_line = f'load anchor "{ANCHOR_NAME}" from "{ANCHOR_FILE}"'

    if anchor_line in pf_conf and load_line in pf_conf:
        print(f"[+] Anchor load lines already present in {PF_CONF}")
        return

    with open(PF_CONF, "a") as f:
        f.write("\n")
        f.write(anchor_line + "\n")
        f.write(load_line + "\n")

    print(f"[+] Appended anchor load lines to {PF_CONF}")


def enable_pf():
    """Load pf rules and enable the firewall safely."""
    try:
        # Disable first to prevent "already enabled" errors
        subprocess.run(["pfctl", "-d"], check=False)
        # Load main pf.conf with anchor
        subprocess.run(["pfctl", "-f", PF_CONF], check=True)
        # Enable PF
        subprocess.run(["pfctl", "-e"], check=True)
        print("[+] PF rules loaded and PF enabled successfully")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error enabling PF: {e}")


def main():
    """Run the full setup."""
    if os.geteuid() != 0:
        print("[!] This script must be run with sudo/root privileges.")
        return

    write_anchor_file()
    check_and_update_pf_conf()
    enable_pf()

    print("\n[✔] Done! HTTP and HTTPS traffic on localhost is redirected to port 8080.")
    print("[✔] Make sure mitmproxy is running and listening on port 8080.")


# -------------------- Entry Point --------------------
if __name__ == "__main__":
    main()


#sudo pfctl -d' this terminates it 

