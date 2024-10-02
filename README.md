# Gestion des Bénéficiaires

<img src="./qj4anmaz.png"
style="width:3.18125in;height:0.79028in" /><img src="./3zhllwp0.png"
style="width:3.17361in;height:0.8618in" />

> ECOLE MAROCAINE DES SCIENCES DE L’INGENIEUR
>
> EMSI LES ORANGERS
>
> RAPPORT DE STAGE
>
> **GESTION** **BÉNÉFICIAIRES**
>
> Présenté par :
>
> **FIRAS** **KOUTARI**
>
> Département : Informatique
>
> Option : Informatique et Réseaux
>
> Encadré par :
>
> **Ch.de** **Serv.** **Mhammed** **Ben** **Said**
>
> **Pr.** **Mbida** **Mohamed**

<u>2022/2023</u>

Tableau des Matières
Remerciments...............................................................................................................................................................
3

> Introduction
> Générale.........................................................................................................................................
> 4
>
> Partie
> Théorique.....................................................................................................................................................
> 5
>
> Introduction......................................................................................................................................................................
> 5
>
> Description........................................................................................................................................................................
> 6
>
> Préparation des
> environnements.....................................................................................................................................
> 7
>
> Logigramme
> Généralisé....................................................................................................................................................
> 8
>
> Diagramme de cas
> d’utilisation.........................................................................................................................................
> 9
>
> Diagramme de
> classe......................................................................................................................................................
> 10
>
> Diagramme de
> séquence................................................................................................................................................
> 11
>
> Conclusion.......................................................................................................................................................................
> 13
>
> Partie
> Pratique.....................................................................................................................................................
> 15
>
> Introduction....................................................................................................................................................................
> 15
>
> Contexte de
> l’application................................................................................................................................................
> 16
>
> Démonstration de
> l’application......................................................................................................................................
> 17
>
> Conclusion.......................................................................................................................................................................
> 20
>
> Conclusion
> Générale............................................................................................................................................
> 21
>
> Annexes.........................................................................................................................................................................
> 22
>
> EXTRAITS DU CODES :
> .....................................................................................................................................................
> 22
>
> CAPTURES D’ECRANT
> :....................................................................................................................................................
> 27
>
> Webographie...............................................................................................................................................................
> 29

Remerciments

Au terme de cette expérience enrichissante, une profonde gratitude est
exprimée envers toutes les personnes ayant contribué à la réussite du
stage au sein de la Direction Provinciale de l'Habitat et de la
Politique de la Ville de Settat.

En premier lieu, les remerciements les plus sincères sont adressés à
Monsieur Mhammed Ben Said, Chef de Service, pour avoir offert une
opportunité exceptionnelle de réalisation du stage au sein de son
équipe. Les conseils avisés, le soutien constant et la vision éclairée
de Monsieur Ben Said ont grandement contribué à l'expérience
professionnelle et à l'épanouissement au sein de l'institution.

Également, une gratitude particulière est exprimée envers Monsieur
Mohamed Mbida, l'encadrant pédagogique, pour ses orientations précieuses
et ses conseils éclairés tout au long du stage. La disponibilité et
l'expertise de Monsieur Mbida ont été inestimables dans l'encadrement
des activités et dans l'enrichissement de l'apprentissage.

Les remerciements s'adressent également à tous les membres de l'équipe
de la Direction Provinciale de l'Habitat et de la Politique de la Ville
de Settat. L'accueil chaleureux, la collaboration et le partage
d'expérience de l'équipe ont permis une intégration rapide et une
compréhension approfondie des enjeux concrets du domaine de
l'amélioration de l'habitat.

Enfin, la gratitude est exprimée envers la famille et les amis pour leur
soutien indéfectible tout au long du parcours académique et
professionnel. Les encouragements et la confiance ont été une source
constante d'inspiration.

Ce rapport de stage représente le fruit d'un travail d'équipe et de la
contribution collective de toutes ces personnes. Une reconnaissance est
exprimée envers chacun pour leur collaboration précieuse ayant rendu
cette expérience aussi formatrice et gratifiante

Introduction Générale

Le stage en milieu professionnel représente une étape cruciale dans le
parcours académique des étudiants, offrant l'opportunité de mettre en
pratique les connaissances acquises en classe au sein d'un environnement
réel. Durant la période allant du 3 juillet 2023 au 31 juillet 2023,
s'est déroulé un stage au sein de la Direction Provinciale de l'Habitat
et de la Politique de la Ville de Settat.

