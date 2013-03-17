class Tar (object):
    def __init__ (self, nomTar):
        self.nomTar = nomTar

    def open_tar (self):
        try :
            self.file = open(self.nomTar, 'r')
            print 'open'
        except IOError as e :
            print 'The file can\'t be opened'

    def close_tar (self):
        pass
    def chdir_tar (self):
        pass
    def get_pwd_tar (self):
        pass
    def opendir_tar (self):
        pass
