# Politique de confidentialité de Girostella

**Dernière mise à jour : 25 octobre 2026**

La présente politique de confidentialité décrit le traitement des données à caractère personnel effectué dans le cadre de l’application mobile **Girostella** (ci-après l’« Application »), conformément au règlement (UE) 2016/679 (ci-après le « RGPD ») et aux autres dispositions applicables en matière de protection des données personnelles.

## 1. Responsable du traitement

Le responsable du traitement est **Girostella**.

Adresse e-mail : **[alessandro_penna@icloud.com](mailto:alessandro_penna@icloud.com)**

## 2. Données traitées par l’Application

Girostella est conçue dans le respect du principe de minimisation des données.

L’Application ne nécessite pas la création d’un compte propre à Girostella et n’utilise pas de serveurs exploités par le Responsable du traitement pour collecter les données de jeu. Elle n’intègre pas de SDK d’analyse statistique indépendants ni de services tiers spécifiquement dédiés au signalement des plantages, sans préjudice du traitement des données techniques et de diagnostic effectué par les services publicitaires décrits à la section 6.

L’Application ne demande pas l’accès à la localisation GPS, à l’appareil photo, au microphone, aux contacts, aux photos, au calendrier ou aux données de santé. Elle ne demande pas non plus aux utilisateurs de fournir leur nom, leur adresse, leur numéro de téléphone ou leur adresse e-mail pour jouer.

Lors de son utilisation, les informations nécessaires au fonctionnement du jeu sont enregistrées localement sur l’appareil, notamment les scores, les records, la progression, les éléments cosmétiques débloqués ou sélectionnés, les préférences sonores et haptiques, les informations relatives aux bonus déjà rencontrés, les identifiants techniques des transactions déjà traitées et les scores éventuellement en attente de synchronisation avec Game Center.

Ces données restent dans l’espace de stockage privé de l’Application sur l’appareil et ne sont pas transmises à des serveurs exploités par le Responsable du traitement. Elles sont normalement supprimées lors de la désinstallation de l’Application, à l’exception des éventuelles copies conservées dans les sauvegardes de l’appareil et des informations stockées de manière autonome par les services Apple.

L’Application utilise également Google Mobile Ads et Google User Messaging Platform, qui peuvent traiter des informations techniques, des identifiants, des données publicitaires et des informations relatives à l’utilisation de l’Application, comme indiqué à la section 6.

Le Responsable du traitement ne dispose pas de sa propre base de données contenant les adresses IP des joueurs. Toutefois, les fournisseurs de services externes utilisés par l’Application peuvent recevoir des adresses IP et d’autres informations techniques nécessaires à la fourniture de leurs services respectifs.

## 3. Game Center

Girostella utilise **Apple Game Center** pour l’authentification facultative des joueurs, la gestion des classements, l’envoi et la synchronisation des scores ainsi que la reconnaissance des succès obtenus dans le jeu.

Par l’intermédiaire de GameKit, l’Application peut recevoir temporairement les informations nécessaires au fonctionnement du service, notamment les identifiants Game Center, les scores et les informations utilisées pour afficher les classements.

Les pseudonymes, avatars et autres informations du profil Game Center peuvent être affichés selon les paramètres du joueur et les fonctionnalités proposées par Apple, mais ne sont pas enregistrés sur des serveurs exploités par le Responsable du traitement.

### Classements et informations de jeu

Girostella utilise Apple Game Center pour gérer et synchroniser les classements. À cette fin, l’Application transmet à Apple les scores obtenus par les joueurs ainsi que certaines informations associées aux éléments du jeu, nécessaires à l’affichage correct des classements et à la vérification de l’intégrité des résultats.

Ces informations ne comprennent pas de données d’identité civile et peuvent être rendues visibles aux autres joueurs par l’intermédiaire des fonctionnalités de Game Center.

### Stockage local des informations relatives aux autres joueurs

Afin d’assurer un affichage plus cohérent des vaisseaux spatiaux dans les classements, Girostella conserve sur l’appareil certaines informations de jeu relatives à d’autres joueurs rencontrés par l’intermédiaire de Game Center.

Ces informations comprennent des codes relatifs aux vaisseaux spatiaux, aux traînées et aux collections, le contexte technique associé au score ainsi que la date de la partie.