Cette institution, basée à Settat, se spécialise dans la conception, la
planification et la mise en œuvre de projets visant à améliorer
l'habitat et la qualité de vie urbaine au Maroc. Le stage a été dédié à
la contribution à un projet significatif au sein de cette entité : le
développement d'une application web destinée à la gestion des
bénéficiaires.

L'objectif principal de cette expérience résidait dans l'acquisition
d'une expérience pratique, en participant à toutes les phases du cycle
de développement d'un projet informatique, tout en étant immergé dans le
contexte spécifique de l'amélioration de l'habitat et de la vie urbaine.
Supervisé par Monsieur Mhammed Ben Said, Chef de Service, ce stage a
permis d'explorer diverses facettes du développement logiciel, depuis la
conception jusqu'à la mise en œuvre, en passant par les phases de tests
et de documentation.

L'encadrement pédagogique a été assuré par le Professeur Mohamed Mbida,
qui a apporté une expertise précieuse et des conseils tout au long de
cette période, favorisant ainsi l'intégration de l'expérience
professionnelle dans le cadre de la formation académique.

Dans le cadre de ce rapport, sera présentée en détail la progression du
stage, les différentes missions et responsabilités qui ont été confiées,
ainsi que les compétences techniques et professionnelles qui ont pu être
développées. Le projet de création de l'application web pour la gestion
des bénéficiaires sera également mis en lumière, avec une explication
des objectifs, des étapes de réalisation, des technologies mises en
œuvre et des résultats obtenus.

Partie Théorique Introduction

L'introduction à la gestion des bénéficiaires revêt une importance
significative dans le contexte des projets liés à l'habitat et à la
politique de la ville. Ces types de projets sont conçus pour améliorer
la qualité de vie des individus et des communautés en leur fournissant
des logements décents, des infrastructures urbaines améliorées et des
services essentiels. La gestion efficace des bénéficiaires constitue un
pilier essentiel pour assurer le succès et la pérennité de tels projets.
Cette gestion englobe la collecte, la mise à jour et la gestion continue
des informations relatives aux individus qui bénéficient des initiatives
mises en place.

Dans le domaine de l'habitat et de la politique de la ville, la gestion
des bénéficiaires joue un rôle clé tout au long du cycle de vie des
projets. Elle intervient dès la phase de planification en permettant
l'identification des personnes éligibles à bénéficier des programmes, en
fonction de critères spécifiques tels que le niveau de revenu, le statut
familial et les besoins particuliers. Une fois les projets mis en œuvre,
la gestion des bénéficiaires permet de suivre l'allocation de
ressources, de garantir une distribution équitable des avantages et de
veiller à ce que les bénéficiaires reçoivent effectivement les services
et les améliorations promis.

En outre, la gestion des bénéficiaires joue un rôle crucial dans
l'évaluation de l'impact des interventions. En suivant les données
démographiques, les situations économiques et sociales des
bénéficiaires, il devient possible de mesurer l'efficacité des projets
et d'apporter des ajustements en temps réel pour répondre aux besoins
changeants de la population. Cette démarche proactive favorise une
meilleure adaptation des projets aux réalités du terrain et renforce
ainsi leur réussite à long terme.

En somme, cette section introductive met en évidence le concept
fondamental de la gestion des bénéficiaires dans le contexte des projets
d'habitat et de politique de la ville. En intégrant cette gestion dans
la planification, l'exécution et le suivi des projets, il devient
possible de maximiser les avantages pour les bénéficiaires, d'assurer la
durabilité des initiatives et de contribuer à l'amélioration globale des
conditions de vie au sein des communautés ciblées.

Description

Cette application a été soigneusement conçue dans le but de fournir une
plateforme à la fois intuitive et exhaustive, avec pour objectif de
rationaliser et d'optimiser la gestion des informations associées aux
bénéficiaires des projets d'habitat et de politique de la ville. Les
modules clés de cette application couvrent un large éventail de
fonctionnalités essentielles, notamment l'inscription des utilisateurs,
une connexion sécurisée, ainsi que la saisie et la mise à jour efficaces
des données des bénéficiaires.

