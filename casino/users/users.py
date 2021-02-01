class BaseUser:
    """A base for users.

    Attributes:
        username: The name of the user.
    """
    def __init__(self, username: str):
        self.username = username


class PlayableUser(BaseUser):
    """A user class representing a player.

    Attributes:
        username: The name of the user.
        balance: The amount of money the user possesses.
    """
    def __init__(self, username: str, balance: float = 100):
        super(PlayableUser, self).__init__(username=username)
        self.balance = balance

    def win_balance(self, amount: float) -> None:
        """Add won amount to balance, return None.

        Args:
            amount: The amount added to the user balance.
        """
        self.balance += amount

    def lose_balance(self, amount: float) -> None:
        """Deduct lost balance, return None.

        Args:
            amount: The amount deducted from user balance.

        Raises:
            ValueError: if the user balance is lower than the amount deducted.
        """
        if self.balance < amount:  # Check if the deducted amount exceeds balance
            raise(ValueError("User balance is too low"))
        self.balance -= amount
