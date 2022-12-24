#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
API_ID=15254258
API_HASH="107dc8de4b11afca514ad02f3e1a2efb"
AUTH_USERS=5756203736
    BOT_TOKEN ="5928583787:AAF_iQsaJtNJe7nItmbnEEpr9sNXCOB4Fpg"
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    AUTH_USERS = os.environ.get("OWNER")

    
