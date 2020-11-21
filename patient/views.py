from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from accounts.forms import LoginForm, UserRegisterForm
from accounts.models import CostumUser, PatientUser
from .models import enregistrementsInformations
from .froms  import RegisterPatientForm
from django.conf import settings
from random import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR


User = settings.AUTH_USER_MODEL


def home_patient(request):
    return render(request, 'patient/home_patient.html')


def check_identifier():
    liste  = []
    identifier = None
    for iden in PatientUser.objects.all():
        liste.append(str(iden.identifier))
    while True:
        identifier = randint(1000, 9999)
        if identifier  not in liste:
            break
    return identifier
    



    

class LoginPatientView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, "index.html", context)
    
    def post(self, request):
        form = LoginForm(request.POST or None)
        identifier = request.POST.get("identifier", None)
        password = request.POST.get("password", None)
        print('id', identifier, 'pass', password)
        try:
            user = authenticate(identifier=identifier, password = password)
        except:
            messages.add_message(request,ERROR , f'Password or Id error')
            print('password ou id error ')
            return redirect('login_patient')
        if user:
            login(request, user)
            return redirect('add_patient_form')
        else:
            messages.add_message(request,ERROR , f'Password or Id error')
            
        context = {
            'form': form,
        }
        return render(request, "patient/login_patient.html", context)
    


def logout_patient(request):
    logout(request)
    return redirect('home_patient')

def static_view(request):
    return render(request, 'patient/static_view.html')


