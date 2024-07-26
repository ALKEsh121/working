from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    ###################### service manager ##########################
    path('manage-services', views.ManageService, name="manage-services"),
    path("add-service",views.AddService, name="add-service"),
    path("update-service/<int:id>/",views.UpdateService.as_view(), name="update-service"),
    path("delete-service/<int:id>/",views.DeleteService.as_view(), name="delete-service"),

    ###################### project manager ##########################
    path('manage-projects', views.ManageProject, name="manage-projects"),
    path("add-project",views.AddProject, name="add-project"),
    path("update-project/<int:id>/",views.UpdateProject.as_view(), name="update-project"),
    path("delete-project/<int:id>/",views.DeleteProject.as_view(), name="delete-project"),
    
    
    ###################### Enquiry manager ##########################
    path('manage-enquiries', views.ManageEnquiry, name="manage-enquiries"),
    path("view-enquiry/<int:id>/",views.ViewEnquiry, name="view-enquiry"),
    path("delete-enquiry/<int:id>/",views.DeleteEnquiry.as_view(), name="delete-enquiry"),


    ###################### Gallery manager ##########################
    path('manage-gallery',views.ManageGallery,name='manage-gallery'),
    path("add-gallery",views.AddGallery, name="add-gallery"),
    path("update-gallery/<int:id>/",views.Updategallery.as_view(), name="update-gallery"),
    path("delete-gallery/<int:id>/",views.Deletegallery.as_view(), name="delete-gallery"),
    # path('update-gallery/<int:id>/', Updategallery.as_view(), name='update-gallery'),

    

    ###################### Blog manager ##########################
    path('manage-blog',views.ManageBlog,name='manage-blog'),
    path("add-blog",views.AddBlog, name="add-blog"),
    path("update-blog/<int:id>/",views.Updateblog.as_view(), name="update-blog"),
    path("delete-blog/<int:id>/",views.Deleteblog.as_view(), name="delete-blog"),


    ################### manage Subscription ############################

    path('manage-gallery',views.ManageGallery,name='manage-gallery'),
    path('manage-subscription', views.ManageSubscribe, name="manage-subscription"),
    path('delete-subscription/<int:id>',views.Deletesub.as_view(), name='delete-subscription'),

    ###################### testimonials manager ########################
    path('manage-testimonials',views.ManageTestimonials,name='manage-testimonial'),
    path("add-testimonials",views.AddTestimonials, name="add-testimonial"),
    path("update-testimonials/<int:id>/",views.UpdateTestimonials.as_view(),name="update-testimonial"),
    path("delete-testimonials/<int:id>/",views.DeleteTestimonials.as_view(), name="delete-testimonial"),

    path('download-data/', views.DownloadDataView.as_view(), name='download_data'),
    
    path('logout',views.UserLogout,name='logout')

]