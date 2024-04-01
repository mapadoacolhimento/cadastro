REJECTED_VOLUNTEERS = ["reprovada_diretrizes_do_mapa", "anti-etica"]

AVAILABLE_VOLUNTEER_CONDITION = 'disponivel'

ACTIVE_VOLUNTEER_CONDITION = [
    AVAILABLE_VOLUNTEER_CONDITION, 
    'indisponivel_sem_vagas'
]

ABSENT_VOLUNTEER_CONDITION = [
    'indisponível_outros_motivos',
    'indisponível_férias',
    'indisponivel_agenda',
    'indisponível_saude',
    'indisponível_maternidade',
    'indisponível_-sem_resposta',
    'indisponível_trabalho_e_estudo'
]

UNETHICAL_VOLUNTEER_CONDITION = 'anti-etica'

REGISTERED_VOLUNTEER_CONDITION = 'cadastrada'

INCOMPLETE_DATA_VOLUNTEER_CONDITION = [
  'dados_incompletos_endereço',
  'dados_incompletos_telefone',
  'dados_incompletos_email' 
  ]
INSCRIBED_VOLUNTEER_CONDITION ='inscrita'

FAIL_VOLUNTEER_CONDITION = [ 
    'reprovada_estudo_de_caso',
    'reprovada_registro_inválido',     
    'reprovada_diretrizes_do_mapa'
  ]

NOT_FOUND_VOLUNTEER_CONDITION ='not_found'

UNSUBSCRIBED_VOLUNTEER_CONDITION = 'descadastrada'

DISABLED_VOLUNTEER_CONDITION = 'desabilitada'

APPROVED_VOLUNTEER_CONDITION = 'aprovada'
