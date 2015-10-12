from models  import oraclelist
from rest_framework import serializers


class OracleListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = oraclelist
        fields = ('ipaddress','instance','password','port')


