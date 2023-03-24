from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    pass


class Section(models.Model):
    sectionName = models.CharField(max_length=200)


    def __str__(self):
        return self.sectionName


class Employee(models.Model):
    employeeName = models.CharField(max_length=200)
    phone = models.IntegerField()
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, blank=True, null=True, related_name="section")
    isActive = models.BooleanField(default=True)
    imageURL = models.CharField(
        max_length=500, default="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/800px-Question_mark_%28black%29.svg.png")
        # max_length=500, default="/auctions/templates/auctions/images/qMark.png")

    def __str__(self):
        return str(self.employeeName)


class Category(models.Model):
    categoryName = models.CharField(max_length=300)

    def __str__(self):
        return self.categoryName


class Listing(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, default="supply")
    imageURL = models.CharField(max_length=500, default="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/800px-Question_mark_%28black%29.svg.png")
    price = models.FloatField(default=0)
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(
        User, blank=True, null=True, related_name="listingWatchlist")
    count = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.title


class EmployeeListing(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, blank=True, null=True, related_name="employee")
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, blank=True, null=True)
    tasks = models.CharField(max_length=1000)
    extras = models.CharField(max_length=1000, default="None")
    extrasPrice = models.FloatField(default=0)

    # default date is today
    startYear = models.PositiveIntegerField(
        validators=[MinValueValidator(2022)])
    startMonth = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)])
    startDay = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(31)])
    startHour = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(23)])
    startMinute = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(59)])

    # endTime
    # endMonth = models.PositiveIntegerField(
    #     validators=[MinValueValidator(1), MaxValueValidator(12)])
    # endDay = models.PositiveIntegerField(
    #     validators=[MinValueValidator(1), MaxValueValidator(31)])
    endHour = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(23)])
    endMinute = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(59)])
    datetime = models.CharField(
         max_length=100, default=datetime.now().strftime("%H:%M:%S EST, %m-%d-%Y"))
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="author")
    #
    # dateStart = datetime.now()
    # dateEnd = datetime.now()
    # create this in views later
    # dateStart = datetime(startYear, startMonth, startDay,startHour, startMinute)
    # dateEnd = datetime(endYear, endMonth, endDay, endDay, endHour, endMinute)
    # purchased = models.ManyToManyField(
    #     User, blank=True, null=True, related_name="listingPurchased")
    # anchor

    #

    def __str__(self):
        return f"{self.employee.employeeName}: {self.employee.employeeName}: {self.startMonth} {self.startDay} {self.startYear}"


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,  blank=True, null=True, related_name="userComment")
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE,  blank=True, null=True, related_name="listingComment")
    message = models.CharField(max_length=200)
    datetime = models.DateTimeField(
        max_length=100, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __str__(self):
        return f"{self.author} about {self.listing}: {self.message}"

class employeeComment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,  blank=True, null=True, related_name="commentUser")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE,  blank=True, null=True, related_name="commentEmployee")
    message = models.CharField(max_length=1000)
    datetime = models.DateTimeField(
        max_length=100, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __str__(self):
        return f"{self.author}: {self.message}"

class VideoSection(models.Model):
    videoSection = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.videoSection}"

class Video(models.Model):
    videoTitle = models.CharField(max_length=280)
    videoSection = models.ForeignKey(
        VideoSection, on_delete=models.CASCADE, blank=True, null=True)
    videoLink = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.videoTitle}"
class Timestamp(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True, related_name="timestampUser")
    datetime = models.CharField(
        max_length=100, default=datetime.now().strftime("%H:%M:%S %m-%d-%Y"))
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"{self.author}, {self.datetime}"
    
class Rooms(models.Model):
    room = models.CharField(max_length=200, blank=True, null = True)   
    def __str__(self):
        return self.sectionName 

class Dog(models.Model):
    dogName = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    phone = models.IntegerField()
    breed = models.CharField(
        max_length=200)
    isActive = models.BooleanField(default=False)
    imageURL = models.CharField(
        max_length=500, default="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/800px-Question_mark_%28black%29.svg.png")
        # max_length=500, default="/auctions/templates/auctions/images/qMark.png")

    def __str__(self):
        return str(self.dogName)
    
class dogListing(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True, related_name="dogAuthor")
    datetime = models.CharField(
        max_length=100, default=datetime.now().strftime("%H:%M:%S %m-%d-%Y"))
    dog = models.ForeignKey(Dog, on_delete = models.CASCADE, max_length = 100, blank = True, null = True,)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE,  blank=True, null=True, related_name="roomName")
    
    def __str__(self): 
        return str(self.dog)

# class Purchase(models.Model):
#     listing = models.ForeignKey(
#         Listing, on_delete=models.CASCADE,  blank=True, null=True, related_name="listingPurchase")
#     purchaseUser = models.ForeignKey(
#         User, on_delete=models.CASCADE,  blank=True, null=True, related_name="purchaseUser"),
#     purchaseListing = models.ForeignKey(
#         Listing, on_delete=models.CASCADE,  blank=True, null=True, related_name="purchaseListing")