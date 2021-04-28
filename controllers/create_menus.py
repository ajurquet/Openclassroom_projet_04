

class CreateMenus:
    """Create the main menu, and then
    leads to branchs of menus according to the number choosen"""
    main_menu = [("1", "Menu Joueur"),
         ("2", "Menu Tournoi"),
          ("3", "Quitter")]

    player_menu = [("1", "Créer un joueur"),
        ("2", "Mettre à jour le classement d'un joueur"),
        ("3", "Afficher un rapport"),
        ("4", "Retour au menu principal")]
    
    tournament_menu = [("1", "Créer un nouveau tournoi"),
    ("2", "Lancer un tournoi existant"),
    ("3", "Afficher un rapport"),
    ("4", "Retour au menu principal")]

    time_control_menu = [("1", "Bullet"),
        ("2", "Blitz"),
        ('3', "Coup rapide")]

    def __init__(self):
        pass

    def __call__(self, menu_to_display):
        """Display a menu and ask the user to choose"""
        for line in menu_to_display:
            print(line[0] + " : "+ line[1])
        while True:
            entry = input("-->")
            for line in menu_to_display:
                if entry == line[0]:
                    return str(line[0])
            print("Vous devez entrer le chiffre correspondant")