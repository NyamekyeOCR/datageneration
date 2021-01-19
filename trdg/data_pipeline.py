import subprocess
'''
1. Run clean_data.py to convert special character which are not rendered. 
    Update : Some pcs are able to render the special characters fine and there is no need to run the clean_data.py files
2. Run run.py to generate images.
    Args:
    -c count(how many images to generate)
    -w width(how many words per line)
    -f (font height?) prefarably = 64
3. Run rename_files.py.
    Update : The images render fine but the file names are not stored with the prefarable special characters so we use this script to convert all illegal character to special characters in the file name.
4. Write a script to divide the images into train, val, test
    Update : This will split the images randomly into three folders.
5. Run generate_gt.py
    Update : This file generates a gt.txt file which is how the data is going to be converted into the lightning database format(lmdb)
6. Write copy_data.py script
    Update : Thiswill copy the train, val and test folder to the recognition folder.
7. Run create_dataset_lmdb.py
    Update : This will generate the lmdb from the gt.txt files of the train, val and test folders.
Data Pipeline
1. Run clean_data.py
2. Run run.py
3. Run rename_files.py
4. Run generate_gt.py
5. Run copy_gt.py
6. Run create_lmdb_dataset.py
'''

def data_pipeline():
    pass
