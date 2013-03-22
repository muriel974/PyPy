from Tar import *
#from TarDir import *
#from TarFile import *

x = Tar('projet2.tar')
x.open_tar()


#x.file.seek(124)
#taille = x.file.read(12)
#print(taille)
#x.file.seek(512)
#print(x.file.readline())

x.read_head()


x.close_tar()

