from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Todo, User, Address

class CustomLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "status", "id")

    def create(self, validated_data):
       return User(**validated_data)    


class TodoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)

    class Meta:
        model = Todo
        fields = ("title", "task", "done", "id", "changed_at")
        # fields = '__all__'
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.task = validated_data.get("task", instance.task)
        instance.save()
        return instance


class AddressSerializer(serializers.ModelSerializer):
    # With ModelSerializer this is not necessary
    country = serializers.CharField(max_length=128, trim_whitespace=True)
    city = serializers.CharField(max_length=128, trim_whitespace=True)
    street = serializers.CharField(max_length=256, allow_blank=False, trim_whitespace=True)
    postal_code = serializers.CharField(max_length=32, allow_blank=False, trim_whitespace=True)

    class Meta:
        model = Address
        fields = ('country', 'city', 'street', 'postal_code')


    def create(self, validated_data):
        return Address.objects.create(**validated_data)
        # user = get_object_or_404(User, id=validated_data.data["userId"])
        # user.address = address
        # return address

    def update(self, instance, validated_data):
        instance.country = validated_data.get('country', instance.email)
        instance.city = validated_data.get('city', instance.content)
        instance.street = validated_data.get('street', instance.created)
        instance.postal_code = validated_data.get('postalCode', instance.created)
        return instance    

    # can also overwrite save function


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'url'
        )

# Example with related models in serializer
# class FirewallChainSerializer(serializers.ModelSerializer):
#     id = serializers.UUIDField(required=False, allow_null=True)
#     spi_box_id = serializers.UUIDField()
#     template_id = serializers.UUIDField(required=False, allow_null=True)
#     machine_id = serializers.UUIDField(required=False, allow_null=True)
#     variables = FirewallVariableSerializer(many=True, required=True, source='firewall_variables')

#     class Meta:
#         model = FirewallChain
#         fields = ('id', 'spi_box_id', 'name', 'template_id', 'machine_id', 'variables', 'rules')

#     def create(self, attrs):
#         data = self.validated_data

#         # Create new box config if now 'in work' config is available
#         box = get_object_or_404(SPIBox, id=data['spi_box_id'])
#         last_config = box.get_latest_config()

#         with transaction.atomic():
#             last_config.create_new_config_from_current()
#             variables = data.pop('firewall_variables')
#             firewall_chain = FirewallChain.objects.create(**data)
#             

#             FirewallVariable.objects.bulk_create([
#                 FirewallVariable(
#                     name=v['name'],
#                     value=v['value'],
#                     firewall_chain_id=firewall_chain.id,
#                 )
#                 for v in variables
#             ])

#         return firewall_chain

#     def update(self, instance, validated_data):
#         instance_box_id = None
#         if instance.spi_box:
#             instance_box_id = instance.spi_box.id

#         instance_template_id = None
#         if instance.template:
#             instance_template_id = instance.template.id

#         instance_machine_id = None
#         if instance.machine:
#             instance_machine_id = instance.machine.id

#         instance.spi_box_id = validated_data.get('spi_box_id', instance_box_id)
#         instance.name = validated_data.get('name', instance.name)
#         instance.machine_id = validated_data.get('machine_id', instance_machine_id)
#         tmp_id = validated_data.get('template_id', instance_template_id)
#         instance.template_id = tmp_id
#         instance.rules = validated_data.get('rules', instance.rules)
#         instance.save()

#         validated_variables = validated_data.pop('firewall_variables')
#         new_variables = []

#         for v in validated_variables:
#             if not v['id']:
#                 # Add new added ones to dict to create them afterwards
#                 new_variables.append(v)
#             else:
#                 # Update existing ones
#                 firewall_variable = instance.firewall_variables.all().filter(id=v['id']).get()
#                 firewall_variable.name = v['name']
#                 firewall_variable.value = v['value']
#                 firewall_variable.save()

#         FirewallVariable.objects.bulk_create([
#             FirewallVariable(
#                 name=v['name'],
#                 value=v['value'],
#                 firewall_chain_id=instance.id,
#              )
#             for v in new_variables
#         ])

#         last_config = instance.spi_box.get_latest_config()
#         last_config.create_new_config_from_current()

#         return instance       