from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from analyzer.controller import Controller
from analyzer import file_handler

class DataAnalyzerBoard(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        if serializer.is_valid(raise_exception=True):
            data,result = Controller.main(request.data)
            file_name = Controller.name_file()
            file_handler.process_file_handling(data,file_name,request.data)
            return Response({
                    'input_dict': serializer.data,
                    'result': result,
                    'file_name': {'file_name': file_name},
                    })
        return Response(serializer.errors)
        
class DataAnalyzerDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        file_name = request.GET.get('file_name')
        file_path = file_handler.get_file_path(file_name)
        with open(file_path,'rb') as file:
            response = HttpResponse(file,content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = f'attachment; filename={file_name}'
        return response


