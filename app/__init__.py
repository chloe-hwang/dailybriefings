

import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", default="development") # use "production" on a remote server

#development env: developing it locally on our computer 
#app_env can be updated via env variables on the server 
    #use "production" on a remote, user-facing server 
#helps detect which env running the app from 