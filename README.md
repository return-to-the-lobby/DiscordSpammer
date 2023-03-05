# Discord-Spammer
Literally Discord message spammer but spams one word.

## The Best Message Length Calculation
```python
counts = 2000 / len(content) if not space else 2000 / (len(content) + 1)
counts = math.floor(counts)
```
`Auto calculates the best length for word to spam.`

## Configuration
```ini
[config]
Content = <Content Here>
Space = False
Delay = <Delay in Python Tuple or ArrayList like (0.1, 0.5)>
Authorization = <Your Discord Authorization>
Channel = <Target Channel>
```
`The filename must be 'config.ini'`
