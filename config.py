#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
API_ID=23539681
API_HASH="ae1430184ae21aa81b4b030d1bd75885"
AUTH_USERS=5007135395
    BOT_TOKEN ="6548483719:AAFCxCqSDGI_VE1KEjrzwB605uCfm3MAAcE"
    BOT_TOKEN = os.environ.get("6548483719:AAFCxCqSDGI_VE1KEjrzwB605uCfm3MAAcE")
    # The Telegram API things
    API_ID = int(os.environ.get("23539681"))
    API_HASH = os.environ.get("ae1430184ae21aa81b4b030d1bd75885")
    AUTH_USERS = os.environ.get("5007135395")

    