Chaque enregistrement est associé à une clé pseudonymisée générée à partir de l’identifiant Game Center au moyen d’une fonction cryptographique et d’une valeur aléatoire locale. L’identifiant Game Center d’origine et le nom du joueur ne sont pas conservés dans le cache.

Le cache contient au maximum **25 000 enregistrements** et ne prévoit aucune durée de conservation fixe. Lorsque cette limite est dépassée, les entrées les plus anciennes sont supprimées en premier. Les données sont normalement supprimées lors de la désinstallation de l’Application, à l’exception des éventuelles copies conservées dans les sauvegardes de l’appareil.

Ces informations ne sont transmises ni au Responsable du traitement, ni à Google, ni à d’autres tiers et ne sont utilisées ni à des fins publicitaires, ni à des fins de profilage, ni à des fins d’analyse statistique.

Le traitement repose sur l’intérêt légitime du Responsable du traitement à garantir un affichage cohérent des informations de jeu dans les classements, conformément à l’article 6, paragraphe 1, point f), du RGPD.

### Amis et succès Game Center

Girostella permet de reconnaître les amis Game Center présents dans les classements au moyen d’un indicateur visuel spécifique.

À cette fin, l’Application utilise les informations fournies par le classement réservé aux amis, sans demander l’accès au carnet d’adresses de l’appareil ni obtenir de manière autonome une liste complète des contacts.

Les identifiants nécessaires à la comparaison sont utilisés exclusivement en mémoire, pendant une durée maximale de cinq minutes, et ne sont pas enregistrés de manière permanente.

L’Application utilise également les succès Game Center, notamment le succès **Founder**, pour enregistrer l’accomplissement de certains objectifs et permettre la récupération des récompenses associées au moyen du même compte Game Center.

Les scores obtenus hors ligne peuvent être conservés temporairement sur l’appareil jusqu’à leur synchronisation.

Apple traite les données gérées par Game Center conformément à sa propre politique de confidentialité et aux conditions applicables au service.

L’utilisation de Game Center est facultative. Sans authentification, certaines fonctionnalités, notamment les classements, la synchronisation des scores et les succès liés au compte, peuvent ne pas être disponibles.

## 4. Achats intégrés

Les éventuels achats intégrés sont gérés par **StoreKit 2 et l’App Store**.

Girostella propose des achats non consommables portant sur des éléments cosmétiques du jeu, tels que des vaisseaux spatiaux et des traînées.

Le Responsable du traitement ne reçoit ni ne conserve les numéros de carte bancaire, les coordonnées bancaires, les identifiants du compte Apple ou les informations complètes relatives aux moyens de paiement.

L’Application reçoit les informations techniques nécessaires à la vérification et à la gestion des achats, notamment l’identifiant du produit, le résultat de la transaction et les identifiants techniques associés à celle-ci.

Les informations nécessaires à la gestion des éléments achetés et à la prévention d’un traitement en double des transactions peuvent être conservées localement sur l’appareil.

Les paiements, la facturation, les remboursements et l’historique des achats sont gérés par Apple conformément à ses propres conditions et politiques de confidentialité.

## 5. Vérification des mises à jour

Au démarrage, Girostella peut télécharger depuis **GitHub Pages** un fichier de configuration public contenant des informations relatives à la version minimale prise en charge de l’Application et à certains paramètres des classements.

La requête ne comprend pas de scores, de données de progression, d’identifiants Game Center ni d’autres données personnelles ajoutées par l’Application.

Comme cela se produit habituellement lors des communications sur Internet, le fournisseur du service peut recevoir l’adresse IP de l’appareil et des informations techniques relatives à la requête. Leur éventuel traitement et leur conservation sont régis par les conditions et les politiques de confidentialité du fournisseur.

Le Responsable du traitement n’utilise pas cette connexion pour collecter des données de jeu, effectuer du profilage ou surveiller individuellement les utilisateurs.

## 6. Publicité et gestion du consentement

Girostella est un jeu gratuit qui utilise **Google Mobile Ads (AdMob)** pour afficher des vidéos publicitaires récompensées.

Les publicités sont proposées uniquement lorsqu’un joueur, après avoir perdu une partie, choisit de regarder une vidéo pour obtenir une seconde chance et reprendre le jeu.

