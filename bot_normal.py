from bot_systatus import *

#bot_normal

##############################
#####cal
class vcal:
    bravo = refdict({
        0: '這裡有一位偉大的數學家發現了要如何除以0',
        1: '我們的0似乎不再是addiion identity elt.', 
        2: '{0:s}年菲爾茲獎得主：{1:s} \n以及他的論文：「除以0的運作原理」',
        3: 'siri: 想像一下你有0塊餅乾，要將他們分給0個朋友，那每個人可以得到幾塊餅乾？你看，一點道理都沒有，餅乾怪物會因為沒有餅乾而悲哀，而你則會因為沒有朋友而難過'
        })
    '''
    bravo.output(
        filetype = "csv",
        location = sysinf.path + "\\ref",
        name = "cal_bravo")
    '''
    baker = refdict({
        0: "我是一台計算機",
        1: "我是一台烤麵包機 SCP-426,\n http://scp-wiki-cn.wikidot.com/scp-426",
        2: "我是一台洗碗機",
        3: "沒想到你是那種不會用計算機的稀世奇才",
        4: "你的小學老師應該要教你怎麼用計算機，\n喔不，這裡是華人社會，根本不該有計算機，教如何使用計算機只會一代不如一代",
        5: "自從有了計算機，現在的人已經連心算都不會了， 一代不如一代\n——fb上的可悲中年",
        6: "數學這麼爛，連早餐店老闆娘都比你會算，還用什麼計算機\n——fb上的可悲中年"
        })
    '''
    baker.output(
        filetype = "csv",
        location = sysinf.path + "\\ref",
        name = "cal_baker")
    '''
    mememen = refdict({0:"meth", 1:"fieldsmedal"})

    _0w0_ = refdict({0:"0w0", 1:"0_0", 2:"0A0"})

    #controll-allowed var.
    var_locals = locals()
    #print(var_locals)
    var_key = list(var_locals)
    var_key.remove('__module__')
    var_key.remove('__qualname__')
    var_key.remove('var_locals')

    #__module__: __main__
    #__qualname__: varping

class ccal:
    def load(ref, location, name):
        fileat = location + '\\' + name
        if type(ref) != refdict:
            return
        if name == '':
            return
        if os.path.exists(fileat):
            ref.read(location=fileat, edit= 'w')
            print(ref.property["name"], 'has load')
        else:
            ref.output(
                filetype = "csv",
                location = sysinf.path + "\\ref",
                name = name)
            return
        
ccal.load(
    ref = vcal.bravo,
    location = sysinf.path + "\\ref",
    name = "cal_bravo_output.csv")
ccal.load(
    ref = vcal.baker,
    location = sysinf.path + "\\ref",
    name = "cal_baker_output.csv")

