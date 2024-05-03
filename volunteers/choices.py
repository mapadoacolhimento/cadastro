COLOR_CHOICES = (
    ("", "Cor"),
    ("black", "Preta"),
    ("brown", "Parda"),
    ("indigenous", "Indígena"),
    ("yellow", "Amarela"),
    ("white", "Branca"),
)

GENDER_CHOICES = (
    ("", "Identidade de gênero"),
    (
        "cis_woman",
        "Mulher cisgênero",
    ),
    (
        "trans_woman",
        "Mulher transgênero/travesti",
    ),
)

AVAILABILITY_CHOICES = (
    ("", "Vagas para atendimento"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
)

MODALITY_CHOICES = (
    ("", "Modalidade de atendimento"),
    ("on_site", "Presencial"),
    ("online", "Online"),
    ("both", "Deixo à escolha da acolhida"),
)

LIBRAS_CHOICE = (
    ("", "Atende em linguagem de sinais (libras)?"),
    (True, "Sim"),
    (False, "Não"),
)

YEARS_OF_EXPERIENCE_CHOICES = (
    ("no_experience", "Não tenho experiência"),
    ("less_than_1_year","Até 1 ano"),
    ("1_to_5_years","Entre 1 e 5 anos"),
    ("5_to_10_years","Entre 5 e 10 anos"),
    ("more_than_10_years","Mais de 10 anos"),
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
    ("Sócio-Histórica", "Sócio-Histórica"),
    ("Não tenho experiência", "Não tenho experiência"),
    ("Outros", "Outros"),
)

FOW_LAWYER_CHOICES = (
    ("Violência de Gênero", "Violência de Gênero"),
    ("Família", "Família"),
    ("Penal", "	Penal"),
    ("Trabalhista", "Trabalhista"),
    ("Cível", "Cível"),
    ("Administrativo", "Administrativo"),
    ("Empresarial", "Empresarial"),
    ("Tributário", "Tributário"),
    ("Digital", "	Digital"),
    ("Ambiental	", "Ambiental"),
    ("Outros", "Outros"),
)
FOW_CHOICES = FOW_THERAPIST_CHOICES + FOW_LAWYER_CHOICES
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

SUPPORT_TYPE = (("psychological", "Psicológico"), ("legal", "Jurídico"))

VOLUNTEER_STATUS = (
    ("registered", "Aprovada"),
    ("available", "Disponível"),
    ("training", "Capacitação"),
    ("totally_booked", "Atingiu máximo de atendimentos"),
    ("unavailable_vacation", "Indisponível - Férias"),
    ("unavailable_maternity", "Indisponível - Maternidade"),
    ("unavailable_health", "Indisponível - Saúde"),
    ("unavailable_work_study", "Indisponível - Trabalho e Estudo"),
    ("unavailable_other", "Indisponível - Outros Motivos"),
    ("unavailable_schedule", "Indisponível - Agenda"),
    ("unavailable_no_answer", "Indisponível - Sem Resposta"),
    ("incomplete_data_address", "Dados incompletos - Endereço"),
    ("incomplete_data_phone", "Dados incompletos - Telefone"),
    ("incomplete_data_email", "Dados incompletos - Email"),
    ("rejected_case_study", "Reprovada - Estudo de Caso"),
    ("rejected_guidelines", "Reprovada - Diretrizes do Mapa"),
    ("rejected_invalid_register", "Reprovada - Registro inválido"),
    ("rejected_unethical", "Anti-ética"),
    ("unsubscribed", "Descadastrada"),
)

OCCUPATION = (("psychologist", "Psicóloga"), ("lawyer", "Advogada"))