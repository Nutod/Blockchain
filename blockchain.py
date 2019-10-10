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

# Hash block function
# TODO: Add this to an utils module
def hash_block(block):
  return '-'.join([str(block[key]) for key in block])