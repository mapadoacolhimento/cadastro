COLOR_CHOICES = (
    ("", "Cor"),
    ("Preta", "Preta"),
    ("Parda", "Parda"),
    ("Indígena", "Indígena"),
    ("Amarela", "Amarela"),
    ("Branca", "Branca"),
)

GENDER_CHOICES = (
    ("cis", "Eu sou uma mulher cis"),
    ("trans", "Eu sou uma mulher trans/travesti"),
    ("nda", "Não me identifico como mulher"),
)

AGE_CHOICES = (
    ("maior", "Eu sou maior de 18 anos"),
    ("menor", "Eu sou menor de 18 anos"),
)

LOCAL_CHOICES = (
    ("brasil", "Sim, dentro do território brasileiro"),
    ("internacional", "Não, aconteceu em outro país"),
)

PHYSICAL_VIOLENCE_CHOICES = (
    ("Soco", "Soco"),
    ("Chute", "Chute"),
    ("Tapa", "Tapa"),
    ("Empurrão", "Empurrão"),
    ("Puxão de cabelo", "Puxão de cabelo"),
    ("Queimadura", "Queimadura"),
    ("Enforcamento", "Enforcamento"),
    ("Sufocamento", "Sufocamento"),
    ("Tiro", "Tiro"),
    ("Afogamento", "Afogamento"),
    ("Paulada", "Paulada"),
    ("Estrangulamento", "Estrangulamento"),
    ("Facada", "Facada"),
    (
        "Me exigiu práticas sexuais que eu não gosto",
        "Me exigiu práticas sexuais que eu não gosto",
    ),
    (
        "Fui forçada à alguma prática sexual na intenção de corrigirem minha orientação sexual",
        "Fui forçada à alguma prática sexual na intenção de corrigirem minha orientação sexual",
    ),
    ("Não estou sofrendo violência física", "Não estou sofrendo violência física"),
)

PSYCH_VIOLENCE_CHOICES = (
    ("Fui controlada", "Fui controlada"),
    ("Fui criticada", "Fui criticada"),
    ("Fui humilhada", "Fui humilhada"),
    ("Fui insultada", "Fui insultada"),
    ("Se/me negou a usar preservativo", "Se/me negou a usar preservativo"),
    (
        "Tive minha identidade inviabilizada e negada",
        "Tive minha identidade inviabilizada e negada",
    ),
    ("Fui isolada", "Fui isolada"),
    (
        "Não me permitiu usar certos tipos de roupa",
        "Não me permitiu usar certos tipos de roupa",
    ),
    ("Fui xingada", "Fui xingada"),
    ("Fui desautorizada", "Fui desautorizada"),
    ("Não me deixou trabalhar", "Não me deixou trabalhar"),
    (
        "Me negou o direito a métodos contraceptivos",
        "Me negou o direito a métodos contraceptivos",
    ),
    ("Fui vigiada", "Fui vigiada"),
    ("Fui perseguida e ameaçada", "Fui perseguida e ameaçada"),
    ("Proibida de ir ao médico", "Proibida de ir ao médico"),
    (
        "Não estou sofrendo violência psicológica",
        "Não estou sofrendo violência psicológica",
    ),
)

SEXUAL_VIOLENCE_CHOICES = (
    ("Se/me negou a usar preservativo", "Se/me negou a usar preservativo"),
    (
        "Me negou o direito a métodos contraceptivos",
        "Me negou o direito a métodos contraceptivos",
    ),
    (
        "Fui forçada à alguma prática sexual na intenção ",
        "de corrigirem minha orientação sexual",
    ),
    (
        "Me exigiu práticas sexuais que eu não gosto",
        "Me exigiu práticas sexuais que eu não gosto",
    ),
    ("Não estou sofrendo violência sexual", "Não estou sofrendo violência sexual"),
)

