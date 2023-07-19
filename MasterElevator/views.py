from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

# Create your views here.
class AddNewElevatorAPIView(APIView):
    def post(self,request):
        serializer = ElevatorSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)

class RequestElevatorAPIView(APIView):
    def post(self,request):
        serializer = RequestElevatorSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)

class FetchRequestAPIView(APIView):
    def post(self,request):
        elevator_id = request.data["elevator_id"]
        requests = []
        request_list = []
        elevator = Elevator.objects.filter(id=elevator_id,is_operational=True).first()
        if(elevator):
            for request in ElevatorRequest.objects.filter(elevator= elevator_id):
                msg = {'request_floor':request.request_floor,'request_time':request.request_time}
                requests.append(msg)
                request_list.append(request.request_floor)
        else:
            return Response({"APIException":"Elevator is not working"})
        return Response({
            'data':requests,
            'request_list':request_list
        })

class FetchNextDestAPIView(APIView):
    def post(self,request):
        elevator_id = request.data['elevator_id']
        elevator = Elevator.objects.filter(id = elevator_id,is_operational=True).first()
        request_list = []
        status = ''
        if(elevator):
            current_floor = elevator.current_floor
            for request in ElevatorRequest.objects.filter(elevator=elevator_id):
                request_list.append(request.request_floor)
            request_list.sort(reverse=True)
            if(int(request_list[0]) < int(current_floor)):
                status = "Down"
            else:
                status = "Up"
        else:
            return Response({"APIException":"Elevator is not Working!!"})
        return Response({
            'current Floor':current_floor,
            'Next Destination Floor': request_list[0],
            'Elevator moving Up / Down': status
        })

class MarkOperationalStatusAPIView(APIView):
    def post(self,request):
        elevator_id = request.data['elevator_id']
        elevator = Elevator.objects.filter(id = elevator_id).first()
        msg = ''
        if(elevator.is_operational):
            elevator.is_operational = False
            msg = "Elevator is not working or in maintenance"
        else:
            elevator.is_operational = True
            msg = "Elevator is working"
        elevator.save()
        return Response({
            'msg': msg
        })

class OpenCloseAPIView(APIView):
    def post(self,request):
        elevator_id = request.data['elevator_id']
        elevator = Elevator.objects.filter(id = elevator_id,is_operational=True).first()
        if(elevator):
            current_floor = elevator.current_floor
            request  = ElevatorRequest.objects.filter(elevator=elevator_id).order_by('-request_floor').values()
            if(len(request)>0):
                dest_floor = request[0]["request_floor"]
                elevator.current_floor = dest_floor
                elevator.save()
                request = ElevatorRequest.objects.filter(request_floor=dest_floor).delete()
            else:
                dest_floor = "No More Request"
        else:
            return Response({"APIException":"Elevator is not Working!!"})
        elevator = Elevator.objects.filter(id = elevator_id,is_operational=True).first()
        request  = ElevatorRequest.objects.filter(elevator=elevator_id).order_by('-request_floor').values()
        if(len(request)>0):
            dest_floor = request[0]["request_floor"]
        else:
            dest_floor = "No More Request"
        return Response({
            'currentfloor':elevator.current_floor,
            'next_floor':dest_floor
        })