from rest_framework import serializers
from api.models import CodeExplainer
from api.utils import gemini
from django.contrib.auth.models import User
class CodeExplainSerializer(serializers.ModelSerializer):
    class Meta:
        model=CodeExplainer
        fields=("id",'_input',"_output")
        extra_kwargs={
            "_output":{"read_only":True}
        }
    def create(self,validated_data):
        ce=CodeExplainer(**validated_data)
        _output=gemini(validated_data["_input"])
        ce._output=_output
        ce.save()
        return ce

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","username","email","password")
        extra_kwargs={
            "password":{"write_only":True}
        }