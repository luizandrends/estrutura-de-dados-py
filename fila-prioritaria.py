main_queue = []
priority_queue = []
fever_queue = []

receive_name = ''
priority_need = ''
menu_option = ''

def assign_to_main_queue():
  receive_name = input('Informe o seu nome: \n')
  main_queue.append(receive_name)
  print('FILA NORMAL \t')
  print(main_queue)
  print('\n\n\n')

def assign_to_priority_queue():
  receive_name = input('Informe o seu nome (FILA PRIORITARIA): \n')
  priority_queue.append(receive_name)
  print('FILA PRIORITARIA \t')
  print(priority_queue)
  print('\n\n\n')

def assign_to_fever_queue():
  receive_name = input('Informe o seu nome (FILA DE FEBRE): \n')
  fever_queue.append(receive_name)
  print('FILA DE FEBRE \t')
  print(fever_queue)
  print('\n\n\n')

def show_queue_data():
  print('\n\n')

  print('Fila prioritaria:\t')
  print(priority_queue)

  print('\n\n')

  print('Fila normal:\t')
  print(main_queue)

  print('\n\n')

  print('Fila de febre:\t')
  print(fever_queue)

  print('\n')

def remove_patient_from_queue():
  if(fever_queue):
    print('Por favor se locomover a sala de atendimento (FEBRE) ')
    print(fever_queue[0])

    fever_queue.pop(0)
    return

  elif(priority_queue):
    print('Por favor se locomover a sala de atendimento (PRIORITARIA) ')
    print(priority_queue[0])

    priority_queue.pop(0)
    return

  else:
    print('Por favor se locomover a sala de atendimento (NORMAL)')
    print(main_queue[0])

    main_queue.pop(0)
    return

def main():
  while(True):
    print('1 - Adicionar na fila\n')
    print('2 - Adicionar na fila de prioridade\n')
    print('3 - Adicionar na fila de febre\n')
    print('4 - Mostrar listas \n')
    print('5 - Chamar o primeiro da fila\n')
    print('6 - Sair')
    menu_option = input('Informe uma opçao: ')

    if(menu_option == '1'):
      assign_to_main_queue()

    if(menu_option == '2'):
      assign_to_priority_queue()

    if(menu_option == '3'):
      assign_to_fever_queue()

    if(menu_option == '4'):
      show_queue_data()

    if(menu_option == '5'):
      remove_patient_from_queue()
    
    if(menu_option == '6'):
      break

main()