class AddPatientFrom(View):
    
    def get(self, request):
        form = RegisterPatientForm()
        context = {
            'form': form,
        }
        return render(request, "patient/formulaire.html", context)
    
    def post(self, request):
        # form = RegisterPatientForm(request.POST or None)
        
        #Informations générales
        poids = request.POST.get('poids')
        tour_de_taille_en_centimetre = request.POST.get('tour_de_taille_en_centimetre')
        
        #Informations cardiaques et tension artérielle
        frequence_cardiaque_par_minute = request.POST.get('frequence_cardiaque_par_minute')
        tension_arterielle_systolique_prise_matin = request.POST.get('tension_arterielle_systolique_matin')
        tension_arterielle_systolique_prise_soir = request.POST.get('tension_arterielle_systolique_prise_soir')
        tension_arterielle_diastolique_prise_matin = request.POST.get('tension_arterielle_diastolique_prise_matin')
        tension_arterielle_diastolique_prise_soir = request.POST.get('tension_arterielle_diastolique_prise_soir')
        description_symptome_cardiovasculaire = request.POST.get('description_symptome_cardiovasculaire')
        
        #Prise de médicaments
        medicaments_nombre_par_jour = request.POST.get('nombre_medicament')
        medicaments_oublie_matin = request.POST.get('oubli_medicament_matin')
        medicaments_oublie_soir = request.POST.get('oubli_medicament_soir')
        effet_secondaire_remarque = request.POST.get('effet_secondaire_remarque')
        medicaments_symptomes_particuliers = request.POST.get('symptome_particulier_remarque')
        medicaments_effet_secondaire_description = request.POST.get('description_effet_secondaire')
        
        #Alimentation
        consommation_alcool = request.POST.get('consommation_alcool')
        grignotage_sucre = request.POST.get('grignotage_sucre')
        grignotage_sale = request.POST.get('grignotage_sale')
        alimentation_nombre_repas_par_jour = request.POST.get('nombre_de_repas_par_jour')
        alimentation_quantite_eau = request.POST.get('quantite_eau_bu')
        alimentation_alcool_consommation = request.POST.get('quantite_alcool_bu')
        
        #Activité physique
        activite_physique_presence = request.POST.get('activite_physique_presence')
        activite_physique_nature = request.POST.get('activite_physique_nature')
        activite_physique_duree = request.POST.get('activite_physique_duree')
        
        #Autres symptômes
        dyspnee = request.POST.get('dyspnee')
        oedeme_presence = request.POST.get('oedeme_presence')
        episode_infectieux_presence = request.POST.get('episode_infectieux_presence')
        fievre_presence = request.POST.get('fievre_presence')
        palpitations_presence = request.POST.get('palpitations_presence')
        douleur_thoracique_presence = request.POST.get('douleur_thoracique_presence')
        malaise_presence = request.POST.get('malaise_presence')
        palpitations_horaire = request.POST.get('palpitations_horaire')
        palpitations_duree = request.POST.get('palpitations_duree')
        douleur_thoracique_horaire = request.POST.get('douleur_thoracique_horaire')
        douleur_thoracique_duree = request.POST.get('douleur_thoracique_duree')
        malaise_horaire = request.POST.get('malaise_horaire')
        malaise_duree = request.POST.get('malaise_duree')
        
        #Autres informations médicales
        natremie = request.POST.get('natremie')
        potassium = request.POST.get('potassium')
        creatinine = request.POST.get('creatinine')
        clairance_de_la_creatinine_mdrd = request.POST.get('clairance_de_la_creatinine_mdrd')
        ntprobnp = request.POST.get('ntprobnp')
        fer_serique = request.POST.get('fer_serique')
        taux_hemoglobine = request.POST.get('taux_hemoglobine')
        vs = request.POST.get('vs')
        crp = request.POST.get('crp')
        troponine = request.POST.get('troponine')
        taux_vitamine_d = request.POST.get('taux_vitamine_d')
        taux_acide_urique = request.POST.get('taux_acide_urique')
        inr = request.POST.get('inr')
        
        try:
            
            daily_form = enregistrementsInformations.objects.create(
                poids =poids,
                tour_de_taille_en_centimetre=tour_de_taille_en_centimetre,
                
                #Informations cardiaques et tension artérielle
                frequence_cardiaque_par_minute=frequence_cardiaque_par_minute,
                tension_arterielle_systolique_prise_matin=tension_arterielle_systolique_prise_matin,
                tension_arterielle_systolique_prise_soir=tension_arterielle_systolique_prise_soir,
                tension_arterielle_diastolique_prise_matin =tension_arterielle_diastolique_prise_matin, 
                tension_arterielle_diastolique_prise_soir = tension_arterielle_diastolique_prise_soir,
                description_symptome_cardiovasculaire=description_symptome_cardiovasculaire,
                
                #Prise de médicaments
                medicaments_nombre_par_jour=medicaments_nombre_par_jour,
                medicaments_oublie_matin =medicaments_oublie_matin,
                medicaments_oublie_soir = medicaments_oublie_soir,
                effet_secondaire_remarque = effet_secondaire_remarque, 
                medicaments_symptomes_particuliers = medicaments_symptomes_particuliers,
                medicaments_effet_secondaire_description = medicaments_effet_secondaire_description,
                
                #Alimentation
                consommation_alcool =consommation_alcool,
                grignotage_sucre =grignotage_sucre,
                grignotage_sale =grignotage_sale,
                alimentation_nombre_repas_par_jour =alimentation_nombre_repas_par_jour,
                alimentation_quantite_eau =alimentation_quantite_eau,
                alimentation_alcool_consommation = alimentation_alcool_consommation,
                
                #Activité physique
                activite_physique_presence = activite_physique_presence,
                activite_physique_nature = activite_physique_nature,
                activite_physique_duree = activite_physique_duree,
                
                #Autres symptômes
                dyspnee = dyspnee,
                oedeme_presence =oedeme_presence,
                episode_infectieux_presence = episode_infectieux_presence,
                fievre_presence = fievre_presence,
                palpitations_presence = palpitations_presence,
                douleur_thoracique_presence = douleur_thoracique_presence,
                malaise_presence = malaise_presence,
                palpitations_horaire = palpitations_horaire,
                palpitations_duree = palpitations_duree,
                douleur_thoracique_horaire = douleur_thoracique_horaire,
                douleur_thoracique_duree = douleur_thoracique_duree,
                malaise_horaire = malaise_horaire,
                malaise_duree = malaise_duree,
                
                #Autres informations médicales
                natremie = natremie,
                potassium = potassium,
                creatinine = creatinine,
                clairance_de_la_creatinine_mdrd = clairance_de_la_creatinine_mdrd,
                ntprobnp = ntprobnp,
                fer_serique = fer_serique,
                taux_hemoglobine = taux_hemoglobine,
                vs = vs,
                crp =crp,
                troponine =troponine,
                taux_vitamine_d =taux_vitamine_d,
                taux_acide_urique =taux_acide_urique,
                inr=inr,
                
               
            )
            messages.success(request, 'information ajoutees  au formulaire avec succes')
            redirect('/')
        except:
            print('error object created ')
        
        
        context = {
            # 'form': form,
        }
        return render(request, "patient/formulaire.html", context)


class AddPatientEvaluationFrom(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass


class RecapitulafiForm(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass


class DashboardView(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass
    
def updatePatientInfo(request, id):
     
     patient = PatientUser.objects.get(id=id)
     
     context = {
         'patient': patient
     }
     
     return render(request, 'patient/parametresPatients.html', context)