L’Application n’affiche pas de bannières publicitaires ni de vidéos publicitaires obligatoires pendant le déroulement normal des parties.

### Données traitées par les services publicitaires

Pour la diffusion, la mesure, la sécurité et l’amélioration des services publicitaires, Google Mobile Ads peut collecter et traiter, selon ses propres modalités et finalités :

- Les adresses IP et les informations de localisation géographique approximative déduites de l’adresse IP ;
- Les identifiants de l’appareil, de l’Application ou propres au développeur ;
- Les informations relatives aux publicités affichées et aux interactions avec les vidéos publicitaires ;
- Les données relatives à l’utilisation de l’Application et aux interactions avec celle-ci ;
- Les informations de diagnostic, les journaux de plantage et les données de performance.

Certaines informations peuvent être associées à des identifiants techniques et utilisées par Google et les fournisseurs publicitaires concernés, conformément à leurs conditions respectives et aux choix de confidentialité applicables.

Le Responsable du traitement ne reçoit pas directement de base de données individualisée contenant les données collectées par Google au moyen de ses SDK publicitaires.

### Consentement et préférences publicitaires

Pour les joueurs situés dans l’Espace économique européen, au Royaume-Uni et en Suisse, Girostella utilise **Google User Messaging Platform (UMP)** afin de présenter, lorsque cela est nécessaire, un message d’information sur les finalités du traitement et les fournisseurs publicitaires concernés.

Ce message permet aux joueurs de donner leur consentement, de le refuser ou de gérer les différentes options disponibles.

Les préférences peuvent ensuite être modifiées dans **Paramètres → Préférences publicitaires**, lorsque cette fonctionnalité est requise et mise à disposition par le système de gestion du consentement.

Les fournisseurs publicitaires peuvent traiter certaines données sur la base du consentement ou, lorsque cela est applicable et conforme à la réglementation, sur d’autres bases juridiques, notamment l’intérêt légitime. Les finalités, les fournisseurs et les options correspondantes sont décrits dans le message de consentement de Google.

Le refus du consentement n’empêche pas d’utiliser le jeu. Toutefois, la disponibilité des vidéos publicitaires récompensées peut varier selon les préférences exprimées, la réglementation applicable et la disponibilité des publicités.

Pour plus d’informations sur les traitements effectués par les services publicitaires, vous pouvez consulter :

- [Règles de confidentialité de Google](https://policies.google.com/privacy?hl=fr) ;
- [Utilisation par Google des informations provenant des sites ou applications qui utilisent ses services](https://policies.google.com/technologies/partner-sites?hl=fr).

## 7. Assistance

Si un utilisateur contacte volontairement le Responsable du traitement par e-mail, les informations suivantes peuvent être traitées : son adresse e-mail, le nom éventuellement indiqué, le contenu de sa demande, les éventuelles pièces jointes et les informations techniques fournies par l’utilisateur.

Ces données sont utilisées exclusivement pour répondre à la demande, fournir une assistance, gérer d’éventuels litiges ou respecter des obligations légales.

Les utilisateurs sont invités à ne pas transmettre de données personnelles qui ne sont pas nécessaires au traitement de leur demande.

## 8. Finalités et bases juridiques du traitement

| Finalité | Base juridique |
|---|---|
| Fonctionnement de l’Application et conservation de la progression | Exécution du service demandé, article 6, paragraphe 1, point b), du RGPD |
| Game Center, classements, succès et synchronisation | Exécution du service demandé, article 6, paragraphe 1, point b), du RGPD |
| Stockage local pseudonymisé des informations relatives aux autres joueurs | Intérêt légitime à assurer un affichage correct des classements, article 6, paragraphe 1, point f), du RGPD |
| Gestion des achats intégrés | Exécution d’un contrat, article 6, paragraphe 1, point b), du RGPD |
| Prévention des erreurs, des traitements en double et des abus | Intérêt légitime à assurer la sécurité et le bon fonctionnement du service, article 6, paragraphe 1, point f), du RGPD |
| Vérification de la version et des paramètres de l’Application | Exécution du service demandé, article 6, paragraphe 1, point b), du RGPD |
| Traitements publicitaires nécessitant le consentement | Consentement de la personne concernée, article 6, paragraphe 1, point a), du RGPD |
| Autres traitements publicitaires autorisés par la réglementation applicable | Bases juridiques indiquées par les fournisseurs, notamment, lorsque cela est applicable, l’intérêt légitime au sens de l’article 6, paragraphe 1, point f), du RGPD |
| Assistance aux utilisateurs | Exécution du service ou intérêt légitime à traiter les demandes, article 6, paragraphe 1, points b) et f), du RGPD |
| Respect des obligations légales | Obligation légale, article 6, paragraphe 1, point c), du RGPD |
| Constatation, exercice ou défense de droits en justice | Intérêt légitime, article 6, paragraphe 1, point f), du RGPD |

