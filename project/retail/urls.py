from django.contrib import admin
from django.urls import include, path
from . import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path("get_chatbot/",v.run_llm,name="chatbot"),
    path("create_customer/",v.create_customer,name="create customer")
]