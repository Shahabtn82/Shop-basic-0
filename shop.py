import json


def first_menu():
    noe_karbar=input("admin ya xaridar:")
    if noe_karbar=="admin":
        admin()
    elif noe_karbar=="xaridar":
        xaridar()
    else:
        print("dade yaft nashod")
    
def admin():
    kar=input("kare khod ra vared konid:")
    if kar=="list ajnas":
        with open("shop.json","r") as file:
            list_ajnas=json.load(file)
        print(list_ajnas)
    
    elif kar=="ezafe kardan jens":
        name_jens=input("name jens:")
        geymat=input("geymate jens:")
        tedad=input("tedad:")
        jens_jadid={
            name_jens:{
            "geymat":geymat,
            "tedade mande":tedad
        
            }
        }
        json_string=json.dumps(jens_jadid)
        with open("shop.json","r") as file:
            x=json.load(file)
            x.update(jens_jadid)
        with open("shop.json","w") as file:
            json.dump(x,file,indent=4)
            
            
    
    elif kar=="tagir geymat":
        name_jens=input("jens morede nazar ra vared konid:")
        geymat=input("geymat jadid ra vared konid:")

        with open("shop.json","r") as file:
            x=json.load(file)
            jens=x[name_jens]
            tedad=jens["tedade mande"]
        tagirat_jens={
            name_jens:{
            "geymat":geymat,
            "tedade mande":tedad
            }
        } 
        x.update(tagirat_jens)
        with open("shop.json","w") as file:
            json.dump(x,file,indent=4)
    else:
        pass


def xaridar():
    jens_morede_nazar=input("jense xod ra vared konid:")
    tedade_morede_nazar=int(input("tedade morede nazar ra vared konid:"))
    if tedade_morede_nazar>0:
        with open("shop.json","r") as file:
            x=json.load(file)
        jens=x[jens_morede_nazar]
        if int(jens["tedade mande"])-tedade_morede_nazar>=0:
            print("xarid ba movafagiyyat anjam shod!")
            mablag_gabele_pardaxt=tedade_morede_nazar*int(jens["geymat"])
            print("reside shoma: "+jens_morede_nazar +" be tedade",tedade_morede_nazar)

        else:
            print("xarid namovafag!")
        tagirat_jens={
                jens_morede_nazar:{
                "geymat":jens["geymat"],
                "tedade mande":str(int(jens["tedade mande"])-tedade_morede_nazar)
                }
            } 
        
        with open("shop.json","r") as file:
            x=json.load(file)
            x.update(tagirat_jens)
        with open("shop.json","w") as file:
            json.dump(x,file,indent=4)
    else:
        pass

     


first_menu()


    

    




