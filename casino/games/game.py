

class Game:
    def __init__(self):
        self.has_ended = False

    def play(self) -> None:
        while self.has_ended is False:
            try:
                while True:
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

    @staticmethod
    def end_game(force: bool = False) -> bool:
        """A static method that checks whether the game should be ended, returns boolean.

        Args:
            force: Checks if game should be ended without prompting the user.

        Returns:
            True if the game should be ended, false if not.
        """
        _return = False

        if force is True:
            _return = True
            return _return

        print("Do you really want to quit?[y/n]")
        while True:
            _user_input = input(">>> ")
            if _user_input.lower().strip(' ') == 'y':
                _return = True
                break
            elif _user_input.lower() == 'n':
                _return = False
                break
            else:
                print("Please enter a valid response.")
                continue
        return _return
