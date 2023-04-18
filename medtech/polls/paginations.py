from rest_framework import pagination

class PaginateBy16(pagination.PageNumberPagination):
    page_size = 16
    max_page_size = 50
    page_query_param = 'p'

