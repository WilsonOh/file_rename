import os
import shutil
import time

# add path to folder/file you want to rename
FILE_PATH = ""

os.chdir(FILE_PATH)


def remove_non_videos(file):
    if os.path.isdir(file):
        shutil.rmtree(file)
    elif os.path.isfile(file):
        os.remove(file)


def check_ans(file_names, new_names=None, is_delete=False):
    os.system('clear')
    while True:
        os.system('clear')
        print("Check if these are correct: ")
        if is_delete:
            print("Files to delete: ")
            for idx, deleting in enumerate(file_names, 1):
                print(f"{idx}: {deleting}")
        else:
            print("Files to rename: ")
            for idx, (old, new) in enumerate(zip(file_names, new_names), 1):
                print(f"{idx}: {old} -> {new}")
        ans = input("enter 'yes' to delete and 'no' to abort\nenter 'rm [file num]' to exclude a file\nenter 'q' to quit: ").lower().strip().split()
        if len(ans) < 1 or ans[0] not in ["yes", "no", "rm", "q"]:
            print("Invalid input")
            time.sleep(1)
            continue
        cmd, *args = ans
        if cmd == "yes":
            if is_delete:
                print("Deleting...")
                for file in file_names:
                    remove_non_videos(file)
            else:
                print("Renaming...")
                for old, new in zip(file_names, new_names):
                    os.rename(old, new)
            return "yes"
        elif cmd == "no":
            print("Skipping...")
            return
        elif cmd == "q":
            print("Exiting...")
            quit()
        elif cmd == "rm":
            new_names_copy =[]
            file_names_copy = file_names[:]
            if not is_delete:
                new_names_copy = new_names[:]
            for arg in args:
                if not arg.isdigit():
                    print("Not a digit")
                    time.sleep(1)
                    break
                if not(1 <= int(arg) <= len(file_names)):
                    print("Invalid range")
                    time.sleep(1)
                    break
                file_names.remove(file_names_copy[int(arg) - 1])
                if not is_delete:
                    new_names.remove(new_names_copy[int(arg) - 1])


# Recursively prints the directory and subdirectory contents with dynamic tab-spacing
def recursive_cd_print(file, tabs=1):
    if os.path.isdir(file):
        print((tabs - 1) * '\t' + file + ':')
        os.chdir(file)
        for item in os.listdir():
            recursive_cd_print(item, tabs + 1)
            if os.path.isfile(item):
                print(tabs * "\t" + item)
        os.chdir("../")


def main():
    for file in os.listdir():
        if os.path.isdir(file):
            os.chdir(file)
            main()
    file_names = []
    new_names = []
    to_delete = []
    for file in os.listdir():
        if '.mkv' in file and '_OP' not in file and '_ED' not in file:
             f_name, f_ext = os.path.splitext(file)
             # ---------- Modify The Pattern Matching Here --------------
             # ----------------------------------------------------------
             new_name = "".join([f_name, f_ext])
             if new_name != file:
                 new_names.append(new_name)
                 file_names.append(file)
        else:
             to_delete.append(file)
    if len(file_names) > 0:
        check_ans(file_names, new_names)
        time.sleep(1)
    if len(to_delete) > 0:
        check_ans(to_delete, is_delete=True)
        time.sleep(1)
    os.chdir('../')
    os.system('clear')


if __name__ == "__main__":
    main()
