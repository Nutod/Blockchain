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

# Function that adds a new Transaction to the block
def add_transaction(recipient, sender=owner, amount=1.0):
  """
    Appends a new transaction to the list of open transactions

    Arguments:
    :sender
    :recipient
    :amount
  """
  transaction = {
    'sender': sender,
    'recipient': recipient,
    'amount': amount
  }
  if verify_transaction(transaction):
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)
    return True

  return False

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

# def get_transaction_value():
#   tx_recipient = input('Enter the sender of the Transaction')
#   tx_amount = float(input('Enter the amount:'))
#   return tx_recipient, tx_amount

def verify_transaction(transaction):
  sender_balance = get_balances(transaction['sender'])
  return sender_balance >= transaction['amount']

def get_balances(participant):
  # We are trying to get a list of amounts that are linked to the blockchain
  tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
  amount_sent = 0
  for elem in tx_sender:
    if len(elem) > 0:
      amount_sent += elem[0]
  tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
  amount_received = 0
  for elem in tx_recipient:
    if len(elem) > 0:
      amount_received += elem[0]
  return amount_sent - amount_received

def verify_chain():
  for (index, block) in enumerate(blockchain):
    if index == 0:
      continue
    if block['previous_hash'] != hash_block(blockchain[index - 1]):
      return False
  return True