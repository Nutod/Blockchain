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

def mine_block():
  last_block = blockchain[-1]
  hashed_block = '-'.join([str(last_block[key]) for key in last_block])
  reward_transaction = {
    'sender': 'MINING',
    'recipient': owner,
    'amount': MINING_REWARD
  }
  copied_transactions = open_transactions[:]
  copied_transactions.append(reward_transaction)
    
  block = {
    'previous_hash': hashed_block,
    'index': len(blockchain),
    'transactions': copied_transactions,
  }

  blockchain.append(block)
  return True

def get_transaction_value():
  tx_recipient = input('Enter the sender of the Transaction')
  tx_amount = float(input('Enter the amount:'))
  return tx_recipient, tx_amount