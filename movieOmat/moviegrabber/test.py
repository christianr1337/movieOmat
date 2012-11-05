'''
Created on Nov 4, 2012

@author: c1337b
'''
from moviegrabber.tools import Tools

def test_grabber():
    grab = Tools()
    grab.get_folder_names_and_save_to_model()

if __name__ == '__main__':
    pass

test_grabber()