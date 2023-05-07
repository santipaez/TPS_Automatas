# Email (nombre@dominio.com) (el nombre debe comenzar con letra y puede tener números, _, puntos y -) (definir 5 dominios y 5 países)

import re

COLOR_GREEN = "\033[32m"
COLOR_RED = "\033[31m"
COLOR_RESET = "\033[0m"

emailRegex = r"^[a-zA-Z][\w.-]*@[\w.-]+\.[a-zA-Z]+$"

with open("emails.txt") as f:
    for line in f:
        line = line.strip()
        if re.match(emailRegex, line):
            print(f"{COLOR_GREEN}[{line}] es un email válido{COLOR_RESET}")
        else:
            print(f"{COLOR_RED}[{line}] no es un email válido{COLOR_RESET}")
