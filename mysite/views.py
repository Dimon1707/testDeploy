# from django.shortcuts import render
#
# from mysite import Contact
#
# def index(reqest):
#     if reqest.metod == 'POST':
#         data = reqest.POST
#         name = data['name']
#         phone = data['phone']
#         a = Contact(name=name, phone=phone)
#         a.save()
#     return render(reqest, 'index.html')


from django.shortcuts import render


def index(request):
    return render(request, 'index.html')