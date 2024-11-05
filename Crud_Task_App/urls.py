from django.urls import path

from Crud_Task_App import views

urlpatterns = [
    # path('',views.test2,name='test2'),
    path('',views.MainPageView,name='MainPageView'),
    path('addStudy',views.addStudy,name='addStudy'),
    path('read',views.read,name = 'read'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('detailedView/<int:id>/',views.detailedView,name = 'detailedView'),

]