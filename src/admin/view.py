from sqladmin import ModelView

import src.models as m


class AdminUser(ModelView, model=m.UserAccount):
    column_list = [m.UserAccount.id, m.UserAccount.email] + [m.UserAccount.booking]
    column_details_exclude_list = [m.UserAccount.hashed_password]
    # TODO: add roles: [user,admin]
    # TODO: investigate how to fix hash password
    name = "UserAccount"
    name_plural = "UserAccounts"
    icon = "fa-solid fa-user"

    can_create = False
    can_edit = False
    can_delete = False
    can_view_details = True


class AdminBooking(ModelView, model=m.Booking):
    column_list = [c.name for c in m.Booking.__table__.c] + [m.Booking.user_account, m.Booking.room]
    name = "Booking"
    name_plural = "Bookings"


class AdminHotel(ModelView, model=m.Hotel):
    column_list = [c.name for c in m.Hotel.__table__.c]
    name = "Hotel"
    name_plural = "Hotels"


class AdminRoom(ModelView, model=m.Room):
    column_list = [c.name for c in m.Room.__table__.c]
    name = "Room"
    name_plural = "Rooms"
