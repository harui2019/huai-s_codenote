import discord
from discord.ext import commands 
import random as rn
import time as ti
import pickle
import os
import asyncio
import inspect

from smartref import *

os.system('python bot_systatus.py')
from bot_systatus import *
import bot_testpack
import bot_game
import bot_normal

#color = 0xc40000
#c40000

##############################
####bot_systatus
####if there is changing, update to bot_systatus.py
##############################
bot = commands.Bot(command_prefix='!!')

def allruncheck():
    os.system('python bot_systatus.py')
    os.system('python bot_testpack.py')
    os.system('python bot_game.py')
    os.system('python bot_normal.py')

token = tokengetter()

print("Initialling ...")
print(sysinf.current)
print('file location detction: ' + sysinf.path)
print("-"*20)

##############################

@bot.event
async def on_ready():
    print("-"*20)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(sysinf.current)
    bot_normal.comrestaur.update()
    act = discord.Activity(
        name = sysinf.gamelist.randref() ,
        type = discord.ActivityType.playing)
    await bot.change_presence(activity = act)
    print("-"*20)

##############################
####bot_main&event
    
class varping:
    method = '0'
    gates = True
    timeshow = '0'

    #controll-allowed var.
    var_locals = locals()
    var_key = list(var_locals)
    var_key.remove('__module__')
    var_key.remove('__qualname__')
    var_key.remove('var_locals')
    #__module__: __main__
    #__qualname__: varping

class comping:
    async def method_0(ctx):
        ping = round(bot.latency * 1000)
        return ping
    
    async def method_1(ctx):
        time_1 = ti.perf_counter()
        await ctx.trigger_typing()
        time_2 = ti.perf_counter()
        ping = round((time_2-time_1)*1000)
        return ping
    
    def cpxmethod(ctx, n):
        way = 'method_' + str(n)
        method = getattr(comping, way, lambda :'Invalid')
        return method(ctx)

    async def gates(ctx):
        if varping.gates:
            pic = discord.File(sysinf.path + '\\other\\pong.jpg')
            await ctx.send(file = pic)
        else:
            print('gates_pingpong off')

    async def timeshow_0(ctx):
        now = discord.Embed(
            title = f"現在時間 : ",
            description = ti.strftime("%Y年%m月%d日 %H時%M分%S秒", ti.localtime()),
            color = 0xc40000)
        await ctx.send(embed = now)

    async def timeshow_1(ctx):
        await ctx.send(ti.strftime("%Y年%m月%d日 %H時%M分%S秒", ti.localtime()))
        
@bot.command()
async def ping(ctx):
    ping = 0
    if varping.method == '0':
        ping = await comping.method_0(ctx)
    elif varping.method == '1':
        ping = await comping.method_1(ctx)
    elif varping.method == 'all':
        for i in range(0, 2):
            ping_i = await comping.cpxmethod(ctx, i)
            ref = 'method_' + str(i) + ' : ' + str(ping_i)
            print(ref)
            await ctx.send(ref)
    else:
        print("method no found, reset to method_0")
        ping = await comping.method_0(ctx)
        varping.method = '0'

    if varping.method != 'all':
        ref = f"這顆球用了{ping}毫秒飛過來\npong"
        print(ref)
        await ctx.send(ref)
        await comping.gates(ctx)
    
    if ping >= 1000:
        await ctx.send("連月球來的訊息都比你快，bb寬頻/中嘉網路") 
    print(sysinf.current)
    print("-"*20)

@bot.command()
async def current(ctx):
    if varping.timeshow == '0':
        await comping.timeshow_0(ctx)
    elif varping.timeshow == '1':
        await comping.timeshow_1(ctx)
    else:
        print("method no found, reset to show embed")
        await comping.timeshow_0(ctx)
        varping.timeshow = '0'
    print(ti.strftime("%Y年%m月%d日 %H時%M分%S秒", ti.localtime()))
    print("-"*20)
##############################

class vmsg:
    private = True

    last = ti.time()
    oversend = 0
    limit = 10
    over_sec = 1000/1000

    allow = 3 #min = 3 max = 10
    lastref = []
    repeat_sec = 5

    #controll-allowed var.
    var_locals = locals()
    #print(var_locals)
    var_key = list(var_locals)
    var_key.remove('__module__')
    var_key.remove('__qualname__')
    var_key.remove('var_locals')
    #__module__: __main__
    #__qualname__: varping

