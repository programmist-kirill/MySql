import os

def main(name_basedata):
    if os.path.exists(name_basedata):
        os.system('rm -rf ' + name_basedata)
    
    if os.path.exists('script.sh'):
        os.remove('script.sh')
