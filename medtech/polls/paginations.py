from rest_framework import pagination

class PaginateBy16(pagination.PageNumberPagination):
    page_size = 16
    max_page_size = 50
    page_query_param = 'p'


class PaginateBy9(pagination.PageNumberPagination):
    page_size = 16
    max_page_size = 50
    page_query_param = 'p'


class PaginateBy25(pagination.PageNumberPagination):
    page_size = 16
    max_page_size = 50
    page_query_param = 'p'


class PaginateBy10(pagination.PageNumberPagination):
    page_size = 16
    max_page_size = 50
    page_query_param = 'p'
