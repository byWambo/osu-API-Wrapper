[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3bd53f2c97bd428597d662db4edf6af0)](https://www.codacy.com/app/byWambo/osu-API-Wrapper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=byWambo/osu-API-Wrapper&amp;utm_campaign=Badge_Grade)
# osu-API-Wrapper
A Python Wrapper for the osu! API. This Library helps you interacting with the osu API. Make sure to see the [Wiki](https://github.com/byWambo/osu-API-Wrapper/wiki)


## How does this work
```python
import osu

osu_client = osu.Client("YOUR API KEY")
user = osu_client.api.get_user("WamboTV") #Get User called WamboTV
print(user.pp) #Return PP from the User
```

## Support
Feel free to create a Issue for help or to create a PR for changes.\
Discord: Wambo#0800 and Emre1504#0117
