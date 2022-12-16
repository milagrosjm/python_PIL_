from heroes.models import Hero

def heroeExists(pk):

    try:
        heroe= Hero.objects.get(id=pk)

        return [True, heroe]

    except:

        return [False]
