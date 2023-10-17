
COLOR_CHOICES = (
    ("", "Cor"),
    ("Preta", "Preta"),
    ("Parda", "Parda"),
    ("Indígena", "Indígena"),
    ("Amarela", "Amarela"),
    ("Branca", "Branca"),
)

GENDER_CHOICES = (
        ('cis', 'Eu sou uma mulher cis'),
        ('trans', 'Eu sou uma mulher trans/travesti'),
        ('nda', 'Não me identifico como mulher'),
    )

AGE_CHOICES = (
        ('maior', 'Eu sou maior de 18 anos'),
        ('menor', 'Eu sou menor de 18 anos'),
    )

LOCAL_CHOICES = (
        ('brasil', 'Sim, dentro do território brasileiro'),
        ('internacional', 'Não, aconteceu em outro país'),
    )

VIOLENCE_CHOICES = (
        ('Fui humilhada', 'Fui humilhada'),
        ('Levei um soco', 'Levei um soco'),
        ('Fui ameaçada', 'Fui ameaçada'),
        ('Levei um chute e/ou tapa', 'Levei um chute e/ou tapa'),
        ('Sofri abusos e maus-tratos', 'Sofri abusos e maus-tratos'),
        ('Se/me negou a usar preservativo', 'Se/me negou a usar preservativo'),
        ('Fui perseguida e/ou vigiada', 'Fui perseguida e/ou vigiada'),
        ('Me expôs na internet', 'Me expôs na internet'),
        ('Fui forçada à alguma prática sexual', 'Fui forçada à alguma prática sexual'),
        ('Fui empurrada', 'Fui empurrada'),
        ('Não estou sofrendo nenhum tipo de violência', 'Não estou sofrendo nenhum tipo de violência'),
    )

SERVICE_CHOICES = (
        ('Não estou sendo acompanhada', 'Não estou sendo acompanhada'),
        ('Estou sendo acompanhada por um(a) psicólogo(a) particular', 'Estou sendo acompanhada por um(a) psicólogo(a) particular'),
        ('Estou sendo acompanhada por um(a) advogado(a) particular', 'Estou sendo acompanhada por um(a) advogado(a) particular'),
        ('Estou sendo acompanhada na defensoria pública/ NUDEM', 'Estou sendo acompanhada na defensoria pública/ NUDEM'),
    ) 

INCOME_CHOICES = options = (
        ('Empregada com CLT', 'Empregada com CLT'),
        ('Empregada sem CLT', 'Empregada sem CLT'),
        ('Desempregada', 'Desempregada'),
        ('Empreendedora autônoma', 'Empreendedora autônoma'),
        ('Estudante e com renda independente', 'Estudante e com renda independente'),
        ('Aposentada', 'Aposentada'),
        ('Estudante e dependente da minha família', 'Estudante e dependente da minha família'),

    )
TO_HAVE_CHOICES = (
        ('Sim', 'Sim, eu tenho'),
        ('Não', 'Não, eu não tenho'),
    )

TO_BE_CHOICES =  (
        ('Sim', 'Sim, eu sou'),
        ('Não', 'Não, eu não sou'),
    )

TYPE_OF_SUPPORT = (
  ("psicologico", "Psicológico"), 
  ("juridico", "Jurídico"),
  
)


EDUCATION_CHOICES = (
  ("Ensino fundamental incompleto","Ensino fundamental incompleto"),
  ("Ensino fundamental completo","Ensino fundamental completo"),
  ("Ensino médio incompleto","Ensino médio incompleto"),
  ("Ensino médio completo","Ensino médio completo"),
  ("Ensino técnico","Ensino técnico"),
  ("Ensino superior incompleto","Ensino superior incompleto"),
  ("Ensino superior completo","Ensino superior completo"),
  ("Pós-graduação","Pós-graduação"),
  ("Mestrado","Mestrado"),
  ("Doutorado","Doutorado"),
  ("Pós-doutorado","Pós-doutorado"),
  ("Nunca frequentei/procurei","Nunca frequentei/procurei"),
  
)

DURATION_CHOICES = (
  ("Mais de 10 anos","Mais de 10 anos"),
  ("Entre 2 anos e 10 anos","Entre 2 anos e 10 anos"),
  ("Entre 1 e 2 anos","Entre 1 e 2 anos"),
  ("Entre 6 meses e 1 ano","Entre 6 meses e 1 ano"),
  ("Entre 3 e 6 meses","Entre 3 e 6 meses"),
  ("Menos de 3 meses","Menos de 3 meses"),
  ("Menos de 1 semana","Menos de 1 semana"),
  ("Nos últimos 3 dias","Nos últimos 3 dias")
)

