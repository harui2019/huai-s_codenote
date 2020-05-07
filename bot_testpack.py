from bot_systatus import *

import bot_game

#from bot_main import sysinf

class vartest():
    test_1 = True

async def isadmin1(ctx):
    
    output = ''
    user = ctx.message.author
    if admin.checker(user.id):
        output = 'yes'
    else :
        output = 'no'
    print(output)
    await ctx.send(output)
    
    print('ctx.message.author: ' + str(user.id))
    print(sysinf.current)
    print("-"*20)

#bot_game.test1a2b()

async def testcommand(ctx):
    vars()
    if vartest.test_1:
        print('test_1 send')
        await ctx.send('test_1 send')

'''
class refkey():
    def __init__(self, content = {}):
        

def output(location = '', name = str(list(locals().keys())[0])):
    if name == "__module__":
        print("###locals() may not detect the variable's name")
        print("###please make a good one")
    print("file name: ",name)
    key = '{0},<_key_<{1}>_>,\n

    
    ref_head = "{0},<_ref_<"
    ref_tail = ">_>,\n"
    endline = '{0},<_end_>,\n'
    
    filename = f"{location}\\{name}_output.csv"
    file = open(filename, 'w+', encoding='utf-8')

    file.write(_title_)
        
        for i in range(0, len(self.content)) :
            file.write(_lead_.format(str(i)))
            
            if type(self.content[i]) == str:
                file.write(self.content[i])
            else:
                file.write(str(self.content[i]))
                
            if i != len(self.content)-1:
                file.write(_enter_)
            else:
                file.write(_end_)
        
        file.close()
        print(_filename_ + "has saved")
'''


print("this is a test")
print("bot_testpack ready")
print(sysinf.current)
print("-"*20)
