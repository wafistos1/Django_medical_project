from django.db import models
from accounts.models import CostumUser, PatientUser


class enregistrementsInformations(models.Model):
    
    date_creation_enregistrement = models.DateTimeField(auto_now_add=True)
    date_derniere_modification_enregistrement = models.DateTimeField(auto_now=False)
    
    #Informations générales
    poids = models.DecimalField(max_digits=5, decimal_places=2)
    tour_de_taille_en_centimetre = models.DecimalField(max_digits=5, decimal_places=2)
    
    #Informations cardiaques et tension artérielle
    frequence_cardiaque_par_minute = models.IntegerField()
    tension_arterielle_systolique_prise_matin = models.IntegerField()
    tension_arterielle_systolique_prise_soir = models.IntegerField()
    tension_arterielle_diastolique_prise_matin = models.IntegerField()
    tension_arterielle_diastolique_prise_soir = models.IntegerField()
    description_symptome_cardiovasculaire = models.TextField(null=True)
    
    #Prise de médicaments
    medicaments_nombre_par_jour = models.IntegerField()
    medicaments_oublie_matin = models.BooleanField(default=False)
    medicaments_oublie_soir = models.BooleanField(default=False)
    effet_secondaire_remarque = models.BooleanField(default=False)
    medicaments_symptomes_particuliers = models.BooleanField(default=False)
    medicaments_effet_secondaire_description = models.TextField(null=True)
    
    #Alimentation
    consommation_alcool = models.BooleanField(default=False)
    grignotage_sucre = models.BooleanField(default=False)
    grignotage_sale = models.BooleanField(default=False)
    alimentation_nombre_repas_par_jour = models.IntegerField()
    alimentation_quantite_eau = models.DecimalField(max_digits=5, decimal_places=2)
    alimentation_alcool_consommation = models.DecimalField(max_digits=5, decimal_places=2)
    
    #Activité physique
    activite_physique_presence = models.BooleanField(default=False)
    activite_physique_nature = models.CharField(max_length=200)
    activite_physique_duree = models.IntegerField()
    
    #Autres symptômes
    dyspnee = models.BooleanField(default=False)
    oedeme_presence = models.BooleanField(default=False)
    episode_infectieux_presence = models.BooleanField(default=False)
    fievre_presence = models.BooleanField(default=False)
    palpitations_presence = models.BooleanField(default=False)
    douleur_thoracique_presence = models.BooleanField(default=False)
    malaise_presence = models.BooleanField(default=False)
    palpitations_horaire = models.DateTimeField(auto_now_add=True)
    palpitations_duree = models.IntegerField()
    douleur_thoracique_horaire = models.DateTimeField(auto_now_add=True)
    douleur_thoracique_duree = models.IntegerField()
    malaise_horaire = models.DateTimeField(auto_now_add=True)
    malaise_duree = models.IntegerField()
    
     #Autres informations médicales
    natremie = models.DecimalField(max_digits=5, decimal_places=2)
    potassium = models.DecimalField(max_digits=5, decimal_places=2)
    creatinine = models.DecimalField(max_digits=5, decimal_places=2)
    clairance_de_la_creatinine_mdrd = models.DecimalField(max_digits=5, decimal_places=2)
    ntprobnp = models.DecimalField(max_digits=5, decimal_places=2)
    fer_serique = models.DecimalField(max_digits=5, decimal_places=2)
    taux_hemoglobine = models.DecimalField(max_digits=5, decimal_places=2)
    vs = models.DecimalField(max_digits=5, decimal_places=2)
    crp = models.DecimalField(max_digits=5, decimal_places=2)
    troponine = models.DecimalField(max_digits=5, decimal_places=2)
    taux_vitamine_d = models.DecimalField(max_digits=5, decimal_places=2)
    taux_acide_urique = models.DecimalField(max_digits=5, decimal_places=2)
    inr = models.DecimalField(max_digits=5, decimal_places=2)
    patients_id = models.ForeignKey(PatientUser, on_delete=models.CASCADE)
    

    class StressEvaluation(models.Model):
        LIST_VALEURS = (
            (0, 0),
            (1, 1),
            (5, 5),
            (10, 10),
        )
        patients_id = models.ForeignKey(PatientUser, on_delete=models.CASCADE)
        doctor = models.ForeignKey(CostumUser, on_delete=models.SET_NULL, null=True)
        irritabilte = models.IntegerField(choices=LIST_VALEURS, default=0)
        depressif = models.IntegerField(choices=LIST_VALEURS, default=0)
        bouche_gorge_seche = models.IntegerField(choices=LIST_VALEURS, default=0)
        geste_impulsif = models.IntegerField(choices=LIST_VALEURS, default=0)
        grincement_dent = models.IntegerField(choices=LIST_VALEURS, default=0)
        difficulte_assis = models.IntegerField(choices=LIST_VALEURS, default=0)
        cauchemar = models.IntegerField(choices=LIST_VALEURS, default=0)
        diarrhee = models.IntegerField(choices=LIST_VALEURS, default=0)
        attaque_verbale = models.IntegerField(choices=LIST_VALEURS, default=0)
        haut_bas_emotif = models.IntegerField(choices=LIST_VALEURS, default=0)
        envie_pleurer = models.IntegerField(choices=LIST_VALEURS, default=0)
        envie_fuir = models.IntegerField(choices=LIST_VALEURS, default=0)
        envie_faire_mal = models.IntegerField(choices=LIST_VALEURS, default=0)
        pensee_embrouille = models.IntegerField(choices=LIST_VALEURS, default=0)
        debit_rapide = models.IntegerField(choices=LIST_VALEURS, default=0)
        fatigue = models.IntegerField(choices=LIST_VALEURS, default=0)
        etre_surcharge = models.IntegerField(choices=LIST_VALEURS, default=0)
        emotivement_fragile = models.IntegerField(choices=LIST_VALEURS, default=0)
        tristresse = models.IntegerField(choices=LIST_VALEURS, default=0)
        anxiete = models.IntegerField(choices=LIST_VALEURS, default=0)
        tension = models.IntegerField(choices=LIST_VALEURS, default=0)
        hostilite = models.IntegerField(choices=LIST_VALEURS, default=0)
        tremblement = models.IntegerField(choices=LIST_VALEURS, default=0)
        begaiement = models.IntegerField(choices=LIST_VALEURS, default=0)
        difficulte_concentrer = models.IntegerField(choices=LIST_VALEURS, default=0)
        organiser_pensee = models.IntegerField(choices=LIST_VALEURS, default=0)
        dormir_nuit_sans_reveille = models.IntegerField(choices=LIST_VALEURS, default=0) 
        frequence_uriner =  models.IntegerField(choices=LIST_VALEURS, default=0)
        maux_estomac = models.IntegerField(choices=LIST_VALEURS, default=0)
        geste_impatience = models.IntegerField(choices=LIST_VALEURS, default=0)
        maux_tete = models.IntegerField(choices=LIST_VALEURS, default=0)
        douleur_dos_nuque = models.IntegerField(choices=LIST_VALEURS, default=0)
        perte_gain_appetit = models.IntegerField(choices=LIST_VALEURS, default=0)
        perte_gain_sexe = models.IntegerField(choices=LIST_VALEURS, default=0)
        oublis_frequent = models.IntegerField(choices=LIST_VALEURS, default=0)
        douleur_poitrine = models.IntegerField(choices=LIST_VALEURS, default=0)
        conflits_avec_autres = models.IntegerField(choices=LIST_VALEURS, default=0)
        difficulte_leve_apres_sommeil = models.IntegerField(choices=LIST_VALEURS, default=0)
        hors_controle = models.IntegerField(choices=LIST_VALEURS, default=0)
        faire_longue_activite = models.IntegerField(choices=LIST_VALEURS, default=0)
        isolement = models.IntegerField(choices=LIST_VALEURS, default=0)
        dfficulte_dormir = models.IntegerField(choices=LIST_VALEURS, default=0)
        difficulte_remettre = models.IntegerField(choices=LIST_VALEURS, default=0)
        main_moite = models.IntegerField(choices=LIST_VALEURS, default=0)
         
        
        def __str__(self):
            return f'{self.patients_id.identifier}- suivi par {self.doctor.identifier}'

    