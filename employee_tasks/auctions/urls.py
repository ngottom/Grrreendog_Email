from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createListing, name="create"),
    path("active", views.activeListings, name="active"),
    path("categories", views.categories, name="categories"),
    path("displayCategory", views.displayCategory, name="displayCategory"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("removeWatchlist/<int:id>", views.removeWatchlist, name="removeWatchlist"),
    path("addWatchlist/<int:id>", views.addWatchlist, name="addWatchlist"),
    path("sortWatchlist", views.sortWatchlist, name="sortWatchlist"),
    path("addComment/<int:id>", views.addComment, name="addComment"),
    path("employees", views.employees, name="employees"),
    path("employeePage/<int:phone>", views.employeePage, name="employeePage"),
    path("createTask/", views.createTask, name="createTasks"),
    path("displaySection", views.displaySection, name="displaySection"),
    path("createTask", views.createTask, name="createTask"),
    path("addEmployeeComment/<int:phone>", views.addEmployeeComment, name="addEmployeeComment"),
    path("videos", views.videos, name="videos"),
    path("displayVideoSection", views.displayVideoSection, name="displayVideoSection"),
    path("uploadVideo", views.uploadVideo, name="uploadVideo"),
    path("dogs", views.dogs,name="dogs"),
    path("employeeComments", views.employeeComments, name="employeeComments"),
    path("sortNotices", views.sortNotices, name="sortNotices"),
    path("inventoryComments", views.inventoryComments, name="inventoryComments"),
    path("sortedInventory", views.sortedInventory, name="sortedInventory"),
    path("emptyListings", views.emptyListings, name="emptyListings"),
    path("sortNotices", views.sortNotices, name="sortNotices"),
    path("todayInventoryComments", views.todayInventoryComments, name="todayInventoryComments"),
    path("todayEmployeeComments", views.todayEmployeeComments, name="todayEmployeeComments"),



]
urlpatterns += staticfiles_urlpatterns()
