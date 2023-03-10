#!/usr/bin/env python3

# {{ ansible_managed }}

from dns_resolver import resolve_ipv4, resolve_ipv6
from util import validate_and_write, load_config, format_var

PROCESS_IPv6 = True
APPENDIX_4 = ''
APPENDIX_6 = 'v6'
DUMP_FILE = '/etc/nftables.d/addons/dns.json'
DUMP_FILE_KEY = 'dns'
OUT_FILE = '/etc/nftables.d/addons/dns.nft'

CONFIG = load_config(file=DUMP_FILE, key=DUMP_FILE_KEY)

if CONFIG is None or len(CONFIG) == 0:
    raise SystemExit(f"Config file could not be loaded: '{DUMP_FILE}'!")

lines = []
for var, hostnames in CONFIG.items():
    if not isinstance(hostnames, list):
        hostnames = [hostnames]

    values_v4 = []
    values_v6 = []

    for hostname in hostnames:
        values_v4.extend(resolve_ipv4(hostname))

        if PROCESS_IPv6:
            values_v6.extend(resolve_ipv6(hostname))

    lines.append(
        format_var(
            name=var,
            append=APPENDIX_4,
            data=values_v4,
            version=4,
        )
    )

    if PROCESS_IPv6:
        lines.append(
            format_var(
                name=var,
                append=APPENDIX_6,
                data=values_v6,
                version=6,
            )
        )

validate_and_write(lines=lines, file=OUT_FILE, key=DUMP_FILE_KEY)
