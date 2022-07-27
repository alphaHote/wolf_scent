import shutil
import os

def adresses_des_fichiers_et_dossiers(d:str):
    fichiers=[]
    dossiers=[]
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        if os.path.isfile(full_path):
            fichiers.append(full_path)
        elif os.path.isdir(full_path):
            dossiers.append(full_path+"\\")
    return [fichiers,dossiers]


def lire_txt(path: str,e=True):
    txt=""
    if e:
        with open(path, 'r',encoding='utf-8') as fis:
            for line in fis.readlines():
                txt+=line+"\n"
        return txt 
    else :
        with open(path, 'r',encoding='cp1252') as fis:
            for line in fis.readlines():
                txt+=line+"\n"
        return txt 
        
def ecrire_txt(path : str, txt: str):
    with open(path, 'a', encoding='utf-8') as fos:
        fos.write(txt)


def copy_file(origine:str, destination: str):
    shutil.copyfile(origine, destination)

def cut_file(origine:str, destination: str):
    shutil.copyfile(origine, destination)
    os.remove(origine)

def supprimer_fichier_ou_dossier(adresse:str):
    os.remove(adresse)


def mkdir(adresse:str):
    if os.path.isdir(adresse)==False:
        os.mkdir(adresse)




def bin(n:int, longueur=30):
    """Convertit un nombre en binaire"""
    q = -1
    res = ''
    while q != 0:
        q = n // 2
        r = n % 2
        res = str(r) + res
        n = q
    return "0"*(longueur-len(res))+res