DIGITAL_VIOLENCE_CHOICES = (
    (
        "Tive vazamento/compartilhamento na internet de minhas informações pessoais e dados sem meu consentimento",
        "Tive vazamento/compartilhamento na internet de minhas informações pessoais e dados sem meu consentimento",
    ),
    (
        "Tive vazamento/compartilhamento na internet de minhas imagens íntimas",
        "Tive vazamento/compartilhamento na internet de minhas imagens íntimas",
    ),
    (
        "Sofri stalking online (perseguição ou observação obsessiva)",
        "Sofri stalking online (perseguição ou observação obsessiva)",
    ),
    ("Não estou sofrendo violência digital", "Não estou sofrendo violência digital"),
)

PROPERTY_VIOLENCE_CHOICES = (
    ("Ocultou bens e propriedades", "Ocultou bens e propriedades"),
    ("Controlou meu dinheiro", "Controlou meu dinheiro"),
    ("Me impediu de ter acesso ao dinheiro", "Me impediu de ter acesso ao dinheiro"),
    ("Destruiu meus objetos", "Destruiu meus objetos"),
    ("Me extorquiu", "Me extorquiu"),
    (
        "Me impediu de ter acesso a conta bancária ou outros bens",
        "Me impediu de ter acesso a conta bancária ou outros bens",
    ),
    (
        "Não estou sofrendo violência patrimonial",
        "Não estou sofrendo violência patrimonial",
    ),
)

OBSTETRIC_VIOLENCE_CHOICES = (
    (
        "Alteraram o processo natural do parto sem meu consentimento voluntário",
        "Alteraram o processo natural do parto sem meu consentimento voluntário",
    ),
    (
        "Sofri abusos e maus-tratos durante a minha gestação",
        "Sofri abusos e maus-tratos durante a minha gestação",
    ),
    (
        "Sofri abusos e maus-tratos no momento do meu parto",
        "Sofri abusos e maus-tratos no momento do meu parto",
    ),
    (
        "Não estou sofrendo violência obstétrica",
        "Não estou sofrendo violência obstétrica",
    ),
)

SERVICE_CHOICES = (
    ("Não estou sendo acompanhada", "Não estou sendo acompanhada"),
    (
        "Estou sendo acompanhada por um(a) psicólogo(a) particular",
        "Estou sendo acompanhada por um(a) psicólogo(a) particular",
    ),
    (
        "Estou sendo acompanhada por um(a) advogado(a) particular",
        "Estou sendo acompanhada por um(a) advogado(a) particular",
    ),
    (
        "Estou sendo acompanhada na defensoria pública/ NUDEM",
        "Estou sendo acompanhada na defensoria pública/ NUDEM",
    ),
)

INCOME_CHOICES = options = (
    ("Empregada com CLT", "Empregada com CLT"),
    ("Empregada sem CLT", "Empregada sem CLT"),
    ("Desempregada", "Desempregada"),
    ("Empreendedora autônoma", "Empreendedora autônoma"),
    ("Estudante e com renda independente", "Estudante e com renda independente"),
    ("Aposentada", "Aposentada"),
    (
        "Estudante e dependente da minha família",
        "Estudante e dependente da minha família",
    ),
)
TO_HAVE_CHOICES = (
    ("Sim", "Sim, eu tenho"),
    ("Não", "Não, eu não tenho"),
)

TO_BE_CHOICES = (
    ("Sim", "Sim, eu sou"),
    ("Não", "Não, eu não sou"),
)

TYPE_OF_SUPPORT = (
    ("psicologico", "Psicológico"),
    ("juridico", "Jurídico"),
)


EDUCATION_CHOICES = (
    ("Ensino fundamental incompleto", "Ensino fundamental incompleto"),
    ("Ensino fundamental completo", "Ensino fundamental completo"),
    ("Ensino médio incompleto", "Ensino médio incompleto"),
    ("Ensino médio completo", "Ensino médio completo"),
    ("Ensino técnico", "Ensino técnico"),
    ("Ensino superior incompleto", "Ensino superior incompleto"),
    ("Ensino superior completo", "Ensino superior completo"),
    ("Pós-graduação", "Pós-graduação"),
    ("Mestrado", "Mestrado"),
    ("Doutorado", "Doutorado"),
    ("Pós-doutorado", "Pós-doutorado"),
    ("Nunca frequentei/procurei", "Nunca frequentei/procurei"),
)

