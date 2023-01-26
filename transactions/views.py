from rest_framework.views import APIView, Request, Response, status
import ipdb


class TransactionView(APIView):
    def post(self, req: Request) -> Response:
        file_request = req.FILES['file']
        lines_list = [line.decode('utf-8').rstrip() for line in file_request]
        for line in lines_list:
            data = {
                type: line[1],
                date: line[2:10],
                value: line[10:20],
                cpf: line[20:31],
                card: line[31:43],
                time: line[43:49],
                store_owner: line[49:63],
                store_name: line[63:82],
            }
            ipdb.set_trace()

        return Response({"message": "Hello"}, status.HTTP_200_OK)
