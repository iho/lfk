from core.models import *
def main(request):
    return {'cc': "",

            'services': ServicePage.objects.all()
            }
