# from .serializers import ModelSerializer 

# class StudentRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         max_length=128,
#         min_length=8,
#         write_only=True
#     )
#     token = serializers.CharField(max_length=255, read_only=True)
 
#     class Meta:
#         model = Student
#         fields = '__all__'
 
#     def create(self, validated_data):
#         return Student.objects.create_student(**validated_data)
 