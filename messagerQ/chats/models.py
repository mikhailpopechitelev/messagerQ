from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=45)
    dateregistration = models.DateField(auto_now_add=True)
    datelastlogin = models.DateField(auto_now=True)


class Notifications(models.Model):
    text = models.TextField(max_length=200)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    
  
class Payments(models.Model):
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    cardinfo = models.CharField(max_length=45)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    
     
class Autorizations(models.Model):
    socialnetworks = models.CharField(max_length=45)
    token = models.CharField(max_length=45)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    
    
class Chats(models.Model):
    datecreation = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=20)
    creator = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    
     
class Friendships(models.Model):
    status = models.CharField(max_length=20)
    firstusr = models.ForeignKey(User, related_name='firstusr_friendships_set', on_delete=models.CASCADE)
    secondusr = models.ForeignKey(User, related_name='secondusr_friendships_set', on_delete=models.CASCADE)


class Messages(models.Model):
    text = models.TextField(max_length=200)
    sender = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    chat = models.ForeignKey('Chats', on_delete=models.CASCADE, null=True)
    
  
class Chatparticipant(models.Model):
    chat = models.ForeignKey('Chats', on_delete=models.CASCADE, null=True)
    participant = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    

class Video(models.Model):
    path = models.CharField(max_length=100)
    sender = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    chat = models.ForeignKey('Chats', on_delete=models.CASCADE, null=True)
    
         
class Image(models.Model):
    path = models.CharField(max_length=100)
    sender = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    chat = models.ForeignKey('Chats', on_delete=models.CASCADE, null=True)
    

class Audio(models.Model):
    path = models.CharField(max_length=100)
    sender = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    chat = models.ForeignKey('Chats', on_delete=models.CASCADE, null=True)

    
class Newsfeed(models.Model):
    description = models.CharField(max_length=45)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    audio = models.ForeignKey('Audio', on_delete=models.CASCADE, null=True)
    video = models.ForeignKey('Video', on_delete=models.CASCADE, null=True)
    image = models.ForeignKey('Image', on_delete=models.CASCADE, null=True)
   
    