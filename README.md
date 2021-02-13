# PiazzaBot
Discord bot to embed Piazza posts in the designated server

## About

PiazzaBot will give you a embeded preview of a Piazza post right on your server!
Just enter in the link to the post, and PiazzaBot will take care of the rest! 

## Installation
To run PiazzaBot locally, do the following: 

1. First make a virtual environment in python using

```
python3 -m venv ./env
source ./env/bin/activate
pip3 install -r requirements
```

2. Export your environment variables as such
Rename `.env.template` to `.env` and fill in all the fields defined in the file

3. Then run the program with `python3 ./connect.py`

NOTE: Your Piazza account must be enrolled in the class to get the embeded preview, or else
it won't work.


## Built With
- Python
- [piazza-api](https://github.com/hfaran/piazza-api)
- [discord.py](https://github.com/Rapptz/discord.py)

## Note
This repository is a fork of [piazza_bot](https://github.com/zzulanas/piazza_bot) by zzulanas but modified to my person use and use embeds instead of plain text

## License
This project is licensed under [MIT](LICENSE) - see the LICENSE file for details
