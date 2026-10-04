#!/usr/bin/env python3
"""Generate raw-ano.json with 17 varied clues per year (answers fixed)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "src/data/raw-ano.json"

ANSWERS = [
    "1500", "1776", "1789", "1808", "1822", "1824", "1865", "1870", "1888", "1889",
    "1900", "1905", "1912", "1914", "1917", "1918", "1922", "1929", "1930", "1932",
    "1939", "1942", "1945", "1948", "1950", "1953", "1957", "1958", "1960", "1961",
    "1962", "1963", "1964", "1968", "1969", "1970", "1972", "1975", "1979", "1980",
    "1985", "1986", "1988", "1989", "1991", "1992", "1994", "1997", "1998", "2000",
    "2001", "2002", "2003", "2004", "2007", "2008", "2010", "2011", "2012", "2013",
    "2014", "2015", "2016", "2017", "2018", "2019", "2021", "2022", "2023", "2024",
]

# 12–14 event/history clues per year; numeric slots filled in compose()
EVENTS: dict[str, list[str]] = {
    "1500": [
        "Cabral avistou costa no que viria a ser o Brasil.",
        "Portugal registrou o contato com a América do Sul nesta data.",
        "Missa de Porto Seguro entrou nos livros escolares.",
        "Frotas lusitanas buscavam rota pras Índias e acharam terra nova.",
        "Colonialismo brasileiro costuma começar a contar daqui.",
        "Calendário europeu ainda vivia Idade Média quando cheguei.",
        "Mapa atlântico ganhou linha extra nesta época.",
        "História do Brasil me cita no primeiro capítulo.",
        "Navegação portuguesa cruzou o Atlântico Sul nesta passagem.",
        "Descobrimento oficial do Brasil entra na conversa comigo.",
        "Pedro Álvares Cabral liderou a expedição que me marcou.",
        "Quem estuda Brasil ouve meu nome cedo.",
    ],
    "1776": [
        "Treze Colônias romperam com a coroa britânica.",
        "Jefferson assinou texto que fundou os EUA.",
        "Guerra de Independência americana ganhou documento nesta data.",
        "Philadelphia virou palco de ruptura imperial.",
        "Rei George III perdeu colônias do outro lado do oceano.",
        "4 de julho virou feriado por causa desta ruptura.",
        "Nação independente nasceu na costa leste americana.",
        "Iluminismo político virou revolução armada aqui.",
        "Exército continental e britânico ainda se enfrentavam.",
        "Declaração de Independência saiu nesta data.",
        "EUA entram no mapa como república a partir daqui.",
        "História americana me trata como ano zero da nação.",
    ],
    "1789": [
        "Multidão invadiu a Bastilha em Paris.",
        "Luís XVI viu o Antigo Regime ruir.",
        "Revolução Francesa estourou de vez.",
        "Tiradentes e inconfidentes aparecem no Brasil nesta mesma data.",
        "Guilhotina e lema de liberdade marcaram a década.",
        "Estados Gerais tinham sido convocados pouco antes.",
        "Europa nunca mais seria a mesma depois daqui.",
        "Livros de história me colocam no ápice do século XVIII.",
        "Povo parisiense tomou prisão símbolo do rei.",
        "Inconfidência Mineira entrou no calendário nacional brasileiro.",
        "França caminhou pra república depois deste estalo.",
        "Revolução atlântica ganhou rosto francês neste ano.",
    ],
    "1808": [
        "Família real portuguesa desembarcou no Rio.",
        "Dom João VI trouxe a corte pro trópico.",
        "Napoleão empurrou Bragança pro outro lado do oceano.",
        "Brasil virou sede do Império lusitano.",
        "Portos abriram às nações amigas na sequência.",
        "Colônia deixou de ser periferia e virou centro.",
        "Transferência da corte mudou economia e política aqui.",
        "Império português respirou do lado americano.",
        "Rio de Janeiro ganhou status de capital imperial.",
        "Abertura comercial veio logo depois desta mudança.",
        "História brasileira fala em virada com a chegada da corte.",
        "Monarquia europeia refugiou-se no Brasil nesta data.",
    ],
    "1822": [
        "Grito do Ipiranga entrou na lenda.",
        "Dom Pedro I proclamou independência de Portugal.",
        "Colônia virou Império independente.",
        "Dia do Fico antecedeu a ruptura final.",
        "Brasil deixou de ser vice-reino submisso.",
        "Bandeira verde-amarela ganhou sentido novo.",
        "Sete de setembro virou feriado por minha causa.",
        "Primeiro imperador brasileiro subiu ao trono nesta fase.",
        "Portugal perdeu colônia mais rica nas Américas.",
        "Independência brasileira fixou data neste calendário.",
        "Monarquia constitucional nasceu nas Américas aqui.",
        "Escola canta hino e cita meu nome todo ano.",
    ],
    "1824": [
        "Primeira Constituição do Império saiu do forno.",
        "Dom Pedro I outorgou carta magna imperial.",
        "Poder Moderador entrou no texto constitucional.",
        "Confederação do Equador eclodiu no Nordeste.",
        "Império ganhou regras escritas de jogo.",
        "Separatistas nordestinos desafiaram Rio e São Paulo.",
        "Constituição imperial durou décadas depois daqui.",
        "Brasil tentou fechar formato de Estado nesta data.",
        "Revolta pernambucana lembra este ano.",
        "Marco jurídico do Império fixou-se aqui.",
        "Parlamento imperial ganhou moldura legal.",
        "Historiador de direito sempre volta a mim.",
    ],
    "1865": [
        "Guerra Civil americana chegou ao fim.",
        "Lincoln morreu assassinado em Ford's Theatre.",
        "13ª Emenda aboliu escravidão nos EUA.",
        "Exército confederado se rendeu nesta fase.",
        "Reconstrução do Sul começou depois daqui.",
        "Guerra do Paraguai ainda sangrava o Cone Sul.",
        "Appomattox virou símbolo de rendição.",
        "EUA saíram unidos, mas arrasados, deste conflito.",
        "Século XIX americano fecha capítulo sangrento aqui.",
        "John Wilkes Booth entrou na história nesta data.",
        "Escravidão legal acabou na república do norte.",
        "Mapa americano ficou inteiro de novo.",
    ],
    "1870": [
        "Guerra Franco-Prussiana estourou.",
        "Bismarck empurrava unificação alemã.",
        "Segundo Império francês ruía.",
        "Sedeão e Metz caíram nas mãos prussianas.",
        "Guerra do Paraguai se aproximava do fim no Brasil.",
        "Napoleão III perdeu trono na sequência.",
        "Terceira República nasceria depois deste choque.",
        "Europa central redesenhou fronteiras daqui pra frente.",
        "Canhões alemães apontavam pra Paris.",
        "Prussia virou motor de Reich unificado.",
        "França viveu humilhação militar nesta década.",
        "Historiador europeu marca virada comigo.",
    ],
    "1888": [
        "Lei Áurea assinada por Isabel.",
        "Escravidão legal acabou no Império.",
        "Treze de maio virou data simbólica.",
        "Princesa Isabel ganhou apelido de redentora.",
        "Últimos escravizados foram libertos por lei.",
        "Império respirou alívio e crise ao mesmo tempo.",
        "Abolicionismo venceu no papel nesta data.",
        "Campo e senzala sentiram mudança imediata.",
        "Movimento negro e abolicionista comemorou.",
        "República viria logo depois deste gesto.",
        "Brasil tentou fechar ciclo escravista aqui.",
        "Escola fala em Golden Law ligada a mim.",
    ],
    "1889": [
        "República proclamada por Deodoro.",
        "Dom Pedro II deixou trono.",
        "Quinze de novembro virou feriado republicano.",
        "Monarquia imperial acabou no Brasil.",
        "Marechal virou primeiro presidente provisório.",
        "Bandeira republicana substituiu símbolos imperiais.",
        "Exército entrou na Praça da República.",
        "Velha ordem imperial não resistiu.",
        "Constituição republica viria depois.",
        "Brasil escolheu república presidencialista.",
        "Império virou capítulo encerrado.",
        "Cartaz de proclamação ainda ilustra livro escolar.",
    ],
    "1900": [
        "Paris sediou Jogos Olímpicos de Verão.",
        "Exposição Universal iluminou torre Eiffel.",
        "Calendário virou pra década que chamam de belle époque.",
        "Nietzsche morreu nesta data.",
        "Reino Unido ainda segurava Boer War.",
        "Mundo comemorou virada sem bug digital.",
        "Art nouveau decorou vitrines europeias.",
        "Freud publicava ideias que fariam barulho.",
        "Primeiro Nobel de literatura já existia quando cheguei.",
        "Aviação ainda era promessa de irmãos Wright.",
        "Século XX na cabeça popular começa perto de mim.",
        "Historiador ainda discute se pertenço ao XIX ou ao XX.",
    ],
    "1905": [
        "Einstein publicou artigos que viraram física moderna.",
        "Annus mirabilis da relatividade especial.",
        "Efeito fotoelétrico ganhou explicação nova.",
        "Patentes de Berna registraram ideias revolucionárias.",
        "Movimento browniano entrou na conta.",
        "Suíça abrigava jovem Einstein produtivo.",
        "Clássica mecânica Newtoniana sentiu rachadura.",
        "Prêmio Nobel viria depois destes textos.",
        "Universidade e revista científica falaram alto.",
        "Laboratório europeu debatia luz e matéria.",
        "Ciência do século XX ganhou ícone neste ano.",
        "Física deixou de ser só fórmula escolar.",
    ],
    "1912": [
        "Titanic afundou na viagem inaugural.",
        "Atlântico Norte engoliu navio supostamente inafundável.",
        "Southampton viu embarque trágico.",
        "Mais de mil vidas se perderam no gelo.",
        "Rádio Marconi transmitiu SOS da catástrofe.",
        "Classe e cor de bilhete decidiram sorte.",
        "Iceberg virou vilão de filme e documentário.",
        "White Star Line perdeu navio estrela.",
        "Regulamentação marítima mudou depois daqui.",
        "Hollywood ainda não tinha feito o blockbuster, mas o fato já era épico.",
        "Tragédia no mar marcou geração.",
        "Naufrágio entrou no vocabulário comum.",
    ],
    "1914": [
        "Grande Guerra estourou na Europa.",
        "Arquiduque Franz Ferdinand morreu em Sarajevo.",
        "Impérios entraram em choque continental.",
        "Trincheiras cortaram França e Bélgica.",
        "Primeira batalha do Marne segurou avanço alemão.",
        "Mundo inteiro foi arrastado pro conflito.",
        "Neutralidade acabou quando alianças puxaram todos.",
        "Soldado jovem foi pras trincheiras nesta data.",
        "Século XX ganhou trauma coletivo daqui.",
        "Revolução russa e tratados viriam depois.",
        "Guerra que mataria milhões começou aqui.",
        "Historiador chama de início da era curta do século XX.",
    ],
    "1917": [
        "Revolução Russa derrubou czar.",
        "Lenin e bolcheviques tomaram poder.",
        "EUA entraram na Primeira Guerra.",
        "Outubro no calendário juliano virou novembro no nosso.",
        "Império Romanov desmoronou.",
        "Greve Geral paralisou São Paulo.",
        "Tratado de Brest-Litovsk viria na sequência.",
        "Mundo viu primeira revolução socialista vitoriosa.",
        "Europa oriental mudou de dono.",
        "Fim da guerra ficou mais perto com entrada americana.",
        "Cartaz de Lenin apontando pra frente nasce desta fase.",
        "Brasil sentiu onda operária neste calendário.",
    ],
    "1918": [
        "Armistício de novembro silenciou canhões.",
        "Primeira Guerra Mundial terminou.",
        "Gripe espanhola matou milhões depois dos tiros.",
        "Império alemão entrou em colapso.",
        "Kaiser Wilhelm abdicou.",
        "Versailles viria no ano seguinte.",
        "Soldados voltaram pra casas destruídas.",
        "Mapa europeu seria redesenhado em conferência.",
        "Paz frágil nasceu das trincheiras.",
        "Brasil participou com Corpo Expedicionário.",
        "Mundo respirou alívio e medo de pandemia.",
        "Fim da guerra virou feriado em vários países.",
    ],
    "1922": [
        "Semana de Arte Moderna lotou teatro em São Paulo.",
        "Mário e Oswald de Andrade mexeram na cultura.",
        "União Soviética foi proclamada formalmente.",
        "Marcha sobre Roma levou Mussolini ao poder.",
        "Modernismo brasileiro ganhou rosto público.",
        "República Velha ainda respirava, mas arte já provocava.",
        "Europa viu fascismo subir escada.",
        "Rádio e imprensa espalharam manifesto modernista.",
        "Brasil deixou de imitar só Paris nos salões.",
        "Pau-Brasil e antropofagia germinaram daqui.",
        "História da arte brasileira marca fevereiro paulista.",
    ],
    "1929": [
        "Bolsa de Nova York desabou.",
        "Quinta-feira Negra entrou no vocabulário.",
        "Grande Depressão começou a morder.",
        "Café brasileiro sentiu preço despencar.",
        "Wall Street virou sinônimo de pânico.",
        "Bancos quebraram em cadeia.",
        "Mundo capitalista entrou em crise longa.",
        "Desemprego subiu nos EUA e na Europa.",
        "New Deal viria como resposta depois.",
        "Economia global lembra este estalo.",
        "Especuladores perderam fortuna da noite pro dia.",
        "Década seguinte seria de fila de sopa.",
    ],
    "1930": [
        "Getúlio Vargas subiu com Revolução.",
        "República Velha ruiu.",
        "Júlio Prestes ganhou eleição, mas não governou.",
        "Uruguai sediou e ganhou primeira Copa.",
        "Era Vargas começou a contar daqui.",
        "Exército e oligarcias perderam rota antiga.",
        "Constituição de 1934 viria depois.",
        "Brasil entrou em experimento autoritário longo.",
        "Política cafeeira perdeu hegemonia.",
        "Mundo ainda sentia crise de 29.",
        "Estado intervencionista ganhou força.",
        "Historiador brasileiro fala em 1930 como ruptura.",
    ],
    "1932": [
        "Paulistas levantaram Revolução Constitucionalista.",
        "Nove de Julho virou data em São Paulo.",
        "Vargas e Frente Negra enfrentaram tropas paulistas.",
        "Obelisco do Ibirapuera lembra este conflito.",
        "Constituição nova era o grito.",
        "Aviões bombardearam cidades paulistas.",
        "Brasil quase entrou em guerra civil.",
        "Bandeira de SP ganhou estrela extra depois.",
        "Martyrs da revolução viraram heróis locais.",
        "Acordo fechou revolta com anistia.",
        "Estado de São Paulo nunca esqueceu.",
        "Ferrovia e indústria paulista pagaram preço alto.",
    ],
    "1939": [
        "Alemanha invadiu Polônia.",
        "Segunda Guerra Mundial começou.",
        "Pacto Molotov-Ribbentrop precedeu invasão.",
        "França e Reino Unido declararam guerra.",
        "Blitzkrieg mostrou nova forma de combate.",
        "Europa entrou em noite longa.",
        "Holocausto ganhou terreno depois daqui.",
        "Neutralidade acabou no continente.",
        "Brasil ainda era neutral quando estourou.",
        "Mapa mundial virou tabuleiro de dois blocos.",
        "Churchill subiu ao palanque britânico.",
        "Historiador marca início do conflito global aqui.",
    ],
    "1942": [
        "Brasil entrou oficialmente na Segunda Guerra.",
        "Batalha de Stalingrado virou ponto de virada.",
        "Midway mudou jogo no Pacífico.",
        "Navios brasileiros torpedeados puxaram entrada.",
        "FEB seria formada depois desta decisão.",
        "Eixo e Aliados mediam forças em três frentes.",
        "Getúlio declarou guerra ao Eixo nesta data.",
        "Soldado brasileiro treinou pra Itália.",
        "Hollywood filmava propaganda.",
        "Racionamento e fila marcaram cidades.",
        "Mundo em chamas, mas virada aliada se desenhou.",
    ],
    "1945": [
        "Segunda Guerra terminou.",
        "Bombas atômicas caíram em Hiroshima e Nagasaki.",
        "ONU foi fundada.",
        "Hitler já estava morto; Alemanha se rendeu.",
        "Getúlio saiu do Estado Novo depois da pressão.",
        "Soldados voltaram pra reconstruir.",
        "Guerra Fria germinou nas conferências.",
        "Júri de Nuremberg viria depois.",
        "Brasil tinha FEB comemorando vitória.",
        "Mundo respirou fim de anos de inferno.",
        "Mapa da Ásia seria redesenhado.",
        "Paz nuclear nasceu assustada.",
    ],
    "1948": [
        "Israel declarou independência.",
        "ONU adotou Declaração Universal dos Direitos Humanos.",
        "Gandhi foi assassinado.",
        "Berlim ainda dividida em zonas.",
        "Guerra árabe-israelense estourou na sequência.",
        "Apartheid ganhou forma legal na África do Sul.",
        "Marshall Plan reconstruía Europa.",
        "Brasil ainda redigia constituinte.",
        "Rádio transmitiu notícia de novo estado.",
        "Oriente Médio entrou em ciclo longo de conflito.",
        "Direitos humanos ganharam texto global.",
        "Pós-guerra ainda reorganizava peças no tabuleiro.",
    ],
    "1950": [
        "Brasil sediou Copa e perdeu final no Maracanã.",
        "Maracanaço entrou na alma torcedora.",
        "Uruguai levantou taça no Rio.",
        "Guerra da Coreia começou.",
        "Ghadi ainda vivo quando cheguei.",
        "McCarthy perseguia comunistas nos EUA.",
        "Futebol brasileiro ganhou trauma coletivo.",
        "Estádio lotado viu virada uruguaia.",
        "Mundo bipolar se formava.",
        "Rádio narrou gol de Ghiggia.",
        "Copa no Brasil era promessa de título em casa.",
        "Seleção brasileira saiu chorando deste julho.",
    ],
    "1953": [
        "Hillary e Tenzing chegaram ao topo do Everest.",
        "Stalin morreu.",
        "Elizabeth II foi coroada.",
        "Guerra da Coreia entrou em armistício.",
        "DNA em double helix foi publicado.",
        "Montanhismo virou feito humano máximo.",
        "URSS entrou em fase pós-Stalin.",
        "Coroação britânica passou na TV.",
        "Everest deixou de ser invicto.",
        "Alpinistas voltaram heróis.",
        "Guerra Fria continuou, mas líder soviético mudou.",
        "Ciência e coroa dividiram manchetes.",
    ],
    "1957": [
        "Sputnik 1 orbitou a Terra.",
        "Corrida espacial decolou de verdade.",
        "EUA levaram susto tecnológico.",
        "Treaty of Rome criou embryo da UE.",
        "Little Rock virou símbolo de segregação escolar.",
        "Satélite bip bipou do espaço.",
        "Laika viria depois no mesmo programa.",
        "Khrushchev e Eisenhower mediam forças.",
        "Televisão mostrou céu diferente.",
        "Escola passou a falar em órbita.",
        "Era espacial nasceu com bipe soviético.",
        "Engenheiro soviético Korolev virou herói oculto.",
    ],
    "1958": [
        "Brasil ganhou primeira Copa.",
        "Pelé estreou em mundial e brilhou.",
        "Final foi contra anfitriã Suécia.",
        "De Gaulle voltou ao poder na França.",
        "NASA foi criada nos EUA.",
        "Futebol brasileiro virou exportação de alegria.",
        "Garotos suecos viram menino de 17 marcar.",
        "Taça Jules Rimet veio pro trópico.",
        "Seleção amarela entrou no mito.",
        "Copa na Europa terminou com samba.",
        "Brasil descobriu que podia ser hegemonia.",
        "Rádio brasileira explodiu com gol de Pelé.",
    ],
    "1960": [
        "Brasília foi inaugurada.",
        "JK transferiu capital pro Planalto.",
        "Rio deixou de ser capital federal.",
        "Niemeyer e Costa entregaram cidade nova.",
        "17 países africanos ficaram independentes.",
        "Kennedy e Nixon debateram na TV.",
        "Primeiro pouso humano no fundo do mar ocorreu nesta década.",
        "Modernismo brasileiro ganhou capital.",
        "Obras na savana viraram símbolo.",
        "Congresso em forma de bowl abriu.",
        "Brasil mostrou que podia construir cidade do zero.",
        "Mapa administrativo mudou comigo.",
    ],
    "1961": [
        "Gagarin orbitou a Terra.",
        "Primeiro humano no espaço veio da URSS.",
        "Muro de Berlim começou a subir.",
        "Jânio Quadros renunciou no Brasil.",
        "João XXIII abriu Vaticano II.",
        "Baía dos Porcos fracassou em Cuba.",
        "Corrida espacial virou vitrine ideológica.",
        "Berliners acordaram com arame.",
        "Brasil entrou em vice de Jango.",
        "Cold War quase esquentou demais.",
        "Capsula Vostok entrou na história.",
        "Mundo mediu altura do muro com medo.",
    ],
    "1962": [
        "Brasil bicampeão no Chile.",
        "Garrincha brilhou com Pelé machucado.",
        "Crise dos Mísseis levou mundo à beira nuclear.",
        "Argélia ficou independente.",
        "Beatles gravaram primeira fita demo.",
        "Final contra Tchecoslováquia consagrou seleção.",
        "Kennedy e Khrushchev mediram nukes em Cuba.",
        "Torcedor brasileiro comemorou no Andes.",
        "Guerra Fria quase virou quente.",
        "Alvinegro levantou taça de novo.",
        "Oswaldo Sampaio narrou gols na rádio.",
    ],
    "1963": [
        "Kennedy morreu em Dallas.",
        "Martin Luther King falou I Have a Dream.",
        "Marcha sobre Washington lotou mall.",
        "Valentina Tereshkova foi pro espaço.",
        "Pope John XXIII morreu; Paulo VI assumiu.",
        "Beatles estouraram na Grã-Bretanha.",
        "EUA choraram presidente jovem.",
        "Direitos civis ganharam voz forte.",
        "Zapruder filmou tragédia.",
        "Brasil ainda era democracia antes do golpe seguinte.",
        "Discurso no Lincoln Memorial entrou nos livros.",
    ],
    "1964": [
        "Golpe militar começou ditadura no Brasil.",
        "João Goulart foi deposto.",
        "AI-1 veio logo depois.",
        "Beatles invadiram EUA.",
        "Tonkin Gulf incident escalou Vietnã.",
        "Democracia brasileira sofreu ruptura.",
        "Generais assumiram Palácio.",
        "Marcha da Família apoiou golpe.",
        "Censura e tortura viriam na sequência.",
        "Jovem brasileiro viu tanque na rua.",
        "Guerra Fria justificou intervenção.",
        "21 anos de regime militar contaram daqui.",
    ],
    "1968": [
        "AI-5 apertou ditadura brasileira.",
        "MLK e Robert Kennedy assassinados.",
        "Protestos de maio tomaram Paris.",
        "Olimpíada no México teve massacre de Tlatelolco.",
        "Prague Spring foi esmagada.",
        "Tanks na rua viraram imagem global.",
        "Estudante levantou pedra e câmera.",
        "Woodstock e contracultura marcaram o ano.",
        "Brasil viveu repressão máxima.",
        "Mundo parecia pegar fogo.",
        "Ditadura fechou Congresso temporariamente.",
    ],
    "1969": [
        "Homem pisou na Lua.",
        "Apollo 11 levou Armstrong e Aldrin.",
        "Pequeno passo virou frase eterna.",
        "Woodstock reuniu meia geração.",
        "Charles Manson horrorizou Califórnia.",
        "Internet precursor ARPANET ligou primeiros nós.",
        "NASA cumpriu promessa de Kennedy.",
        "TV global transmitiu bandeira lunar.",
        "Beatles deram último show na laje.",
        "Guerra do Vietnã ainda sangrava.",
        "Corrida espacial teve vencedor americano.",
        "Lua deixou de ser só poema.",
    ],
    "1970": [
        "Brasil tricampeão no México.",
        "Pelé, Tostão e Rivelino levantaram taça.",
        "Final contra Itália virou clássico.",
        "Beatles anunciaram fim.",
        "Nixon invadiu Camboja.",
        "My Lai ainda ecoava.",
        "Seleção de 70 virou lenda.",
        "Gol de Carlos Alberto fechou título.",
        "Torcedor cantou com três estrelas.",
        "Copa colorida na TV mexicana.",
        "Futebol brasileiro atingiu pico artístico.",
        "Mundo viu futebol total verde-amarelo.",
    ],
    "1972": [
        "Watergate começou a vazar.",
        "Munique teve atentado olímpico.",
        "Pong estourou arcade.",
        "Pioneer 10 saiu pro Júpiter.",
        "Nixon visitou China.",
        "Bloody Sunday marcou Irlanda do Norte.",
        "Escândalo político americano nasceu aqui.",
        "Atletas israelenses foram sequestrados na vila.",
        "Videogame entrou em bar.",
        "Brasil ainda vivia ditadura.",
        "Jornalismo investigativo ganhou troféu.",
    ],
    "1975": [
        "Vietnã do Norte tomou Saigon.",
        "Guerra do Vietnã terminou.",
        "Microsoft nasceu em Albuquerque.",
        "Angola e Moçambique ficaram independentes.",
        "Franco morreu; Espanha transitou.",
        "Chile vivia Pinochet.",
        "Helicópteros evacuaram embarcador americano.",
        "Bill Gates e Paul Allen registraram empresa.",
        "Brasil ainda tinha AI-5 vigente.",
        "Sudeste asiático unificou sob comunismo no norte.",
        "Longo conflito americano fechou capítulo.",
        "Mapa africano ganhou novos nomes.",
    ],
    "1979": [
        "Thatcher virou primeira-ministra.",
        "Revolução Iraniana derrubou xá.",
        "URSS invadiu Afeganistão.",
        "Walkman da Sony estourou.",
        "Three Mile Island assustou com nuclear.",
        "Papa João Paulo II visitou Polônia.",
        "Margaret quebrou vidro britânico.",
        "Ayatollah Khomeini voltou de exílio.",
        "Disco morreu aos poucos enquanto punk rugia.",
        "Brasil vivia abertura lenta.",
        "Petrolão e islamismo mudaram Oriente Médio.",
    ],
    "1980": [
        "John Lennon morreu baleado em NY.",
        "Moscou sediou Olimpíada boicotada.",
        "Pac-Man virou febre.",
        "Reagan foi eleito nos EUA.",
        "Solidarity nasceu na Polônia.",
        "Irã e Iraque entraram em guerra.",
        "Beatles fan chorou na calçada Dakota.",
        "Atletas ocidentais faltaram em Moscou.",
        "Arcade ganhou fantasma amarelo.",
        "Brasil ainda digeria abertura.",
        "AIDS começou a ser identificada.",
    ],
    "1985": [
        "Ditadura militar fechou com eleição de Tancredo.",
        "Tancredo morreu; Sarney assumiu.",
        "Nova República nasceu.",
        "Gorbachev subiu na URSS.",
        "Live Aid lotou estádios contra fome.",
        "Brasil respirou redemocratização.",
        "Plano Cruzado viria depois.",
        "Civil voltou ao Planalto simbolicamente.",
        "21 anos de uniforme terminaram.",
        "Mundo assistiu show beneficente.",
        "Constituinte viria na sequência.",
        "Generais entregaram faixa.",
    ],
    "1986": [
        "Chernobyl explodiu.",
        "Challenger explodiu depois do lançamento.",
        "Argentina de Maradona ganhou Copa no México.",
        "Plano Cruzado tentou congelar preços.",
        "Gol de mão e gol do século saíram no mesmo jogo.",
        "Nuclear ucraniano contaminou Europa.",
        "Professora McAuliffe morreu na nave.",
        "Brasil torcia e sofria inflação.",
        "Fim do mundo pareceu perto duas vezes.",
        "Maradona virou deus e vilão.",
        "Televisão mostrou desastres ao vivo.",
    ],
    "1988": [
        "Constituição Cidadã promulgada.",
        "Ulysses Guimarães entregou texto.",
        "Constituinte fechou trabalho.",
        "Benazir Bhutto liderou Paquistão.",
        "Pan Am 103 explodiu sobre Lockerbie.",
        "Brasil ganhou lei magna nova.",
        "Direitos sociais ganharam capítulo.",
        "Redemocratização ganhou regra escrita.",
        "Carta de 88 ainda vale.",
        "Eleição direta presidencial viria depois.",
        "Congresso promulgou em outubro.",
    ],
    "1989": [
        "Muro de Berlim caiu.",
        "Alemanha caminhou pra reunificação.",
        "Tiananmen chocou China.",
        "Collor venceu eleição direta no Brasil.",
        "Velvet Revolution limpou Tchecoslováquia.",
        "Ceaușescu caiu na Romênia.",
        "Berliners picotaram concreto.",
        "Guerra Fria pareceu acabar.",
        "Internet ainda era acadêmica, mas mundo mudou.",
        "Brasil trocou presidente civilmente.",
        "Símbolo de divisão virou souvenir.",
        "Fim de década virou filme de montagem.",
    ],
    "1991": [
        "URSS dissolveu-se.",
        "Bandeira soviética desceu no Kremlin.",
        "Guerra do Golfo expulsou Iraque do Kuwait.",
        "WWW ficou pública.",
        "Yeltsin virou figura central.",
        "Mapa da Eurásia ganhou 15 repúblicas.",
        "Tank parado em Moscou virou ícone.",
        "Tim Berners-Lee abriu web ao mundo.",
        "Brasil ainda inflacionava.",
        "Fim da Guerra Fria ficou oficial.",
        "Scud e Patriot apareceram na TV.",
    ],
    "1992": [
        "Eco-92 reuniu planeta no Rio.",
        "Maastricht firmou União Europeia.",
        "Barcelona sediou Olimpíada.",
        "Bill Clinton venceu nos EUA.",
        "Rodney King verdict causou revolta.",
        "Sustentabilidade virou palavra de cúpula.",
        "Diplomacia ambiental lotou Riocentro.",
        "Euro viria depois do tratado.",
        "Dream Team de basquete brilhou.",
        "Brasil foi palco de cúpula verde.",
        "Agenda 21 saiu desta conferência.",
    ],
    "1994": [
        "Brasil tetra nos EUA.",
        "Romário e Bebeto fizeram dança.",
        "Plano Real estabilizou moeda.",
        "Mandela virou presidente na África do Sul.",
        "Final nos pênaltis contra Itália.",
        "Inflação brasileira arrefeceu.",
        "Copa nos EUA lotou estádios.",
        "Real nasceu como moeda confiável.",
        "Apartheid perdeu último líder branco.",
        "Torcedor colou o quarto estrela.",
        "Economia e bola comemoraram juntas.",
        "Fim de ano brasileiro foi festa dupla.",
    ],
    "1997": [
        "Pathfinder pousou em Marte.",
        "Hong Kong voltou pra China.",
        "Diana morreu em túnel parisiense.",
        "Filme Titanic estourou bilheteria.",
        "Ovelha Dolly mostrou clone viável.",
        "Harry Potter saiu no Reino Unido.",
        "Rover Sojourner mandou fotos de Marte.",
        "Handover britânico-chinês foi cerimônia global.",
        "Paparazzi perseguiram carro real.",
        "Celine Dion cantou trilha de navio.",
        "Ciência e tabloide dividiram manchetes.",
    ],
    "1998": [
        "França ganhou Copa em casa.",
        "Zidane marcou dois na final.",
        "Google nasceu em garagem.",
        "Brasil perdeu final pra franceses.",
        "Impeachment de Clinton avançou.",
        "Good Friday Agreement chegou na Irlanda.",
        "Apple apresentou iMac colorido.",
        "Euro foi anunciado pra 99.",
        "Ronaldo Fenômeno sofreu antes da final.",
        "Busca na web mudou de patamar.",
        "Chuva e Zidane frustraram Brasil.",
    ],
    "2000": [
        "Mundo comemorou virada do milênio.",
        "Sydney sediou Olimpíada.",
        "Bug do milênio assustou TI.",
        "Putin assumiu presidência russa.",
        "Eleição Bush vs Gore foi novela.",
        "Planeta fez festa em fusos diferentes.",
        "Real já segurava preço no Brasil.",
        "Torre de Sydney virou cartão postal olímpico.",
        "Y2K virou piada depois da meia-noite.",
        "Terror ainda não dominava manchete como depois.",
        "Calendário comum abriu século XXI.",
    ],
    "2001": [
        "Onze de setembro destruiu Torres Gêmeas.",
        "Wikipedia nasceu.",
        "iPod da Apple estreou.",
        "Guerra ao Terror ganhou impulso.",
        "Talibã ainda governava Afeganistão.",
        "Mundo viu fumaça em Manhattan.",
        "Segurança de aeroporto mudou pra sempre.",
        "Bush declarou guerra contra terror.",
        "Brasil acompanhou choque ao vivo na TV.",
        "Internet ganhou enciclopédia colaborativa.",
        "Música no bolso virou produto Apple.",
    ],
    "2002": [
        "Brasil pentacampeão na Coreia e Japão.",
        "Ronaldo Fenômeno artilheiro.",
        "Lula eleito presidente.",
        "Euro entrou em circulação em notas e moedas.",
        "Final contra Alemanha no Yokohama.",
        "Torcedor colou quinta estrela.",
        "Política brasileira virou página.",
        "Seleção amarela dominou Ásia.",
        "Campanha petista venceu no segundo turno.",
        "Mundo viu copa longe do eixo EU-Europa.",
        "Economia europeia unificou troco.",
    ],
    "2003": [
        "EUA invadiram Iraque.",
        "Columbia desintegrou na reentrada.",
        "Lula completava primeiro ano.",
        "SARS assustou Ásia.",
        "Concorde fez último voo.",
        "MySpace e Skype surgiram.",
        "Guerra no deserto voltou à TV.",
        "Astronautas morreram na reentrada.",
        "Brasil negociava aliança sul.",
        "Oriente Médio virou manchete diária.",
        "Protesto global contra guerra lotou ruas.",
    ],
    "2004": [
        "Tsunami no Índico matou centenas de milhares.",
        "Facebook nasceu em Harvard.",
        "Atenas sediou Olimpíada.",
        "Red social começou em dormitório.",
        "Ondas gigantes atingiram Aceh e Sri Lanka.",
        "Bush reeleito nos EUA.",
        "Brasil foi vice na Copa América.",
        "Google estreou na bolsa.",
        "Mundo se mobilizou com doações.",
        "Terremoto submarino gerou mar de lama.",
        "Rede social mudaria amizade digital.",
    ],
    "2007": [
        "Steve Jobs apresentou iPhone.",
        "Smartphone touch virou objeto de desejo.",
        "Crise subprime começou a rachar.",
        "Tratado de Lisboa foi assinado.",
        "Harry Potter fechou saga no cinema.",
        "Bolsa de valores brasileira subia.",
        "Apple mudou bolso e bolsa.",
        "Primeira geração iPhone saiu em junho.",
        "Mundo mobile nunca mais foi o mesmo.",
        "Subprime era sinal fraco ainda.",
        "UE reformou tratados.",
    ],
    "2008": [
        "Lehman quebrou e crise global estourou.",
        "Obama eleito primeiro presidente negro dos EUA.",
        "Pequim sediou Olimpíada espetacular.",
        "Bitcoin whitepaper circulou.",
        "Brasil ainda crescia enquanto mundo caía.",
        "Subprime virou recessão planetária.",
        "Hope poster colou na parede.",
        "Bird's Nest brilhou na abertura.",
        "Economia entrou em modo pânico.",
        "Banco central cortou juro no mundo todo.",
        "Crédito imobiliário virou palavrão.",
    ],
    "2010": [
        "Terremoto destruiu Haiti.",
        "Chile resgatou 33 mineiros.",
        "África do Sul sediou Copa.",
        "Instagram nasceu.",
        "Espanha ganhou primeira taça.",
        "iPad da Apple estreou.",
        "Mundo doou pro Haiti.",
        "Cápsula Fénix puxou mineiros.",
        "Vuvuzela encheu ouvido na África do Sul.",
        "Foto filtrada começou moda.",
        "Tablet voltou à moda.",
    ],
    "2011": [
        "Primavera Árabe tomou praças.",
        "Bin Laden morto em Abbottabad.",
        "Fukushima derretiu confiança nuclear.",
        "Steve Jobs morreu.",
        "Occupy Wall Street acampou.",
        "Dilma no segundo ano de mandato.",
        "Tahrir virou símbolo.",
        "Tsunami japonês veio antes da crise nuclear.",
        "Smartphone gravou revoltas.",
        "Mundo árabe trocou ditadores.",
        "Cartaz de protesto virou wallpaper.",
    ],
    "2012": [
        "Londres sediou Olimpíada.",
        "CERN anunciou bóson de Higgs.",
        "Calendário maia virou meme de fim do mundo.",
        "Obama reeleito.",
        "Curiosity pousou em Marte.",
        "Gangnam Style estourou YouTube.",
        "Atletas britânicos brilharam em casa.",
        "Partícula de Deus ganhou manchete.",
        "Profecia apocalíptica virou piada de 21 de dezembro.",
        "Rover mandou selfie marciano.",
        "Dilma completava segundo ano.",
    ],
    "2013": [
        "Jornadas de Junho lotaram Brasil.",
        "Papa Francisco eleito.",
        "Snowden vazou NSA.",
        "Mandela morreu.",
        "Boston Marathon sofreu atentado.",
        "Passagem livre virou grito nas ruas.",
        "Primeiro papa latino-americano saiu do conclave.",
        "Privacidade digital virou debate.",
        "Ícone anti-apartheid partiu.",
        "Protesto começou com vinte centavos.",
        "Guarda-chuva e spray marcaron fotos.",
    ],
    "2014": [
        "Brasil sediou Copa.",
        "Alemanha aplicou 7 a 1 na semifinal.",
        "Alemanha campeã no Maracanã.",
        "Rússia anexou Crimeia.",
        "ISIS declarou califado.",
        "Mineiraço entrou no trauma esportivo.",
        "Obra de estádio virou pauta.",
        "Neymar lesionado antes da semifinal.",
        "Geopolítica europeia rachou com Crimeia.",
        "Torcedor brasileiro calou no intervalo.",
        "Copa no Brasil terminou sem taça.",
    ],
    "2015": [
        "Acordo de Paris sobre clima fechado.",
        "Crise política e impeachment ganharam força no Brasil.",
        "New Horizons sobrevoou Plutão.",
        "Crise de refugiados na Europa.",
        "Marriage equality chegou nos EUA.",
        "Dilma enfrentou pedalada.",
        "Quase 200 países prometeram meta climática.",
        "Foto de Plutão encheu telas.",
        "Barco de refugiados virou símbolo.",
        "Suprema Corte americana liberou casamento igual.",
        "Manifestação verde e vermelha dividiu Brasil.",
    ],
    "2016": [
        "Rio sediou Olimpíada.",
        "Brasil ganhou ouro olímpico no futebol masculino.",
        "Brexit venceu referendo.",
        "Trump eleito nos EUA.",
        "Zika assustou grávidas.",
        "Abertura no Maracanã marcou verão.",
        "Reino Unido votou sair da UE.",
        "Polarização americana explodiu.",
        "Primeira Olimpíada na América do Sul.",
        "Medalha inédita no futebol olímpico.",
        "Vírus transmitido por mosquito dominou notícia.",
    ],
    "2017": [
        "Trump tomou posse.",
        "Me Too explodiu depois de Weinstein.",
        "Macron eleito na França.",
        "Brexit começou negociação formal.",
        "Eclipse solar cruzou EUA.",
        "Brasil ainda digeria pós-impeachment.",
        "Pink hat marchou em Washington.",
        "Jovem francês virou presidente.",
        "Artigo 50 foi acionado.",
        "Céu escureceu em faixa americana.",
        "Rede social virou tribunal moral.",
    ],
    "2018": [
        "França de Mbappé campeã na Rússia.",
        "Bolsonaro eleito no Brasil.",
        "Hawking morreu.",
        "Croácia chegou à primeira final.",
        "Incêndio no Museu Nacional no Rio.",
        "GDPR entrou na Europa.",
        "Brasil mudou rumo político na urna.",
        "Var do mundial estreou.",
        "Físico britânico deixou legado.",
        "Fogo consumiu acervo brasileiro.",
        "Privacidade digital ganhou lei europeia.",
    ],
    "2019": [
        "Notre-Dame pegou fogo.",
        "EHT fotografou buraco negro.",
        "Queimadas na Amazônia alarmaram.",
        "COVID ainda não era pandemia global.",
        "Brexit travava Westminster.",
        "Paris chorou catedral.",
        "Sombra de M87 virou poster científico.",
        "Fumaça amazônica apareceu de satélite.",
        "Vírus circulava, mas mundo ainda viajava normal.",
        "Greta Thunberg cruzou o Atlântico de veleiro.",
        "Hong Kong protestou extradição.",
    ],
    "2021": [
        "Vacina contra COVID aplicada em massa.",
        "Biden tomou posse.",
        "Olimpíada de Tóquio atrasada aconteceu.",
        "Talibã retomou Cabul.",
        "Ever Given encalhou no Suez.",
        "Capitol invadido em janeiro nos EUA.",
        "Agulha no braço virou esperança.",
        "Máscara ainda era rotina.",
        "Jogos sem público marcaram verão japonês.",
        "Afeganistão voltou ao Talibã.",
        "Navio encalhou e memes explodiram.",
    ],
    "2022": [
        "Rússia invadiu Ucrânia em larga escala.",
        "Argentina de Messi ganhou Copa no Catar.",
        "Lula eleito pro terceiro mandato.",
        "Musk fechou compra do Twitter.",
        "Rainha Elizabeth morreu.",
        "Inflação global subiu.",
        "Tanque russo cruzou fronteira.",
        "Final contra França consagrou albiceleste.",
        "Urna brasileira decidiu de novo.",
        "Rede social trocou dono.",
        "Trono britânico passou ao filho.",
    ],
    "2023": [
        "ChatGPT e IA generativa dominaram conversa.",
        "Conflito Israel-Hamas intensificou.",
        "Barbie e Oppenheimer lotaram cinema.",
        "Lula retomou Planalto no mandato.",
        "Titan submersível implodiu.",
        "Chatbot virou ferramenta de escritório.",
        "Oriente Médio entrou em crise nova.",
        "Bomba atômica voltou ao blockbuster.",
        "Brasil reassumiu papel em COP.",
        "Expedição turística ao Titanic falhou.",
        "Greve de roteiristas parou Hollywood.",
    ],
    "2024": [
        "Paris sediou Olimpíada de Verão.",
        "Trump venceu eleição americana de novo.",
        "IA seguiu mexendo mercado de trabalho.",
        "Brasil acompanhou COP e clima.",
        "Abertura no Sena virou show.",
        "Urna americana surpreendeu de novo.",
        "Modelo de linguagem entrou em planilha.",
        "Atletas nadaram no rio parisiense.",
        "Memória coletiva ainda guarda este calendário perto.",
        "Eleições municipais movimentaram Brasil.",
        "Solstício olímpico iluminou torre Eiffel.",
    ],
}


def roman(n: int) -> str:
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    out = []
    for v, sym in vals:
        while n >= v:
            out.append(sym)
            n -= v
    return "".join(out)


def is_leap(y: int) -> bool:
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


def century_pt(y: int) -> str:
    # 1500 -> século 16 (common for historical dating of 1500s)
    c = (y - 1) // 100 + 1
    names = {
        15: "XV", 16: "XVI", 17: "XVII", 18: "XVIII", 19: "XIX",
        20: "XX", 21: "XXI",
    }
    return names.get(c, str(c))


def millennium_pt(y: int) -> str:
    if y < 1000:
        return "primeiro milênio da era comum"
    if y < 2000:
        return "segundo milênio da era comum"
    return "terceiro milênio da era comum"


def digits(y: int) -> list[int]:
    return [int(c) for c in str(y)]


def numeric_clues(y: int, variant: int) -> list[str]:
    d = digits(y)
    s = sum(d)
    prod = 1
    for x in d:
        prod *= x
    uniq = len(set(d))
    mx, mn = max(d), min(d)
    mid_sum = d[1] + d[2] if len(d) == 4 else 0
    rom = roman(y)
    leap = is_leap(y)
    even = y % 2 == 0
    ends_zero = y % 10 == 0
    cent = century_pt(y)
    mil = millennium_pt(y)

    pools = {
        "parity_even": [
            "Divido certinho por dois.",
            "Na roda da mesa, sou par.",
            "Dois grupos iguais saem quando me repartem.",
            "Meu último algarismo garante paridade par.",
        ],
        "parity_odd": [
            "Sobra um se me dividirem por dois.",
            "Chutam ímpar quando olham meu fim.",
            "Não fecho par: sempre sobra um.",
            "Repito: por dois não fecha conta redonda.",
        ],
        "sum": [
            f"Some os quatro algarismos: fecha em {s}.",
            f"Soma dos dígitos me dá {s}.",
            f"Na prova de matemática, minha soma digit a digit é {s}.",
            f"Contador de calendário some meus números e acha {s}.",
        ],
        "roman": [
            f"Em romano escrevem {rom}.",
            f"Latim numérico me registra como {rom}.",
            f"Pedra antiga usaria {rom} pra me marcar.",
            f"No manual escolar apareço como {rom}.",
        ],
        "century": [
            f"História me guarda no século {cent}.",
            f"Professor de história me coloca no {cent}.",
            f"Linha do tempo me puxa pro século {cent}.",
            f"Atlas escolar me fileira no {cent}.",
        ],
        "leap_yes": [
            "Fevereiro me empresta um dia a mais.",
            "Sou bissexto: caio a cada quatro, salvo exceção de século.",
            "Calendário gregoriano me dá 29 de fevereiro.",
            "Ano de olimpíada de verão costuma ser meu tipo bissexto.",
        ],
        "leap_no": [
            "Meu fevereiro para no 28.",
            "Não sou bissexto no calendário atual.",
            "Fevereiro não me estica em 29.",
            "Quatro não me divide com aquela regra extra de século.",
        ] if not leap else [],
        "product": [
            f"Multiplique meus dígitos e chega a {prod}.",
            f"Produto dos algarismos fecha em {prod}.",
            f"Na mesa, quem multiplica os quatro números acha {prod}.",
            f"Regra de três brincadeira: dígitos vezes dígitos dá {prod}.",
        ],
        "ends_zero": [
            "Fecho com zero no fim.",
            "Meu último algarismo é zero.",
            "Termino em zero, redondo.",
        ],
        "ends_not_zero": [
            "Não termino em zero, mas ainda sou par." if even else "Meu último algarismo não é zero.",
            "Fim da fila não é zero.",
        ],
        "millennium": [
            f"Moro no {mil}.",
            f"Contagem longa me coloca no {mil}.",
            f"Cronologia cristã me situa no {mil}.",
        ],
        "uniq": [
            f"Repito pouco: só {uniq} algarismos diferentes.",
            f"Tenho {uniq} dígitos distintos na fila.",
            f"Variedade numérica: {uniq} símbolos diferentes.",
        ],
        "mid_sum": [
            f"O segundo e o terceiro dígito somam {mid_sum}.",
            f"Meio do meu número: {d[1]} mais {d[2]} dá {mid_sum}.",
            f"Centralizando algarismos, a soma do miolo é {mid_sum}.",
        ],
        "spread": [
            f"Maior algarismo menos o menor: {mx - mn}.",
            f"Distância entre meu dígito forte e o fraco: {mx - mn}.",
            f"Amplitude dos quatro números: {mx - mn}.",
        ],
    }

    pick = lambda key: pools[key][variant % len(pools[key])]

    out: list[str] = []
    out.append(pick("parity_even") if even else pick("parity_odd"))
    out.append(pick("sum"))
    out.append(pick("roman"))
    out.append(pick("leap_yes") if leap else pick("leap_no"))
    out.append(pick("century"))
    out.append(pick("product"))
    out.append(pick("uniq"))
    out.append(pick("mid_sum"))
    if ends_zero:
        out.append(pick("ends_zero"))
    elif even:
        out.append(pools["ends_not_zero"][variant % len(pools["ends_not_zero"])])
    else:
        out.append(pick("parity_odd"))
    out.append(pick("millennium"))
    out.append(pick("spread"))
    return out


def voice_event(text: str, slot: int) -> str:
    """Year speaks in first person without mangling the historical phrase."""
    markers = (
        " me ", " meu ", " minha ", " mim ", "Cheguei", "Moro", "Divido", "Some ",
        "Sou ", "Fui ", "Vi ", "Carrego", "Guardo", "Tenho", "Caio", "Vivo",
        "Repito", "Fecho", "Termino", "Chutam", "Neste meu", "Nesse meu",
        "Me citam", "Me lembro", "Conto que",
    )
    if any(m in text for m in markers):
        return text
    prefixes = (
        "Nesse meu giro, ",
        "Me citam porque ",
        "Na mesa lembram que ",
        "No livro escolar dizem que ",
        "Eu carrego o fato: ",
    )
    return prefixes[slot % len(prefixes)] + text


def compose(year: str, idx: int) -> list[str]:
    events = [voice_event(e, i) for i, e in enumerate(EVENTS[year])]
    variant = idx * 7 + int(year) % 11
    nums = numeric_clues(int(year), variant)

    # vague → specific: interleave events with light numeric hints
    clues: list[str] = []
    clues.append(events[0])
    clues.append(nums[0])
    clues.append(events[1])
    clues.append(nums[1])
    clues.append(events[2])
    clues.append(events[3])
    clues.append(events[4])
    clues.append(nums[2])
    clues.append(events[5])
    clues.append(nums[3])
    clues.append(events[6])
    clues.append(events[7])
    clues.append(nums[4])
    clues.append(events[8])
    clues.append(nums[5])
    clues.append(events[9])
    clues.append(nums[6])
    # replace last slots with sharper tail (skip meta summaries like "Ano par de...")
    concrete = [e for e in events if not e.startswith("Ano ")]
    tail_events = concrete[-2:] if len(concrete) >= 2 else events[-2:]
    tail_nums = nums[7:]
    clues[-1] = tail_nums[-1]
    clues[-2] = tail_events[-1]
    clues[-3] = tail_nums[-2] if len(tail_nums) >= 2 else nums[-2]
    clues[-4] = tail_events[-2]

    if len(clues) != 17:
        raise ValueError(f"{year}: expected 17 clues, got {len(clues)}")
    # no em dash
    for i, c in enumerate(clues):
        if "—" in c or "–" in c:
            raise ValueError(f"em dash in {year} clue {i}")
    return clues


def main() -> None:
    cards = []
    for i, ans in enumerate(ANSWERS):
        if ans not in EVENTS:
            raise KeyError(ans)
        cards.append({"answer": ans, "clues": compose(ans, i)})

    OUT.write_text(json.dumps(cards, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(cards)} cards to {OUT}")


if __name__ == "__main__":
    main()