Dotée d'une interface conviviale, l'application permet aux utilisateurs
de manipuler aisément les informations liées aux bénéficiaires, offrant
ainsi une solution pratique pour suivre, enregistrer et organiser les
détails cruciaux des personnes impliquées dans les projets. Avec cette
application, les utilisateurs peuvent désormais gérer de manière
efficace l'ensemble du processus, de l'inscription des bénéficiaires à
la gestion en continu de leurs informations.

En résumé, cette section vise à présenter l'application web comme un
outil d'une valeur inestimable pour l'amélioration de la gestion des
bénéficiaires. Elle contribue également à optimiser la réalisation des
projets d'habitat et de politique de la ville en offrant une plateforme
centralisée et conviviale pour collecter, stocker et mettre à jour les
informations pertinentes. En offrant une expérience fluide et efficace,
cette application est destinée à faciliter la gestion des bénéficiaires
et à accroître l'efficacité de la mise en œuvre des projets.

Préparation des environnements

La phase de préparation des environnements a revêtu une importance
capitale dans le processus de développement de l'application web
destinée à la gestion des bénéficiaires. Dans le but d'assurer une
expérience de développement aussi fluide que sécurisée, j'ai pris la
décision judicieuse d'opter pour l'utilisation de technologies modernes
et puissantes, telles que Django, HTML, CSS et JavaScript. Cette
sélection minutieuse a eu pour conséquence la création d'une application
à la fois robuste, réactive et conviviale pour les utilisateurs finaux.

Une attention particulière a également été portée à la configuration
optimale des environnements de développement. J'ai mis en œuvre des
pratiques exemplaires en créant des environnements virtuels dédiés, ce
qui a permis d'isoler les différentes dépendances de manière efficace.
Cette approche a favorisé la gestion harmonieuse des bibliothèques et
des modules requis pour le bon fonctionnement de l'application, évitant
ainsi les conflits potentiels entre différentes versions de logiciels.

Pour garantir la qualité et la fiabilité de l'application, des tests
rigoureux ont été effectués. Ces tests ont couvert une variété de
scénarios et de conditions d'utilisation afin d'identifier et de
résoudre d'éventuels problèmes ou erreurs. Cette démarche proactive a
permis de déceler et de corriger les anomalies avant qu'elles ne
puissent impacter les utilisateurs finaux.

En somme, la minutieuse préparation de ces environnements de
développement a joué un rôle essentiel dans l'obtention d'une
application finale de haute qualité, stable et sécurisée. Cette démarche
a grandement contribué à instaurer un processus de développement
efficace, en s'assurant que l'application soit prête à répondre aux
besoins des utilisateurs tout en assurant leur satisfaction continue.

<img src="./unhnn21o.png"
style="width:3.64236in;height:9.08055in" />

Logigramme Généralisé

> Figure 1 :Logigramme Generalisé

<img src="./ry3o1wmd.png" style="width:7.5in;height:5.71181in" />

Diagramme de cas d’utilisation

> Figure 2: diagramme de cas d’utilisation

<img src="./pfb4ukrz.png"
style="width:7.89903in;height:4.75694in" />

Diagramme de classe

> Figure 3 : digramme de classe

<img src="./flidb1u1.png" style="width:7.7in;height:6.45in" />

Diagramme de séquence

> 1\. **L’inscription**
>
> Figure 4:Diagramme Séquence sur l’inscription

<img src="./p4oumk4b.png"
style="width:7.50694in;height:6.92153in" />

2\. **Gestion** **du** **bénéficiaires**

> Figure 5 :Diagramme Séquence gestion bénéficiaires

<img src="./egfiwhfj.png" style="width:7.5in;height:6.42361in" />

**3.** **Exporter** **en** **excel**

> Figure 6 :Diagramme Séquence Exporter en Excel

Conclusion

En conclusion de la partie théorique de ce rapport, nous avons plongé
profondément dans les principes fondamentaux de la gestion des
bénéficiaires dans le contexte des projets d'habitat et de la politique
de la ville. Notre exploration nous a permis de mettre en lumière
l'importance cruciale d'une gestion efficiente des bénéficiaires pour le
succès et la durabilité de ces projets. Nous avons mis en exergue le
rôle central que joue cette gestion dans toutes les phases des
initiatives, de la planification à la mise en œuvre en passant par le
suivi.

