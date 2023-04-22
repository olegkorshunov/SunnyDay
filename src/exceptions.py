from fastapi import HTTPException, status


class HttpException:
    UserAlredyExis = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="User alredy exist",
    )
    IncorrectEmailOrPassword = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Incorrect email or password",
    )
    AuthTokenExpier = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Auth token has expired",
    )
    TokenAbsent = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token is absent",
    )
    IncorrectTokenFormat = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect token format",
    )
    UserDataNotFound = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User data not found",
    )
    RoomCanNotBeBooked = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="The room can not be booked",
    )