async def cal(ctx, a, b, c):
    print('cal')
    user = ctx.message.author
    ref_bravo = vcal.bravo.randref().format(ti.strftime("%Y", ti.localtime()), ''+'@'+str(user))
    ref_baker = vcal.baker.randref()
    cal = discord.Embed(title=f"計算結果", color = 0xc40000)
    pick = False
    open_bravo = False
    open_baker = False
    if a == "help":
        cal = discord.Embed(title=f"計算機使用說明", color = 0xc40000)#c40000

        cal.add_field(name="加", value="+", inline=False)
        cal.add_field(name="減", value="-", inline=False)
        cal.add_field(name="乘", value="*", inline=False)
        cal.add_field(name="除", value="/", inline=False)
        cal.add_field(name="餘", value="%", inline=False)
        cal.add_field(name="括號", value="()", inline=False)
        cal.add_field(name="示範", value="輸入'2+3'\n=5", inline=False)
    
    elif a == "bravo":
        if b.isdigit():
            if 0 <= int(b) < vcal.bravo.property['len']:
                ref_bravo = vcal.bravo.showref(int(b)).format(
                    ti.strftime("%Y", ti.localtime()), ''+'@'+str(user))
                pick = True
        open_bravo = True
    elif a == "baker":
        if b.isdigit():
            if 0 <= int(b) < vcal.baker.property['len']:
                ref_baker = vcal.baker.showref(int(b))
                pick = True
        open_baker = True
    else :
        try :
            ans = eval(a)
            if ans == 0.0 :
                ans = vcal._0w0_.randref()
            cal.add_field(name=f"{a}=", value=f"{ans}", inline=False)
        except ZeroDivisionError as i :
            ref_pic = vcal.mememen.randref()
            pic = discord.File(sysinf.path+f"\\other\\{ref_pic}.jpg")
            await ctx.send(file = pic)
            open_bravo = True
            print(i, ref_bravo, ref_pic)        
        except:
            if admin.checker(user.id):
                await ctx.send("御主，目前沒有這個指令喔")
            else :
                #await ctx.send(kln_speak.randref().format(str(ctx.message.author)))
                #pic = discord.File(_path_ + f'\\kln\\{kln_version.randref()}.jpg')
                #await ctx.send(file = pic)
                pass
            open_baker = True
            print(ref_baker)
    if open_bravo:
        cal = discord.Embed(
            title = f"計算結果", description = ref_bravo, color = 0xc40000)
        if pick:
            cal.add_field(name=f"你選了bravo {b}", value="_", inline=False)
    elif open_baker:
        cal = discord.Embed(
            title = f"計算結果", description = ref_baker, color = 0xc40000)
        if pick:
            cal.add_field(name=f"你選了baker {b}", value="_", inline=False)
    else:
        pass
    await ctx.send(embed = cal)
    print('ctx.message.author: ' + str(user.id))
    print(sysinf.current)
    print("-"*20)

##############################
#####meme
    
class kln:
    version = refdict({
        0: 'origin', 1: 'multi', 2: 'jojo',
        3: 'pixel', 4: '3m_1', 5: 'brain',
        6: 'idontknow', 7: 'ontree', 8: '',
        9: 'panda_swx', 10: 'xi_hello', 11: 'xi_excalibur',
        12: 'shark_wtf' , 13: 'num4_smile'
        })

    speak = refdict({
        0: '@{0:s}，你好可憐，連指令都打不好',
        1: 'Rythm：我操你媽 你是在亂打三小?',
        2: '%dedwed'
        })

async def memeadmin(ctx, *args):
    print('memeadmin')
    print("*args : " + str(args))
    filename = ''
    for i in args:
        filename = filename + i + '_'
    filename = filename[:-1]
    print("filename : " + filename)

    final_path = sysinf.path + f'\\memeadmin\\{filename}'
    
    user = ctx.message.author
    if admin.checker(user.id):
        if os.path.exists(final_path + '.jpg'):
            pic = discord.File(final_path + '.jpg')
            await ctx.send(file = pic)
        elif os.path.exists(final_path + '.png'):
            pic = discord.File(final_path + '.png')
            await ctx.send(file = pic)
        else:
            await ctx.send("還沒有這個圖片喔")
        '''更新世界的锋芒'''
    else:
        await ctx.send("you aren't administrator")
        
    print('ctx.message.author: ' + str(user))
    print(sysinf.current)
    print("-"*20)


async def meme(ctx, *args):
    print('meme')
    print("*args : " + str(args))
    user = ctx.message.author
    
    filename = ''
    for i in args:
        filename = filename + i + '_'
    filename = filename[:-1]
    print("filename : " + filename)

    if filename == 'rand':
        final_path = sysinf.path + f'\\meme\\{kln.version.randref()}'
    else:
        final_path = sysinf.path + f'\\meme\\{filename}'
        
    if os.path.exists(final_path + '.jpg'):
        pic = discord.File(final_path + '.jpg')
        await ctx.send(file = pic)
        
    elif os.path.exists(final_path + '.png'):
        pic = discord.File(final_path + '.png')
        await ctx.send(file = pic)

    else:
        await ctx.send(kln.speak.randref().format(str(user)))
        final_path = sysinf.path + f'\\kln\\{kln.version.randref()}.jpg'
        #this part will need update
        pic = discord.File(final_path)
        await ctx.send(file = pic)
        
    print('ctx.message.author: ' + str(user))
    print(sysinf.current)
    print("-"*20)


