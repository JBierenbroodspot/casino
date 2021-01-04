class User:
    def __init__(self, username: str, balance: float = 100):
        self.username = username
        self.balance = balance
        
    def win_balance(self, amount: float) -> None:
        """Add won amount to balance, return None"""
        self.balance += amount
        return None
    
    def lose_balance(self, amount: float) -> None:
        """Deduct lost balance, return None"""
        if self.balance < amount: #  Check if the deducted amount exceeds balance
            # TODO add low balance consequences 
            pass
        self.balance -= amount
        return None