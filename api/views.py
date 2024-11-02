# Create your views here.
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils.graph_algorithms import warshall_algorithm


@extend_schema(responses={200: 'Success'}, summary="Warshall's Algorithm API",
               tags=['Calculate the reachability matrix'])
class MatrixTransposeAPIView(APIView):
    """
    API endpoint for transposing a matrix.
    """

    @extend_schema(
        request={
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'matrix': {
                            'type': 'array',
                            'items': {
                                'type': 'array',
                                'items': {'type': 'number'}
                            }
                        }
                    },
                    'required': ['matrix']
                }
            }
        },
        responses={200: str, 400: str},
        description="Accepts a 2D matrix (list of lists) and use warshall_algorithm to calculate reachability matrix."
    )
    def post(self, request):
        try:
            matrix = request.data.get('matrix')
            if not matrix or not all(isinstance(row, list) for row in matrix):
                return Response("Invalid input. Expected a 2D matrix.", status=status.HTTP_400_BAD_REQUEST)

            # Transpose the matrix
            transpose_matrix = warshall_algorithm(matrix)

            for row in transpose_matrix:
                print(row)

            return Response(transpose_matrix, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_400_BAD_REQUEST)
