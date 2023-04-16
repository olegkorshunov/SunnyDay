from src.auth.models import UserAccount
from src.dao.daobase import DaoBase


class DaoAuth(DaoBase):
    model = UserAccount
