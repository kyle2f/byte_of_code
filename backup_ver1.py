import os
import time

source = [r'C:\Users\Bello\Documents\CoDinG\Python\byteofcode\bebackeup']



target_dir = r'C:\Users\Bello\Documents\CoDinG\Python\byteofcode\backup'



if not os.path.exists(target_dir):
    os.mkdir(target_dir)

target = target_dir + os.sep +time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -r {0} {1}".format(target,
                                      ' '.join(source))

print ("Zip command is:")
print (zip_command)
print ("Running:")

if os.system(zip_command) == 0:
    print('Successful', target)
else:
    print('Backup failed')
