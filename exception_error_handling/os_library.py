import os


def fix_filenames(folder_name):
    try:
        files = os.listdir(folder_name)
        for file in files:
            if file.endswith('mp3') and str(file)[0].isdigit():
                old_name = file
                file_name, file_extension = os.path.splitext(file)
                splitted = file_name.split('-')
                new_name = str(splitted[2])+'-'+str(splitted[1])+file_extension
                os.rename(folder_name+'/'+old_name, folder_name+'/'+new_name)
    except FileNotFoundError as ex:
        pass


def main():
    file_path = input("Enter the file path: ")
    fix_filenames(file_path)


main()
