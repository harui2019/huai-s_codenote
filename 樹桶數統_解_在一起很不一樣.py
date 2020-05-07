from bot_systatus import *

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
            print(type(menu))
            
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
            print(type(menu))
            
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

    async def tip(ctx):
        print('tip')
        await ctx.send(
            '今天想吃哪一類?\n先輸入數字表示種類，再輸入字母表示價位')
        for i in varrestaur.discript.keys():
            await ctx.send(i, '代表', varrestaur.discript[i])
        await ctx.send(
            '範例如下： lunch 2 a')
            
async def lunch(ctx, *args):
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

    pricepick = False
    typepick = False
    temp_restlist = {}
    therest = '--no signal--'
    
    if args[0] == 'rand':
        if varrestaur.allrestaur == {}:
            comrestaur.allrand()
        varrestaur.allrestaur.randref()

    elif comrestaur.isrightnum(ctx, arg[0]):
        pricepick = True

    elif comrestaur.isalpha(ctx, arg[0]):
        typepick = True
    
    elif arg[0] == 'help':
        await comrestaur.tip(ctx)
        
    else:
        if varrestaur.allrestaur == {}:
            comrestaur.allrand()
        varrestaur.allrestaur.randref()
        
    if typepick or pricepick:
        if len(arg) < 2:
            arg.append('null')
        
    if typepick:
        alpha = arg[0].upper()
        num = 0
        if comrestaur.isrightnum(ctx, arg[1]):
            num = int(arg[1])
            menu = getattr(
                varrestaur, 'type'+alpha,
                lambda : print('index no found'))
            rest = getattr(
                menu, num, lambda : print('index no found'))
            therest = rest.randref()
            
        elif arg[1] == 'null':
            for num_i in range(1, varrestaur.lentype+1):
                menu = getattr(
                    varrestaur, 'type'+alpha,
                    lambda : print('index no found'))
                rest = getattr(
                    menu, num_i, lambda : print('index no found'))
                temp_restlist.update(rest.content)
            temp_restlist = refdict(temp_restlist)
            therest = temp_restlist.randref()
            
        else:
            therest = '請不要亂輸'
        print(therest)
        await ctx.send(therest)
            

    if pricepick:
        alpha = ''
        num = int(arg[0])
        if comrestaur.isalpha(ctx, arg[1]):
            alpha = arg[1].upper()
            menu = getattr(
                varrestaur, 'type'+alpha,
                lambda : print('index no found'))
            rest = getattr(
                menu, num, lambda : print('index no found'))
            therest = rest.randref()
            print(therest)
            await ctx.send(therest)
            
        elif arg[1] == 'null':
            for alpha_i in ['A', 'B', 'C']:
                menu = getattr(
                    varrestaur, 'type'+alpha_i,
                    lambda : print('index no found'))
                rest = getattr(
                    menu, num, lambda : print('index no found'))
                temp_restlist.update(rest.content)
            temp_restlist = refdict(temp_restlist)
            therest = temp_restlist.randref()
            
        else:
            therest = '請不要亂輸'
        print(therest)
        await ctx.send(therest)

    print('ctx.message.author: ' + str(user))
    print(sysinf.current)
    print("-"*20)

    
print(varrestaur.type2.C.randref())

Q1 = True
while Q1:
    type_dish = input('今天想吃哪一類?\n'+discription[1]+'輸入1，'+
                  discription[2]+'輸入2，'+discription[3]+'輸入3'+'\n>>>')
    if type_dish.isdigit():
        type_dish = int(type_dish)
        if 0 < type_dish < len(uni_dict)+1:
            Q1 = False
            print('你選擇了'+discription[type_dish])
        else:
            print('數字要是1,2,3，再試一次吧')
    else:
        print('奇怪，你輸入的好像不是數字，再試一次吧')


Q2 = True
alphbeta_check1 = False
menu = {}
while Q2:
    type_prise = input('輸入想要的價位等級?\n'+discription['A']+'輸入A，'+
                  discription['B']+'輸入B，'+discription['C']+'輸入C'+'\n>>>')
    type_prise = str(type_prise.upper())
    for alphbeta in list(uni_dict[type_dish].keys()):
        if type_prise == alphbeta:
            alphbeta_check1 = True
    if alphbeta_check1:
        print('你選擇了'+discription[type_prise]+'的餐點')
        menu = uni_dict[type_dish][type_prise]
        Q2 = False
    else:
        print('輸入的東西要是A,B,C喔，再試一次吧')   


null_set = True
alphbeta_check2 = False
contichose = True
while len(menu) != 0 and contichose:
    null_set = False
    restaur = rn.sample(list(menu),1)[0]
    print('我們今天推薦你吃'+'<<'+menu[restaur]+'>>')
    liked = input('(如果不喜歡程式推薦，可再輸入N/如果滿意請輸入Y)\n>>>')
    liked = str(liked.upper())
    for alphbeta in ['Y','N']:
        if liked == alphbeta:
            alphbeta_check2 = True
    if alphbeta_check2:
        if liked == 'Y':
            print('去吃飯吧！')
            contichose = False
        else:
            del menu[restaur]
    else:
        print('輸入的東西要是Y,N喔，再試一次吧')

if null_set:
    print('唉呀，這個分類是空的啊!!!')
else:
    if contichose:
        print('沒有餐廳可選囉!!!')


#print(menu)

#print(list(uni_dict[1].keys()))
#for alphbeta in list(uni_dict[1].keys()):
#    print(alphbeta)
#    print(type(alphbeta))
#type_prise = input('輸入想要的價位等級?\n'+discription['A']+'輸入A'+
#                  discription['B']+'輸入B'+discription['C']+'輸入C'+'\n')
#print(type(type_prise))

#uni_dict_2={1:{'A':{1:'餐研社'}}}

#print(uni_dict[1]['C'][0])
#type_dish = list(uni_dict[1].keys())
#print(list(uni_dict[1].keys()))
#print(type(uni_dict[1].keys()))
