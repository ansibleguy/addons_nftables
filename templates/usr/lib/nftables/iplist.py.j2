#!/usr/bin/env python3

# {{ ansible_managed }}

from urllib import request
from ipaddress import IPv4Network, IPv6Network, IPv4Address, IPv6Address, AddressValueError, NetmaskValueError

from util import validate_and_write, load_config, format_var

PROCESS_IPv6 = {% if NTF_ADD_CONFIG.enable.iplist_v6 %}True{% else %}False{% endif %}
APPENDIX_4 = '{{ NTF_ADD_CONFIG.appendix.ipv4 }}'
APPENDIX_6 = '{{ NTF_ADD_CONFIG.appendix.ipv6 }}'
DUMP_FILE = '{{ NTF_ADD_CONFIG.path.addon.dir }}/{{ NTF_ADD_CONFIG.path.addon.iplist_dump }}'
DUMP_FILE_KEY = '{{ NFT_ADD_HC.dump_keys.iplist }}'
OUT_FILE = '{{ NTF_ADD_CONFIG.path.addon.dir }}/{{ NTF_ADD_CONFIG.path.addon.iplist }}'

{% raw %}

def _filter_result_protocol(protocol: int, results: list) -> list:
    filtered = []
    protocols = {
        4: dict(network=IPv4Network, address=IPv4Address),
        6: dict(network=IPv6Network, address=IPv6Address),
    }

    if protocol not in protocols:
        protocol = 4

    for result in results:
        result = result.strip()

        try:
            protocols[protocol]['address'](result)
            filtered.append(result)

        except AddressValueError:
            try:
                protocols[protocol]['network'](result)
                filtered.append(result)

            except (AddressValueError, NetmaskValueError):
                pass

    filtered.sort()
    return filtered


def _download_list(url: str, sep: str) -> list:
    with request.urlopen(url) as u:
        return u.read().decode('utf-8').split(sep)


CONFIG = load_config(file=DUMP_FILE, key=DUMP_FILE_KEY)

if CONFIG is None or len(CONFIG) == 0:
    raise SystemExit(f"Config file could not be loaded: '{DUMP_FILE}'!")

lines = []
for var, iplist_config in CONFIG.items():
    urls = iplist_config['urls']
    separator = iplist_config['separator'] if 'separator' in iplist_config else '\n'

    if not isinstance(urls, list):
        urls = [urls]

    values_v4 = []
    values_v6 = []

    for entry in urls:
        data = _download_list(url=entry, sep=separator)

        lines.append(
            format_var(
                name=var,
                append=APPENDIX_4,
                data=_filter_result_protocol(
                    protocol=4,
                    results=data,
                ),
                version=4,
            )
        )

        if PROCESS_IPv6:
            lines.append(
                format_var(
                    name=var,
                    append=APPENDIX_6,
                    data=_filter_result_protocol(
                        protocol=6,
                        results=data,
                    ),
                    version=6,
                )
            )

validate_and_write(lines=lines, file=OUT_FILE, key=DUMP_FILE_KEY)

{% endraw %}
