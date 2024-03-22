import os
import shutil
from pathlib import Path

# source_dir = Path("C:\\Users\\Documents\\Certs\\")
# dest_dir = Path("C:\\Users\\Documents\\Certs_NEW\\")

def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
    if path.is_dir():
        # Use blue color for directories
        print(indent + prefix + str(path.name))
        indent += "   " if prefix else ""

        # Get a sorted list of children, with directories last
        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            # Check if the current child is the last one in the directory
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
            extension = extension.lower()[1:]  # Remove the dot

            # Create a subdirectory for the file extension if it doesn't exist
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


if __name__ == "__main__":
    # Parse arguments
    try:
        source_dir = Path(input("Введіть шлях до вихідної директорії: "))
        dest_dir = Path(input("Введіть шлях до директорії призначення (за замовчуванням dist): ") or "dist")
    except Exception as e:
        print(f"Непередбачена помилка при парсингу аргументів: {e}")
        exit(1)

    # Check if source directory exists
    if not source_dir.exists():
        print(f"Помилка: Директорія '{source_dir}' не існує!")
        exit(1)

    # Create destination directory if it doesn't exist
    if not dest_dir.exists():
        try:
            os.makedirs(dest_dir)
        except Exception as e:
            print(f"Непередбачена помилка при створенні директорії '{dest_dir}': {e}")
            exit(1)

    # Recursively copy files
    copy_files(source_dir, dest_dir)

    # Display the tree of the destination directory
    print("Дерево директорії призначення:")
    try:
        display_tree(dest_dir)
    except Exception as e:
        print(f"Непередбачена помилка при візуалізації ієрархії директорії '{dest_dir}': {e}")
