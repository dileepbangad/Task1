from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework.exceptions import APIException

class ElevatorSerializer(ModelSerializer):
    class Meta:
        model = Elevator
        fields = ['id','name','current_floor','max_floor','is_operational']

    def create(self,validated_data):
        name = validated_data.pop("name",None)
        current_floor = validated_data.pop("current_floor",0)
        max_floor = validated_data.pop("max_floor",None)
        is_operational = validated_data.pop("is_operational",True)
        instance = self.Meta.model(**validated_data)
        if name is not None:
            elevator  = Elevator.objects.filter(name = name).first()
            if(elevator):
                raise APIException("Same Elevator Name Already Exist!")
            else:
                instance.name = name
                instance.current_floor = current_floor
                instance.max_floor = max_floor
                instance.is_operational = is_operational
        instance.save()
        return instance

class RequestElevatorSerializer(ModelSerializer):
    class Meta:
        model = ElevatorRequest
        fields = ['id','request_floor','request_time','elevator']

    def create(self,validated_data):
        request_floor = validated_data.pop("request_floor",None)
        elevator_id = validated_data.pop("elevator",None)
        instance = self.Meta.model(**validated_data)
        if elevator_id is not None:
            elevator  = Elevator.objects.filter(id = elevator_id,is_operational=True).first()
            if(elevator):
                if int(request_floor) > int(elevator.max_floor):
                    raise APIException("Requested Floor Not Found!!!")
                else:
                    instance.request_floor = request_floor
                    instance.elevator = elevator_id
            else:
                raise APIException("Requested Elevator not Working!!!")
        instance.save()
        return instance