L'application web que nous avons élaborée dans cette section se révèle
être une réponse concrète à ces besoins. En fournissant une plateforme
efficace pour la saisie, la gestion et l'analyse des données relatives
aux bénéficiaires, cette solution technologique vise à améliorer la
manière dont ces projets sont gérés et suivis. Tout au long de notre
exploration des concepts théoriques, ainsi que de la mise en pratique de
ces concepts au sein de l'application que nous avons développée, une
chose est devenue manifeste : la technologie détient un rôle crucial
dans l'optimisation des processus internes et dans la contribution au
succès global des projets d'habitat et de la politique de la ville.

Ce rapport, mêlant concepts théoriques et applications pratiques, met en
avant la synergie entre les connaissances acquises et leur mise en
œuvre. Il renforce l'idée que la technologie offre des opportunités pour
accroître l'efficacité, la traçabilité et la transparence des processus,
offrant ainsi des avantages tangibles à toutes les parties prenantes
impliquées dans ces initiatives. En fin de compte, ce rapport témoigne
de la manière dont la convergence entre la théorie et la pratique peut
apporter une véritable valeur ajoutée aux projets d'habitat et de la
politique de la ville, renforçant ainsi leur impact positif sur les
communautés et l'environnement urbain.

Partie Pratique

Introduction

Cette section de la présentation se concentre sur la mise en œuvre
pratique de l'application développée pour répondre aux besoins
spécifiques de la Direction Provinciale de l'Habitat et de la Politique
de la Ville à Settat. Alors que la première partie a fourni un aperçu
théorique des objectifs et des concepts, cette section offre une vue
détaillée des fonctionnalités clés de l'application et démontre comment
elle apporte une réelle valeur ajoutée en optimisant la gestion des
informations liées aux bénéficiaires.

En se plongeant dans la mise en pratique, cette section se propose de
guider le lecteur à travers une exploration en profondeur des
différentes facettes de l'application. Elle utilisera des captures
d'écran illustratives accompagnées d'explications détaillées pour mettre
en évidence les différentes fonctionnalités et processus mis en place.
Grâce à cette approche, le lecteur pourra obtenir une compréhension
concrète de la manière dont l'application fonctionne et comment elle
peut répondre aux besoins de la Direction Provinciale de l'Habitat et de
la Politique de la Ville à Settat.

L'objectif principal de cette introduction est de préparer le lecteur à
explorer les modules et les processus implémentés au sein de
l'application. À travers cette exploration, le lecteur pourra se
familiariser avec les fonctionnalités clés, comprendre comment elles
sont intégrées et comment elles peuvent être utilisées pour améliorer
efficacement la gestion des informations concernant les bénéficiaires.

Contexte de l’application

Le contexte de l'application est étroitement lié à une institution qui
s'investit activement dans la réalisation de projets ayant pour objectif
d'améliorer les conditions de vie en matière d'habitat et de qualité de
vie urbaine dans la région. Cette tâche complexe requiert une gestion
précise des bénéficiaires impliqués dans ces projets, afin d'assurer une
répartition juste des avantages et des ressources. Pour répondre à ce
défi, l'application de gestion des bénéficiaires a été développée.

L'objectif principal de cette application est de simplifier et
d'optimiser le suivi des individus concernés par les projets en
centralisant les informations relatives aux bénéficiaires et aux
opérations. En agissant ainsi, l'application comble un besoin crucial au
sein de la Direction Provinciale, en offrant une plateforme
transparente, efficace et équitable pour gérer les données liées aux
bénéficiaires des projets liés à l'habitat et à la politique de la
ville.

En résumé, cette application a pour mission de répondre directement aux
besoins spécifiques de l'institution en matière de gestion de
l'information, permettant ainsi une meilleure planification, exécution
et suivi des projets d'habitat et de politique de la ville, tout en
garantissant une répartition équitable des ressources et avantages parmi
les bénéficiaires impliqués.

Démonstration de l’application

> • **Page** **d'Accueil**

Lorsqu'un utilisateur accède à l'application, la page d'accueil lui
offre une vue d'ensemble des fonctionnalités disponibles. Des options de
connexion et d'inscription sont clairement présentées, incitant les
utilisateurs à créer un compte ou à se connecter s'ils en possèdent déjà
un.