##############################
#####lunch

class varrestaur:
    class type1:
        A = refdict({
            1:'餐研社', 2:'私房麵', 3:'丐幫滷味', 4:'鹽水雞',
            5:'八方雲集', 6:'敏忠小吃店', 7:'大胖小吃(廢墟)', 8:'楊記小吃',
            9:'赤肉羹', 10:'吃的小館', 11:'喜記', 12:'老麵水煎包',
            13:'廣東粥/甜不辣', 14:'羹大王', 15:'佳味自助餐'
            })
        B = refdict({
            1:'菁英', 2:'重慶酸辣粉', 3:'四川飯館', 4:'豚匠拉麵',
            5:'大呼過癮', 6:'大汗'
            })
        C = refdict({
            })

    class type2:
        A = refdict({
            1:'元吉食堂',2:'美香味'
            })
        B = refdict({
            1:'加賀屋',2:'小曼谷',3:'阿里郎',4:'鬼匠拉麵',
            5:'湯饌',6:'波波恰恰',7:'吉野家',8:'高句麗',
            9:'滇味食堂'
            })
        C = refdict({
            1:'Shabu鮮'
            })

    class type3:
        A = refdict({
            })
        B = refdict({
            1:'享窩',2:'麥當勞',3:'摩斯',4:'世界大同',
            5:'Subway',6:'提洛斯',7:'贊來食府(蝴蝶漾)(已死)'})
        C = refdict({
            1:'米塔',2:'舒曼',3:'Juicy Bun'
            })
    
    discript = {
        1:'台式／中式／港式', 2:'日式／韓式／東南亞式', 3:'歐式／美式',
        'A':'低價', 'B':'中等價格', 'C':'高價'
        }

    allrestaur = {}
    lentype = 3

class comrestaur:
    def update():
        varrestaur.allrestaur = {}
        for i in range(1, varrestaur.lentype+1):
            menu = getattr(
                varrestaur, 'type'+str(i),
                lambda : print('index no found'))
            
            for j in ['A', 'B', 'C']:
                restaurlist = getattr(
                    menu, j, lambda : print('index no found'))
                filename = 'type'+str(i)+'_'+j+'_output.csv'
                fileat = sysinf.path + "\\ref\\" + filename
                
                if os.path.exists(fileat):
                    restaurlist.read(
                        location = fileat, edit = 'w')
                    print(restaurlist.property["name"], 'has load')
                    
                else:
                    restaurlist.output(
                        filetype = "csv",
                        location = sysinf.path + "\\ref",
                        name = 'type'+str(i)+'_'+j)
                    print(restaurlist.property["name"], 'has created')
        
    def allrand():
        gether = {}
        for i in range(1, varrestaur.lentype+1):
            menu = getattr(
                varrestaur, 'type'+str(i),
                lambda : print('index no found'))
            
            for j in ['A', 'B', 'C']:
                restaurlist = getattr(
                    menu, j, lambda : print('index no found'))
                gether.update(restaurlist.content)
        varrestaur.allrestaur = refdict(gether)
        
    def isalpha(ctx, alpha):
        whether = False
        alpha = alpha.upper()
        for i in ['A', 'B', 'C']:
            if alpha == i:
                whether = True
        if whether:
            pass
        else:
            print('價位只有a,b,c三個分類')
        return whether

    def isrightnum(ctx, alpha):
        whether = False
        if str(alpha).isdigit():
            a = int(alpha)
            if 0 < a < varrestaur.lentype+1:
                whether = True
        if whether:
            pass
        else:
            print('目前只有3種喔')
        return whether

    async def tip(ctx):
        print('tip')
        await ctx.send(
            '今天想吃哪一類?\n先輸入數字表示種類，再輸入字母表示價位')
        for i in varrestaur.discript.keys():
            await ctx.send(str(i) + '代表' + varrestaur.discript[i])
        await ctx.send(
            '範例如下： lunch 2 a')
            
