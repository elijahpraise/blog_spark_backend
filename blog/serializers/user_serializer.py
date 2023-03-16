from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from blog.models.user_model import UserModelClass
from blog.serializers.validators import validate_gender


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    token = serializers.CharField(max_length=255, read_only=True)
    image = serializers.URLField(required=False)
    phone_number = serializers.CharField(required=True)
    gender = serializers.CharField(required=True, validators=[validate_gender])
    password = serializers.CharField(min_length=8, write_only=True)
    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(queryset=UserModelClass.objects.all(), message="A user already exists with this email")])
    username = serializers.CharField(required=True, validators=[
        UniqueValidator(queryset=UserModelClass.objects.all(), message="A user already exists with this username")])

    class Meta:
        model = UserModelClass
        fields = (
            'id', 'username', 'email', 'phone_number', 'gender', 'token', 'image', "first_name", "last_name",
            "password", "last_updated", "date_created")

    def create(self, validated_data):
        username = validated_data["username"]
        firstname = validated_data["first_name"]
        lastname = validated_data["last_name"]
        email = validated_data["email"]
        gender = validated_data["gender"]
        image = validated_data["image"] if validated_data.__contains__("image") else None
        password = validated_data["password"]
        phone_number = validated_data["phone_number"]
        user = UserModelClass(first_name=firstname, last_name=lastname, email=email, gender=gender, image=image,
                              username=username, phone_number=phone_number)
        user.set_password(raw_password=password)
        user.save()
        user = UserModelClass.objects.get(username=username)
        return user

    def update(self, instance, validated_data):
        pass


class UserProfile(serializers.ModelSerializer):
    class Meta:
        model = UserModelClass
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'gender', 'token']
