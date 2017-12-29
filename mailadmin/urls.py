from django.urls import re_path
from . import views
from .models import *

app_name = 'mailAdmin'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(model=Domain), name='domainIndex'),
    re_path(r'^login/', views.LoginView.as_view(), name='login'),
    re_path(r'^logout/', views.LogoutView.as_view(), name='logout'),
    re_path(r'^new/$', views.NewView.as_view(model=Domain), name='domainNew'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/$', views.EditView.as_view(model=Domain), name='domainEdit'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/delete/$', views.DeleteView.as_view(model=Domain), name='domainDelete'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/accounts/$', views.IndexView.as_view(model=Account), name='domainAccounts'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/accounts/new/$', views.NewView.as_view(model=Account), name='accountNew'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/accounts/(?P<account>[\w\d\-\.]+)/$', views.EditView.as_view(model=Account), name='accountEdit'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/accounts/(?P<account>[\w\d\-\.]+)/delete/$', views.DeleteView.as_view(model=Account), name='accountDelete'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/accounts/(?P<account>[\w\d\-\.]+)/aliases/$', views.SubModelIndexView.as_view(model=Account, sub_model=Alias), name='accountAliases'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/accounts/(?P<account>[\w\d\-\.]+)/aliases/add/$', views.SubModelAddView.as_view(model=Account, sub_model=Alias), name='accountAliasAdd'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/accounts/(?P<account>[\w\d\-\.]+)/aliases/(?P<alias>\d+)/remove/$', views.SubModelRemoveView.as_view(model=Account, sub_model=Alias), name='accountAliasRemove'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/accounts/(?P<account>[\w\d\-\.]+)/lists/$', views.SubModelIndexView.as_view(model=Account, sub_model=Mailinglist), name='accountMailinglists'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/accounts/(?P<account>[\w\d\-\.]+)/lists/add/$', views.SubModelAddView.as_view(model=Account, sub_model=Mailinglist), name='accountMailinglistAdd'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/accounts/(?P<account>[\w\d\-\.]+)/lists/(?P<mailing_list>\d+)/remove/$', views.SubModelRemoveView.as_view(model=Account, sub_model=Mailinglist), name='accountMailinglistRemove'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/aliases/$', views.IndexView.as_view(model=Alias), name='domainAliases'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/aliases/new/$', views.NewView.as_view(model=Alias), name='aliasNew'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/aliases/(?P<alias>[\w\d\-\.]+)/delete/$', views.DeleteView.as_view(model=Alias), name='aliasDelete'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/lists/$', views.IndexView.as_view(model=Mailinglist), name='domainLists'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/lists/new/$', views.NewView.as_view(model=Mailinglist), name='mailinglistNew'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/lists/(?P<list>[\w\d\-\.]+)/delete/$', views.DeleteView.as_view(model=Mailinglist), name='mailinglistDelete'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/lists/(?P<list>[\w\d\-\.]+)/accounts/$', views.SubModelIndexView.as_view(model=Mailinglist, sub_model=Account), name='mailinglistAccounts'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/lists/(?P<list>[\w\d\-\.]+)/accounts/add/$', views.SubModelAddView.as_view(model=Mailinglist, sub_model=Account), name='mailinglistAccountAdd'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/lists/(?P<list>[\w\d\-\.]+)/accounts/(?P<account>\d+)/delete/$', views.SubModelRemoveView.as_view(model=Mailinglist, sub_model=Account), name='mailinglistAccountRemove'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/lists/(?P<list>[\w\d\-\.]+)/externals/$', views.SubModelIndexView.as_view(model=Mailinglist, sub_model=ExternalReceiver), name='mailinglistExternals'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/lists/(?P<list>[\w\d\-\.]+)/externals/add/$', views.SubModelAddView.as_view(model=Mailinglist, sub_model=ExternalReceiver), name='mailinglistExternalAdd'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/lists/(?P<list>[\w\d\-\.]+)/externals/(?P<external_receiver>\d+)/delete/$', views.SubModelRemoveView.as_view(model=Mailinglist, sub_model=ExternalReceiver), name='mailinglistExternalRemove'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/redirects/$', views.IndexView.as_view(model=Redirect), name='domainRedirects'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/redirects/new/$', views.NewView.as_view(model=Redirect), name='redirectNew'),
    re_path(r'^(?P<domain>[\w\d\-\.]+\.[\w\d\-\.]{2,})/redirects/(?P<redirect>[\w\d\-\.]+)/delete/$', views.DeleteView.as_view(model=Redirect), name='redirectDelete'),
]