Lorsque le traitement repose sur le consentement, celui-ci peut être retiré au moyen des mécanismes proposés par le service de gestion des préférences, sans porter atteinte à la licéité des traitements effectués avant son retrait.

Lorsque le traitement repose sur l’intérêt légitime, la personne concernée peut exercer son droit d’opposition dans les conditions prévues à l’article 21 du RGPD.

## 9. Destinataires des données

Le Responsable du traitement ne vend pas directement les données personnelles des joueurs et ne constitue pas de base de données destinée à leur commercialisation.

Les données peuvent être traitées, lorsque cela est nécessaire, par :

- **Apple**, dans le cadre des services Game Center, App Store et StoreKit ;
- **Google**, par l’intermédiaire de Google Mobile Ads et Google User Messaging Platform, ainsi que les éventuels fournisseurs publicitaires participant à la diffusion des annonces ;
- Le fournisseur de **GitHub Pages**, dans le cadre des requêtes nécessaires au téléchargement du fichier de configuration public ;
- Le fournisseur du service de messagerie électronique utilisé pour l’assistance ;
- Des conseillers professionnels ou des autorités publiques dans les cas prévus par la loi.

Les informations conservées dans le cache local des classements ne sont pas communiquées par le Responsable du traitement à ces destinataires.

Les traitements effectués par l’intermédiaire de services externes sont soumis à leurs politiques de confidentialité respectives et aux conditions prévues par la réglementation applicable.

## 10. Transferts internationaux de données

Le Responsable du traitement n’exploite pas de serveurs propres destinés à la conservation des données de jeu.

L’utilisation des services fournis par Apple, Google et GitHub peut entraîner le traitement de données personnelles en dehors de l’Espace économique européen.

Ces traitements sont soumis aux conditions, aux politiques de confidentialité et aux garanties adoptées par les fournisseurs concernés, dans le respect des dispositions applicables aux transferts internationaux de données à caractère personnel.

Des informations concernant les transferts internationaux et les éventuelles garanties applicables peuvent être demandées au Responsable du traitement ou consultées dans les politiques de confidentialité des fournisseurs concernés.

## 11. Conservation des données

La progression, les préférences et les autres données conservées exclusivement sur l’appareil sont normalement maintenues jusqu’à la désinstallation de l’Application, à l’exception des éventuelles copies conservées dans les sauvegardes de l’appareil.

Le cache local des informations relatives aux autres joueurs contient au maximum **25 000 enregistrements**, sans durée de conservation prédéterminée. Lorsque cette limite est dépassée, les entrées les plus anciennes sont supprimées en premier. Les données sont normalement supprimées lors de la désinstallation de l’Application, à l’exception des éventuelles copies conservées dans les sauvegardes de l’appareil.

Les scores en attente de synchronisation sont conservés jusqu’à leur synchronisation, leur éventuelle expiration ou la suppression de l’Application.

Les préférences relatives au consentement publicitaire sont gérées au moyen d’UMP et de ses systèmes associés, selon les critères de conservation applicables et les conditions des fournisseurs.

Les données collectées par les services publicitaires sont conservées par Google et les autres fournisseurs éventuellement concernés conformément à leurs politiques de conservation respectives et aux finalités applicables.

Les demandes d’assistance sont conservées pendant la durée nécessaire à leur traitement et, en règle générale, pendant une période n’excédant pas **24 mois**, sauf obligation légale ou nécessité de protéger les droits du Responsable du traitement.

