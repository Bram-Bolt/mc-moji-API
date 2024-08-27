> **DISCLAIMER**: API is currently deployed at the free plan of render.com, therefore will take a couple seconds at first boot.

# mc-moji-API

This project is a FastAPI-based web service for generating and serving Minecraft avatar images using [mc-moji.](https://github.com/Bram-Bolt/mc-moji)
 ##  Usage
The most basic usage consists of:
```vbnet
https://api.brambolt.me/mc-moji/[your playername]
```
This returns a 330x480 avatar of a minecraft skin.

A more complex usage can be found below.
### API Endpoints

- **GET /mc-moji/{playername}**
    - **Description**: Generate and retrieve a Minecraft avatar image.
    - **Parameters**:
        - `playername` (path): The name of the player.
        - `shadows` (query, optional): Include shadows in the avatar. Default is `True`.
        - `overlay` (query, optional): Include overlay in the avatar. Default is `True`.
        - `size` (query, optional): Size of the avatar. Must be between 1 and 255. Default is `30`.

    - **Example Request**:
		 ```vbnet
		https://api.brambolt.me/mc-moji/Steve?shadows=true&overlay=true&size=30
		```
	
	 - **Example Response**:
	![example](https://i.imgur.com/YIR6egw.png)
## Self-Hosting
Please feel free to host this API yourself. However, for large scale personal use I recommend using the mc-moji package.

## Contact & Contributing
All types of contributions are encouraged and valued. From adding extra mappings to code refactors. Just open a pull request or issue and I will take a look at it.
For more complex suggestions, or questions, reach out to [contact@brambolt.me](mailto:contact@brambolt.me).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
