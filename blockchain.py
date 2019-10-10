# Initialize the Variables
MINING_REWARD = 10
GENESIS_BLOCK = {
  'previous_hash': 'XYZ',
  'index': 0,
  'transactions': [],
}

blockchain = list(GENESIS_BLOCK)
open_transactions = list()
owner = 'Nutod'
participants = {'Nutod'}