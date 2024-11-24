import os
import re
import shutil


def search_files(directory, targetdir=None):
    pattern1 = r'^table_i.*'
    pattern2 = r'^table_t.*'
    os.makedirs(targetdir, exist_ok=True)
    for root, directory, files in os.walk(directory):
        for file in files:
            if re.match(pattern1, file) or re.match(pattern2, file):
                source_file = os.path.join(root, file)
                target_file = os.path.join(targetdir, file)
                shutil.move(source_file, target_file)
                print(f"Переміщено: {source_file} -> {target_file}")


if __name__ == '__main__':
    search_files(r"C:\Users\Ilona\Downloads\daily_sp500\quantquote_daily_sp500_83986\daily", r"C:\Users\Ilona\Downloads\daily_sp500\quantquote_daily_sp500_83986\new")
