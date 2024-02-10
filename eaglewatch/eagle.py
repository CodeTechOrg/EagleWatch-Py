import requests
from json import JSONDecodeError
from typing import Union, List, Dist



class error(Exception):
    '''some error'''
    pass

class Banned():
    UserId: int
    Crime: str
    Date: str
    Admin: int
    Link: str

    def __init__(self, UserId: int, Crime: str, Admin: int, Date: int, Link: int) -> None:
        self.UserId = UserId
        self.Crime = Crime
        self.Admin = Admin
        self.Date = Date       
        self.Link = Link


class Eagle(object):

    def __init__(self) -> None:
        response = requests.get(
            f"https://eaglewatch-1081dedcfdfb.herokuapp.com/"
        )
        if resp.status_code != 201:
            self._error_(resp)
    
    
       
    
    def getinfo(self, UserId: int) -> Union[Banned, bool]:
        resp = requests.get(f"https://eaglewatch-1081dedcfdfb.herokuapp.com/info/{UserId}")
        if resp.status_code == 201:
            if resp.json()["banned"]:
                return Banned(**response.json())
            else:
                return False
        else:
            self._error_(resp)

        
    def getban(self, UserId: int, Crime: str, Admin: int, Date: str, Link: str, Eagle_Token: str) -> bool:
        data = {          
            "UserId": UserId,
            "Crime": Crime,
            "Admin": Admin,
            "Date": Date,
            "Link": Link,
            "Eagle_Token" : Eagle_Token
        }

        resp = requests.post("https://eaglewatch-1081dedcfdfb.herokuapp.com/addban", data=data)
        if resp.status_code == 201:
            return True
        else:
            self._error_(resp)
    
    def updateban(self, UserId: int, Crime: str, Admin: int, Date: str, Link: str, Eagle_Token: str) -> bool:
        data = {          
            "UserId": UserId,
            "Crime": Crime,
            "Admin": Admin,
            "Date": Date,
            "Link": Link,
            "Eagle_Token" : Eagle_Token
        }


        resp = requests.post("https://eaglewatch-1081dedcfdfb.herokuapp.com/updateban", data=data).json()
        if resp.status_code == 201:
            return True
        else:
            self._error_(resp)

    def deleteban(self, UserId: int, Eagle_Token : str) -> bool:
        data = {
            "UserId": UserId,
            "Eagle_Token" : Eagle_Token
        }

        resp = requests.delete("https://eaglewatch-1081dedcfdfb.herokuapp.com/removeban", data=data)
        if resp.status_code == 201:
            return True
        else:
            self._error_(resp)
    
    
    

    def _error_(self, resp):
        try:
            msg = resp.json()["msg"]
        except JSONDecodeError:
            raise InternalServerError("Server issue")
        if resp.status_code == 401:
            raise error(msg)
        else:
            raise BadRequest(msg)
