# Enasis Network Chatting Robie

> :warning: Will probably only work with UnrealIRCd 5.

## Build virtual environment
```shell
python -m venv venv
source venv/bin/activate
pip install enrobie
```

## Run the prototype script
Update [launcher.py](launcher.py) to your liking and start.
```
python -m ircservices.launcher --console --debug
```
You should see something like this in `/who *`
```
[*] ChatServ (service@services) H* 0 (Invitable LLM chatting)
[*] HelpServ (service@services) H* 0 (Help about the services)
[*] HostServ (service@services) H* 0 (Host cloak management)
[*] MemoServ (service@services) H* 0 (Offline message sharing)
[*] ChanServ (service@services) H* 0 (Channel registration)
[*] NickServ (service@services) H* 0 (Nickname registration)
[*] StatServ (service@services) H* 0 (Statistics and analysis)
[*] OperServ (service@services) H* 0 (Network administration)
[*] RootServ (service@services) H* 0 (Network administration)
```

> :mute: These services do not actually do anything!
