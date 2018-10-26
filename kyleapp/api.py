from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = PersonalNote
        fields = ('title', 'content')
    

    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    # queryset = PersonalNote.objects.all()



# django calls the below itself, so we dont need to personally call it 

    def get_queryset(self):
        # import pdb; pdb.set_trace()

        logged_in_user = self.request.user

        if logged_in_user.is_anonymous:
            return PersonalNote.objects.none()
        else: 
            return PersonalNote.objects.filter(user=logged_in_user)
