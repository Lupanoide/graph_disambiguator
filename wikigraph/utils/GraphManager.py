#! /usr/bin/python
# -*- coding: utf-8 -*-


from wikigraph.business.WikiBusiness import WikiBusiness
from wikigraph.business.GraphAnalisysBusiness import GraphBusiness
import requests
import ast


if __name__ == '__main__':

    #===========================================================================
    #splitted_phrase = "mi è scivolata la rivoltella , il cane ha premuto contro il suolo ed ha provocato la deflagrazione di un proiettile ".split()
    #splitted_phrase = "il ladro ha colpito il poliziotto con il cane della pistola".split()
    #splitted_phrase = " in araldica il cane è simbolo di fedeltà ".split()
    #splitted_phrase = " il python è un genere di grossi serpenti".split()
    #splitted_phrase = "ho dovuto portare il cane dal veterinario . Sospetto abbia la rabbia".split()
    #
    #splitted_phrase = "I dodici animali dello zodiaco cinese nell'ordine sono: Topo, Bue, Tigre, Coniglio, Dragone, Serpente, Cavallo, Capra, Scimmia, Gallo, Cane e Maiale.".split()
    #===========================================================================
    #### English
    #splitted_phrase = "Apollo killed Python in Delphi".split()
    #splitted_phrase = "I coded microservices in python for this app".split()
    splitted_phrase = "a python is eating a mouse".split()


    #resd = {'percosso': {}, 'pistola': {'Pistola': ['Rivoltella', 'Pistola semiautomatica', 'Pistola mitragliatrice', '.45 ACP', '1880', '1884', '1897', '1939', '9 mm Parabellum', 'Acciaio', 'Acciarino (arma da fuoco)', 'Archibugio', 'Arma', 'Arma automatica', 'Arma da fuoco', 'Armi ad aria compressa', 'Armi da fuoco portatili', 'Avancarica', 'Balistite', 'Beretta 93R', 'Beretta M9', 'Biblioteca Nazionale Centrale di Firenze', 'Biblioteca della Dieta nazionale del Giappone', 'Biblioth\xc3\xa8que nationale de France', 'Bossolo', 'Calibro', 'Calibro (arma)', 'Cane (armi)', 'Capsula a percussione', 'Carabina', 'Caricatore', 'Carrello (armi)', 'Cartuccia (munizione)', 'Casimir Lefaucheux', 'Clorato di potassio', 'Colt Government 1911', 'Colt M1911', 'Colt Navy', 'Colt Single Action Army', 'Combustione', 'Composto chimico', 'Cordite', 'Doppia azione', 'Enciclopedia Britannica', 'Energia cinetica', 'Etimologia', 'Fucile', 'Fucile a canna liscia', 'Fucile anticarro', "Fucile d'assalto", 'Fucile da battaglia', 'Fucile mitragliatore', 'Fucile semiautomatico', 'Fulminato di mercurio', 'Gemeinsame Normdatei', 'Georg Luger', 'Glock 18', 'Grilletto', 'Heckler & Koch', 'Heckler & Koch MK23', 'Hiram Maxim', 'John Moses Browning', 'Lanciagranate', 'Library of Congress Control Number', 'Lingua ceca', 'Lubrificazione', 'Luger P08', 'Manutenzione', 'Metal Gear (serie)', 'Mitra (arma)', 'Mitragliatrice', 'Mitragliatrice Maxim', 'Mitragliatrice ad uso generale', 'Mitragliatrice di squadra', 'Mitragliatrice leggera', 'Mitragliatrice media', 'Mitragliatrice pesante', 'Moschetto', 'Navy SEAL', 'Otturatore (armi)', 'Otturatore girevole-scorrevole', 'Pietra focaia', 'Pistoia', 'Pistola (moneta)', 'Pistola a ruota', 'Pistola automatica', 'Pistola ottica', 'Polizia', 'Polvere infume', 'Proiettili ad espansione', 'Retrocarica', 'Rinculo', 'SIG-Sauer P220', 'Samuel Colt', 'Semiautomatico', 'Singola azione', 'Smith & Wesson', 'Tamburo (rivoltella)', 'Toscana', 'Usura (metallurgia)', 'XIX secolo', 'XVIII secolo', 'XVII secolo', 'Solfuro di antimonio', 'Nitrocellulose', 'Hugo Borchardt', 'Peter Paul Mauser', 'Brochard 1896', 'Karl Walther', 'Matchlock', 'Wheellock', 'Terzetta', 'Smith & Wesson Model 39', 'Basculante'], 'Pistola (moneta)': ['1911', 'Africa', 'Alexandre Dumas (padre)', "Alfonso IV d'Este", 'Anni 1620', 'Anni 1720', 'Aquila bicipite', 'Arsenio Crespellani', 'Baiocco', 'Baviera', 'Besan\xc3\xa7on', 'Carlo III Filippo del Palatinato', 'Carlo III di Lorena', 'Carlo V', 'Carlo VII di Baviera', 'Casa Savoia', "Cesare d'Este", 'Croce di Gerusalemme', 'Croce di Malta', 'Danimarca', 'Doblone', 'Doppia', 'Ducato (moneta)', 'Duchi di Modena e Reggio', 'Edoardo Martinori', 'Elenco dei reggenti di Lorena', 'Enciclopedia Britannica', 'Escudo', 'Filippo II di Spagna', 'Fiorino', "Francesco I d'Este", 'Ghinea', 'Ginevra', 'Giovanna di Aragona e Castiglia', "Gran Maestri dell'Ordine di Malta", 'Guglielmo II di Scozia', 'IHS', 'ISBN', 'I tre moschettieri (romanzo)', 'Istituto italiano di numismatica', 'Lira genovese', 'Livre', 'Livre tournois', 'Luigi (moneta)', 'Luigi XIII di Francia', 'Malta', 'Manuel Pinto de Fonseca', 'Modena', 'Nancy', 'Notgeld', 'Palatinato', 'Prussia', 'Ribellione irlandese del 1641', 'Scozia', 'Scudo pontificio', 'Sou (moneta)', 'Tallero', 'XVIII secolo', 'XVII secolo', 'XVI secolo', '\xc3\x89cu', 'Darien Company', 'Inchiquin money', "Murrough O'Brien", 'Inchiquin', 'Herbert Grueber']}, 'delinquente': {'Delinquente': ['Abitualit\xc3\xa0', 'Anticriminologia', 'Assassino', 'Associazione per delinquere', 'Associazione per delinquere di tipo mafioso', 'Baby gang', 'Banda (criminalit\xc3\xa0)', 'Bande di motociclisti', 'Banditismo', 'Bandito sociale', 'Benigno Di Tullio', 'Biblioteca Nazionale Centrale di Firenze', 'Biblioth\xc3\xa8que nationale de France', 'Bossing', 'Brigantaggio', 'Bullismo', 'Buon costume', 'Colpevolizzazione della vittima', 'Comportamento del gregge', 'Condotta (diritto)', 'Contrabbando', 'Criminalistica', 'Criminalit\xc3\xa0', 'Criminalit\xc3\xa0 organizzata', 'Criminalizzazione', 'Crimine', 'Crimine informatico', 'Criminofobia', 'Criminologia', 'Criminologia applicata', 'Criminologia costitutiva', 'Criminologia critica', 'Delinquente professionale', 'Delinquenza', 'Delinquenza minorile', 'Delitto', 'Devianza (sociologia)', 'Difesa sociale', 'Diritto penale italiano', 'Disturbo della condotta', 'Droga', 'Falsario', 'Furto', 'Gangster', 'Gemeinsame Normdatei', 'Ijime', 'Ladro', 'Legge', 'Mafia', 'Microcriminalit\xc3\xa0', 'Mobbing', 'Mobster', 'Nonnismo', 'Patrimonio', 'Pedofilia', 'Pericolosit\xc3\xa0 sociale', 'Persona fisica', 'Persona scomparsa', 'Propriet\xc3\xa0 (diritto)', 'Psicopatia', 'Psicopatologia', 'Rapina', 'Razza e criminalit\xc3\xa0', 'Reato', 'Recidiva', 'Reo', 'Serial killer', "Sicurezza urbana e dell'ambiente", 'Spree killer', 'Stalking', 'Storia della criminologia', 'Tecniche di neutralizzazione', 'Teoria della scelta razionale (criminologia)', 'Teoria delle finestre rotte', 'Teppismo', 'Terrorismo', 'Truffa', 'Vandalismo', 'Vittimologia', 'Delinquente per tendenza'], 'Delinquente (singolo)': ['1969 (album Achille Lauro)', '1969 (singolo Achille Lauro)', '1990 (Achille Lauro)', 'Achille Idol immortale', 'Achille Lauro (rapper)', 'Album in studio', 'Amm\xc3\xb2', 'Amore mi', 'Angelo blu (Achille Lauro)', "C'est la vie (Achille Lauro)", 'Carillon (Nahaze e Achille Lauro)', "Dio c'\xc3\xa8 (album)", 'Etichetta discografica', 'Featuring', 'Genere musicale', 'Italia', 'Mamacita', 'Me ne frego (singolo)', 'Midnight Carnival', 'Non sei come me', "Pour l'amour", 'Produttore discografico', 'Punk rock', 'Ragazza di periferia 2.0', 'Ragazzi madre', 'Rapper', 'Rolls Royce (singolo)', 'Singolo (musica)', 'Sky TG 24', 'Sony Music', 'Thoiry Remix', 'Ulalala', 'YouTube', 'Young Crazy EP', 'Barabba (Achille Lauro)', 'Harvard (Achille Lauro)', 'Il mio D.J.']}, 'il': {'IL': ['.il', 'Articolo (grammatica)', 'Austria', 'Biologia', 'Cananei', 'Codice vettore IATA', 'Distretto di Ialomi\xc8\x9ba', 'Dominio di primo livello', 'IL (rivista)', 'IL - Vocabolario della lingua latina', 'ISO 3166-1 alpha-2', 'Ialoveni', 'Il (divinit\xc3\xa0)', 'Il Sole 24 ORE', 'Illinois', 'Ilyushin', 'Innsbruck-Land', 'Interleuchina', 'Israele', 'Lingua italiana', 'Moldavia', 'Romania', 'Sigla automobilistica internazionale', "Stati Uniti d'America", "Targhe d'immatricolazione austriache", 'Lankair', 'Instruction list', 'EC 61131-3', 'IL (casa discografica)']}, 'della': {}, 'ha': {'Ha (kana)': ['A (kana)', 'Chi (kana)', 'Ch\xc5\x8don', 'Dakuten', 'E (kana)', 'Fu (kana)', 'Handakuten', 'He (kana)', 'Hi (kana)', 'Hiragana', 'Ho (kana)', 'I (kana)', 'Ka (kana)', 'Kana', 'Katakana', 'Ke (kana)', 'Ki (kana)', 'Ko (kana)', 'Ku (kana)', 'Ma (kana)', 'Me (kana)', 'Mi (kana)', 'Mo (kana)', 'Mora (fonologia)', 'Mu (kana)', 'N (kana)', 'Na (kana)', 'Ne (kana)', 'Ni (kana)', 'No (kana)', 'Nu (kana)', 'O (kana)', 'Ra (kana)', 'Re (kana)', 'Ri (kana)', 'Ro (kana)', 'Ru (kana)', 'R\xc5\x8dmaji', 'Sa (kana)', 'Se (kana)', 'Shi (kana)', 'Sistema Hepburn', 'Sistema Kunrei', 'So (kana)', 'Sokuon', 'Su (kana)', 'Ta (kana)', 'Te (kana)', 'To (kana)', 'Traslitterazione', 'Tsu (kana)', 'U (kana)', 'Unicode', 'Wa (kana)', 'We (kana)', 'Wi (kana)', 'Wo (kana)', 'Ya (kana)', 'Yo (kana)', 'Yu (kana)', 'Goj\xc5\xabon'], 'HA': ['Acido ialuronico', 'Africa orientale', 'Albania', 'Alfabeto cirillico', 'Ampere', 'Antico Egitto', 'Austria', 'Bhutan', 'Cluster HA', 'Codice vettore IATA', 'Comuni della Norvegia', 'Creta', 'Distretto di Haifa', 'Distretto di Has', 'Dubnio', 'Etiopia', 'Ettaro', 'Etto', 'FIPS 10-4', 'Germania', 'Gola di Ha', 'Grecia', 'Ha (Bhutan)', 'Hagen', 'Hahnio', 'Haiti', 'Hallein', 'Harare', 'Harari', 'Hardap', 'Hawaiian Airlines', 'H\xc3\xa5', 'H\xc4\x81\xca\xbe', 'ISO 639-2', 'ISO 639-3', 'Ilia', 'Informatica', 'Israele', 'Lingua hausa', 'Namibia', 'Rogaland', 'Simbolo chimico', "Targhe d'immatricolazione austriache", "Targhe d'immatricolazione greche", "Targhe d'immatricolazione tedesche", 'Zimbabwe', '\xd0\xa5', '\xe1\xb8\xa4\xc4\x81\xca\xbe', '\xe1\xb8\xaa\xc4\x81\xca\xbe', 'Ha (divinit\xc3\xa0)', 'Ha (popolo)', 'Lingua ha'], 'Ha (Bhutan)': ['Altitudine', 'Bhutan', 'Coordinate geografiche', 'Distretti del Bhutan', 'Distretto di Haa', 'Fuso orario', 'Livello del mare', 'Metro', 'Popolazione', 'Stato', 'UTC+6'], 'Ha (mitologia)': ['Aaru', 'Abeshimiduat', 'Ahmose Nefertari', 'Aker', 'Akh (mitologia)', 'Am-eh', 'Amenhotep (figlio di Hapu)', 'Amenofi I', 'Amon', 'Amon-Ra', 'Amonet', 'Anat', 'Anditi', "Anima nella religione dell'antico Egitto", 'Animali sacri delle divinit\xc3\xa0 egizie', 'Ankh', 'Anput', 'Anti (divinit\xc3\xa0)', 'Antico Egitto', 'Antinoo', 'Anubi', 'Anuqet', 'Api (mitologia egizia)', 'Apopi', 'Aqen', 'Arensnuphis', 'Arpocrate', 'Ash (mitologia)', 'Astarte', 'Aton', 'Atum', 'Ba-Pef', 'Babi (mitologia egizia)', 'Banebdjedet', 'Barca di Amon', 'Barca sacra', 'Barca solare (Egitto)', 'Barca solare di Cheope', 'Bastet', 'Bat (mitologia)', 'Bata (mitologia egizia)', 'Benu', 'Bes (divinit\xc3\xa0)', 'Buchis', 'Caos (mitologia egizia)', 'Ded\xc3\xb9n', 'Denuen', 'Deserto Libico-Nubiano', 'Disco solare alato egizio', "Divinit\xc3\xa0 dei cancelli dell'oltretomba", "Divinit\xc3\xa0 delle caverne dell'oltretomba", 'Divinit\xc3\xa0 egizia', 'Djed', 'Duamutef', 'Duat', 'Enneade', 'Fetket', 'Figli di Horus', 'Flabello egizio', 'Geb', 'Gebka', "Geografia dell'antico Egitto", 'Geroglifici egizi', 'Giove (astronomia)', 'Giudici di Maat', 'Grande gatto di Eliopoli', 'Hagryphus giganteus', 'Hapi', 'Harmakis', 'Haroeris', 'Harsiesi', 'Hathor', 'Hatmehit', 'Hededet', 'Hehu', 'Heka (mitologia)', 'Hekaib', 'Heket', 'Hemsut', 'Hershef', 'Hesat', 'Horakhti', 'Hordesher', 'Horkapet', 'Horuepeshtaui', 'Horus', 'Hu (mitologia)', 'Huh (mitologia)', 'Huhet', 'Iah', 'Igai', 'Ihi (divinit\xc3\xa0)', 'Imentet', 'Imhotep', 'Imset', 'Inno al Nilo', 'Inno al Sole', 'Ipetueretemkhetnut', 'Iside', 'Iusaas', 'Kebechet', 'Keket', 'Khensit', 'Khentamentyu', 'Khepri', 'Kherti', 'Khnum', 'Khonsu', 'Kuk (mitologia)', 'Libri di Thot', 'Libro dei morti', 'Libro del respirare', 'Lindsay Zanno', 'Loto egizio', 'Maahes', 'Maat', 'Maledizione di Tutankhamon', 'Marte (astronomia)', 'Mehen', 'Mehetueret', 'Menhit', 'Mercurio (astronomia)', 'Meret (divinit\xc3\xa0)', 'Mertseger', 'Meskhenet', 'Miket', 'Min (mitologia)', 'Miti di nascite divine nelle dinastie egizie', 'Mito di Iside e Osiride', 'Mnevis', 'Montu', 'Mut', 'Nefertum', 'Nefti', 'Neith', 'Nekhbet', 'Nepri', 'Netjerduai', 'Nodo di Iside', 'Nomo (Egitto)', 'Nun (mitologia)', 'Nunet', 'Nut (mitologia)', 'Oasi', 'Occhio di Horus', 'Ogdoade', 'Oltretomba', 'Onuris', 'Oracolo di Amon', 'Ore (mitologia egizia)', 'Osiride', 'Pakhet', 'Pateco', 'Popoli del mare', 'Ptah', 'Ptah-Seker-Osiride', 'Qadesh (dea)', 'Qebehsenuf', 'Qebui', 'Qed-her', 'Ra', 'Ra-Horakhti', 'Rattaui', 'Religione egizia', 'Renenet', 'Renpet', 'Richard Wilkinson (egittologo)', 'Sameref', 'Satet', 'Saturno (astronomia)', 'Scarabeo (amuleto)', 'Scettri egizi', 'Scott Sampson', 'Sebeg', 'Sefegiru', 'Sekhmet', 'Selkis', 'Serapide', 'Seshat', 'Seth', 'Shai', 'Shed (mitologia)', 'Shen (magia egizia)', 'Shesmetet', 'Shesmu', 'Shu (divinit\xc3\xa0)', 'Sia (mitologia)', 'Simbolo', 'Sobek', 'Sokar', 'Sopdu', 'Sopedet', 'Tait', 'Tatenen', 'Tefnut', 'Tenenet', 'Testi di esecrazione', 'Thot', 'Triade egizia', 'Tueret', 'Tutu (mitologia egizia)', 'Uadjet', 'Uadjuer', 'Ueneg (mitologia)', 'Uepset', 'Uerethekau', 'Ueru', 'Unut', 'Uosret', 'Upuaut', 'Ureo', 'Ushabti', 'Utah', 'Venere (astronomia)']}, 'cane': {'Canis lupus familiaris': ['Neotenia', 'Addomesticamento del cane', 'Razze canine', 'Rinario', 'Intelligenza dei cani', 'Carne di cane', '1758', '2001', 'Acondroplasia', 'Addestramento', 'Addomesticamento', 'Africa occidentale', 'Alano', 'Allevamento', 'America', 'Animalia', 'Apparato riproduttore maschile canino', 'Apprendimento', 'Arabidopsis thaliana', 'Arbacia punctulata', 'Archive.is', 'Ardenne', 'Aria', 'Asia', 'Asia orientale', 'Aspergillus nidulans', 'Bacillus subtilis', 'Barbone (cane)', 'Basenji', 'Bassotto', 'Beagle (cane)', 'Beagle (razza canina)', 'Biblioteca Nazionale Centrale di Firenze', 'Biblioteca della Dieta nazionale del Giappone', 'Biblioth\xc3\xa8que nationale de France', 'Bichon Fris\xc3\xa9', 'Bloodhound', 'Bocca', 'Boxer (cane)', 'Bracco Italiano', 'Bracco italiano', 'Brachicefalia', 'Brachypodium distachyon', 'Bulldog', 'Cacao', 'Caccia', 'Caccia e raccolta', 'Caenorhabditis elegans', 'Cane (disambigua)', 'Cane da caccia', 'Cane da ferma', 'Cane da pastore', 'Cane da pastore tedesco', 'Cane da punta', 'Cane da riporto', 'Cane da sangue', 'Cane da seguita', 'Cane da traccia', 'Cane dei faraoni', 'Cane di San Bernardo', 'Cane di Terranova', 'Cane lupo cecoslovacco', 'Cane lupo di Saarloos', 'Cane primitivo', 'Cani da compagnia', 'Cani da guardia', 'Cani da montagna', 'Cani pariah', 'Canidae', 'Caniformia', 'Caninae', 'Canis', 'Canis lupus', 'Carcinoma del colon-retto', 'Carlino (cane)', 'Carnivora', 'Cavalier King Charles Spaniel', 'Cavia porcellus', 'Cervello', 'Chihuahua (cane)', 'Chihuahua (razza canina)', 'Chlamydomonas reinhardtii', 'Chordata', 'Chow Chow', 'Ciclo estrale', 'Cina', 'Cinometro', 'Cioccolato', 'Ciona intestinalis', 'Civilt\xc3\xa0 occidentale', 'Civilt\xc3\xa0 romana', 'Classe (tassonomia)', 'Classificazione scientifica', 'Clicker training', 'Cocker', 'Coda (anatomia)', 'Coevoluzione', 'Collie', 'Controilluminazione', 'Coping', 'Corea', 'Corteccia visiva', 'Cuccia', 'Cultura natufiana', 'DNA mitocondriale', 'Dalmata (cane)', 'Danio rerio', 'Dente', 'Deuterostomia', 'Diafanizzazione', 'Dictyostelium discoideum', 'Dieta BARF', 'Digital object identifier', 'Dizionario storico della Svizzera', 'Dmitrij Beljaev', 'Dogo argentino', 'Dolicocefalia', 'Dominio (biologia)', 'Dorado (Porto Rico)', 'Doryteuthis pealeii', 'Drosophila melanogaster', 'Eberhard Trumler', 'Educatore cinofilo', 'Enciclopedia Britannica', 'Enciclopedia canadese', 'Epagneul Breton', 'Escherichia coli', 'Esplosivi', 'Etologia', 'Eukaryota', 'Eumetazoa', 'Euprymna scolopes', 'Europa', 'Evaporazione', 'Fago lambda', 'Famiglia (tassonomia)', 'Finlandia', 'Fossili', 'Fox Terrier', 'Francia', 'Fungi', 'GUT', 'Gemeinsame Normdatei', 'Genere (tassonomia)', 'Gestazione', 'Ghiandola sudoripara', 'Gnathostomata', 'Golden Retriever', 'Golden retriever', 'Gravettiano', 'Groenlandese (cane)', 'Grotta di Chauvet', 'Guinzaglio', 'Homo sapiens', 'Hydra (zoologia)', 'ISBN', 'ISSN', 'Infraclasse', 'Infraphylum', 'Internet Archive', 'Invertebrata', 'Israele', 'Istituto Treccani', 'Konrad Lorenz', "L'anello di Re Salomone", 'Labrador Retriever', 'Largo (Florida)', 'Lavoro (economia)', 'Levrieri', 'Levriero', 'Levriero irlandese', 'Library of Congress Control Number', 'Lingua greca', 'Lingua latina', 'Lingua sanscrita', 'Lingua vedica', 'Linneo', 'Lista delle razze canine pericolose', 'Lista di razze canine', 'Londra', 'Lotus japonicus', 'Lupo grigio', 'Lupo italiano', 'Mammalia', 'Mammifero', 'Mammut', 'Mastiff', 'Mastino', 'Mastino napoletano', 'Mastino tibetano', 'Medicago truncatula', 'Molosso (cane)', 'Molossoidi', 'Monti Altaj', 'Mus musculus', 'Museruola', 'Mycoplasma genitalium', 'Natufiano', 'Neurospora crassa', 'New Iberia', 'Nicotiana tabacum', 'Nomadi', 'Nomenclatura trinomiale', 'Occhio', 'Oceania', 'Olfatto', 'Online Computer Library Center', 'Onnivoro', 'Ordine (tassonomia)', 'Organismo modello', 'Oryza glaberrima', 'Oryza sativa', 'Oryzias latipes', 'Otsego (Michigan)', 'PMID', 'Paleontologia', 'Paracentrotus lividus', 'Passo dello Stelvio', 'Pastore belga', 'Pechinese', 'Peter Ronald Messent', 'Phylum', 'Pinscher', 'Placentalia', 'Plantae', 'Pointer', 'Pomodoro', 'Predatori', 'Preistoria', 'Prokaryota', 'Protista', 'Pseudomonas fluorescens', 'Psicologia', 'Rattus norvegicus', 'Razza', 'Regno (biologia)', 'Retriever', 'Revisione paritaria', 'Rottweiler', 'Saccharomyces cerevisiae', 'Samoiedo', 'Schizosaccharomyces pombe', 'Schnauzer (variet\xc3\xa0)', 'Science', 'Segugio', 'Segugio italiano a pelo raso', 'Selezione artificiale', 'Setter', 'Siberia', 'Siberian Husky', 'Solanacee', 'Solanina', 'Sottofamiglia', 'Sottordine', 'Sottoregno', 'Sottospecie', 'Specie', 'Spitz (razza canina)', 'Sport cinofili', 'Stato di conservazione (biologia)', 'Stupefacenti', 'Subphylum', 'Sud-est asiatico', 'Superclasse (tassonomia)', 'Superphylum', 'Sus scrofa domesticus', 'Synechocystis', 'TPLO', 'Tab\xc3\xb9', 'Takifugu rubripes', 'Tassa sul cane', 'Teobromina', 'Terranova (cane)', 'Terrier', 'Testa', 'Tetrahymena', 'Tetrapoda', 'Topo', 'Tribolium castaneum', 'Umidit\xc3\xa0', 'Universit\xc3\xa0 di Turku', 'Vertebrata', 'Vibrio fischeri', 'Vibrissa', 'Vietnam', 'Virus (biologia)', 'Volpino italiano', 'V\xc3\xa4stg\xc3\xb6taspets', 'Xenopus laevis', 'Zea mays', 'Mesaticefalia', 'Caverna di Goyet', 'Ein Mallaha', 'Cani da presa', 'Cane da pista', 'Cane da tana', 'Caccia in tana', 'Stanley Coren', 'Universit\xc3\xa0 di Kyushu'], 'Cane (Honduras)': ['1867', 'Aguanqueterique', 'Altitudine', 'Area', 'Caba\xc3\xb1as (La Paz)', 'Chilometro quadrato', 'Chinacla', "Comuni dell'Honduras", 'Coordinate geografiche', 'Densit\xc3\xa0 di popolazione', "Dipartimenti dell'Honduras", 'Dipartimento di La Paz (Honduras)', 'Fuso orario', 'Guajiquiro', 'Honduras', 'La Paz (Honduras)', 'Lauterique', 'Livello del mare', 'Marcala', 'Mercedes de Oriente', 'Metro', 'Opatoro', 'Popolazione', 'San Antonio del Norte', 'San Jos\xc3\xa9 (La Paz)', 'San Juan (La Paz)', 'San Pedro de Tutule', 'Santa Ana (La Paz)', 'Santa Elena (Honduras)', 'Santa Mar\xc3\xada (Honduras)', 'Santiago de Puringla', 'Stato', 'UTC-6', 'Virtual International Authority File', 'WorldCat', 'Yarula'], 'Cane (armi)': ['Acciaio', 'Acciarino (arma da fuoco)', 'Alluminio', 'Arma da fuoco', 'Armi', 'Armi da fuoco', 'Azione doppia', 'Azione singola', 'Caccia', 'Calcio (armi)', 'Canna (armi)', 'Capsula a percussione', 'Cartuccia (munizione)', 'Cassa (armi)', "Colt's Manufacturing Company", 'Colt Navy', 'Deflagrazione', 'Detonazione', 'Doppia azione', 'Grilletto', 'Percussore', 'Pietra focaia', 'Pirite', 'Pistola', 'Rinculo', 'Rivoltella', 'Slang', 'Tamburo', 'Tiro dinamico', 'Titanio', 'Velo-dog', 'West', 'Colt Dragoon', 'Beretta mod. 21a', 'Smith & Wesson Bodyguard'], 'Cane (araldica)': ['Abete (araldica)', 'Agnello (araldica)', 'Agnello pasquale (araldica)', 'Airone (araldica)', 'Alabarda (araldica)', 'Albero (araldica)', 'Alerione', 'Anatrella', 'Anfesibena', 'Angelo (araldica)', 'Angioletto', 'Anguilla (araldica)', 'Animali araldici', 'Ape (araldica)', 'Aquila (araldica)', 'Araldica', 'Aringa (araldica)', 'Arpia (araldica)', "Ascia d'armi (araldica)", 'Asino (araldica)', 'Avellane', 'Barbo (araldica)', 'Basilisco (mitologia)', 'Bastone (araldica)', 'Bastone noderoso', 'Biscia (araldica)', 'Biscione (araldica)', 'Bove (araldica)', 'Castagno (araldica)', 'Castello (araldica)', 'Castoro (araldica)', 'Catena (araldica)', 'Cavallo (araldica)', 'Cedro (araldica)', 'Centauro', 'Cerbero', 'Cervo (araldica)', 'Cherubino (araldica)', 'Chiave (araldica)', 'Chollima', 'Cicogna (araldica)', 'Cigno (araldica)', 'Cincia (araldica)', 'Cinghiale (araldica)', 'Civetta (araldica)', 'Coccodrillo (araldica)', 'Colomba (araldica)', 'Cometa (araldica)', 'Conchiglia (araldica)', 'Conchiglia di Santiago', 'Coniglio (araldica)', 'Corona (araldica)', "Corona all'antica", 'Corvo (araldica)', 'Creatura leggendaria', 'Cremlino (araldica)', 'Cupido', 'Delfino (araldica)', 'Dolce (araldica)', 'Donnola (araldica)', 'Drago (araldica)', 'Elefante (araldica)', 'Falcone (araldica)', 'Fenice (araldica)', 'Figura araldica', 'Figura artificiale', 'Figura chimerica', 'Figura naturale', 'Frassino (araldica)', 'Gallo (araldica)', 'Gambero (araldica)', 'Gelso (araldica)', 'Gerione (araldica)', 'Giglio (araldica)', 'Giglio dal pi\xc3\xa8 nodrito', 'Giglio di Firenze', 'Giglio di giardino', 'Grifone (araldica)', 'Gru (araldica)', 'ISBN', 'Idra (araldica)', 'Ippocampo (araldica)', 'Leoncino (araldica)', 'Leone (araldica)', 'Leone di Giuda', 'Levriere', 'Lindworm', 'Luigi Volpicella', 'Luna (araldica)', 'Lupo (araldica)', 'Marzocco', 'Mazzapicchio (araldica)', 'Merla (araldica)', 'Mosca (araldica)', 'Oca (araldica)', 'Orso (araldica)', 'Pantera (araldica)', 'Pecora (araldica)', 'Pegaso (araldica)', 'Piante araldiche', 'Rosa (araldica)', 'Salamandra (araldica)', 'Salmone (araldica)', 'Scimitarra (araldica)', 'Scure (araldica)', 'Serafino', 'Servizio bibliotecario nazionale', 'Sirena (araldica)', 'Sole (araldica)', 'Spada (araldica)', 'Spiga di grano', 'Stella (araldica)', 'Struzzo (araldica)', 'Toro (araldica)', 'Tortora (araldica)', 'Unicorno', 'Vacca (araldica)', 'Volpe (araldica)'], 'Cane (zodiaco cinese)': ['1910', '1922', '1934', '1946', '1958', '1970', '1982', '1994', '2006', '2018', 'Acqua (elemento)', 'Argentina', 'Astrologia cinese', 'Australia', 'Bilancia (astrologia)', 'Bufalo (zodiaco cinese)', 'Canada', 'Capra (zodiaco cinese)', 'Cavallo (zodiaco cinese)', 'Coniglio (zodiaco cinese)', 'Diamante', 'Drago (zodiaco cinese)', 'Etiopia', 'Fuoco (elemento)', 'Gallo (zodiaco cinese)', 'Irlanda', 'Legno (elemento)', 'Maiale (zodiaco cinese)', 'Metallo (elemento)', 'Nuova Zelanda', 'Scimmia (zodiaco cinese)', 'Serpente (zodiaco cinese)', 'Terra (elemento)', 'Tigre (zodiaco cinese)', 'Topo (zodiaco cinese)', 'Wu Xing', 'Yang']}, 'poliziotto': {'Polizia': ['Polizia locale', 'Autorit\xc3\xa0 di pubblica sicurezza', 'Polizia di prossimit\xc3\xa0', 'Polizia amministrativa', 'Polizia giudiziaria', 'Australian Federal Police', 'Forze di polizia brasiliane', 'J\xc7\x90ngch\xc3\xa1', 'Polizia armata del popolo', 'Bundeskriminalamt (Germania)', 'Forze di polizia in Germania', 'Landespolizei (Germania)', 'Police nationale', 'Gendarmerie nationale', 'Forze di polizia italiane', 'Landespolizei (Liechtenstein)', 'Polizia del Regno Unito', 'Forze di polizia in Polonia', 'Policija (Russia)', 'Guardia Russa', 'Kantonspolizei', '1821', '1829', 'Albania', 'Andorra', 'Antiterrorismo pronto impiego', 'Arma dei Carabinieri', 'Armenia', 'Associazione per delinquere', 'Austria', 'Autorit\xc3\xa0', 'Autorit\xc3\xa0 giudiziaria', 'Azerbaigian', 'Baliato di Jersey', 'Bartolommeo Fiani', 'Belgio', 'Bene comune', 'Biblioteca Nazionale Centrale di Firenze', 'Biblioteca della Dieta nazionale del Giappone', 'Bielorussia', 'Bosnia ed Erzegovina', 'Boston Police Department', 'Bulgaria', 'Bundespolizei (Austria)', 'Bundespolizei (Germania)', 'Bureau of Alcohol, Tobacco, Firearms and Explosives', 'Burocrazia', 'California Highway Patrol', 'Cavallo', 'Chicago Police Department', 'Cipro', 'Citt\xc3\xa0 del Vaticano', 'Coast Guard Investigative Service', 'Comando carabinieri per la tutela del lavoro', "Comando carabinieri per la tutela dell'ambiente", 'Commercio', 'Commissario di polizia', 'Compagnia barracellare', 'Contea della Scania', 'Contea di Blekinge', 'Contea di Dalarna', 'Contea di Gotland', 'Contea di G\xc3\xa4vleborg', 'Contea di Halland', 'Contea di J\xc3\xa4mtland', 'Contea di J\xc3\xb6nk\xc3\xb6ping', 'Contea di Kalmar', 'Contea di Kronoberg', 'Contea di Norrbotten', 'Contea di Stoccolma', 'Contea di S\xc3\xb6dermanland', 'Contea di Uppsala', 'Contea di V\xc3\xa4rmland', 'Contea di V\xc3\xa4sterbotten', 'Contea di V\xc3\xa4sternorrland', 'Contea di V\xc3\xa4stmanland', 'Contea di V\xc3\xa4stra G\xc3\xb6taland', 'Contea di \xc3\x96rebro', 'Contea di \xc3\x96sterg\xc3\xb6tland', 'Contratto sociale', 'Corpo della gendarmeria della Repubblica di San Marino', 'Corpo della gendarmeria dello Stato della Citt\xc3\xa0 del Vaticano', 'Corpo delle capitanerie di porto - Guardia costiera', 'Corpo di Polizia Penitenziaria', 'Corpo di polizia civile della Repubblica di San Marino', 'Corpo di polizia penitenziaria', 'Corpo forestale della Regione siciliana', "Corpo forestale della Valle d'Aosta", 'Corpo forestale e di vigilanza ambientale', 'Corpo forestale provinciale della Provincia autonoma di Bolzano', 'Corpo forestale provinciale della Provincia autonoma di Trento', 'Criminal Investigation Command', 'Criminalit\xc3\xa0', 'Crimine', 'Croazia', 'Cuerpo Nacional de Polic\xc3\xada', 'Cultura', 'Danimarca', 'Delitto', "Dipartimento della giustizia degli Stati Uniti d'America", 'Direzione Investigativa Antimafia', 'Diritto del lavoro in Italia', 'Distintivi di grado e di qualifica italiani', 'Drug Enforcement Administration', "El Cos de Policia d'Andorra", 'Emergenza', 'Enciclopedia Britannica', 'Enciclopedia canadese', 'Enti locali', 'Estonia', 'FBI', 'Federal Bureau of Investigation', 'Finlandia', 'Firenze', 'Forze speciali', 'Francia', 'F\xc3\xa6r \xc3\x98er', 'Garanzia', 'Garda S\xc3\xadoch\xc3\xa1na', 'Gemeinsame Normdatei', 'Gendarmeria', 'Georgia', 'Germania', 'Gibilterra', 'Giudizio (diritto)', 'Governo', 'Grecia', 'Grecia antica', 'Gruppo di intervento speciale', 'Gruppo operativo mobile', 'Guarda Municipal', 'Guarda Nacional Republicana', 'Guardia Civil', 'Guardia di Finanza', 'Guernsey', "Guerra d'Iraq", 'Interpol', 'Investigazione', 'Irlanda', 'Islanda', 'Isola di Man', 'Isole \xc3\x85land', 'Italia', 'Kazakistan', 'Koninklijke Marechaussee', 'Korps landelijke politiediensten', 'Lettonia', 'Library of Congress Control Number', 'Liechtenstein', 'Lituania', 'Los Angeles Police Department', 'Lussemburgo', 'Macedonia del Nord', 'Magistratura', 'Malta', 'Malta Police Force', 'Miami-Dade Police Department', 'Milano', 'Military Police Corps', 'Militsiya', 'Ministero degli affari interni (Russia)', 'Mitragliatore PK', 'Mitragliatrice', 'Moldavia', 'Montenegro', 'Naval Criminal Investigative Service', 'New York City Police Department', 'New York State Forest Rangers', 'Norma (diritto)', 'Norvegia', 'Nucleo antisofisticazioni', 'Nucleo operativo centrale di sicurezza', 'Nucleo tutela patrimonio culturale', 'Ordinamento giuridico', 'Ordine pubblico', 'Organismo di diritto pubblico', 'Paesi Bassi', 'Policja', 'Polis', 'Polizia albanese', 'Polizia ambientale', 'Polizia cantonale', 'Polizia di Stato', 'Polizia di frontiera', 'Polizia federale', 'Polizia islandese', 'Polizia locale in Italia', 'Polizia militare', 'Polizia monegasca', 'Polizia montata', 'Polizia municipale', 'Polizia politica', 'Polizia provinciale', 'Polizia scientifica', 'Polizia scientifica (disambigua)', 'Polizia segreta', 'Polizia serba', 'Poli\xc8\x9bia Rom\xc3\xa2n\xc4\x83', 'Polonia', 'Port Authority of New York and New Jersey Police Department', 'Portogallo', 'Potere esecutivo', 'Presidente della Federazione Russa', 'Prevenzione', 'Principato di Monaco', 'Progetto', 'Psicopolizia', 'Pubblica sicurezza', 'Raggruppamento operativo speciale', 'Reato', 'Regno Unito', 'Religione', 'Rend\xc5\x91rs\xc3\xa9g', 'Repressione', 'Repubblica Ceca', 'Romania', 'Russia', 'San Marino', 'Sceriffo', 'Scotland Yard', 'Serbia', 'Sicurezza pubblica', 'Slovacchia', 'Slovenia', 'Soccorso', 'Societ\xc3\xa0 aperta', 'Spagna', 'State police', "Stati Uniti d'America", "Stati degli Stati Uniti d'America", 'Stati federali', 'Stati federali della Germania', 'Stato', 'Stra\xc5\xbc Graniczna', 'Stra\xc5\xbc miejska', 'Suojelupoliisi', 'Svezia', 'Svizzera', 'Tecnologia', 'Teocrazia', 'Teste di cuoio', 'Texas Ranger Division', 'Turchia', 'U.S. Customs and Border Protection', 'Ucraina', 'Ungheria', 'United States Marshals Service', 'United States Secret Service', 'Unit\xc3\xa0 militari terrestri', 'Vnutrennie vojska Ministerstva vnutrennikh del', 'XVI secolo', '\xc5\xbbandarmeria Wojskowa', 'Codice di Winchester', 'HH Vostikanut\xe2\x80\x99yun', 'Az\xc9\x99rbaycan Respublikas\xc4\xb1n\xc4\xb1n Milli T\xc9\x99hl\xc3\xbck\xc9\x99sizlik', 'Polizia federale (Belgio)', 'Palicyja Bielarusi', 'Polizia bosniaca', 'Servizio di polizia nazionale', 'Astinomia Kiprou', 'Hrvatska policija', 'Politiet', 'Eesti Politsei', "Dats'vis polits'ia", 'Elliniki Astinomia', 'Polizia kazaka', 'Valsts policija', 'Lietuvos policijos paj\xc4\x97gos', 'Police grand-ducale', 'Makedonija policija', 'Poli\xc8\x9bia Republicii Moldova', 'Uprava Policije', 'Politi- og lensmannsetaten', 'Pol\xc3\xadcia de Seguran\xc3\xa7a P\xc3\xbablica', 'Pol\xc3\xadcia Judici\xc3\xa1ria', 'Policie \xc4\x8cesk\xc3\xa9 Republiky', 'Politsiya', 'Sledstveny Komitet', 'Policajn\xc3\xbd zbor', 'Policija Slovenije', 'Polisen', 'T\xc3\xbcrk Polisi', "Vnutrishni Viys'ka Ukrayiny", 'F\xc3\xa6r\xc3\xb8erne Politi', 'Royal Gibraltar Police', 'States of Guernsey Police Service', 'Isle of Man Constabulary', 'Polismyndigheten i \xc3\x85land', 'States of Jersey Police']}, 'con': {'CON': ['Cratere Con', 'ISO 639-3', 'Lingua italiana', 'Preposizione semplice', 'Rea (astronomia)', 'Lingua cof\xc3\xa1n']}}

    #bus = GraphBusiness()
    #aux = bus.getMostRelatedSubGraph(resd)
    #print(aux)

    bus = WikiBusiness()
    busn = GraphBusiness()
    aux = bus.bulkGetPages(splitted_phrase)
    #print(aux.keys())
    #list_of_entities = []
    #for key in aux.keys():
    #    listaccia = []
    #    for k in aux[key]:
    #        listaccia.append(k)
    #    if listaccia:
    #        list_of_entities.append(listaccia)
    #print(list_of_entities)
    print(aux)
    print( [ a for a in aux.keys() if aux[a] ] )
    grapR = busn.getMostRelatedSubGraph(aux)
    print(grapR)
    #r = requests.post("http://localhost:8000/disambiguate", json={"phrases": splitted_phrase})
    #if r.status_code != 200:
    #    print("There is an error: {}".format(r.text))

    #else:
    #    result = ast.literal_eval( r.text )
    #print(result)
