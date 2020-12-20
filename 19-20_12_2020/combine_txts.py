import os

def combine_txts():
    current_path = os.getcwd()

    with open(os.path.join(current_path, 'combined.txt'), 'w') as fd:
        for root, directories, files in os.walk(current_path):
            for file_name in files:
                if file_name.endswith('.txt'):
                    with open(os.path.normpath(f'{root}/{file_name}'), 'r') as read_file:
                        context = read_file.read()
                        fd.write(context)


combine_txts()
                        


