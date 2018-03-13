from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from tickets_app.models import Status
#from clients.api.serializers import ClientDetailSerializer, ClientListSerializer


#crear video.
class StatusCreateSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ['name', ]

    def get_image(self, obj):
        return "/static/ang/assets/images/nature/4.jpg"

post_detail_url = HyperlinkedIdentityField(
		view_name='detail',
		lookup_field='slug',
		)


#lista de videos
class StatusListSerializer(ModelSerializer):
	#client = ClientDetailSerializer(read_only=True)
	class Meta:
		model = Status
		fields = [ 'id', 'name', ]

		def filter_query(self, queryset):
			queryset = super(InvoiceViewSet)




#detalle del video
class StatusDetailSerializer(ModelSerializer):

	class Meta:
		model = Status
		fields = ['id', 'name',  ]