class cmsg:
    def lastref():
        temp = []
        for i in range(vmsg.allow):
            temp.append(str(i))
        return temp

    def isallsame():
        n = vmsg.allow - 1
        m = 0
        for i in range(n):
            if vmsg.lastref[i+1] == vmsg.lastref[i]: m += 1
        
        if m == n: return True
        else     : return False
    
    def record(message):
        print(">>> ", sysinf.current)
        print(">>> message.author: ", message.author)
        print(">>> message :", message.content.lower())
        print("-" * 20)
    
    async def botref(message):
        i = message.content.lower()
        end_sign = i.find(">->")
        msg_sign = i.find("<-")
        inf_sign = i.find("-<")
        _str_= ''

        if end_sign == -1:
            await message.channel.send("end sign '>->' no found")
            print("end sign '>->' no found")
            print(_str_)
        
        elif '<-embed' in i:
            _str_ = i[inf_sign + 2 : end_sign]            
            #if '+color' in i:
                #color = 0xc40000
            _embed_ = discord.Embed(title = _str_)
            print(_str_)
            await message.channel.send(embed = _embed_)
        elif '<-<' in i:
            _str_ = i[inf_sign + 2 : end_sign]
            print(_str_)
            await message.channel.send(_str_)
        print('special input: ', _str_)
        print('message.author: ' + str(message.author))
        print(sysinf.current)
        print("-"*20)
            
    async def check(key, delta):
        #input key, delta
        warn = ''
        #prevent repeat send
        if type(key[0]) == int:
            del vmsg.lastref[0]
            vmsg.lastref.append(key)
            print(vmsg.lastref)
        else: pass
        if delta >= vmsg.repeat_sec:
            vmsg.lastref[1] = ['_','null']
            print(vmsg.lastref, vmsg.repeat_sec)
        else: pass
        
        #prevent oversend
        if delta <= vmsg.over_sec:
            vmsg.oversend += 1
            print('oversend',vmsg.oversend)
        else:
            if vmsg.oversend > 0:
                timecut = int(int(delta)/vmsg.over_sec) - 1
                if timecut <= vmsg.oversend:
                    vmsg.oversend -= timecut
                else:
                    vmsg.oversend = 0
                print('oversend-=',vmsg.oversend, timecut)
            else: pass

        #stopper
        if vmsg.oversend >= vmsg.limit:
            #oversend break
            warn = 'send overload, please type later'
            vmsg.oversend -= 1
        elif cmsg.isallsame():
            #repeat warning
            warn = 'repeat msg, please type other one'
        else: pass
        return warn

    async def dig_eq(talk):
        key = ['_','null']
        close = False
        for i in range(commend.num_eq):
            if commend.by_eq[i]['key'] == talk:
                key = [i, 'eq']
                close = True
        return close, key

    async def dig_in(talk):
        key = ['_','null']
        close = False
        for i in range(commend.num_in):
            if commend.by_in[i]['key'] in talk:
                key = [i, 'in']
                close = True
        return close, key

    ###O(n)
    async def powerpick(message, key = ['_','null']):
        ref = []
        if key[1] == 'eq':
            target = commend.by_eq[key[0]]['ref']
        elif key[1] == 'in':
            target = commend.by_in[key[0]]['ref']
        else:
            return ref
        for j in target:
            if j[0] == 'file':
                if os.path.exists(j[1]):
                    ref.append(
                        await message.channel.send(
                            file = discord.File(j[1])))
                else:
                    print(FileNotFoundError)
            else:
                ref.append(
                    await message.channel.send(j))
        return ref
    #this class contains 11 def/async def
vmsg.lastref = cmsg.lastref()

class commend:
    #key: 0 for = , 1 for in
    by_eq = {
        0 : {'key' : '666',
             'ref' : ['666']
             },
        1 : {'key' : '令咒',
             'ref' : [('The prefix for this server is `'+ bot.command_prefix
                      +'`, which has been customised.')]
             },
        2 : {'key' : '哦三小',
             'ref' : ['閉嘴啦，你知道你主人代數55嗎']
             },
        3 : {'key' : '夢霆0a0',
             'ref' : ['起床上課','<@636214432476954633>']
             }
        }

    by_in = {
        0 : {'key' : 'moodle',
             'ref' : ['http://moodle.nccu.edu.tw/my/']
             },
        1 : {'key' : 'wm5',
             'ref' : ['https://wm5.nccu.edu.tw/mooc/index.php']
             },
        2 : {'key' : '哦三小',
             'ref' : ['閉嘴啦，你知道你主人代數55嗎']
             },
        3 : {'key' : '巴哈我大哥',
             'ref' : ['https://ani.gamer.com.tw/',
                      ['file',sysinf.path + '\\other\\bahamyboss.jpg']
                      ]},
        4 : {'key' : '夜襲',
             'ref' : [['file', sysinf.path + '\\other\\ironhanfan.png']
                      ]},
        5 : {'key' : 'microbit',
             'ref' : ['https://makecode.microbit.org/',
                      "Let's coding"
                      ]},
        6 : {'key' : ':weary:',
             'ref' : [['file', sysinf.path + '\\memeadmin\\spfield_.jpg'],
                      "嗯"
                      ]}
        }

    num_eq = len(by_eq)
    num_in = len(by_in)
    #print(num_eq)

