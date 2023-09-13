Today i review all of my previous concept and i apply them in my 
Blackjack project.

About my project : Blackjack Strategy
1. When the value of dealer's revealed card is 4,5 or 6, it may be fruitful to double your bet with an Ace and 4 in hand.

2. You may want to surrender if you have 16 in your hand while the dealer has a 9,10 or A.

3. You should always split if you have a pair of Aces.

4. If you get a pair of 7s, only press hit if the dealer has 8,9,10 or Ace.

## Testing

1. Deal both user and computer a starting hand of 2 random card values.
2. Detect when computer or user has a blackjack. (Ace + 10 value card).
3. If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a
blackjack, then they win (unless the computer also has a blackjack).
4. Calculate the user's and computer's scores based on their card values.
5. If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
Reveal computer's first card to the user.
6. Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
7. Ask the user if they want to get another card.
9. Once the user is done and no longer wants to draw any more cards, let the computer play. The computer
should keep drawing cards unless their score goes over 16.
10. Compare user and computer scores and see if it's a win, loss, or draw.
11. Print out the player's and computer's final hand and their scores at the end of the game.
12. After the game ends, ask the user if they'd like to play again. Clear the console for a fresh sta