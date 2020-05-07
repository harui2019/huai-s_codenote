from bot_systatus import *

##############################

class com1a2b:
    def ansmaker():
        a = True
        while a:
            r = rn.sample(range(0, 10),4)
            if r[0] == 0: continue
            else: a = False
        return r[0]*1000 + r[1]*100 + r[2]*10 + r[3]*1

    def istruetype(g):
        if g.isdigit():
            repeat_check = 0  
            if len(g)==4:
                for i in range(0,4):
                    print(g[i])
                    for j in range(0,4):
                        if g[i] == g[j]:
                            repeat_check += 1
                print('repeat_check',repeat_check)
                if repeat_check == 4:
                    return True
        return False

class var1a2b:
    
    time: int = 0
    limit: int = 8
    answer = com1a2b.ansmaker()

    gameref = {
        0 : "4A0B,你答對了 共猜{0:d}次，棒棒答｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡",
        1 : "0不會在第一位喔",
        2 : "{0:d}A{1:d}B，你己猜{2:d}次，加油d(`･∀･)b",
        3 : "答案是{0:d}，休息下再來挑戰吧_(:3 」∠ )_",
        4 : "哪個智障把次數設成{0:d}，出來挨打（╯°□°）╯︵(\ .o.)\'，{1:d}A{2:d}B，你己猜{3:d}次",
        5 : "var1a2b times change {0:d} -> {1:d}",
        6 : "沒有輸入的話我啥都不會做ㄛ(๑¯ω¯๑)",
        7 : "重來囉_(:3 」∠ )_",
        8 : "本作品由樹桶數統出品",
        9 : "你目前共猜{0:d}次，棒棒答｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡"
        }
       
    badentry = refdict({
        0: '不要亂打~好嗎~(๑¯ω¯๑)',
        1: '不要亂輸啦(╬ﾟдﾟ)'
        })

    #controll-allowed var.
    var_locals = locals()
    #print(var_locals)
    var_key = list(var_locals)
    var_key.remove('__module__')
    var_key.remove('__qualname__')
    var_key.remove('var_locals')

    var_key.remove('__annotations__')
    #__module__: __main__
    #__qualname__: varping

def test1a2b():
    try:
        print(var1a2b.answer)
        print(var1a2b.limit)
        print(var1a2b.time)
        print(var1a2b.gameref[0])
        print(var1a2b.badentry.randref())
        
        print(type(var1a2b.answer))
        print(type(var1a2b.limit))
        print(type(var1a2b.time))
        print(type(var1a2b.gameref[0]))
        print(type(var1a2b.badentry))
    
        var1a2b.answer = com1a2b.ansmaker()
        print(var1a2b.answer,1)
        var1a2b.answer = com1a2b.ansmaker()
        print(var1a2b.answer,2)
    
        var1a2b.answer = com1a2b.ansmaker()
        a_str = str(var1a2b.answer)
        print(a_str)
        print(type(a_str))
    
        g_str = '1234'
        print(g_str)
        print(com1a2b.istruetype(g_str))
    
        g_str = '1224'
        print(g_str)
        print(com1a2b.istruetype(g_str))
    
        g_str = '12342'
        print(g_str)
        print(com1a2b.istruetype(g_str))
    
        print(var1a2b)
        print(com1a2b)
        return True
    except:
        return False

    
async def main1a2b(ctx, g_str: str = '', h :int = 8):
    print('1a2b')
    t = ''
    if com1a2b.istruetype(g_str):        
        guess = int(g_str)
        a_str = str(var1a2b.answer)
        
        print("guess : ", guess)
        print("answer: ", var1a2b.answer)
        
        if guess == var1a2b.answer:
            var1a2b.time += 1
            t = var1a2b.gameref[0]
            await ctx.send(t)
            var1a2b.answer = com1a2b.ansmaker()
            var1a2b.time = 0
        
        elif guess < 1000:
            t = var1a2b.gameref[1].format(var1a2b.time)
            await ctx.send(t)
            
        else:
            a = 0
            b = 0
            var1a2b.time += 1
    
            for i in range(4):
                if g_str[i] == a_str[i]:
                    a += 1
                else:
                    for j in range(4):
                        if g_str[i] == a_str[j]:
                            b += 1
                            
            if var1a2b.time <= var1a2b.limit:
                t = var1a2b.gameref[2].format(a, b, var1a2b.time)
                await ctx.send(t)
                
                if var1a2b.time == var1a2b.limit:
                    t = var1a2b.gameref[3].format(var1a2b.answer)
                    await ctx.send(t)
                    var1a2b.answer = com1a2b.ansmaker()
                    var1a2b.time = 0
                    
            elif var1a2b.limit <= 0:
                t = var1a2b.gameref[5].format(var1a2b.limit, 8)
                await ctx.send(
                    var1a2b.gameref[4].format(var1a2b.limit, a, b, var1a2b.time))
                await ctx.send(t)
                var1a2b.limit = 8
            else: pass
            
    elif g_str == '':
        t = var1a2b.gameref[6]
        await ctx.send(t)
        
    elif g_str == "reset":
        t = var1a2b.gameref[7]
        await ctx.send(t)
        var1a2b.answer = com1a2b.ansmaker()
        var1a2b.time = 0
        print("answer: ", var1a2b.answer)
        
    elif g_str == "settime" :
        if type(h) == int:
            h = int(h)
            t = var1a2b.gameref[5].format(var1a2b.limit, h)
            await ctx.send(t)
            var1a2b.limit = h
        else:
            t = var1a2b.badentry.randref()
            await ctx.send(t)

    elif g_str == "author":
        await ctx.send(
            embed = discord.Embed(
                title = var1a2b.gameref[8], color = 0xc40000))

    elif g_str == "time":
        t = var1a2b.gameref[9].format(var1a2b.time)
        await ctx.send(t)

    else:
        t = var1a2b.badentry.randref()
        await ctx.send(t)

    print(t)
    
    print('ctx.message.author: ' + str(ctx.message.author))
    print(sysinf.current)
    print("-"*20)

##############################


##############################

print("bot_game ready")
print(sysinf.current)
print("-"*20)
