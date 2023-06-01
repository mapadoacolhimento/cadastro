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
    (
        "Mulher cisgênero",
        "Mulher cisgênero (que se identifica com o sexo que lhe foi designado ao nascer)",
    ),
    (
        "Mulher transgênero/travesti",
        "Mulher transgênero/travesti (possui outra identidade de gênero, diferente da que lhe foi designada ao nascer)",
    ),
    ("Prefiro não responder", "Prefiro não responder"),
)

AVAILABILITY_CHOICES = (
    ("", "Vagas para atendimento"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5+"),
)

MODALITY_CHOICES = (
    ("", "Modalidade de atendimento"),
    ("Presencial", "Presencial"),
    ("Online", "Online"),
    ("Deixo à escolha da acolhida", "Deixo à escolha da acolhida"),
)

LIBRAS_CHOICE = (
    ("", "Atende em linguagem de sinais (libras)"),
    ("Sim", "Sim"),
    ("Não", "Não"),
)

YEARS_OF_EXPERIENCE_CHOICES = (
    ("Não tenho experiência ", "Não tenho experiência"),
    ("Menos 6 meses", "Menos 6 meses"),
    ("Menos de 1 ano", "Menos de 1 ano"),
    ("Menos de 2 anos", "Menos de 2 anos"),
    ("Menos de 5 anos", "Menos de 5 anos"),
    ("Menos de 10 anos", "Menos de 10 anos"),
)

FOW_THERAPIST_CHOICES = (
    ("Violência contra as mulheres", "Violência contra as mulheres"),
    ("Assistência social", "Assistência social"),
    ("Saúde mental", "Saúde mental"),
    ("Psicologia clínica", "Psicologia clínica"),
    ("Psicologia jurídica", "Psicologia jurídica"),
    ("Psicologia social", "Psicologia social"),
    ("Terapia sistêmica/familiar", "Terapia sistêmica/familiar"),
    ("Serviços públicos", "Serviços públicos"),
    ("Não tenho experiência", "Não tenho experiência"),
    ("Outros", "Outros"),
)

FOW_LAWYER_CHOICES = (
    ("Violência de Gênero", "Violência de Gênero"),
    ("Família", "Família"),
    ("Penal", "	Penal"),
    ("Trabalhista", "Trabalhista"),
    ("Cível	Cível", "Cível	Cível"),
    ("Administrativo", "Administrativo"),
    ("Empresarial", "Empresarial"),
    ("Tributário", "Tributário"),
    ("Digital", "	Digital"),
    ("Ambiental	", "Ambiental"),
    ("Outros", "Outros"),
)

APPROACH_CHOICES = (
    (
        "Psicologia Analítica de Jung ou Análise Junguiana",
        "Psicologia Analítica de Jung ou Análise Junguiana",
    ),
    ("Psicanálise", "Psicanálise"),
    (
        "Behaviorismo ou Analítico Comportamental",
        "Behaviorismo ou Analítico Comportamental",
    ),
    ("Humanismo", "Humanismo"),
    ("Psicoterapia Corporal", "Psicoterapia Corporal"),
    ("Cognitivo-Comportamental ou TCC", "Cognitivo-Comportamental ou TCC"),
    ("Gestalt-terapia", "Gestalt-terapia"),
    ("Abordagem Centrada na Pessoa (ACP)", "Abordagem Centrada na Pessoa (ACP)"),
    ("Outros", "Outros"),
)

TERM_CHOICES = (("Aceito", "Aceito"), ("Não aceito", "Não aceito"))
