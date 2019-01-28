# osu-API-Wrapper
A Python Wrapper for the osu! API


## How does this work?
```python
import osu

osu_client = osu.Client("YOUR API KEY")
user = osu_client.api.get_user("WamboTV") #Get User called WamboTV
print(user.pp) #Return PP from the User
```

## Support
Feel free to create a Issue for help or to create a PR for changes.\
Discord: Wambo#0800
