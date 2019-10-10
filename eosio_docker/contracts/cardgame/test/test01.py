from eosfactory.eosf import *
c = ContractBuilder("/mnt/d/Workspaces/EOSIO/eosio-card-game-repo-lesson-8/eosio_docker/contracts/cardgame")
c.build()

--

from eosfactory.eosf import *
reset()
create_master_account("master")
create_account("alice", master)

create_account("host", master, account_name="cardgameacc")
c = Contract(host, "/mnt/d/Workspaces/EOSIO/eosio-card-game-repo-lesson-8/eosio_docker/contracts/cardgame")
c.deploy()

--

nano /home/sygnet/eosio-wallet/_127_0_0_1_8888_passwords.json
cleos wallet private_keys -n _127_0_0_1_8888_default

--

get_account()
expose private key

teos.py:
"--access-control-allow-origin=*",

--

c.deploy(host)
create_account("host", master, name="cardgameacc")