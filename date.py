# Implémentation des dates et calendriers
# Implémentation des tests (voir main en fin de fichier)

from typing import Dict, List, Tuple, NoReturn



# =============================================================================
def est_bissextile(annee: int) -> bool :
    # Function est_bissextile
    # Args:
    #   annee : int (contient une année)
    
    # Cette fonction booléenne vérifie si une année est bissextile.
    """
    retourne vrai si l'année est bissextile

    >>> est_bissextile(2020)
    True
    >>> est_bissextile(2021)
    False
    >>> est_bissextile(2022)
    False
    >>> est_bissextile(1900)
    False
    >>> est_bissextile(2000)
    True
    """ 
    if ((annee % 400 == 0) or (annee % 4 == 0) and (annee % 100 != 0)):
        return True
    else:
        return False
            
    
# =============================================================================
def cree_date(j: int, m: int, a: int) -> Dict :
    # Function creer_date
    # Args:
    #   j : int (contient le jour issue de la date.)
    #   m : int (contient le mois issue de la date.)
    #   a : int (contient la valeur de l'année de la date)
    
    # Return:
    #   date : dict (contient toutes les paramètres sous forme de dictionnaire)
    
    # Cette fonction permet de créer une date selon les conditions suivantes:
    #   - Les arguments doivent être des entiers,
    """
    Crée une date à partir des entiers la décrivant.
    Si l'un des paramètres n'est pas un entier, la fonction retournera None

    >>> cree_date(15,12,2020)
    {'jour': 15, 'mois': 12, 'annee': 2020}
    >>> cree_date(1.5,12,2020)

    """
    if (type(j) != int) or (type(m) != int) or (type(a) != int):
        return None
    else:
        date = {
            'jour': j,
            'mois': m,
            'annee': a
        }
    return date

# =============================================================================
def copie_date(date: Dict) -> Dict :
    # Function copie_date
    # Args:
    #   date : dict (Crée dans la convtion creer_date)
    
    # Return:
        # copie_date : dict (copie exacte du dictionnaire passé en paramètre.)
        
    # Cette fonction permet de copier un dictionnaire entré en paramètre.
    """
    copie la date passée en paramètre
    """
    copie_date = date.copy() 
    return copie_date
    
# =============================================================================
def compare(d1: Dict, d2: Dict) -> int :
    # Finction compare
    #   Args:
    #   d1 : dict (contient une date)
    #   d2 : dict (contient une autre date)
    
    # returns:
    #   -1 si la date d1 < d2
    #   +1 si la date d1 > d2
    #   0 si les dates sont identiques
    
    # Cette fonction permet de comparer deux dates, si l'une est plus grande ou égale.
    """
    Permet de classer deux dates.
    Retourne
    -1 si la date d1 < d2
    +1 si la date d1 > d2
    0 si les dates sont identiques
    on considère que les dates sont croissantes 
    dans l'ordre chronologique

    >>> date1 = cree_date(25,12,2021)
    >>> date2 = cree_date(31,12,2021)
    >>> compare(date1,date2)
    -1
    >>> compare(date2,date1)
    1
    >>> compare(date1,date1)
    0
    """
    d1_jour = d1.get('jour')
    d1_mois = d1.get('mois')
    d1_annee = d1.get('annee')
    
    d2_jour = d2.get('jour')
    d2_mois = d2.get('mois')
    d2_annee = d2.get('annee')
    
    if (d1_jour < d2_jour) and (d1_mois <= d2_mois) and (d1_annee <= d2_annee):
        return -1
    elif (d1_jour > d2_jour) and (d1_mois >= d2_mois) and (d1_annee >= d2_annee):
        return 1
    else:
        return 0
    


# =============================================================================
def valide_simple(d: Dict) -> bool :
    # Function valide_simple
    # Args:
    #   d : dict
    
    # Return:
    #   bool
    
    # Cette fonction permet de vérifier que le paramètre:
    #         - si le premier (le jour) est un entier compris entre 1 et 31
            # - si le second (le mois) est un entier compris entre 1 et 12
    """   
    retourne vrai si la date est valide.
    on supposera que la date est valide si :
    - si le premier (le jour) est un entier compris entre 1 et 31
    - si le second (le mois) est un entier compris entre 1 et 12

    >>> date = cree_date(1, 2, 0)
    >>> valide_simple(date)
    True
    >>> date = cree_date(1.5, 5, 6)
    >>> valide_simple(date)
    False
    >>> date = cree_date(0, 5, 6)
    >>> valide_simple(date)
    False
    >>> date = cree_date(20, 8, 2021)
    >>> valide_simple(date)
    True
    """
    if d != None:
        if (type(d['jour'])==int) and (type(d['mois'])==int) and (type(d['annee'])==int):
            if (0 < d['jour'] < 32) and (0 < d['mois'] < 13):

                return True
            else:
                return False     
        else:
            return False
    else:
        return False
 
# =============================================================================
def valide_complet(d: Dict) -> bool :
    """ 
    retourne vrai si la date est valide.
    on supposera que la date est valide si :
    - la validation simple est vraie
    - si la date représente une date réelle 

    >>> date = cree_date(15, 1, 2022)
    >>> valide_complet(date)
    True
    >>> date = cree_date(32, 1, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(-1, 1, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(31, 6, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(29, 2, 2020)
    >>> valide_complet(date)
    True
    >>> date = cree_date(29, 2, 2022)
    >>> valide_complet(date)
    False
    """
    
    moisImpairs = [1, 3, 5, 7, 8, 10, 12]
    moisPairs = [4, 6, 9, 11]
    
    if (valide_simple(d) == True):
        if d['mois'] in moisImpairs:
            if d['jour'] <= 31:
                return True
            else:
                return False
        
        elif  d['mois'] in moisPairs:
            if d['jour'] <= 30:
                return True
            else:
                return False
        
        elif est_bissextile(d['annee']):
            if d['jour'] <= 28:
                return True
            
            elif d['jour'] <= 29:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
                
    


# =============================================================================
def ajoute_calendrier(calendrier: List, date: Dict, description: str ) -> NoReturn :
    """
    ajoute un élément à la liste du calendrier.
    """
    # date['description'] = description
    calendrier.append({'jour' : date['jour'], 'mois' : date['mois'], 'annee' : date['annee'], 'evennement' : description})
    print(calendrier)
    return calendrier

    
# =============================================================================
def affiche_calendrier(calendrier: List) -> NoReturn :
    """
    affiche le calendrier sous forme de liste.
    """
    # for i in calendrier:
    for i in range(len(calendrier)):
        print('Le {}/{}/{} : {}'.format(calendrier[i]['jour'], calendrier[i]['mois'], calendrier[i]['annee'], calendrier[i]['evennement']))

# =============================================================================    
if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    
    # # Créer la liste calendrier
    calendrier=[]
    date = {'jour': 0, 'mois': 0, 'annee': 0}
    
    while valide_complet(date) == False:
        date_list = input('Choisir une date au format JJ MM AAAA : ').split()
        print(f'Debug {type(date_list), date_list[0], date_list[1], date_list[2]}')
        jour = int(date_list[0])
        mois = int(date_list[1])
        annee = int(date_list[2])
        print(f'Debug {type(jour), jour, mois, annee}')
        date = cree_date(jour, mois, annee)
    description = input('Ajouter une description :')
    
    calendrier = ajoute_calendrier(calendrier, date, description)
    affiche_calendrier(calendrier)