Les éventuels documents administratifs ou comptables sont conservés pendant les durées prévues par la réglementation applicable.

Les données gérées de manière autonome par Apple et les autres services externes sont conservées selon les critères définis par les fournisseurs concernés.

## 12. Droits des personnes concernées

Dans les conditions prévues aux articles 15 à 22 du RGPD, les personnes concernées peuvent exercer leurs droits d’accès, de rectification, d’effacement, de limitation du traitement, d’opposition et de portabilité des données.

Les demandes peuvent être envoyées à l’adresse e-mail indiquée dans la section **Responsable du traitement**.

Les données conservées exclusivement dans l’espace de stockage local de l’Application ne sont pas accessibles à distance par le Responsable du traitement. La désinstallation de l’Application entraîne normalement la suppression des données présentes dans son espace de stockage local, à l’exception des éventuelles copies conservées dans les sauvegardes de l’appareil.

Les demandes concernant les informations pseudonymisées relatives à d’autres joueurs et conservées localement sur les appareils des utilisateurs seront examinées au regard des possibilités techniques d’identification et d’intervention sur les données concernées, dans le respect des droits prévus par la réglementation applicable.

Les préférences relatives au consentement publicitaire peuvent être gérées au moyen de la fonctionnalité **Préférences publicitaires**, disponible dans les paramètres de l’Application lorsqu’elle est prévue.

Pour les données gérées de manière autonome par Game Center, l’App Store ou d’autres services Apple, les personnes concernées peuvent utiliser les outils mis à disposition par Apple. De même, pour les traitements effectués par les fournisseurs publicitaires, les outils de gestion de la confidentialité correspondants peuvent être utilisés.

Les personnes concernées ont également le droit d’introduire une réclamation auprès de l’**Autorité italienne de protection des données personnelles (Garante per la protezione dei dati personali)**, conformément à l’article 77 du RGPD.

## 13. Mineurs

Girostella ne demande pas aux utilisateurs de fournir des données d’identité civile et ne propose pas de chat, de messagerie ou de fonctionnalités permettant aux utilisateurs de publier librement du contenu.

L’utilisation de Game Center, de l’App Store et des achats par les mineurs est soumise aux paramètres du compte Apple, aux fonctionnalités familiales et aux restrictions proposées par Apple.

Tout traitement de données publicitaires relatives aux mineurs est soumis aux restrictions prévues par la réglementation applicable et aux paramètres adoptés par les services publicitaires utilisés par l’Application.

Si le Responsable du traitement reçoit, dans le cadre de l’assistance, des données personnelles concernant un mineur qui ne sont pas nécessaires au traitement de la demande, ces données seront supprimées lorsqu’aucun autre motif légitime ne justifie leur conservation.

## 14. Sécurité, profilage et prise de décision automatisée

Les données locales de l’Application sont conservées dans l’environnement isolé (« sandbox ») prévu par iOS.

L’Application utilise, lorsque cela est prévu, des identifiants pseudonymisés afin de limiter la conservation d’informations directement attribuables à d’autres joueurs.

Les communications avec Game Center et l’App Store utilisent les frameworks et les systèmes de sécurité fournis par Apple.

Le Responsable du traitement adopte des mesures raisonnables et proportionnées pour protéger les données personnelles contre les accès non autorisés, la perte ou l’altération.

Girostella ne crée pas de manière autonome de profils publicitaires des joueurs et ne procède pas à des décisions automatisées produisant des effets juridiques ou des effets significatifs similaires sur les utilisateurs au sens de l’article 22 du RGPD.

Les fournisseurs publicitaires peuvent traiter des données aux fins de sélection, de personnalisation ou de mesure des publicités, conformément aux finalités et aux bases juridiques applicables.

## 15. Modifications de la présente politique de confidentialité et coordonnées

La présente politique de confidentialité peut être mise à jour en cas de modifications de l’Application, des services utilisés ou de la réglementation applicable.

La version actualisée sera publiée à la même adresse et indiquera sa date de mise à jour. En cas de modifications importantes, une notification pourra être affichée dans l’Application.

Pour toute information, demande ou pour exercer vos droits relatifs à la protection des données personnelles :

**[alessandro_penna@icloud.com](mailto:alessandro_penna@icloud.com)**