from datetime import datetime
from . import models

class SignUp():
    def __init__(self,username,password,name,email,phone,nickname,identity):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone
        self.nickname = nickname
        self.identity_ = identity

    def __call__(self, *args, **kwargs):

        if self.is_exist():
            return False
        self.add_user()
        self.add_identity()
        self.add_role()
        return True


    def is_exist(self):
        user = models.User.objects.filter(username=self.username)
        if user:
            return True
        else:
            self.user = models.User()
            self.role = models.Role()
            if self.identity_:
                self.identity = models.Employer()
            else:
                self.identity = models.Hirer()

    def add_user(self):
        self.user.username = self.username
        self.user.password = self.password
        self.user.create_time = datetime.now()
        self.user.save()

    def add_role(self):
        self.role.name = self.name
        self.role.email = self.email
        self.role.phone = self.phone
        self.role.nick_name = self.nickname
        self.role.user = self.user
        self.role.save()

    def add_identity(self):
        self.identity.user = self.user
        self.identity.save()


class Login():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.exist = None

    def __call__(self, *args, **kwargs):
        if self.is_exist():
            return self.identification()

        return False


    def is_exist(self):
        exist =  models.User.objects.filter(username=self.username, password=self.password).first()
        if exist:
            self.exist = exist
            return True
        else:
            return False

    def identification(self):

        if models.Hirer.objects.filter(user_id=self.exist.u_id):
            return 'hirer'
        if models.Employer.objects.filter(user_id=self.exist.u_id):
            return 'employer'
        return False











