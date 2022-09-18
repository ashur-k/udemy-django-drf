from rest_framework.exceptions import APIException


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "You can't edit a profile that doesnt't belong to you!"


class CantFollowYourself(APIException):
    status_code = 403
    default_detail = "You can't follow yourself!"


class NotValidData(APIException):
    status_code = 403
    default_detail = "Serializer data is not valid!"
