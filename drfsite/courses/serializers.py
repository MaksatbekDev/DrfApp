from rest_framework import serializers

from .models import Course, Category, Branch, Contact


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'description', 'logo', 'category', 'contacts', 'branches')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','imgpath')


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'value')