> • **Inscription** **d'un** **Utilisateur**

<img src="./1i2mzupx.png"
style="width:3.49167in;height:2.99236in" />En cliquant sur l'option
d'inscription, l'utilisateur est redirigé vers un formulaire de création
de compte. Ce formulaire lui demande de fournir des informations telles
que son nom d'utilisateur, son adresse e-mail et un mot de passe
sécurisé. Une fois soumis, le système vérifie la validité des données
saisies et crée un nouveau compte utilisateur.

> Figure 7 : Page d’inscription
>
> <img src="./5lkidygl.png"
> style="width:3.50625in;height:2.41667in" />• **Connexion** **à**
> **l'Application**

Pour les utilisateurs enregistrés, la page de connexion permet d'accéder
au tableau de bord de l'application. L'utilisateur entre ses
identifiants, et le système les vérifie pour autoriser l'accès à
l'interface utilisateur principale.

> Figure 8 : Page de connexion

<img src="./u5xzut30.png"
style="width:7.50694in;height:1.51319in" /><img src="./pxwff2k5.png" style="width:7.31806in;height:2.75in" />

> • **Gestion** **des** **Bénéficiaires**
>
> Figure 9: Page Gestion Beneficiaires
>
> Figure 10 : Page recherche Beneficiaires

Le tableau de bord offre une section dédiée à la gestion des
bénéficiaires. L'utilisateur peut ajouter de nouveaux bénéficiaires en
saisissant toutes les informations liées au bénéficiaire. Il peut
également rechercher et afficher des bénéficiaires existants.

<img src="./dgt3smv2.png"
style="width:7.71389in;height:1.85833in" />

> • **Exportation** **en** **Excel**

L'application offre la possibilité d'exporter les données des
bénéficiaires et des opérations au format Excel. Cette fonctionnalité
permet aux utilisateurs d'analyser les données hors ligne et de générer
des rapports pour des besoins spécifiques.

> Figure 11 : Page recherche Beneficiaires

Conclusion

Le contexte de l'application est étroitement lié à une institution qui
s'investit activement dans la réalisation de projets ayant pour objectif
d'améliorer les conditions de vie en matière d'habitat et de qualité de
vie urbaine dans la région. Cette tâche complexe requiert une gestion
précise des bénéficiaires impliqués dans ces projets, afin d'assurer une
répartition juste des avantages et des ressources. Pour répondre à ce
défi, l'application de gestion des bénéficiaires a été développée.

L'objectif principal de cette application est de simplifier et
d'optimiser le suivi des individus concernés par les projets en
centralisant les informations relatives aux bénéficiaires et aux
opérations. En agissant ainsi, l'application comble un besoin crucial au
sein de la Direction Provinciale, en offrant une plateforme
transparente, efficace et équitable pour gérer les données liées aux
bénéficiaires des projets liés à l'habitat et à la politique de la
ville.

En résumé, cette application a pour mission de répondre directement aux
besoins spécifiques de l'institution en matière de gestion de
l'information, permettant ainsi une meilleure planification, exécution
et suivi des projets d'habitat et de politique de la ville, tout en
garantissant une répartition équitable des ressources et avantages parmi
les bénéficiaires impliqués.

Conclusion Générale

Mon stage au sein de la Direction Provinciale de l'Habitat et de la
Politique de la Ville de Settat a été une expérience exceptionnelle qui
a enrichi ma formation académique et élargi ma perspective
professionnelle. À travers ce rapport, j'ai tenté de refléter les
moments marquants, les défis relevés et les enseignements tirés au cours
de cette période riche en découvertes.

Au cours de ces quelques semaines, j'ai pu plonger au cœur des projets
liés à l'amélioration de l'habitat et à la gestion des bénéficiaires.
J'ai non seulement acquis des compétences techniques en développement
d'applications web, mais j'ai également compris l'importance de la
collaboration au sein d'une équipe dynamique et la nécessité d'adapter
ses connaissances théoriques à des problématiques concrètes.

La réalisation du projet d'application web de gestion des bénéficiaires
a été une expérience gratifiante. J'ai eu l'opportunité de mettre en
œuvre des technologies actuelles et de participer à toutes les phases de
développement, de la conception à la mise en production. Cette
expérience a renforcé ma confiance en mes compétences techniques et m'a
permis de voir comment mes contributions pouvaient avoir un impact réel.

