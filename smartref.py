import random as rn
import pickle
import inspect

#made by huai

class refdict():
    #import random as rn
    #print("attention: this class, ref_set(), will import random as rn")
    def resortdict(self):
        redo_content = False
        for i in range(len(self.content)):
            if (list(self.content.keys())[i]) == i:
                pass
            else: redo_content = True
        if redo_content:
            print("redo dict to standard")
            content_redo: dict = {}
            for i in range(len(self.content)):
                content_redo[i] = (list(self.content.values()))[i]
            print(content_redo)
            self.content = content_redo
           #resort
            
    class inform():
        def __init__(self, refdict_content, refdict_name):
            self.target = refdict_content
            self.name = refdict_name
            self.informdict = {
                "name": str(self.name),
                "isallstr": self.isallstr(),
                "typecplx": self.typecplx(),
                "len": len(self.target),
                "note": 'type something you want'
                }
        
        def isallstr(self):
            _isallstr_ = True
            
            for i in self.target.values():
                if type(i) == str :
                    pass
                else :
                    _isallstr_ = False
            
            
            return _isallstr_
        
        def typecplx(self):
            if self.isallstr():
                return {"<class 'str'>": len(self.target)}
            
            _typesum_ = {}
            check = 0
            _len_ = len(self.target)
            add = True
    
            for i in self.target.values():
                i_type = str(type(i))
                for j in list(_typesum_.keys()):
                    if i_type == j:
                        _typesum_[j] += 1
                        add = False   

                if add:      
                    _typesum_[i_type] = 1
                add = True
                check += 1

            n = 0
            for i in _typesum_.values():
                n += i
            
            if check != _len_ or n != _len_:
                raise AttributeError(
                    "error occurs counting type",
                    "len: " + _len_, "check: " + check, "sum: " + n)

            return _typesum_
        
    def __init__(self, content = {}):
        if type(content) == dict:
            self.content: dict = content
            self.resortdict()
            
        elif type(content) == list:
            n = len(content)
            self.content: dict = {}
            for i in range(0, n):
               self.content[i] = content[i]
            self.resortdict()

        else :
            raise TypeError("content must be 'dict' or 'list'", content)

        self._name_ = ''
        #this is the keypart
        self._inform_()
        #error like fcn
        #if wants to make self-def error, then make one by class

    def _inform_(self):
        self.inform = refdict.inform(self.content, self._name_)
        self.property = self.inform.informdict
        
    def nameset(self, name = ''):
        if type(name) == str:
        
            self._name_ = name
        elif name == "__reset__":
            self._name_ = ''
            print("name changes to ''")
        elif name == "":
            raise AttributeError("name can not be ''", name)
        else:
            raise TypeError("name must be 'str'", name)
        self._inform_()
        return self._name_
    
    def randref(self):
        if len(self.content) == 0:
            pick = 'refdict is null'
            print(pick)
            return pick
        else:
            pick = rn.sample(range(len(self.content)), 1)[0]
            return self.content[pick]
        #give ref randomly
        #the first
    
    def show(self):
        return self.content
        #show all dict
    
    def add(self, new):
        self.content[len(self.content)] = new
        self._inform_()
        #add
        
    def remove(self, target):
        if type(target) == int:
            del self.content[target]
            self.resortdict()
        else:
            raise TypeError("key need to be 'int'", content)
        self._inform_()
        #remove
        
    def showref(self, target):
        if type(target) == int:
            return self.content[target]
        else:
            raise TypeError("key need to be 'int'", content)
        #show the setence that be chosen
        
    def searchref(self, target):
        return list(self.content.keys())[list(self.content.values()).index(target)]
        #find the num of the setence
    
    def output(self, filetype = '', location = '', name = str(list(locals().keys())[0])):
        if self._name_ != '':
            name = self._name_

        if name == "__module__":
            print("###locals() may not detect the variable's name")
            print("###please make a good one")
        
        print("file name: ",name)

        '''
        ver1 way
        if filetype == 'csv':
            _title_ = f'{name},csv,\n'
            _lead_ = "{0},_,"
            _enter_ = ",_,\n"
            _end_ = ',_,\n'
            
        elif filetype == 'txt':
            _title_ = f'{name} = '+'{\n'
            _lead_ = "{0}:"
            _enter_ = ",\n"
            _end_ = '>_>\n},txt'
        '''

        if filetype == 'csv':
            _title_ = f'<_name_<{name}>_>,\n<_type_<csv>_>,\n'
            _lead_ = "{0},<_<"
            _enter_ = ">_>,\n"
            _end_ = '>_>,\n'
            
        elif filetype == 'txt':
            _title_ = f'<_name_<{name}>_>,\n<_type_<txt>_> = '+'{\n'
            _lead_ = "{0}:<_<"
            _enter_ = ">_>,\n"
            _end_ = '>_>\n}'
            
        else:
            raise ValueError("unknown filetype, you can use 'csv', 'txt'.", filetype)
        
        if type(name) != str:
            raise TypeError("files name need to be 'str'", name)

        _filename_ = f"{location}\\{name}_output.{filetype}"
        file = open(_filename_, 'w+', encoding='utf-8')

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
        print(_filename_ + " has saved")
        
        #output current refdict as txt
        
    #def insertwords(self, spedict):

        #2: '{0:s}年菲爾茲獎得主：{1:s} \n以及他的論文：「除以0的運作原理」'
        #bravo.showref(2).format(ti.strftime("%Y", ti.localtime()), ''+'@'+str(user))
        #this line works!!!

        #the plan to insert special words and how many of them in randref and more fcn
        #it is to be delay
        #by there is an another way to reach the same effection
        #except the next ver of py
        #beginning to demand that format() must exist after {0:s}
        
    def save(self, location = '', name = str(list(locals().keys())[0])):
        #it's using pickle
        #if self._name_ != str(list(locals().keys())[0]) and name == str(list(locals().keys())[0]):
        #   name = self._name_
        if name == "__module__":
            print("###locals() may not detect the variable's name")
            print("###please make a good one")
            
        print("file name: ",name)
        file = open(f'{location}\\{name}.refdict', 'wb+')
        pickle.dump(self.content, file)
        file.close()
        print(f"{name}.refdict has saved")
    
    def load(self, location = '', edit = ''):
        #C:\\_\\__file__.sample
        #'a' to add, 'w' to rewrite
        file = open(f'{location}', 'rb+')
        dict_1 = pickle.load(file)
        if type(dict_1) == type(self.content):
            if edit == 'a':
                for i in range(len(dict_1)):
                    self.add(dict_1[i])
                self.resortdict()
            elif edit == 'w':
                self.content = dict_1
                self.resortdict()
            else:
                raise ValueError("'a' to add, 'w' to rewrite")
        else:
            raise TypeError(f"the new content from [{location}] is not 'dict'", location)

    def read(self, location = '', edit = ''):
        #C:\\_\\__file__.sample
        #'a' to add, 'w' to rewrite
        if (".csv" not in location) or (location[-4:] != ".csv"):
            raise ImportError("only 'csv' files can read, or you forget to type '.csv'", location)
        file = open(location, 'r+', encoding='utf-8')

        ref_lines_1 = file.readlines()
        #print(ref_lines_1)

        ref_lines_2 = []
        wait_nxtline = False
        otherinf = {}
        
        for i in ref_lines_1:
            beg_sign = i.find("<_<")
            end_sign = i.find(">_>")
            msg_sign = 0
            inf_sign = 0
            
            if   beg_sign == -1 and end_sign == -1:
                #no beg_sign & no end_sign
                ref_lines_2[-1] = ref_lines_2[-1] + i[:]
                
            elif beg_sign != -1 and end_sign == -1:
                #no end_sign
                wait_nxtline = True
                ref_lines_2.append(i[beg_sign + 3 : ])

            elif beg_sign == -1 and end_sign != -1:
                #no beg_sign
                if wait_nxtline:
                    ref_lines_2[-1] = ref_lines_2[-1] + i[: end_sign]
                else:
                    msg_sign = i.find("<_")
                    inf_sign = i.find("_<")
                    inf = i[msg_sign + 2 : inf_sign]
                    if inf == "name":
                        self._name_ = i[inf_sign + 2 : end_sign]
                    else:
                        otherinf[inf] = i[inf_sign + 2 : end_sign]
            else:
                #beg_sign & end_sign can be found
                ref_lines_2.append(i[beg_sign + 3 : end_sign])        
        #print(ref_lines_2)

        n = len(ref_lines_2)
        m = self.property["len"]
        tempdict = {}
        
        #print(n, m)
        if edit == "a":
            for i in range(n):
                tempdict[m + i] = (ref_lines_2[i])

        elif edit == "w":
            for i in range(n):
                tempdict[i] = (ref_lines_2[i])
        else:
            raise ValueError("'a' to add, 'w' to rewrite")
        #print("tempdict")
        #print(tempdict)
        #print("otherinf")
        #print(otherinf)

        self.content.update(tempdict)
        self.inform.informdict["note"] = otherinf
        self.resortdict()
        self._inform_()
        
    def _read_ver1(self, location = '', edit = ''):
        #C:\\_\\__file__.sample
        #'a' to add, 'w' to rewrite
        if (".csv" not in location) or (location[-4:] != ".csv"):
            raise ImportError("only 'csv' files can read, or you forget to type '.csv'", location)
        file = open(location, 'r+', encoding='utf-8')

        ref_lines_1 = file.readlines()
        #print(ref_lines_1)

        ref_lines_2 = []

        for i in ref_lines_1:
            if i == ref_lines_1[0] or i[0].isdigit():
                ref_lines_2.append(i[:-1])
            else:
                ref_lines_2[-1] = ref_lines_2[-1] + '\n' + i[:-1]
        #print(ref_lines_2)

        del ref_lines_1
        ref_lines_1 = []
        for i in ref_lines_2:
            ref_lines_1.append(i.split(',_,'))
        #print(ref_lines_1)

        n = len(ref_lines_2)
        m = self.property["len"]
        tempdict = {}

        #print(n, m)
        if edit == "a":
            for i in range(1, n):
                tempdict[m + i -1] = (ref_lines_1[i])[1]

        elif edit == "w":
            for i in range(1, n):
                tempdict[i - 1] = (ref_lines_1[i])[1]
        else:
            raise ValueError("'a' to add, 'w' to rewrite")
        #print("tempdict")
        #print(tempdict)
        
        self.content.update(tempdict)
        self.resortdict()
        self._name_ = (ref_lines_1[0])[0]
        self._inform_()

    def _output_ver1(self, filetype = '', location = '', name = str(list(locals().keys())[0])):
        if self._name_ != '':
            name = self._name_

        if name == "__module__":
            print("###locals() may not detect the variable's name")
            print("###please make a good one")
        
        print("file name: ",name)

        
        #ver1 way
        if filetype == 'csv':
            _title_ = f'{name},csv,\n'
            _lead_ = "{0},_,"
            _enter_ = ",_,\n"
            _end_ = ',_,\n'
            
        elif filetype == 'txt':
            _title_ = f'{name} = '+'{\n'
            _lead_ = "{0}:"
            _enter_ = ",\n"
            _end_ = '>_>\n},txt'

        else:
            raise ValueError("unknown filetype, you can use 'csv', 'txt'.", filetype)
        
        if type(name) != str:
            raise TypeError("files name need to be 'str'", name)

        _filename_ = f"{location}\\{name}_ver1_output.{filetype}"
        file = open(_filename_, 'w+', encoding='utf-8')

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

     
    def __self__(self):
        return self

#made by huai
