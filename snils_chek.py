import re

SNILS_MACH = re.compile(r"\d+")

def snils_chek(snils: str):

    if SNILS_MACH.findall(snils):
        snils = "".join(SNILS_MACH.findall(snils))
        if len(snils) == 11:
            result = f"{snils[:3]}-{snils[3:6]}-{snils[6:9]}-{snils[9:]}"

            return result

if __name__ == "__main__":
    snils_chek("asdf123 45dsfsdf6-78901")

