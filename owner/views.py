from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from tezcoapp.models import *
from django.contrib import messages
from owner.forms import *
from django.views.generic import UpdateView, DeleteView
from django.views import View
import csv
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def dashboard(request):
    enquiry_count = Enquiry.objects.filter(status="unread").count()
    context = {"enquiry_count":enquiry_count}
    return render(request, "dashboard.html", context)

#services
def ManageService(request):
    services = Services.objects.all()
    enquiry_count = Enquiry.objects.filter(status="unread").count()
    context = {"services":services, "enquiry_count":enquiry_count}
    return render(request, "manage-services.html", context)



def AddService(request):
    form = AddServiceForm()
    if request.method == 'POST':
        form = AddServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Service added successfully !!")
            return redirect('manage-services')
    return render(request, "add-service.html", {"form":form})


class UpdateService(UpdateView):
    model = Services
    pk_url_kwarg = "id"
    template_name = "update-service.html"
    success_url = reverse_lazy("manage-services")
    form_class = UpdateServiceForm

    def form_valid(self, form):
        messages.success(self.request, "Service  updated successfully")
        return super().form_valid(form)


class DeleteService(DeleteView):
    model = Services
    pk_url_kwarg = "id"
    success_url = reverse_lazy("manage-services")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "Service deleted successfully")
        return super(DeleteService, self).form_valid(form)


#Projects
def ManageProject(request):
    projects = Projects.objects.all()
    enquiry_count = Enquiry.objects.filter(status="unread").count()
    context = {"projects":projects, "enquiry_count":enquiry_count}
    return render(request, "manage-projects.html", context)


def AddProject(request):
    form = AddProjectForm()
    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Project added successfully !!")
            return redirect('manage-projects')
    return render(request, "add-project.html", {"form":form})


class UpdateProject(UpdateView):
    model = Projects
    pk_url_kwarg = "id"
    template_name = "update-project.html"
    success_url = reverse_lazy("manage-projects")
    form_class = UpdateProjectForm

    def form_valid(self, form):
        messages.success(self.request, "Project  updated successfully")
        return super().form_valid(form)


class DeleteProject(DeleteView):
    model = Projects
    pk_url_kwarg = "id"
    success_url = reverse_lazy("manage-projects")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "Project deleted successfully")
        return super(DeleteProject, self).form_valid(form)


###################### Enquiry ######################
def ManageEnquiry(request):
    enquiries = Enquiry.objects.all()
    enquiry_count = Enquiry.objects.filter(status="unread").count()
    context = {"enquiries":enquiries, "enquiry_count":enquiry_count}
    return render(request, "manage-enquiries.html", context)


def ViewEnquiry(request, id):
    enquiry = Enquiry.objects.get(id=id)
    if enquiry.status == "unread":
        enquiry.status = "viewed"
        enquiry.save()
    return render(request, "view-enquiry.html", {"enquiry":enquiry})


class DeleteEnquiry(DeleteView):
    model = Enquiry
    pk_url_kwarg = "id"
    success_url = reverse_lazy("manage-enquiries")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "Enquiry deleted successfully")
        return super(DeleteEnquiry, self).form_valid(form)



############################## subscription ##############################
def ManageSubscribe(request):
    subscription = Subscription.objects.all()
    enquiry_count = Enquiry.objects.filter(status="unread").count()
    context = {"subscription":subscription, "enquiry_count":enquiry_count}
    return render(request, "manage-subscription.html", context)


class Deletesub(DeleteView):
    model = Subscription
    pk_url_kwarg = "id"
    success_url = reverse_lazy("manage-subscription")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "subscription deleted successfully")
        return super(Deletesub, self).form_valid(form)




############################## Gallery ########################
def ManageGallery(request):
    gal = Gallery.objects.all()
    # enquiry_count = Enquiry.objects.filter(status="unread").count()
    context = {"proj":gal}
    return render(request, "manage-gallery.html", context)


def AddGallery(request):
    form = AddGalleryForm()
    if request.method == 'POST':
        form = AddGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Images added successfully !!")
            return redirect('manage-gallery')
    return render(request, "add-gallery.html", {"forms":form})


class Updategallery(UpdateView):
    model = Gallery
    pk_url_kwarg = "id"
    template_name = "update-gallery.html"
    success_url = reverse_lazy("manage-gallery")
    form_class = UpdateGalleryForm

    def form_valid(self, form):
        messages.success(self.request, "Gallery  updated successfully")
        return super().form_valid(form)


class Deletegallery(DeleteView):
    model = Gallery
    pk_url_kwarg = "id"
    success_url = reverse_lazy("manage-gallery")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "image deleted successfully")
        return super(Deletegallery, self).form_valid(form)

################### Download ########################
class DownloadDataView(View):
    def get(self, request):
        data = Enquiry.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="mydata.csv"'
        writer = csv.writer(response)
        writer.writerow(['name','email','phone','message'])
        for row in data:
            writer.writerow([row.name,row.email,row.phone,row.message])


        return response






########################## BLOG ############################



def ManageBlog(request):
    blogs = Blog.objects.all()
    context = {"blog":blogs}
    return render(request, 'manage-blog.html',context)


def AddBlog(request):
    form = AddBlogForm()
    if request.method == 'POST':
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "blog added successfully !!")
            return redirect('manage-blog')
    return render(request, "add-blog.html", {"forms":form})


class Updateblog(UpdateView):
    model = Blog
    pk_url_kwarg = "id"
    template_name = "update-blog.html"
    success_url = reverse_lazy("manage-blog")
    form_class = UpdateBlogForm

    def form_valid(self, form):
        messages.success(self.request, "blog  updated successfully")
        return super().form_valid(form)
    

class Deleteblog(DeleteView):
    model = Blog
    pk_url_kwarg = "id"
    success_url = reverse_lazy("manage-blog")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "Blog deleted successfully")
        return super(Deleteblog, self).form_valid(form)
    


##################### Testimonials ###########################


def ManageTestimonials(request):
    testimonial = Testimo.objects.all()
    context = {'testimonial' :testimonial }
    return render (request , 'manage-testimonials.html' , context )

def AddTestimonials(request):
    form = AddTestForm()
    if request.method == 'POST':
        form = AddTestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Testimonials added successfully !!")
            return redirect('manage-testimonials')
    return render(request, "add-testimonials.html", {"forms":form})


class UpdateTestimonials(UpdateView):
    model = Testimo
    pk_url_kwarg = "id"
    template_name = "update-testimonials.html"
    success_url = reverse_lazy("manage-testimonials")
    form_class = UpdateTestForm

    def form_valid(self, form):
        messages.success(self.request, "testimonials  updated successfully")
        return super().form_valid(form)
    

class DeleteTestimonials(DeleteView):
    model = Testimo
    pk_url_kwarg = "id"
    success_url = reverse_lazy("manage-testimonials")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "testimonials deleted successfully")
        return super(DeleteTestimonials, self).form_valid(form)
    



def UserLogout(request):
    logout(request)
    messages.success(request,"Logged out Successfully !!")
    return redirect('home')