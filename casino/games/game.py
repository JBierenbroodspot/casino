from casino.users.users import BaseUser


class Game:
    """A skeleton for a game

    This class should inherited by another class which should extend the content method. You use this class by invoking
    the play method which repeats the content method in a loop.

    Attributes:
        has_ended: Checks if the game has ended.
        user: The player that plays the game.
    """
    def __init__(self, user: BaseUser):
        self.has_ended = False
        self.user = user

    def play(self) -> None:
        """Event loop of the game, returns None"""
        while self.has_ended is False:
            try:
                while self.has_ended is False:
                    self.content()
            except KeyboardInterrupt:
                if self.end_game() is True:
                    self.has_ended = True
                    break
                else:
                    continue

    def content(self) -> None:
        """This is the main code in which the game is executed, returns None

        The code for the game should be added to this method. Do not edit the play() method as it is only a wrapper
        for this method.
        """
        return None

    def end_game(self, force: bool = False) -> bool:
        """Checks whether the game should be ended, returns boolean.

        Args:
            force: Checks if game should be ended without prompting the user.

        Returns:
            True if the game should be ended, false if not.
        """
        return_ = False
        if force is True:
            return_ = True
        else:
            user_input = self.validate_input("Do you really want to quit?[y/n]", ('y', 'n'))
            if user_input == 'y':
                return_ = True
            elif user_input == 'n':
                return_ = False
        return return_

    @staticmethod
    def validate_input(prompt: str, options: tuple) -> str:
        """A staticmethod which will wait until user has entered a correct input, returns string."""
        print(prompt)
        while True:
            user_input = input(">>> ")
            if user_input.lower().strip(' ') in [option.lower() for option in options]:
                return_ = user_input.lower()
                break
            else:
                print(f"Please enter {options}")
        return return_