La collaboration avec mon encadrant, Monsieur Mhammed Ben Said, ainsi
qu'avec l'ensemble de l'équipe, a été une source d'inspiration et
d'apprentissage. Leurs conseils, leur expertise et leur soutien ont
contribué à mon développement professionnel et ont facilité mon
intégration au sein de l'institution.

Ce stage m'a également permis de constater l'importance de la
polyvalence et de l'adaptabilité dans le domaine professionnel. J'ai été
confronté à des situations variées et j'ai dû ajuster mes compétences en
fonction des besoins du projet.

En conclusion, ce stage a été une étape fondamentale dans mon parcours
académique et professionnel. Il a consolidé mes connaissances
techniques, renforcé mes compétences en gestion de projet et a développé
mon sens de la responsabilité professionnelle. Je suis convaincu que les
enseignements tirés de cette expérience m'accompagneront dans toutes mes
futures entreprises et contribueront à mon développement continu en tant
que professionnel de l'informatique.

Annexes

EXTRAITS DU CODES :

from django.db import models

class Beneficiaire(models.Model):

> cin = models.CharField(max_length=255, primary_key=True) nom =
> models.CharField(max_length=255)
>
> prenom = models.CharField(max_length=255)
>
> def \_\_str\_\_(self): return self.nom
>
> class Meta:
>
> ordering = \['nom'\]

class Conjoint(models.Model):

> cin = models.CharField(max_length=255, primary_key=True) nom =
> models.CharField(max_length=255)
>
> prenom = models.CharField(max_length=255)
>
> beneficiaire = models.ForeignKey(Beneficiaire,
> on_delete=models.CASCADE)
>
> def \_\_str\_\_(self): return self.nom
>
> class Meta:
>
> ordering = \['nom'\]

class Enfant(models.Model):

> id_enfant = models.AutoField(primary_key=True) nom =
> models.CharField(max_length=255)
>
> prenom = models.CharField(max_length=255)
>
> beneficiaire = models.ForeignKey(Beneficiaire,
> on_delete=models.CASCADE)
>
> def \_\_str\_\_(self): return self.nom
>
> class Meta:
>
> ordering = \['nom'\]

class OrigineBeneficiaire(models.Model): villes = \[

> ('Settat','Settat'), \]
>
> communes = \[ ('commune_Settat','commune_Settat'),
>
> \]
>
> douars = \[ ('kilaz','kilaz'),
>
> \]
>
> ville = models.CharField(max_length=255,choices=villes) commune =
> models.CharField(max_length=255,choices=communes) douar =
> models.CharField(max_length=255,choices=douars)
>
> beneficiaire = models.ForeignKey(Beneficiaire,
> on_delete=models.CASCADE)
>
> def \_\_str\_\_(self): return self.ville
>
> class Meta:
>
> ordering = \['ville'\]

class InformationOperation(models.Model): operateurs = \[

> ('Alomrane','Alomrane'), \]
>
> type_inter = \[ ('type1','type1'), ('type2','type2'),
>
> \]
>
> num_pv = models.CharField(max_length=255)
>
> operateur = models.CharField(max_length=255,choices=operateurs)
> nom_operation = models.CharField(max_length=255) num_ressencement =
> models.CharField(max_length=255) date_ressencement =
> models.DateField(null=True,default=None) date_affectation =
> models.DateField(null=True,default=None)
>
> type_intervention = models.CharField(max_length=255,
> choices=type_inter) prix_produit = models.DecimalField(max_digits=10,
> decimal_places=2) subvention_fshiu =
> models.DecimalField(max_digits=10, decimal_places=2) date_demolition =
> models.DateField(null=True,default=None)
>
> num_lot = models.CharField(max_length=255) fichier_joint =
> models.FileField(upload_to='uploads/') observation =
> models.TextField()
>
> beneficiaire = models.ForeignKey(Beneficiaire,
> on_delete=models.CASCADE)
>
> def \_\_str\_\_(self):
>
> return self.nom_operation class Meta:
>
> ordering = \['nom_operation'\]

La capture d'écran montre les modèles Django pour l'application de
gestion des bénéficiaires. Les modèles sont :

**Bénéficiaire** : Ce modèle représente un bénéficiaire. Il comporte les
champs suivants :

