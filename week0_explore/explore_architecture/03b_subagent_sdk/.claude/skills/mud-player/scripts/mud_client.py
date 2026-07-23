#!/usr/bin/env python3
"""Send a batch of commands to a CircleMUD/tbaMUD server and print the output.

Handles the login handshake (name -> password -> "press return" -> menu
choice, or straight "Reconnecting." if the character is already in-game),
then sends each command from stdin (one per line) and waits for the next
game prompt before sending the next one.

Usage:
    echo -e "look\nscore\ninventory" | python3 mud_client.py --user <name> --pass <password>

Defaults to localhost:4000; pass --host/--port to point at a different
server. --user/--pass are required — this script is shared across multiple
characters/agents, so credentials are never hardcoded here. Look them up in
the calling project's own CLAUDE.md.

The connection is closed without sending "quit" unless "quit" is itself one
of the given commands, so the character is simply left link-dead in the
game world and a later run will reconnect into the same spot.
"""
import argparse
import re
import socket
import sys
import time

IAC_RE = re.compile(rb"\xff[\xfb\xfc\xfd\xfe].")
ANSI_RE = re.compile(rb"\x1b\[[0-9;]*[a-zA-Z]")


def strip_noise(data: bytes) -> bytes:
    return ANSI_RE.sub(b"", IAC_RE.sub(b"", data))


def read_idle(sock: socket.socket, idle_timeout: float, max_wait: float) -> bytes:
    """Read until no new bytes arrive for idle_timeout seconds, or max_wait elapses."""
    buf = b""
    sock.settimeout(0.2)
    deadline = time.time() + max_wait
    last_data = time.time()
    while time.time() < deadline:
        try:
            chunk = sock.recv(4096)
            if not chunk:
                break
            buf += chunk
            last_data = time.time()
        except socket.timeout:
            if buf and (time.time() - last_data) >= idle_timeout:
                break
    return buf


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--host", default="localhost")
    p.add_argument("--port", type=int, default=4000)
    p.add_argument("--user", required=True, help="account username (see this project's CLAUDE.md)")
    p.add_argument("--pass", dest="password", required=True, help="account password (see this project's CLAUDE.md)")
    p.add_argument("--idle-timeout", type=float, default=1.5,
                    help="seconds of silence that mark the end of a response")
    p.add_argument("--max-wait", type=float, default=10.0,
                    help="max seconds to wait for a single response")
    p.add_argument("--raw", action="store_true",
                    help="don't strip ANSI color codes / telnet negotiation bytes")
    args = p.parse_args()

    commands = [line.rstrip("\n") for line in sys.stdin.readlines()]
    commands = [c for c in commands if c != ""] or [""]

    def show(label: str, data: bytes):
        raw = data if args.raw else strip_noise(data)
        text = raw.decode("latin-1")
        print(f"=== {label} ===")
        print(text, end="" if text.endswith("\n") else "\n")
        sys.stdout.flush()

    try:
        sock = socket.create_connection((args.host, args.port), timeout=10)
    except OSError as e:
        print(f"ERROR: could not connect to {args.host}:{args.port}: {e}", file=sys.stderr)
        sys.exit(1)

    banner = read_idle(sock, args.idle_timeout, args.max_wait)
    show("LOGIN", banner)
    sock.sendall(args.user.encode() + b"\r\n")

    after_name = read_idle(sock, args.idle_timeout, args.max_wait)
    show("LOGIN", after_name)
    sock.sendall(args.password.encode() + b"\r\n")

    after_pass = read_idle(sock, args.idle_timeout, args.max_wait)
    show("LOGIN", after_pass)

    if b"PRESS RETURN" in after_pass:
        sock.sendall(b"\r\n")
        menu = read_idle(sock, args.idle_timeout, args.max_wait)
        show("LOGIN", menu)
        if b"Make your choice" in menu:
            sock.sendall(b"1\r\n")
            entered = read_idle(sock, args.idle_timeout, args.max_wait)
            show("LOGIN", entered)
    elif b"Make your choice" in after_pass:
        sock.sendall(b"1\r\n")
        entered = read_idle(sock, args.idle_timeout, args.max_wait)
        show("LOGIN", entered)
    # else: "Reconnecting." (or similar) -- already in game, nothing more to do

    for cmd in commands:
        sock.sendall(cmd.encode() + b"\r\n")
        out = read_idle(sock, args.idle_timeout, args.max_wait)
        show(f"COMMAND: {cmd}", out)

    sock.close()


if __name__ == "__main__":
    main()
