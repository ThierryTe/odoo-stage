{
    
'name':"stage",
'author':"nebrataTeam",
'description':"Module de test permettant d'obtenir les relations entre stagiaires et leur maitre de stage",

'depends': ['base'],
'application': True,
'data':['security/stage_security.xml',
        'security/ir.model.access.csv',
        'views/stage_responsable_view.xml',
        'views/stage_stagiaire_view.xml',
        'views/taf_view.xml',
        'report.xml',
        ],

}
