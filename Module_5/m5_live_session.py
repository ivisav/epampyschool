import os

print(os.getcwd())
if os.path.isdir('new_dir'):
    os.chdir('new_dir')
    print('dir is here')
    print(os.getcwd())

else:
    print('dir is not here')
    os.mkdir('new_dir')
    os.chdir('new_dir')
    print(os.getcwd())

import platform

print(platform.system())
print(platform.release())
print(platform.mac_ver())


