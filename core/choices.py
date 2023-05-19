COLOR_CHOICES = (
    ("", "Cor"),
    ("Preta", "Preta"),
    ("Parda", "Parda"),
    ("Indígena", "Indígena"),
    ("Amarela", "Amarela"),
    ("Branca", "Branca"),
)

GENDER_CHOICES = (
    ("", "Identidade de gênero"),
    ("Mulher cisgênero", "Mulher cisgênero (que se identifica com o sexo que lhe foi designado ao nascer)"),
    ("Mulher transgênero/travesti", "Mulher transgênero/travesti (possui outra identidade de gênero, diferente da que lhe foi designada ao nascer)"),
    ("Prefiro não responder", "Prefiro não responder"),
)

AVAILABILITY_CHOICES = (
  ("","Vagas para atendimento"),
  ("1","1"),
  ("2","2"),
  ("3","3"),
  ("4","4"),
  ("5","5+")
)

MODALITY_CHOICES = (
  ("","Modalidade de atendimento"),
  ("Presencial","Presencial"),
  ("Online","Online"),
  ("Deixo à escolha da acolhida","Deixo à escolha da acolhida")
)

LIBRAS_CHOICE = (
  ("","Atende em linguagem de sinais (libras)"),
  (True,"Sim"),
  (False,"Não"),    
)