from django.shortcuts import render
import uuid

def home(request):
    uidarr = ['uuid1','uuid4']
    context = {
        'uidarr':uidarr
         }
    return render(request, 'app/home.html', context)


def GenerateId(request):
    uidarr = ['uuid1','uuid4']
    uidict = dict()
    idinfo = dict()
    componentinfo = dict()
    msg = ""
    q = request.GET['q']  
    if q != "":
        try:
            if q == uidarr[0]:
                uid1 = uuid.uuid1()
                uidict['uid1'] = uid1
                 
                print ("Representations of uuid1() are : ")
                idinfo['bytrepr'] = repr(uid1.bytes)
                idinfo['intrepr'] = repr(uid1.int)
                idinfo['hexrepr'] = repr(uid1.hex)  

                print ("The Components of uuid1() are : ")
                componentinfo['version'] = uid1.version 
                componentinfo['variant'] = uid1.variant 
                componentinfo['fields'] = uid1.fields    
                componentinfo['node'] = uid1.node      

            elif q == uidarr[1]:
                uid4 = uuid.uuid4()
                uidict['uid4'] = uid4
                
                print ("The Representations of uuid4() are : ")
                idinfo['byterepr'] = repr(uid4.bytes)
                idinfo['intrepr'] = repr(uid4.int)
                idinfo['hexrepr'] = repr(uid4.hex)    

                print ("The Components of uuid4() are : ")
                componentinfo['version'] = uid4.version 
                componentinfo['variant'] = uid4.variant 
                componentinfo['fields'] = uid4.fields    
                componentinfo['node'] = uid4.node                     
            
            else:
                 print("Please Chose UUID Version......")   
                 uidict['error'] = "Please Provide Valid Input"                     
 
        except Exception as e:
              uidict['exception'] = "Something went wrong......"   
    else:
        msg = "User Input Can't be null......"   

    print(idinfo)
    context = {
       
        'uidarr':uidarr,
        'uidict': uidict,
        'message':msg,
        'idinfo':idinfo,
        'componentinfo':componentinfo,
    }
     
    return render(request, 'app/home.html', context)



# def GenerateUUID1(request):
#     uid1 = request.GET['q']
    
#     try:
#         uid1 = uuid.uuid1()
#         uid4 = uuid.uuid4()
#         dictuid = dict()
#         print("=========================================")
#         print ("Generating Random Id Using uuid1()")
#         print ("The random id using uuid1() is : ",uid1)
#         print("\n")
#         print("=========================================")    
#         print ("The Representations of uuid1() are : ")
#         print ("byte Representation : ",end="")
#         print(repr(uid1.bytes))
#         print ("Integer Representation : ",end="")
#         print(repr(uid1.int))
#         print ("Hex Representation : ",end="")
#         print(repr(uid1.hex))
#         print("\n")
#         print("=========================================")   
#         print ("The Components of uuid1() are : ")
#         print ("Version  : ",uid1.version)
#         print ("Variant : ",uid1.variant)
#         print ("Fields : ", uid1.fields)
#         print ("Time : ", uid1.node)
#         print("\n")

#         print("=========================================")
#         print ("Generating Random Id Using uuid4()")
#         print ("The random id using uuid4() is : ",uid4)
#         print("\n")
#         print("=========================================")    
#         print ("The Representations of uuid4() are : ")
#         print ("byte Representation : ",repr(uid4.bytes))
#         print ("Integer Representation : ",repr(uid4.int))
#         print ("Hex Representation : ",repr(uid4.hex))
#         print("\n")
#         print("=========================================")   
#         print ("The Components of uuid4() are : ")
#         print ("Version  : ",uid4.version)
#         print ("Variant : ",uid4.variant)
#         print ("Fields : ", uid4.fields)
#         print ("Time : ", uid4.node)
#         print("\n")

#         context = {
#         'uid1': uid1,
#         'uid4':uid4,
#          }
#         return render(request, 'app/uuid.html.html', context)

#     except:
#         pass 
#         return render(request, 'app/idhome.html')
    
  