@bot.event
async def on_message(message):
    now = ti.time()
    talk = message.content.lower()
    
    n = vmsg.allow - 1
    delta = now - vmsg.last
    key = ['_','null']
    warn = ''
    close = False
    ref = []

    #vmsg.private = True
    if vmsg.private == True:
        cmsg.record(message)
    
    if message.author == bot.user:
        return
    
    if talk == '':
        close = True
    elif "<-" in talk:
        await cmsg.botref(message)
        close = True
    elif bot.user.mentioned_in(message):
        await message.channel.send(
            'The prefix for this server is`' +
            bot.command_prefix + '`, which is the default.')
        close = True
    else: pass

    if close:
        vmsg.last = now
        ##### warning! warning! warning! warning! warning! warning! #####
        await bot.process_commands(message)     #do not delete this line
        ##### warning! warning! warning! warning! warning! warning! #####
        return

    task_eq = asyncio.create_task(cmsg.dig_eq(talk))
    task_in = asyncio.create_task(cmsg.dig_in(talk))
    result_eq = await task_eq
    result_in = await task_in
    if result_eq[0] or result_in[0]:
        task_eq.cancel() and task_in.cancel()
    if result_eq[0]: close, key = result_eq
    if result_in[0]: close, key = result_in
    
    if close:
        task_check = asyncio.create_task(cmsg.check(key, delta))
        warn = await task_check
        if warn != '':
            print('warning: ',warn)
            await message.channel.send(warn)
        else:
            await cmsg.powerpick(message, key)
    
    vmsg.last = now
    ##### warning! warning! warning! warning! warning! warning! #####
    await bot.process_commands(message)     #do not delete this line
    ##### warning! warning! warning! warning! warning! warning! #####


##############################
#####
'''
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f' 歡迎御主{member.name}，的加入')
    print(f"new member : {member.name}")
    print(sysinf.current)
    print("-"*20)
'''
##############################
#####
#@bot.event
async def on_command_error(ctx, error):
    '''
    if isinstance(error, commands.errors.CommandNotFound):
        print(error)
    elif isinstance(error, commands.BadArgument):
        print(error)
    elif isinstance(error, FileNotFoundError):
        print(error)
    '''
    print('####################')
    print('###error detected###')
    print('####################')
    await ctx.send('error detected')
    print(error)
    await ctx.send(error)
    print('ctx.message.author: ' + str(ctx.message.author))
    print(sysinf.current)
    print("-"*20)

##############################
#####
    
async def unsummon(ctx):
    print('unsummon')
    user = ctx.message.author
    if admin.checker(user.id):
        await ctx.send("administrator, " + str(user) + ", confirmed")
        print("administrator, " + str(user) + ", confirmed")
    else:
        
        r = rn.sample(range(0,2),1)
        #try switch case
        if r == 0:line_recall = f'{ctx.message.author}你誰'
        else     :line_recall = f'{ctx.message.author}，汝非吾之御主'
        recall = discord.Embed(title = line_recall)
        await ctx.send(embed = recall)
        
        print('ctx.message.author: ' + str(user))
        print(sysinf.current)
        print("-"*20)
        return
    msg = "從者 " + str(bot.user.name) + " 解除召喚"
    unsummon = discord.Embed(title = msg, color = 0xc40000)
    await ctx.send(embed = unsummon)
    print(msg)
    print(sysinf.current)
    print(str(bot.user.name) + ", logout and close")
    await ctx.send(str(bot.user.name) + ", logout and close")
    print("-"*20)
    print("-"*20)
    #await bot.logout()
    await bot.close()

##############################
def varcalling():
    print('sysinf', sysinf.var_key)
    print('varping', varping.var_key)
    print('onmsg.commend',commend)
    print('onmsg', vmsg.var_key)
    
    print('cal', bot_normal.vcal.var_key)
    print('game1a2b', bot_game.var1a2b.var_key)
    
varcalling()

@bot.command()
async def varset(ctx, *args):
    #varping.method = 'all' work!!
    print("varset")
    print("*args : " + str(args))
    user = ctx.message.author
    if len(args) == 0:
        await ctx.send('no code detected')
        return
    temp_args = list(args)
    print(type(temp_args))
    del args
    args = temp_args
    
    com_name = ''
    for i in args:
        com_name = com_name + i + '_'
    com_name = com_name[:-1]
    print("var name: " + com_name)

    var_class = ''
    var_name = ''
    var_change = ''

    for name, obj in inspect.getmembers():
        # TypeError: getmembers() missing 1 required positional argument: 'object'
        if inspect.isclass(obj):
            print(name)


##############################
####bot_testpack

@bot.command()
async def isadmin(ctx):
    await bot_testpack.isadmin1(ctx)

@bot.command()
async def testcommand(ctx):
    await bot_testpack.testcommand(ctx)
    
##############################
####bot_game

@bot.command()
async def game1a2b(ctx, g_str: str = '',h :int = 8):
    await bot_game.main1a2b(ctx, g_str ,h)
    #print(bot_game.g1a2b.limit)
    #bot_game.g1a2b.limit = 2 #it's working
    #print(bot_game.g1a2b.limit)

##############################
####bot_normal

@bot.command()
async def cal(ctx, a:str = '', b:str = '', c:str = ''):
    await bot_normal.cal(ctx, a, b, c)

@bot.command()
async def lunch(ctx, *args):
    await bot_normal.lunch(ctx, args)
##############################
##############################
bot.run(token)
