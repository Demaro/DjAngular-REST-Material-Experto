from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
	)


class TicketLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 8
	max_limit = 8

class TicketPageNumberPagination(PageNumberPagination):
	page_size = 5