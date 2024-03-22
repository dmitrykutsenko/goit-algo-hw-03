import os
import shutil
from pathlib import Path
# Додамо для обробки командного рядка
import argparse


def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
    if path.is_dir():
        print(indent + prefix + str(path.name))
        indent += "   " if prefix else ""
        
        #  Отримаємо сортований список дочірніх з останніми директоріями
        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            # Перевка чи поточний дочірній елемент є останнім у каталозі
            is_last = index == len(children) - 1
            display_tree(child, indent, "└── " if is_last else "├── ")
    else:
        print(indent + prefix + str(path.name))


def copy_files(source_dir: Path, dest_dir: Path) -> None:
    """
    Рекурсивно копіює файли з source_dir до dest_dir, сортуючи їх за розширенням.

    Args:
        source_dir: Шлях до вихідної директорії.
        dest_dir: Шлях до директорії призначення.
    """

    for item in os.listdir(source_dir):
        item_path = Path(source_dir, item)

        if item_path.is_dir():
            try:
                copy_files(item_path, dest_dir / item)
            except Exception as e:
                print(f"Непередбачена помилка при рекурсивному копіюванні '{item_path}': {e}")
        else:
            filename, extension = os.path.splitext(item)
            extension = extension.lower()[1:]
            
            # Створити підкаталог для розширення файлу, якщо він ще не існує
            ext_dir = dest_dir / extension
    
            try:
                if not ext_dir.exists():
                    os.makedirs(ext_dir)
            except Exception as e:
                print(f"Непередбачена помилка при створенні директорії '{ext_dir}': {e}")

            try:
                shutil.copy2(item_path, ext_dir)
            except Exception as e:
                print(f"Непередбачена помилка при копіюванні файлу '{item_path}': {e}")


if (__name__ == "__main__") or (__name__ == "__hw_03_01__"):
    # Parse arguments
    try:
        
        parser = argparse.ArgumentParser(description="Копіює файли з однієї директорії в іншу, сортуючи їх за розширенням.")
        parser.add_argument("source_dir", type=str, nargs='?', help="Шлях до директорії для розгляду")
        parser.add_argument("dest_dir", type=str, nargs='?', help="Шлях до директорії з результатами")
        args = parser.parse_args()

        if args.source_dir is None:
            args.source_dir = str(input("Вкажи шлях до директорії для розгляду: "))

        if args.dest_dir is None:
            args.dest_dir = str(input("Вкажи шлях до директорії з результатами? "))

        if not Path(str(args.source_dir)).exists():
            parser.print_help()
            exit(1)

        source_dir = Path(str(args.source_dir))
        dest_dir = Path(str(args.dest_dir))

        print("all is fine, let's go...")
    
    except Exception as e:
        print(f"Непередбачена помилка при парсингу аргументів: {e}")
        exit(1)
    
    # Перевірка чи існує та директорія для розгляду
    if not source_dir.exists():
        print(f"Помилка: Директорія '{source_dir}' не існує!")
        exit(1)
    
    # Створення директорії з результатами, якщо її ще немає
    if not dest_dir.exists():
        try:
            os.makedirs(dest_dir)
        except Exception as e:
            print(f"Непередбачена помилка при створенні директорії '{dest_dir}': {e}")
            exit(1)

    # Рекурсивне копіювання файлів
    copy_files(source_dir, dest_dir)

    # Відобразити дерево директорії з результатами
    print("Дерево директорії призначення:")
    try:
        display_tree(dest_dir)
    except Exception as e:
        print(f"Непередбачена помилка при візуалізації ієрархії директорії '{dest_dir}': {e}")
    