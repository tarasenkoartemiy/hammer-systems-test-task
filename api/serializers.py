from django.contrib.auth import get_user_model
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

User = get_user_model()

class PhoneSerializer(serializers.Serializer):
    phone_number = PhoneNumberField()

class ActivateSerializer(PhoneSerializer):
    auth_code = serializers.IntegerField()

class UserSerializer(serializers.ModelSerializer):
    invited_users = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["phone_number", "auth_code", "own_invite_code", "activated_invite_code", "invited_users"]
        read_only_fields = ['phone_number', 'auth_code', "own_invite_code"]


    def validate(self, data):
        invite_code = data.get("activated_invite_code", "")
        if not invite_code:
            super().validate(data)
        if self.context.get('request').user.activated_invite_code:
            raise serializers.ValidationError("You already have an activated invite code")
        if not User.objects.filter(own_invite_code=invite_code).exists():
            raise serializers.ValidationError("There is no user with such an invite code")
        return super().validate(data)
    
    def get_invited_users(self, obj):
        own_invite_code = obj.own_invite_code
        return User.objects.filter(activated_invite_code=own_invite_code).values_list('phone_number', flat=True)