DURATION_CHOICES = (
    ("", "Há quanto tempo está sofrendo violência?"),
    ("Mais de 10 anos", "Mais de 10 anos"),
    ("Entre 2 anos e 10 anos", "Entre 2 anos e 10 anos"),
    ("Entre 1 e 2 anos", "Entre 1 e 2 anos"),
    ("Entre 6 meses e 1 ano", "Entre 6 meses e 1 ano"),
    ("Entre 3 e 6 meses", "Entre 3 e 6 meses"),
    ("Menos de 3 meses", "Menos de 3 meses"),
    ("Menos de 1 semana", "Menos de 1 semana"),
    ("Nos últimos 3 dias", "Nos últimos 3 dias"),
)

AUTHOR_CHOICES = (
    ("", "Quem é ou foi o(a) autor(a) da violência?"),
    ("Pai", "Pai"),
    ("Mãe", "Mãe"),
    ("Irmão/Irmã", "Irmão/Irmã"),
    ("Tio/Tia", "Tio/Tia"),
    ("Primo/Prima", "Primo/Prima"),
    ("Vizinho/Vizinha", "Vizinho/Vizinha"),
    ("Namorado/Namorada", "Namorado/Namorada"),
    ("Marido/Esposa", "Marido/Esposa"),
    ("Ex-namorado/Ex-namorada", "Ex-namorado/Ex-namorada"),
    ("Ex-marido/Ex-esposa", "Ex-marido/Ex-esposa"),
    ("Amigo/Amiga", "Amigo/Amiga"),
    ("Filho/Filha", "Filho/Filha"),
)

RISK_CHOICES = (
    (
        "O(A) autor(a) da violência possui acesso à arma de fogo",
        "O(A) autor(a) da violência possui acesso à arma de fogo",
    ),
    ("Estou em cárcere privado", "Estou em cárcere privado"),
    (
        "A violência ocorreu em ambiente doméstico",
        "A violência ocorreu em ambiente doméstico",
    ),
    (
        "A violência ocorreu durante a gestação",
        "A violência ocorreu durante a gestação",
    ),
    ("Eu não me sinto segura em casa", "Eu não me sinto segura em casa"),
    (
        "O(A) autor(a) da violência tem diagnóstico de doença psiquiátrica",
        "O(A) autor(a) da violência tem diagnóstico de doença psiquiátrica",
    ),
    (
        "O(A) autor(a) da violência faz uso de substância psicoativa ",
        "O(A) autor(a) da violência faz uso de substância psicoativa ",
    ),
    (
        "Dependo financeiramente do(a) autor(a) da violência",
        "Dependo financeiramente do(a) autor(a) da violência",
    ),
    (
        "A violência ocorreu em ambiente de trabalho",
        "A violência ocorreu em ambiente de trabalho",
    ),
    (
        "A violência ocorreu em ambiente público (internet, rua, etc)",
        "A violência ocorreu em ambiente público (internet, rua, etc)",
    ),
    (
        "Tive acesso negado aos serviços públicos de atendimento à mulher",
        "Tive acesso negado aos serviços públicos de atendimento à mulher",
    ),
    (
        "As agressões ou ameaças do(a) autor(a) da violência contra mim se tornaram mais frequentes ou mais graves nos últimos meses",
        "As agressões ou ameaças do(a) autor(a) da violência contra mim se tornaram mais frequentes ou mais graves nos últimos meses",
    ),
)

PROTECTIVE_CHOICES = (
    (
        "Eu possuo rede de apoio (familiares, amigos, vizinhos etc)",
        "Eu possuo rede de apoio (familiares, amigos, vizinhos etc)",
    ),
    (
        "Não resido com o(a) autor(a) da violência",
        "Não resido com o(a) autor(a) da violência",
    ),
    ("Me sinto segura em casa", "Me sinto segura em casa"),
    (
        "Não dependo financeiramente do(a) autor(a) da violência",
        "Não dependo financeiramente do(a) autor(a) da violência",
    ),
    (
        "O local onde resido possui serviços públicos de atendimento à mulher com atendimento qualificado",
        "O local onde resido possui serviços públicos de atendimento à mulher com atendimento qualificado",
    ),
)

