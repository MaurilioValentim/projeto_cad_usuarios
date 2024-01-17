from django.shortcuts import render, redirect
import requests
import json


# Create your views here.
def home(request):

    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Receber Dados
    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    url = 'https://api.thingspeak.com/channels/2405090/feeds.json?api_key=UBFU1RWZF7YCM9KX&results=2'
    
    response = requests.get(url)
    data = json.loads(response.text)
    last_entry_id = data["channel"]["last_entry_id"]
    #Tensao
    field1_value = data["channel"]["field1"]
    field1_value = None
    #Corrente
    field2_value = data["channel"]["field2"]
    field2_value = None
    #Potencia
    field3_value = data["channel"]["field3"]
    field3_value = None
    
    #Frequencia
    field4_value = data["channel"]["field4"]
    field4_value = None
    
    #Estado do Dia
    field5_value = data["channel"]["field5"]
    field5_value = None
    
    #Estado da Luminaria
    field6_value = data["channel"]["field6"]
    field6_value = None
    
    
    
    for feed in data["feeds"]:
        if feed["entry_id"] == last_entry_id:
            #Tensao
            field1_value = feed["field1"]
            #Corrente
            field2_value = feed["field2"]
            #Potencia
            field3_value = feed["field3"]
            #Frequencia
            field4_value = feed["field4"]
            #Estado do Dia
            field5_value = feed["field5"]
            #Estado da Luminaria
            field6_value = feed["field6"]
            
            break

    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    #Intensidade
    #---------------------------------------------------------------------------------------------------------------------------------------------------------
        
    url1 = 'https://api.thingspeak.com/channels/2405035/feeds.json?api_key=7NFYJ4K0WIBOGKSL&results=2'
    response1 = requests.get(url1)
    data1 = json.loads(response1.text)
    last_entry_id1 = data1["channel"]["last_entry_id"]

    field8_value = data1["channel"]["field1"]
    field8_value = None

    for feed in data1["feeds"]:
        if feed["entry_id"] == last_entry_id1:
            
            #Intensidade
            field8_value = feed["field1"]
            break
    #---------------------------------------------------------------------------------------------------------------------------------------------------------
        
    #Tensao
    valor1 = field1_value 
    #Corrente
    valor2 = field2_value
    #Potencia
    valor3 = field3_value

    #Fator de Potencia
    
    valor4 = float(valor3)/(float(valor1)* float(valor2))
    
    #Frequencia
    valor5 = field4_value
    #Estado do Dia
    #valor6 = field5_value

    if  field5_value == '1':
        valor6 = 'Noite'
    else:
        valor6 = 'Dia'

    #Estado da Luminaria
    #valor7 = field6_value
    if  field6_value == '1':
        valor7 = 'Ligado'
    else:
        valor7 = 'Desligado'

    #Intensidade
    valor8 = field8_value

    return render(request,'usuarios/home.html', { 'Tensao': valor1, 'Corrente': valor2, 'Potencia': valor3, 'fp': valor4, 'frequencia': valor5, 'EstadoDia': valor6, 'EstadodaLuminaria': valor7, 'Intensidadea': valor8})


#Enviar os dados
def recebevalor(request):
    
        if request.method == 'POST':
            texto = request.POST.get('texto')
            valor2 = request.POST.get('texto2')
            valor3 = request.POST.get('texto3')
            valor4 = request.POST.get('texto4')
            valor5 = request.POST.get('texto5')
            valor6 = request.POST.get('texto6')
            valor7 = request.POST.get('texto7')
            valor8 = request.POST.get('texto8')
            if texto:
                print(texto)
                url = 'https://api.thingspeak.com/update?api_key=676O239213T88NGE&field1=' + valor8
                #url = 'https://api.thingspeak.com/update?api_key=60GSXN7N64BU0PSQ&field1='+ texto + '&field2=' + valor2 + '&field3=' + valor3 + '&field4=' + valor4 + '&field5=' + valor5 + '&field6=' + valor6 + '&field7=' + valor7 + '&field8=' + valor8
                response = requests.get(url)
            
        return redirect('/')