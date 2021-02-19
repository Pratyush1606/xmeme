from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from memeStream.models import Meme
from memeStream.serializers import MemeSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404

schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

# Creating class based API view for /memes requests
class meme_list(APIView):
    """
    List all meme contents, or create a new meme content
    """
    # method for getting upto 100 latest Memes for API request /memes in json format
    def get(self, request):
        meme = Meme.objects.all()
        serializer = MemeSerializer(meme, many=True)
        return Response(serializer.data[-100:].__reversed__())

    # method for posting the Meme using API resquest /memes
    def post(self, request):
        serializer = MemeSerializer(data=request.data)
        # validating if the post request data
        if serializer.is_valid():
            serializer.save()
            # sending response containing the id of the posted meme with a status code
            return Response({"id":serializer.data.get("id")}, status=status.HTTP_201_CREATED)
        # sending bad request for invalid request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Creating class based API view for /memes/<int:pk> requests
class meme_detail(APIView):
    """
    Retrieve, update or delete a meme content
    """
    # checking if the meme exists or not with the requested id
    def get_object(self, pk):
        try:
            return Meme.objects.get(pk=pk)
        except Meme.DoesNotExist:
            # raising a htt404 response if no meme found with requested id
            raise Http404

    # method for getting the meme in json format
    def get(self, request, pk):
        meme = self.get_object(pk)
        serializer = MemeSerializer(meme) # Serialising the meme
        return Response(serializer.data)
    
    # method for the patch request
    def patch(self, request, pk):
        meme = self.get_object(pk)
        # checking if the name field being tried to be updated
        if(request.data.get("name",None)!=None):
            # removing the name update request as it is not permitted
            del request.data["name"]
        # Partially updating the meme instance
        serializer = MemeSerializer(meme, data=request.data, partial=True)
        # validating the PATCH request
        if serializer.is_valid():
            serializer.save()
            # sending response with 201 status status code and a message "Updated Meme :)"
            return Response(status=status.HTTP_201_CREATED, data="Updated Meme :)")
        # sending bad request for invalid request
        return HttpResponse("Wrong Parameters", status=status.HTTP_404_NOT_FOUND)

# Creating class based API view for renderring the HTML pages and getting the post request from the base html page
class meme_list_1(APIView):
    """
    List all meme contents, or create a new meme content
    """
    # class for renderring HTML page based on a template
    renderer_classes = [TemplateHTMLRenderer]

    # method for renderring the first html page for posting memes
    def get(self, request):
        form = MemeSerializer() # Form serializer for getting the data of new memes

        # renderring meme_detail.html page, having the form for posting new memes
        return Response({"form": form},template_name="meme_detail.html")

    # method for receving the post request from meme_detail.html for saving the new memes
    def post(self, request):
        # Serialising the requested data
        serializer = MemeSerializer(data=request.data)
        # redirecting back to the meme_detail.html page if the posted data is invalid
        if not serializer.is_valid():
            return redirect("/")

        # saving the meme
        serializer.save()
        meme = Meme.objects.all()
        serializer = MemeSerializer(meme, many=True)
        # sending a response for dispalying the latest 100 memes on meme_list.hmtl page with a status code for the successfull post request
        return Response({"memes": serializer.data[-100:].__reversed__(), "form": MemeSerializer()},template_name="meme_list.html", status=status.HTTP_201_CREATED)
        
# a teamporary api for getting the latest 100 memes
class meme_list_2(APIView):
    """
    List all meme contents, or create a new meme content
    """
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        meme = Meme.objects.all()
        serializer = MemeSerializer(meme, many=True)
        form = MemeSerializer()
        return Response({"memes": serializer.data[-100:].__reversed__(), "form": form},template_name="meme_list.html", status=status.HTTP_201_CREATED)

# function for deleting the meme after getting triggered from the delete button on meme_list.html 
def delete_meme(request, pk):
    # checking if the meme exists or not
    # However it must be there as the button would be on the meme card but still this function is implemented because if the button is repeatedly clicked before loading of the new meme_list.html page, it would handle that request
    try:
        meme = Meme.objects.get(pk=pk)
    except Meme.DoesNotExist:           
        raise Http404

    if request.method == "POST":
        meme.delete()
        return redirect("meme_list")

# Creating class based API view for updating or say editing a meme, being called from the update button in the meme_list.html
class update_meme(APIView):
    # checking if the meme exists
    def get_object(self, pk):
        try:
            return Meme.objects.get(pk=pk)
        except Meme.DoesNotExist:
            raise Http404
    
    # method for renderring the update_meme.html
    def get(self, request, pk):
        meme = self.get_object(pk)
        serializer = MemeSerializer(meme)
        form = MemeSerializer()
        # making the name field read only as the name is not allowed to be changed
        form.fields.get("name").read_only = True
        # renderring update.html with a form conatining "editable" url and caption fields and the current meme data
        return render(request, "update.html", {"meme": serializer.data, "form": form})

    # method for posting the updating the meme data
    def post(self, request, pk):
        meme = self.get_object(pk)
        # extracting the url and caption fields from the request data
        url = request.data.get("url")
        caption = request.data.get("caption")

        d = {} # dictionary for storing the data that needs to be changed
        # checking if the url field is empty or not
        if(url!=""):
            # if not empty, means it contains some data to be updated, add it to the dictionary
            d["url"] = url
        # checking if the caption field is empty or not
        if(caption!=""):
            # if not empty, means it contains some data to be updated, add it to the dictionary
            d["caption"] = caption
        
        # partially update the meme instance
        serializer = MemeSerializer(meme, data=d, partial=True)
        # validating the new updated data
        if serializer.is_valid():
            serializer.save()
            # after saving, redirecting back to the meme_list.html
            return redirect("meme_list")
        return HttpResponse("Wrong Parameters", status=status.HTTP_404_NOT_FOUND)