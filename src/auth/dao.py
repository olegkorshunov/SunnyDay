from src.auth.models import UserAccount
from src.dao.daobase import DaoBase


class DaoAuth(DaoBase[UserAccount]):
    model = UserAccount
