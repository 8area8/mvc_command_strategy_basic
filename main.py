"""MVC simple avec le pattern Command et le pattern Strategy."""


class Command:
    """Base command."""

    def execute(self, app):
        """Résoud du code.

        Le paramètre "app" fait référence à l'application. On peut donc
        mettre à jour des données de l'application depuis cette méthode.
        """
        pass


class WrongCommand(Command):
    """Mauvaise command."""

    def execute(self, app):
        print("La commande n'est pas bonne !")


class HomeCommand(Command):
    """Command pour aller au menu principal."""

    def execute(self, app):
        app.change_page("home")


class ProductsCommand(Command):
    """Va à la page des produits."""

    def execute(self, app):
        app.change_page("products")


class QuitCommand(Command):
    """Quitte le programme."""

    def execute(self, app):
        app.running = False


# Les Vues


class View:
    """Vue de base."""

    def display(self):
        """Affiche les données de la page."""
        pass

    def ask_for_choice(self):
        """Demande un choix et retourne un objet Command."""
        return WrongCommand()


class Home(View):
    """Page principale."""

    def display(self):
        print()
        print("welcome home !")
        print("choix:")
        print("1 - voir les produits")
        print("2 - quitter")

    def ask_for_choice(self):
        choice = input("entrez un choix : ")
        if choice == "1":
            return ProductsCommand()
        elif choice == "2":
            return QuitCommand()
        return WrongCommand()


class ShowProducts(View):
    """Page des produits."""

    def display(self):
        print()
        print("Banane, pomme, orange")
        print("choix:")
        print("1 - retour au menu principal")
        print("2 - quitter")

    def ask_for_choice(self):
        choice = input("entrez un choix : ")
        if choice == "1":
            return HomeCommand()
        elif choice == "2":
            return QuitCommand()
        return WrongCommand()


# Le Controller


class Controller:
    """Classe principale qui gère le séquencage de l'application.

    Args:
        - view (View): une vue. La vue représente une page, et peut être changé avec
        la méthode "change_page".
        - running (bool): True pour faire tourner le programme, False pour l'arrêter.
    """

    pages = {"home": Home, "products": ShowProducts}

    def __init__(self):
        """Possède running et une vue."""
        self.runnning = False
        self.view = Home()

    def change_page(self, page_name):
        """Change la vue courante en une autre vue."""
        view = self.pages[page_name]
        self.view = view()

    def run(self):
        """Boucle principale du programme !"""
        self.running = True
        while self.running:
            self.view.display()
            choice = self.view.ask_for_choice()
            choice.execute(app=self)


if __name__ == "__main__":
    Controller().run()
