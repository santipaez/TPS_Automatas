# Dirección IPv4 (000.000.000.000-255.255.255.255)

import re

COLOR_GREEN = "\033[32m"
COLOR_RED = "\033[31m"
COLOR_RESET = "\033[0m"

ipv4Regex = r"^([01]?\d{1,2}|2[0-4]\d|25[0-5])\.([01]?\d{1,2}|2[0-4]\d|25[0-5])\.([01]?\d{1,2}|2[0-4]\d|25[0-5])\.([01]?\d{1,2}|2[0-4]\d|25[0-5])$"

with open("ipv4.txt") as f:
    for line in f:
        line = line.strip()
        if re.match(ipv4Regex, line):
            print(f"{COLOR_GREEN}[{line}] es una dirección IPv4 válida{COLOR_RESET}")
        else:
            print(f"{COLOR_RED}[{line}] no es una dirección IPv4 válida{COLOR_RESET}")
