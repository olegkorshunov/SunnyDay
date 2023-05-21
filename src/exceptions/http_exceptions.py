from fastapi import HTTPException, status


class SunnyDayException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlredyExis(SunnyDayException):
    status_code = (status.HTTP_409_CONFLICT,)
    detail = ("User alredy exist",)


class IncorrectEmailOrPassword(SunnyDayException):
    status_code = (status.HTTP_409_CONFLICT,)
    detail = ("Incorrect email or password",)


class AuthTokenExpier(SunnyDayException):
    status_code = (status.HTTP_401_UNAUTHORIZED,)
    detail = ("Auth token has expired",)


class TokenAbsent(SunnyDayException):
    status_code = (status.HTTP_401_UNAUTHORIZED,)
    detail = ("Token is absent",)


class IncorrectTokenFormat(SunnyDayException):
    status_code = (status.HTTP_401_UNAUTHORIZED,)
    detail = ("Incorrect token format",)


class UserDataNotFound(SunnyDayException):
    status_code = (status.HTTP_404_NOT_FOUND,)
    detail = ("User data not found",)


class RoomCanNotBeBooked(SunnyDayException):
    status_code = (status.HTTP_409_CONFLICT,)
    detail = ("The room can not be booked",)


print(globals())
