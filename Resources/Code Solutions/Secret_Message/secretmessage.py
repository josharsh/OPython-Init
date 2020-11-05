import os
def getfiles():
    """
    Translate a list of the files in a list.

    Args:
    """
    file_list=os.listdir(r"C:\Users\Sukanya\Desktop\Object Oriented Python Udacity\Prank\prank")
    os.chdir(r"C:\Users\Sukanya\Desktop\Object Oriented Python Udacity\Prank\prank")
    for filename in file_list:
        os.rename(filename,filename.translate(str.maketrans('', '', '1234567890')))
    print(file_list)
getfiles()
        
