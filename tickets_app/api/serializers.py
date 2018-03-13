from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from tickets_app.models import Ticket

from tickets_app.api_accounts.serializers import UserDetailSerializer
from tickets_app.api_status.serializers import StatusDetailSerializer


#crear video.
class TicketCreateSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['name', "description", "user", "status", ]

    def get_image(self, obj):
        return "/static/ang/assets/images/nature/4.jpg"

post_detail_url = HyperlinkedIdentityField(
		view_name='detail',
		lookup_field='slug',
		)


#lista de videos
class TicketListSerializer(ModelSerializer):
	user = UserDetailSerializer(read_only=True)
	status = StatusDetailSerializer(read_only=True)
	createdAt = serializers.DateTimeField(format="%d-%m-%Y a las %H:%M")
	class Meta:
		model = Ticket
		fields = [ 'id', 'name', 'slug', "description", 'createdAt', 'updatedAt', "user", "status", ]

		def filter_query(self, queryset):
			queryset = super(InvoiceViewSet)




#detalle del video
class TicketDetailSerializer(ModelSerializer):

	class Meta:
		model = Ticket
		fields = ['id', 'name', 'slug', "description", 'createdAt', 'updatedAt', "user", "status", ]


