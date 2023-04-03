from rest_framework import serializers
from . models import Movie


class MoviesSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()


    class Meta:
        model = Movie
        fields = '__all__'

    def get_len_name(self, object):
        return len(object.name)

    def validate(self, data):
        if data['name'] == data[ 'description']:
            raise serializers.ValidationError('Title and Decription should be different!')
        else:
            return data