> cin : Le numéro CIN du bénéficiaire
>
> nom : Le nom du bénéficiaire prenom : Le prénom du bénéficiaire

**Conjoint** : Ce modèle représente le conjoint du bénéficiaire. Il
comporte les champs suivants : cin : Le numéro CIN du conjoint

> nom : Le nom du conjoint prenom : Le prénom du conjoint

**Enfant** : Ce modèle représente les enfants du bénéficiaire. Il
comporte les champs suivants : id_enfant : L'identifiant unique de
l'enfant

> nom : Le nom de l'enfant prenom : Le prénom de l'enfant

**OrigineBeneficiaire** : Ce modèle représente l'origine du
bénéficiaire. Il comporte les champs suivants : ville : La ville du
bénéficiaire

> commune : La commune du bénéficiaire douar : Le douar du bénéficiaire

**InformationOperation** : ce modèle représente une opération
d’information. Il comporte les champs suivants :

> num_pv : Le numéro PV
>
> opérateur : L'opérateur
>
> nom_operation : Le nom de l'opération num_ressencement : Le numéro de
> recensement date_ressencement : La date du recensement
> date_affectation : La date de la mission type_intervention : le type
> d'intervention prix_produit : Le prix du produit subvention_fshiu : La
> subvention du FSIU date_demolition : La date de démolition num_lot :
> Le numéro de lot
>
> fichier_joint : Le fichier joint observation : L'observation

def export_to_excel(request):

> response = HttpResponse(content_type='application/ms-excel')
> response\['Content-Disposition'\] = 'attachment;
> filename="search_results.xlsx"'
>
> beneficiaires = Beneficiaire.objects.all()
>
> \# Applying filters based on the GET parameters cin =
> request.GET.get('cin')
>
> nom = request.GET.get('nom') prenom = request.GET.get('prenom') num_pv
> = request.GET.get('num_pv')
>
> nom_operation = request.GET.get('nom_operation') cin_conjoint =
> request.GET.get('cin_conjoint') nom_conjoint =
> request.GET.get('nom_conjoint') prenom_conjoint =
> request.GET.get('prenom_conjoint') nom_enfant =
> request.GET.get('nom_enfant') prenom_enfant =
> request.GET.get('prenom_enfant') num_lot = request.GET.get('num_lot')
>
> if cin:
>
> beneficiaires = beneficiaires.filter(cin\_\_icontains=cin) if nom:
>
> beneficiaires = beneficiaires.filter(nom\_\_icontains=nom) if prenom:
>
> beneficiaires = beneficiaires.filter(prenom\_\_icontains=prenom) if
> num_pv:
>
> beneficiaires =
> beneficiaires.filter(informationoperation\_\_num_pv\_\_icontains=num_pv)
> if nom_operation:

beneficiaires =
beneficiaires.filter(informationoperation\_\_nom_operation\_\_icontains=nom_operation)

> if num_lot: beneficiaires =

beneficiaires.filter(informationoperation\_\_num_lot\_\_icontains=num_lot)

\# Filtering conjoint and enfant separately if cin_conjoint:

