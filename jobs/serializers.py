from rest_framework.serializers import ModelSerializer
from .models import Job


# class ContactSerializer(ModelSerializer):

#     class Meta:
#         model = Contact

#         fields = ['country_code', 'id', 'first_name', 'last_name', 'phone_number',
#                   'contact_picture', 'is_favorite'
#                   ]
class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ['id','title', 'description', 'location', 'jtype', 'category', 'post_image', 'last_date','company_name', 'company_description', 'website', 'created_at', 'status', 'posts', 'required_exp']
        # fields = '__all__'
        list_display = ['title', 'description', 'location', 'jtype', 'category', 'post_image', 'last_date','company_name', 'company_description', 'website', 'created_at', 'status', 'posts', 'required_exp']
