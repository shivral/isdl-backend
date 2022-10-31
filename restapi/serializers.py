from asyncore import write
from rest_framework import serializers

from restapi.models import User,LectureHall,Booking
class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model=LectureHall
        fields=['hall_name','hall_location','hall_capacity','hall_rating','hall_image','id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
    

class USerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','password','name']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password!=None:
            instance.set_password(password)
        instance.save()
        return instance

class BookingSerializer(serializers.ModelSerializer):
        class Meta:
            model=Booking
            fields='__all__'
            