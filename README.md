# DiscordSpammer
Literally Discord message spammer but spams one word.

## The Best Message Length Calculation
```python
counts = 2000 / len(content) if not space else 2000 / (len(content) + 1)
counts = math.floor(counts)
```
`Auto calculates the best length for word to spam.`
