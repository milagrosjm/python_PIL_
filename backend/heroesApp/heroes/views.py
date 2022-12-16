from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from heroes.models import Hero
from heroes.serializer import HeroSerializer
from heroes.helpers.heroeErrors import heroeExists
from rest_framework.decorators import api_view


# Create your views here. Cada view tiene una url

class HeroApiView(APIView):

    def get(self, request):
        """Retorna una lista con todos los heroes"""

        #Busco los objetos heroes que tengo en la base de datos
        heroes = Hero.objects.all()

        #Serializo para poder enviar al front
        heroes_serializer = HeroSerializer(heroes, many=True)
        
        return Response(data=heroes_serializer.data, status=status.HTTP_200_OK)

class CreateHeroApiView(APIView):

     def post(self, request):
        """"Crea un nuevo heroe"""

        serializer = HeroSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            
            data = {
                'mensaje': 'Post funciona'
            }

            return Response(
                data=data, status=status.HTTP_201_CREATED
            )
        
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class DetailHeroApiView(APIView):

    def get (self, request, pk):
        
        try: 
            heroe = Hero.objects.get(id=pk)

            heroe_serializer = HeroSerializer(heroe)

            return Response(
                data=heroe_serializer.data,
                status=status.HTTP_200_OK
            )
        except:
            data = {
                'mensaje': 'El heroe no existe'
            }
            return Response(
                data=data,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk):
        
        response = heroeExists(pk)

        if response[0]:

            heroe_serializer = HeroSerializer(response[1], data=request.data)

            if heroe_serializer.is_valid():
                heroe_serializer.save()
                
                data = {
                    'mensaje': 'Put funciona'
                }

                return Response(
                    data=heroe_serializer.data,
                    status=status.HTTP_200_OK
                )

        return Response(
            data=heroe_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        
        heroe = Hero.objects.get(id=pk)
        heroe.delete()

        data = {
            'mensaje': 'El delete funciona'
        }

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )

# Con Decoradores

@api_view(['GET'])
def hero_api_view(request):
    
    #Busco los objetos heroes que tengo en la base de datos
    heroes = Hero.objects.all()

    #Serializo para poder enviar al front
    heroes_serializer = HeroSerializer(heroes, many=True)
        
    return Response(data=heroes_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def hero_detail_api_view(request, pk):
    
    if request.method == 'GET':
        try: 
            heroe = Hero.objects.get(id=pk)

            heroe_serializer = HeroSerializer(heroe)

            return Response(
                data=heroe_serializer.data,
                status=status.HTTP_200_OK
            )
        except:
            data = {
                'mensaje': 'El heroe no existe'
            }
            return Response(
                data=data,
                status=status.HTTP_400_BAD_REQUEST
            )
    elif request.method == 'PUT':
        response = heroeExists(pk)

        if response[0]:

            heroe_serializer = HeroSerializer(response[1], data=request.data)

            if heroe_serializer.is_valid():
                heroe_serializer.save()
                
                data = {
                    'mensaje': 'Put funciona'
                }

                return Response(
                    data=heroe_serializer.data,
                    status=status.HTTP_200_OK
                )

        return Response(
            data=heroe_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'DELETE':
        heroe = Hero.objects.get(id=pk)
        heroe.delete()

        data = {
            'mensaje': 'El delete funciona'
        }

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )







