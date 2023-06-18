from typing import Optional
import pandas as pd


PATH_TO_FILE = "snils_to_marks.xlsx"
SNILS_ERROR_TEXT = f"СНИЛС должен содержать 11 цифр, "\
                    "а также до 4-х разделителе ' ' или '-'\n"\
                    "<b>Например:</b>\n"\
                    "<i>123-456-789-01</i>\n"\
                    "<i>123456789 01</i>"

SNILS_NOT_FOUND = "Информация по данному СНИЛС отсутствует в базе"

def make_sub_mark_dict(subjects: list, mark_index: str, data) -> dict:
    
    subjects_marks_dict = {}

    for subject in subjects:
        mark = data[subject].get(mark_index, None)
        if mark:
            subjects_marks_dict[subject] = mark

    return subjects_marks_dict


def make_message(snils: str, subjects_marks_dict: dict) -> str:
    
    message = f"<b>СНИЛС</b>: {snils}\n\n"\
              f"Баллы за экзамены:\n\n"
    for subject, mark in subjects_marks_dict.items():
        message += f"{subject}: {mark}\n"
    
    message += f"<b>Сумма балов: {sum(subjects_marks_dict.values())}</b>"

    return message

def get_message(snils = "123-456-789-01") -> Optional[str]:
    exc_file = pd.read_excel(PATH_TO_FILE)

    data = exc_file.to_dict() 
    
    subjects = list(data.keys())[1:]
    data["СНИЛС"] = dict(zip(data["СНИЛС"].values(), data["СНИЛС"].keys()))
    mark_row_index = data["СНИЛС"].get(snils, None)

    if mark_row_index is None:
        return SNILS_NOT_FOUND

    subjects_marks_dict = make_sub_mark_dict(subjects, mark_row_index, data)
    
    reply_message = make_message(snils, subjects_marks_dict)

    return reply_message




if __name__ == "__main__":
    get_message()

