from core.models import *
def main(request):
    return {
            'services': ServicePage.objects.all(), 
            'personals': Personal.objects.all(),
            'comments': Comment.objects.filter(published=True).select_related('user')
            }
