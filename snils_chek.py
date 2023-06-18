import re

SNILS_MACH = re.compile(r"[\d\- ]{11,14}")

def snils_chek(snils: str):

    if SNILS_MACH.search(snils):
        snils = str(SNILS_MACH.search(snils).group())
        snils = snils.replace("-", "").replace(" ", "")
        result = f"{snils[:3]}-{snils[3:6]}-{snils[6:9]}-{snils[9:]}"
        return result