> conjoint = Conjoint.objects.filter(cin\_\_icontains=cin_conjoint)
> beneficiaires = beneficiaires.filter(conjoint\_\_in=conjoint)
>
> if nom_conjoint:
>
> conjoint = Conjoint.objects.filter(nom\_\_icontains=nom_conjoint)
> beneficiaires = beneficiaires.filter(conjoint\_\_in=conjoint)
>
> if prenom_conjoint:
>
> conjoint =
> Conjoint.objects.filter(prenom\_\_icontains=prenom_conjoint)
> beneficiaires = beneficiaires.filter(conjoint\_\_in=conjoint)
>
> if nom_enfant:
>
> enfant = Enfant.objects.filter(nom\_\_icontains=nom_enfant)
> beneficiaires = beneficiaires.filter(enfant\_\_in=enfant)
>
> if prenom_enfant:
>
> enfant = Enfant.objects.filter(prenom\_\_icontains=prenom_enfant)
> beneficiaires = beneficiaires.filter(enfant\_\_in=enfant)
>
> \# Create Excel workbook and worksheet wb = openpyxl.Workbook()
>
> ws = wb.active
>
> \# Write headers
>
> headers = \['CIN du bénéficiaire', 'Nom du bénéficiaire', 'Prénom du
> bénéficiaire', 'Nom de l\\opération', 'Opérateur', 'Date
> d\\affectation', 'N° de

Ressencement'\]

> for col_num, header in enumerate(headers, 1): col_letter =
> get_column_letter(col_num) ws\[f'{col_letter}1'\] = header
>
> \# Write data rows
>
> for row_num, beneficiaire in enumerate(beneficiaires, 2):
> ws.cell(row=row_num, column=1, value=beneficiaire.cin)
> ws.cell(row=row_num, column=2, value=beneficiaire.nom)
> ws.cell(row=row_num, column=3, value=beneficiaire.prenom)
> info_operations = beneficiaire.informationoperation_set.all() if
> info_operations.exists():
>
> ws.cell(row=row_num, column=4,
> value=info_operations\[0\].nom_operation) ws.cell(row=row_num,
> column=5, value=info_operations\[0\].operateur) ws.cell(row=row_num,
> column=6, value=info_operations\[0\].date_affectation)
> ws.cell(row=row_num, column=7,
> value=info_operations\[0\].num_ressencement)
>
> \# Save the Excel file wb.save(response) return response

La fonction export_to_excel() exporte les données des bénéficiaires dans
un fichier Excel. La fonction prend en entrée une requête HTTP et
renvoie une réponse HTTP avec le fichier Excel attaché.

La fonction commence par créer un workbook et un worksheet Excel.
Ensuite, elle écrit les en-têtes du tableau dans le worksheet. Enfin,
elle écrit les données des bénéficiaires dans le worksheet.

La fonction utilise la méthode get_column_letter() pour convertir un
numéro de colonne en une lettre de colonne. Par exemple, la méthode
get_column_letter(1) renvoie la lettre A.

La fonction utilise la méthode cell() pour écrire une valeur dans une
cellule du worksheet. Par exemple, la méthode cell(row=row_num,
column=1, value=beneficiaire.cin) écrit le CIN du bénéficiaire dans la
cellule A de la ligne row_num.

La fonction utilise la méthode save() pour enregistrer le fichier Excel.

<img src="./cqou3xui.png"
style="width:7.50694in;height:3.3743in" />

CAPTURES D’ECRANT :

> Figure 12 : Page Ajouter Bénéficiaire

<img src="./hueaamy1.png"
style="width:6.02917in;height:2.875in" /><img src="./wsafxgga.png"
style="width:6.05833in;height:2.91042in" /><img src="./mnbdipaw.png"
style="width:7.50694in;height:2.92292in" />

> Figure 13 : Page Details du bénéficiare
>
> Figure 14 : Page Modifier bénéficiaire

Webographie

**1.** **Bootstrap**

\- Le Framework Bootstrap a été utilisé pour créer une interface
utilisateur moderne et réactive. Les composants prêts à l'emploi de
Bootstrap ont grandement accéléré le développement de l'interface
utilisateur.

> **https://getbootstrap.com/**

**2.** **Tutoriel** **Django** **pour** **les** **Débutants**

\- Ce tutoriel vidéo détaillé sur Django m'a aidé à acquérir une
compréhension approfondie du Framework Django, de ses fonctionnalités
clés et de son utilisation pour développer des applications web.

> **https://youtube.com/playlist?list=PLknwEmKsW8OtK_n48UOuYGxJPbSFrICxm&si=S4QfGiT**
> **oVge0T4sM**

**3.** **Site** **Web** **Officiel** **de** **Django**

\- Le site officiel de Django a été une ressource précieuse pour accéder
à la documentation, aux guides de référence et aux tutoriels pour le
développement avec Django.

> **https://www.djangoproject.com/**

**4.** **Visual** **Studio** **Code**

\- J'ai utilisé l'éditeur de code Visual Studio Code pour le
développement du projet. Ses fonctionnalités de débogage, de gestion de
code et d'intégration avec Git ont été très utiles pour optimiser mon
flux de travail.

> **https://code.visualstudio.com/**

**5.GitHub**

> \- La plateforme de gestion de code source où le projet a été hébergé.
>
> **https://github.com/**

Ces ressources ont joué un rôle crucial dans la réussite de mon projet
en me fournissant les connaissances nécessaires pour prendre des
décisions techniques éclairées et pour résoudre les défis rencontrés
pendant le développement.
