# URL (http-https://www……com)  (puede o no figurar el protocolo, y el www) puede terminar con la / o ? (query param “?clave=valor&clave=valor )

import re

COLOR_GREEN = "\033[32m"
COLOR_RED = "\033[31m"
COLOR_RESET = "\033[0m"

urlRegex = r"^(http|https)://[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,63}(:[0-9]{1,5})?(/.*)?$"

with open("urls.txt") as f:
    for line in f:
        line = line.strip()
        if re.match(urlRegex, line):
            print(f"{COLOR_GREEN}[{line}] es una URL válida{COLOR_RESET}")
        else:
            print(f"{COLOR_RED}[{line}] no es una URL válida{COLOR_RESET}")
