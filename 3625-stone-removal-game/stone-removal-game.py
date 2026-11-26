class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_turn=True
        remove=10
        while n>=remove:
            n-=remove
            remove-=1
            alice_turn=not alice_turn
        return not alice_turn