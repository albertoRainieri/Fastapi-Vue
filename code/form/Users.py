import sys, os
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from typing import List
from typing import Optional
from fastapi import Request
from models.UserModel import UserSchema


class UserCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.username: Optional[str] = None
        self.email: Optional[str] = None
        self.password: Optional[str] = None

    async def load_data(self):
        form = self.request
        self.username = form.name
        self.email = form.email
        self.password = form.hashed_password

    async def is_valid(self):
        if not self.username or not len(self.username) > 3:
            self.errors.append("Username should be > 3 chars")
        if not self.email or not (self.email.__contains__("@")):
            self.errors.append("A correct email is required")
        if not self.password or not len(self.password) >= 4:
            self.errors.append("Password must be > 4 chars")
        if not self.errors:
            return True
        return False

    