async def lunch(ctx, args):
    print("lunch")
    print("*args : " + str(args))
    user = ctx.message.author
    temp_args = []
    if len(args) == 0:
        temp_args = ['no code']
    else:
        temp_args = list(args)
    del args
    args = temp_args
    print("var name: ", args)

    def nulltreat(rest):
        if rest == 'refdict is null':
            return '...痾，好像沒有這個分類的選項喔'
        else:
            return rest

    pricepick = False
    typepick = False
    temp_restlist = {}
    therest = ''
    
    if args[0] == 'rand':
        if varrestaur.allrestaur == {}:
            comrestaur.allrand()
        therest = '我們今天推薦你吃：' + nulltreat(varrestaur.allrestaur.randref())

    elif comrestaur.isrightnum(ctx, args[0]):
        pricepick = True

    elif comrestaur.isalpha(ctx, args[0]):
        typepick = True

    elif args[0] == 'update':
        comrestaur.update()
        therest = 'list updated'
    
    elif args[0] == 'help':
        await comrestaur.tip(ctx)
        
    elif args[0] == 'no code':
        if varrestaur.allrestaur == {}:
            comrestaur.allrand()
        therest = '我們今天推薦你吃：' + nulltreat(varrestaur.allrestaur.randref())
    else:
        therest = '請不要亂輸，好嗎?'
        
    if typepick or pricepick:
        if len(args) < 2:
            args.append('null')
        
    if typepick:
        alpha = args[0].upper()
        num = 0
        if comrestaur.isrightnum(ctx, args[1]):
            num = int(args[1])
            menu = getattr(
                varrestaur, 'type'+str(num),
                lambda : print('index no found'))
            rest = getattr(
                menu, alpha, lambda : print('index no found'))
            therest = (
                '你選擇了'+ varrestaur.discript[alpha] + '，' +
                varrestaur.discript[num] + '的：' + nulltreat((rest.randref()))
                )
            
        elif args[1] == 'null':
            for num_i in range(1, varrestaur.lentype+1):
                menu = getattr(
                    varrestaur, 'type'+str(num_i),
                    lambda : print('index no found'))
                rest = getattr(
                    menu, alpha, lambda : print('index no found'))
                temp_restlist.update(rest.content)
            temp_restlist = refdict(temp_restlist)
            therest = (
                '我們今天推薦你吃' + varrestaur.discript[alpha] + '的：' +
                nulltreat(temp_restlist.randref())
                )
            
        else:
            therest = '請不要亂輸，好嗎?'

    if pricepick:
        alpha = ''
        num = int(args[0])
        if comrestaur.isalpha(ctx, args[1]):
            alpha = args[1].upper()
            menu = getattr(
                varrestaur, 'type'+str(num),
                lambda : print('index no found'))
            rest = getattr(
                menu, alpha, lambda : print('index no found'))
            therest = (
                '你選擇了'+ varrestaur.discript[alpha] + '，' +
                varrestaur.discript[num] + '的：' + nulltreat(rest.randref())
                )
            
        elif args[1] == 'null':
            for alpha_i in ['A', 'B', 'C']:
                menu = getattr(
                    varrestaur, 'type'+str(num),
                    lambda : print('index no found'))
                rest = getattr(
                    menu, alpha_i, lambda : print('index no found'))
                temp_restlist.update(rest.content)
            temp_restlist = refdict(temp_restlist)
            therest = (
                '我們今天推薦你吃' + varrestaur.discript[num] + '的：' +
                nulltreat(temp_restlist.randref())
                )
            
        else:
            therest = '請不要亂輸，好嗎?'
    
    print(therest)
    await ctx.send(therest)

    print('ctx.message.author: ' + str(user))
    print(sysinf.current)
    print("-"*20)



print("bot_normal ready")
print(sysinf.current)
print("-"*20)
