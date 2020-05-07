import discord
from discord.ext import commands 
import random as rn
import time as ti
import pickle
import os
import asyncio

from smartref import *

#if you need
#copy this:
#from bot_systatus import *

def tokengetter():
    if os.path.exists("servant.token"):
        theshell = open("servant.token","rb")
        token = pickle.load(theshell)
        #print(token)
        return token
    else:
        if os.path.exists("guard.py"):
            os.system('python guard.py')
            print("Token is not found, please execute guard.py to add token")
        else:
            raise FileNotFoundError(
                "'guard.py' is not found, please reinstall the pyfile of bot")

def ownergetter():
    if os.path.exists("admin.token"):
        theshell = open("admin.token","rb")
        admin = pickle.load(theshell)
        #print(token)
        return admin
    else:
        if os.path.exists("guard.py"):
            os.system('python guard.py')
            print("Owner ID is not yet to set, please execute guard.py to add token")
        else:
            raise FileNotFoundError(
                "'guard.py' is not found, please reinstall the pyfile of bot")

class sysinf:
    path = os.getcwd()
    current = ti.strftime("%Y-%m-%d %H:%M:%S", ti.localtime())

    gamelist = refdict([
        'League of Legend', 'Minecraft',
        'Minecraft: Hypixel Server', "少女前線 Girls' Frontline",
        'Fate / Grand Order', 'Asphalt 8',
        '巴哈姆特動畫瘋', 'Shironeko Project',
        '神魔之塔', '賽爾號', 'n94爾號',
        'Fire Emblem Heros', '2048', 'Rebel Inc.',
        '波蘭球：末世維穩', '靈異陰陽錄'
        ])

    #controll-allowed var.
    var_locals = locals()
    var_key = list(var_locals)
    var_key.remove('__module__')
    var_key.remove('__qualname__')
    var_key.remove('var_locals')
    #__module__: __main__
    #__qualname__: varping
    #print(var_key)

class admin:
    owner = ownergetter()
    coowner = []
    member = owner + coowner

    def checker(user_id):
        for i in admin.member:
            if user_id == i:
                print(i, 'confirm')
                return True
        print(user_id, 'fail to confirm')
        return False

    def append():
        print('adminappend active')
        return
##############################

print("bot_systatus ready")
print(sysinf.current)
print("-"*20)