AUTHOR_CHOICES = (
  ("Pai","Pai"),
  ("Mãe","Mãe"),
  ("Irmão/Irmã","Irmão/Irmã"),
  ("Tio/Tia","Tio/Tia"),
  ("Primo/Prima","Primo/Prima"),
  ("Vizinho/Vizinha","Vizinho/Vizinha"),
  ("Namorado/Namorada","Namorado/Namorada"),
  ("Marido/Esposa","Marido/Esposa"),
  ("Ex-namorado/Ex-namorada","Ex-namorado/Ex-namorada"),
  ("Ex-marido/Ex-esposa","Ex-marido/Ex-esposa"),
  ("Amigo/Amiga","Amigo/Amiga"),
  ("Filho/Filha","Filho/Filha"),
)

RISK_CHOICES = (
  ("O(A) autor(a) da violência possui acesso à arma de fogo","O(A) autor(a) da violência possui acesso à arma de fogo"),
  ("Estou em cárcere privado","Estou em cárcere privado"),
  ("A violência ocorreu em ambiente doméstico","A violência ocorreu em ambiente doméstico"),
  ("A violência ocorreu durante a gestação","A violência ocorreu durante a gestação"),
  ("Eu não me sinto segura em casa","Eu não me sinto segura em casa"),
  ("O(A) autor(a) da violência tem diagnóstico de doença psiquiátrica","O(A) autor(a) da violência tem diagnóstico de doença psiquiátrica"),
  ("O(A) autor(a) da violência faz uso de substância psicoativa ","O(A) autor(a) da violência faz uso de substância psicoativa "),
  ("Dependo financeiramente do(a) autor(a) da violência","Dependo financeiramente do(a) autor(a) da violência"),
  ("A violência ocorreu em ambiente de trabalho","A violência ocorreu em ambiente de trabalho"),
  ("A violência ocorreu em ambiente público (internet, rua, etc)","A violência ocorreu em ambiente público (internet, rua, etc)"),
  ("Tive acesso negado aos serviços públicos de atendimento à mulher","Tive acesso negado aos serviços públicos de atendimento à mulher"),
  ("As agressões ou ameaças do(a) autor(a) da violência contra mim se tornaram mais frequentes ou mais graves nos últimos meses","As agressões ou ameaças do(a) autor(a) da violência contra mim se tornaram mais frequentes ou mais graves nos últimos meses"),

)

PROTECTIVE_CHOICES = (
  ("Eu possuo rede de apoio (familiares, amigos, vizinhos etc)","Eu possuo rede de apoio (familiares, amigos, vizinhos etc)"),
  ("Não resido com o(a) autor(a) da violência","Não resido com o(a) autor(a) da violência"),
  ("Me sinto segura em casa","Me sinto segura em casa"),
  ("Não dependo financeiramente do(a) autor(a) da violência","Não dependo financeiramente do(a) autor(a) da violência"),
  ("O local onde resido possui serviços públicos de atendimento à mulher com atendimento qualificado","O local onde resido possui serviços públicos de atendimento à mulher com atendimento qualificado"),

)

PUBLIC_SERVICE_CHOICES = (
  ("CREAS","Centro de Referência Especializado de Assistência Social (CREAS)"),
  ("CRAS","Centro de Referência de Assistência Social (CRAS)"),
  ("UBS","Unidade Básica de Saúde (UBS) "),
  ("CRM/CDCM/CRAM/CIAM ","Centro de Referência da Mulher (CRM); Centro de Defesa e de Convivência da Mulher (CDCM); Centro de Referência de Atendimento à Mulher (CRAM); Centro Integrado de Atendimento à Mulher (CIAM) "),
  ("CMB","Casa da Mulher Brasileira (CMB)"),
  ("DEAM","Delegacia Especializada da Mulher (DEAM)"),
  ("Delegacia Civil","Delegacia Civil"),
  ("Hospital de Abortamento Legal ","Hospital de Abortamento Legal "),
  ("MP","Ministério Público (MP)"),
  ("CAPS","Centro de Atenção Psicossocial (CAPS)"),
  ("Estou sendo atendida por um coletivo/movimento","Estou sendo atendida por um coletivo/movimento"),

)

STATUS_CHOICES = (
  
  ("Inscrita", "Inscrita"), 
  ("Incompleta", "Incompleta")
  
)

ACCESS_CHOICES = (
  ("Instagram","Instagram"),
  ("Facebook","Facebook"),
  ("Twitter","Twitter"),
  ("Podcast","Podcast"),
  ("Reportagem/notícia","Reportagem/notícia"),
  ("Indicação","Indicação"),
  ("Outros","Outros"),
)

PRIORITY_CHOICES = (
  ("verde", "verde"), 
  ("vermelho", "vermelho"), 
  ("amarelo", "amarelo")
)