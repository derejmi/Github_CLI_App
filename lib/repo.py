''' Defining the Repo Class ''' 

class Repo():
    all = []

    def __init__(self, data):
        self._name = data['name']
        self._isFork = data['fork']
        self._language = data['language']
        self._created_at = data['created_at']
        self._username = data['owner']['login']
        self._save()
    
    def _save(self):
        self.all.append(self)
    
    def get_name(self):
        return self._name
    
    def check_fork(self):
        return self._isFork

    def get_language(self):
        return self._language
    
    def created_at(self):
        return self._created_at
    
    def username(self):
        return self._username
    
    @classmethod 
    def find_by_input(cls,user_input):
        return cls.all[int(user_input)-1]
    
