queue = []
recieve_name = ''
finalize_flag = False
finalize_question = ''

def finalize_session():
  print('finalized')

def print_array():
  print(queue)
  recieve_name = input('informe seu nome para entrar na fila: \n')
  queue.append(recieve_name)
  print(queue)
  finalize_question = input('Terminou? \n')

  if(finalize_question == 'sim'):
    finalize_session()

  if(finalize_question == 'nao'):
    print_array()

finalize_session()     
print_array()
