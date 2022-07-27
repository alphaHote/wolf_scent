# wolf_scent
# LES ETAPES POUR FAIRE FONCTIONNER LE CODE
je présume que vous avez python installé sur votre pc
(1)sur son invite de commande tapper

pip install virtualenv

(cette commande vous permet de créer des environnement virtuels qui ont plusieurs avantages)

(2) allez sur le lien : https://github.com/ultralytics/yolov5
téléchargez le code sous extension .zip et dizziper le
puis naviguez avec votre invite de commande jusqu'à l'emplacement des fichiers source detect.py ....

(3) tappez la commande 
virtualenv venv 

(ceci créera un environnement virtuel appelé venv 
si la commande ne fonctionne pas c'est que probablement vous avez un problème de la variable d'environnement 
penser à ajouter virtualenv à cette dernière)

(4) tappez ensuite la commande 
dir
(un dossier nommé venv doit apparitre)
(5) tappez la commande :
venv\Scripts\activate
(si tous fonctionne bien vous devez voir apparaitre (venv) avant le chemin sur votre invite de commande

(6) tappez la commande :
pip install -r requirements.txt
(attendez que l'installation des packages finisse)

(7) téléchargez le code ici présent et décompresser dans le dossier des fichiers sources
(8) tapez la commande
py main_camera.py
(vous pouvez arrêtez avec eshape)



