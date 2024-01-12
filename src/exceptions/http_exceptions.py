from fastapi import HTTPException, status


class SunnyDayBaseException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExist(SunnyDayBaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User alredy exist"


class IncorrectEmailOrPassword(SunnyDayBaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Incorrect email or password"


class AuthTokenExpire(SunnyDayBaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Auth token has expired"


class TokenAbsent(SunnyDayBaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token is absent"


class IncorrectTokenFormat(SunnyDayBaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"


class UserDataNotFound(SunnyDayBaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User data not found"


class RoomCanNotBeBooked(SunnyDayBaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "The room can not be booked"

