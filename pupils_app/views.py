from django.shortcuts import render

# Create your views here.


pupils_list=[
    {"id":1,"Ism": "Alijonov Asilbek", "math": 5, "pyh": 4, "history": 3,"image":"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2Fkakashi--87679523989107131%2F&psig=AOvVaw0FxLoODejoVOH_PZkD8mRm&ust=1710091032073000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCIDMutbX54QDFQAAAAAdAAAAABAE"},
    {"id":2,"Ism": "Qosimov Shohruz", "math": 4, "pyh": 3, "history": 5,"image":"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wionews.com%2Fweb-stories%2Ftrending%2Ftop-10-best-ninja-anime-of-all-time-1688104838221&psig=AOvVaw0FxLoODejoVOH_PZkD8mRm&ust=1710091032073000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCIDMutbX54QDFQAAAAAdAAAAABAJ"},
    {"id":3,"Ism": "Xudoyberdiyev Komil", "math": 3, "pyh": 5, "history": 4},
    {"id":4,"Ism": "Zokirov Navruz", "math": 4, "pyh": 5, "history": 4},
    {"id":5,"Ism": "Olimov Shavkat", "math": 5, "pyh": 4, "history": 3},
    {"id":6,"Ism": "Rahmonov Farhod", "math": 3, "pyh": 4, "history": 5},
    {"id":7,"Ism": "Nigmatov Asadbek", "math": 4, "pyh": 3, "history": 4},
    {"id":8,"Ism": "Xolmurodov Odil", "math": 3, "pyh": 5, "history": 4},
    {"id":9,"Ism": "Karimov Jahongir", "math": 5, "pyh": 4, "history": 3},
    {"id":10,"Ism": "Tursunov Dilshod", "math": 4, "pyh": 5, "history": 4}
]

def pupils(request):
    return render(request,'pupils_list.html',context={'pupils':pupils_list})


def pupil_info(request,pk):
    return render(request,"pupil_info.html",context={'pupil':pupils_list[pk-1]})