PUBLIC_SERVICE_CHOICES = (
    ("CREAS", "Centro de Referência Especializado de Assistência Social (CREAS)"),
    ("CRAS", "Centro de Referência de Assistência Social (CRAS)"),
    ("UBS", "Unidade Básica de Saúde (UBS) "),
    (
        "CRM/CDCM/CRAM/CIAM ",
        "Centro de Referência da Mulher (CRM); Centro de Defesa e de Convivência da Mulher (CDCM); Centro de Referência de Atendimento à Mulher (CRAM); Centro Integrado de Atendimento à Mulher (CIAM) ",
    ),
    ("CMB", "Casa da Mulher Brasileira (CMB)"),
    ("DEAM", "Delegacia Especializada da Mulher (DEAM)"),
    ("Delegacia Civil", "Delegacia Civil"),
    ("Hospital de Abortamento Legal ", "Hospital de Abortamento Legal "),
    ("MP", "Ministério Público (MP)"),
    ("CAPS", "Centro de Atenção Psicossocial (CAPS)"),
    (
        "Estou sendo atendida por um coletivo/movimento",
        "Estou sendo atendida por um coletivo/movimento",
    ),
)

STATUS_CHOICES = (("Inscrita", "Inscrita"), ("Incompleta", "Incompleta"))

ACCESS_CHOICES = (
    ("Instagram", "Instagram"),
    ("Facebook", "Facebook"),
    ("Twitter", "Twitter"),
    ("Podcast", "Podcast"),
    ("Reportagem/notícia", "Reportagem/notícia"),
    ("Indicação", "Indicação"),
    ("Outros", "Outros"),
)

PRIORITY_CHOICES = (
    ("verde", "verde"),
    ("vermelho", "vermelho"),
    ("amarelo", "amarelo"),
)

# REGISTER CHOICES

REGISTER_RISK_CHOICES = (
    (
        "O(A) autor(a) da violência possui acesso à arma de fogo",
        "O(A) autor(a) da violência possui acesso à arma de fogo",
    ),
    ("Ocorreu em ambiente doméstico", "Ocorreu em ambiente doméstico"),
    ("Não me sinto segura em casa", "Não me sinto segura em casa"),
    ("Estou em cárcere privado", "Estou em cárcere privado"),
    (
        "Ocorreu em ambiente público (internet, rua, etc)",
        "Ocorreu em ambiente público (internet, rua, etc)",
    ),
    ("Ocorreu em ambiente de trabalho", "Ocorreu em ambiente de trabalho"),
    (
        "O(A) autor(a) tem diagnóstico de doença psiquiátrica",
        "O(A) autor(a) tem diagnóstico de doença psiquiátrica",
    ),
    (
        "O(A) autor(a) faz uso de substância psicoativa",
        "O(A) autor(a) faz uso de substância psicoativa",
    ),
    (
        "Dependo financeiramente do(a) autor(a) da violência",
        "Dependo financeiramente do(a) autor(a) da violência",
    ),
    (
        "Tive acesso negado aos serviços públicos de atendimento à mulher",
        "Tive acesso negado aos serviços públicos de atendimento à mulher",
    ),
    (
        "As agressões ou ameaças do(a) autor(a) da violência contra mim se ",
        "tornaram mais frequentes ou mais graves nos últimos meses",
    ),
)

REGISTER_PROTECTION_CHOICES = (
    (
        "Eu possuo rede de apoio (familiares, amigos, vizinhos etc)",
        "Eu possuo rede de apoio (familiares, amigos, vizinhos etc)",
    ),
    (
        "Não resido com o(a) autor(a) da violência",
        "Não resido com o(a) autor(a) da violência",
    ),
    ("Não me sinto segura em casa", "Não me sinto segura em casa"),
    ("Me sinto segura em casa", "Me sinto segura em casa"),
    (
        "Não dependo financeiramente do(a) autor(a) da violência",
        "Não dependo financeiramente do(a) autor(a) da violência",
    ),
    (
        "O local onde resido possui serviços públicos de atendimento à mulher com atendimento qualificado",
        "O local onde resido possui serviços públicos de atendimento à mulher com atendimento qualificado",
    ),
)
