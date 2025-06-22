from fastapi import FastAPI
from pydantic import BaseModel,Field
from datetime import datetime
  


class user_info(BaseModel):
    user_name    : str
    phone_number : str
    experince    : str
    education    : str
    address      : str
    created_at: datetime = Field(default_factory=datetime.now)



App= FastAPI()

@App.post("/info")
def get_info(user_input:user_info):
 # store_info_data=user_input=params
  
    return{
        
        'message':'store_info_data  is get successfully',
        'name':user_input.user_name
        # 'phone_number': user_input.phone_number
           
           }


